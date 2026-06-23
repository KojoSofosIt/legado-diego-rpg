"""Command parser — translates raw player input into game actions."""
from __future__ import annotations
from content.world_data import ITEMS, CREATURES, NPCS
from src.ui import _c, _GR, _RD, _YL, _CY, _D, _B, _R, wrap
from src.save import save_game, load_game, list_saves

DIRECTION_MAP = {
    "n": "norte", "norte": "norte",
    "s": "sur",   "sur": "sur",
    "e": "este",  "este": "este",
    "o": "oeste", "oeste": "oeste",
}


class CommandParser:
    def __init__(self, player, world, ui, combat_engine, challenge_engine=None) -> None:
        self.player = player
        self.world = world
        self.ui = ui
        self.combat = combat_engine
        self.challenge = challenge_engine

    def execute(self, raw: str) -> None:
        raw = raw.strip()
        if not raw:
            return
        parts = raw.lower().split(None, 1)
        verb = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        if verb in DIRECTION_MAP:
            self._go(DIRECTION_MAP[verb])
        elif verb in ("mirar", "m", "look"):
            self._look()
        elif verb in ("examinar", "x", "exam", "ver"):
            self._examine(arg)
        elif verb in ("tomar", "coger", "recoger", "take", "get"):
            self._take(arg)
        elif verb in ("soltar", "drop"):
            self._drop(arg)
        elif verb in ("inventario", "i", "inv"):
            self.ui.status(self.player)
        elif verb in ("equipar", "equip"):
            self._equip(arg)
        elif verb in ("usar", "use"):
            self._use(arg)
        elif verb in ("atacar", "ataque", "attack"):
            self._attack(arg)
        elif verb in ("hablar", "habla", "talk"):
            self._talk(arg)
        elif verb in ("estado", "stats"):
            self.ui.status(self.player)
        elif verb in ("guardar", "save", "g"):
            self._save(arg)
        elif verb in ("cargar", "load"):
            self._load(arg)
        elif verb in ("ayuda", "help", "?", "h"):
            self.ui.help()
        elif verb in ("salir", "quit", "exit", "q"):
            self._quit()
        else:
            print(f"  {_c(_D)}No entiendo '{raw}'. Escribe 'ayuda' para ver los comandos.{_c(_R)}")

    # ── movement ─────────────────────────────────────────────────────────────

    def _go(self, direction: str) -> None:
        room = self.world.get_room(self.player.position)

        # Check locked exits first
        locked = room.get("locked_exits", {})
        if direction in locked:
            gate = locked[direction]
            # Requires item in inventory
            if "requires" in gate:
                if self.player.has_item(gate["requires"]):
                    print(f"  {_c(_GR)}Usas {ITEMS[gate['requires']]['name']} para abrir el paso.{_c(_R)}")
                    self.player.remove_item(gate["requires"])
                    self.player.position = gate["destination"]
                    self._look()
                    return
                else:
                    print(f"  {_c(_RD)}{gate['msg']}{_c(_R)}")
                    return
            # Requires creature to be defeated
            if "requires_defeated" in gate:
                if gate["requires_defeated"] in self.player.defeated:
                    self.player.position = gate["destination"]
                    self._look()
                    return
                else:
                    print(f"  {_c(_RD)}{gate['msg']}{_c(_R)}")
                    return
            # Requires completing a narrative challenge
            if "requires_challenge" in gate:
                cid = gate["requires_challenge"]
                done_flag = f"challenge_{cid}_done"
                if done_flag in self.player.flags:
                    self.player.position = gate["destination"]
                    self._look()
                    return
                if self.challenge is None:
                    print(f"  {_c(_RD)}{gate.get('msg', 'Bloqueado.')}{_c(_R)}")
                    return
                self.challenge.run(cid)
                if done_flag in self.player.flags:
                    if cid == "nivel9_trono":
                        flags = self.player.flags
                        if "eleccion_final_a" in flags:
                            dest = "final_a"
                        elif "eleccion_final_c" in flags:
                            dest = "final_c"
                        else:
                            dest = "final_b"
                    else:
                        dest = gate["destination"]
                    self.player.position = dest
                    self._look()
                return

        normal = room.get("exits", {})
        if direction in normal:
            self.player.position = normal[direction]
            self._look()
        else:
            print(f"  {_c(_D)}No puedes ir al {direction} desde aquí.{_c(_R)}")

    # ── look / examine ────────────────────────────────────────────────────────

    def _look(self) -> None:
        room = self.world.get_room(self.player.position)
        self.ui.describe_room(room, self.player)

    def _examine(self, arg: str) -> None:
        if not arg:
            self._look()
            return

        room = self.world.get_room(self.player.position)

        # Try item in room or inventory
        item_id = self._resolve_item(arg, room)
        if item_id and item_id in ITEMS:
            item = ITEMS[item_id]
            print(f"\n{_c(_B)}{item['name']}{_c(_R)}")
            print(wrap(item.get("examine", item.get("description", ""))))
            if item.get("type") == "weapon":
                print(f"  Daño: {item.get('damage', 2)}")
            elif item.get("type") == "shield":
                print(f"  Defensa: {item.get('defense', 0)}")
            elif item.get("type") == "healing":
                print(f"  Curación: +{item.get('healing', 0)} HP")
            return

        # Try creature
        cid = self._resolve_creature(arg, room)
        if cid and cid in CREATURES:
            c = CREATURES[cid]
            print(f"\n{_c(_B, _RD)}{c['name']}{_c(_R)}")
            print(wrap(c.get("description", "")))
            if cid not in self.player.defeated:
                print(f"  HP: {c['hp']}  ATK: {c['attack']}  DEF: {c['defense']}")
            return

        # Try NPC
        nid = self._resolve_npc(arg, room)
        if nid and nid in NPCS:
            n = NPCS[nid]
            print(f"\n{_c(_B, _GR)}{n['name']}{_c(_R)}")
            print(wrap(n.get("description", "")))
            return

        # Try room feature
        for fname, fdesc in room.get("features", {}).items():
            if arg in fname.lower():
                print(f"\n{_c(_B)}{fname}{_c(_R)}")
                print(wrap(fdesc))
                return

        print(f"  {_c(_D)}No ves nada especial sobre '{arg}'.{_c(_R)}")

    # ── inventory management ──────────────────────────────────────────────────

    def _take(self, arg: str) -> None:
        if not arg:
            print(f"  {_c(_D)}¿Qué quieres tomar?{_c(_R)}")
            return
        room = self.world.get_room(self.player.position)
        available = [i for i in room.get("items", []) if i not in self.player.picked_up]
        item_id = self._match_name(arg, available, ITEMS)
        if not item_id:
            print(f"  {_c(_D)}No hay '{arg}' aquí para tomar.{_c(_R)}")
            return
        self.player.add_item(item_id)
        print(f"  {_c(_GR)}Tomas: {ITEMS[item_id]['name']}.{_c(_R)}")
        take_msg = ITEMS[item_id].get("take_msg")
        if take_msg:
            print(f"  {_c(_D)}{take_msg}{_c(_R)}")

    def _drop(self, arg: str) -> None:
        if not arg:
            print(f"  {_c(_D)}¿Qué quieres soltar?{_c(_R)}")
            return
        item_id = self._match_name(arg, self.player.inventory, ITEMS)
        if not item_id:
            print(f"  {_c(_D)}No llevas '{arg}'.{_c(_R)}")
            return
        self.player.remove_item(item_id)
        if self.player.equipped_weapon == item_id:
            self.player.equipped_weapon = None
        print(f"  {_c(_D)}Dejas {ITEMS[item_id]['name']} en el suelo.{_c(_R)}")

    def _equip(self, arg: str) -> None:
        if not arg:
            print(f"  {_c(_D)}¿Qué quieres equipar?{_c(_R)}")
            return
        candidates = [i for i in self.player.inventory
                      if ITEMS.get(i, {}).get("type") in ("weapon", "shield")]
        item_id = self._match_name(arg, candidates, ITEMS)
        if not item_id:
            print(f"  {_c(_D)}No puedes equipar '{arg}'. Asegúrate de tenerlo en la mochila.{_c(_R)}")
            return
        self.player.equipped_weapon = item_id
        print(f"  {_c(_YL)}Equipas: {ITEMS[item_id]['name']}.{_c(_R)}")

    def _use(self, arg: str) -> None:
        if not arg:
            print(f"  {_c(_D)}¿Qué quieres usar?{_c(_R)}")
            return
        candidates = [i for i in self.player.inventory
                      if ITEMS.get(i, {}).get("type") in ("healing", "key", "lore")]
        item_id = self._match_name(arg, candidates, ITEMS)
        if not item_id:
            print(f"  {_c(_D)}No puedes usar '{arg}' ahora.{_c(_R)}")
            return
        item = ITEMS[item_id]
        if item["type"] == "healing":
            gained = self.player.heal(item.get("healing", 10))
            self.player.remove_item(item_id)
            print(f"  {_c(_GR)}Usas {item['name']}. +{gained} HP "
                  f"({self.player.hp}/{self.player.max_hp}){_c(_R)}")
        elif item["type"] == "lore":
            print(f"\n{_c(_B)}{item['name']}{_c(_R)}")
            print(wrap(item.get("lore_text", item.get("description", ""))))
        else:
            print(f"  {_c(_D)}No hay nada que abrir aquí con eso.{_c(_R)}")

    # ── combat / talk ─────────────────────────────────────────────────────────

    def _attack(self, arg: str) -> None:
        room = self.world.get_room(self.player.position)
        alive = [c for c in room.get("creatures", []) if c not in self.player.defeated]
        if not alive:
            print(f"  {_c(_D)}No hay criaturas aquí para atacar.{_c(_R)}")
            return
        if arg:
            cid = self._match_name(arg, alive, CREATURES)
            if not cid:
                print(f"  {_c(_D)}No ves a '{arg}' aquí.{_c(_R)}")
                return
        else:
            cid = alive[0]
        self.combat.run(cid)

    def _talk(self, arg: str) -> None:
        room = self.world.get_room(self.player.position)
        npcs = room.get("npcs", [])
        if not npcs:
            print(f"  {_c(_D)}No hay nadie con quien hablar aquí.{_c(_R)}")
            return
        if arg:
            nid = self._match_name(arg, npcs, NPCS)
            if not nid:
                print(f"  {_c(_D)}No ves a '{arg}' aquí.{_c(_R)}")
                return
        else:
            nid = npcs[0]
        npc = NPCS[nid]
        already_spoken = nid in self.player.npc_spoken

        # Support both "dialogue" (list) and "dialog" (str) keys
        raw = npc.get("dialogue") or npc.get("dialog") or "..."
        lines = raw if isinstance(raw, list) else [raw]
        repeat_raw = npc.get("dialogue_repeat") or npc.get("dialog_repeat")
        if already_spoken and repeat_raw:
            repeat = repeat_raw if isinstance(repeat_raw, list) else [repeat_raw]
            lines = repeat

        print()
        for line in lines:
            print(f"{_c(_B, _GR)}{npc['name']}{_c(_R)}: {_c(_CY)}\"{line}\"{_c(_R)}")
        self.player.npc_spoken.add(nid)

        # Give item on first talk if configured
        if not already_spoken and npc.get("gives_item"):
            gift = npc["gives_item"]
            if gift not in self.player.inventory:
                self.player.add_item(gift)
                give_msg = npc.get("give_msg", f"Recibes: {ITEMS[gift]['name']}.")
                print(f"  {_c(_YL)}{give_msg}{_c(_R)}")

    # ── save / load ───────────────────────────────────────────────────────────

    def _save(self, arg: str) -> None:
        slot = self._parse_slot(arg, default=1)
        try:
            path = save_game(self.player, slot=slot)
            print(f"  {_c(_GR)}Partida guardada en slot {slot}. ({path.name}){_c(_R)}")
        except Exception as exc:
            print(f"  {_c(_RD)}Error al guardar: {exc}{_c(_R)}")

    def _load(self, arg: str) -> None:
        saves = list_saves()
        if not arg:
            if not saves:
                print(f"  {_c(_D)}No hay partidas guardadas.{_c(_R)}")
                return
            print(f"\n{_c(_B)}─── Partidas guardadas ───{_c(_R)}")
            for s in saves:
                print(f"  [{s['slot']}] HP {s['hp']}/{s['max_hp']}  "
                      f"Sala: {s['position']}  ({s['saved_at']})")
            print(f"  [0] Cancelar")
            try:
                choice = input(f"\n  {_c(_D)}Slot a cargar: {_c(_R)}").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return
            if not choice or choice == "0":
                return
            arg = choice

        slot = self._parse_slot(arg, default=None)
        if slot is None:
            print(f"  {_c(_D)}Slot inválido.{_c(_R)}")
            return
        try:
            loaded = load_game(slot=slot)
        except FileNotFoundError as exc:
            print(f"  {_c(_RD)}{exc}{_c(_R)}")
            return
        except Exception as exc:
            print(f"  {_c(_RD)}Error al cargar: {exc}{_c(_R)}")
            return

        # Transfer loaded state into current player object (in-place)
        self.player.__dict__.update(loaded.__dict__)
        print(f"  {_c(_GR)}Partida cargada (slot {slot}).{_c(_R)}")
        self._look()

    @staticmethod
    def _parse_slot(arg: str, default: int | None) -> int | None:
        try:
            return int(arg.strip())
        except (ValueError, AttributeError):
            return default

    # ── quit ──────────────────────────────────────────────────────────────────

    def _quit(self) -> None:
        try:
            ans = input(f"  {_c(_D)}¿Guardar antes de salir? (s/n): {_c(_R)}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            self.player.game_over = True
            return
        if ans in ("s", "si", "sí", "y", "yes"):
            self._save("")
        try:
            ans2 = input(f"  {_c(_D)}¿Salir del juego? (s/n): {_c(_R)}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            self.player.game_over = True
            return
        if ans2 in ("s", "si", "sí", "y", "yes"):
            print(f"\n{_c(_D)}¡Hasta pronto!{_c(_R)}")
            self.player.game_over = True

    # ── resolver helpers ──────────────────────────────────────────────────────

    def _match_name(self, arg: str, candidates: list[str], catalog: dict) -> str | None:
        arg = arg.lower()
        for cid in candidates:
            entry = catalog.get(cid, {})
            if arg in cid or arg in entry.get("name", "").lower():
                return cid
        # partial match on individual words
        for cid in candidates:
            entry = catalog.get(cid, {})
            name_words = entry.get("name", "").lower().split()
            if any(arg in w for w in name_words) or any(arg in cid for _ in [None]):
                return cid
        return None

    def _resolve_item(self, arg: str, room: dict) -> str | None:
        room_items = room.get("items", [])
        visible = [i for i in room_items if i not in self.player.picked_up]
        return self._match_name(arg, visible + self.player.inventory, ITEMS)

    def _resolve_creature(self, arg: str, room: dict) -> str | None:
        return self._match_name(arg, room.get("creatures", []), CREATURES)

    def _resolve_npc(self, arg: str, room: dict) -> str | None:
        return self._match_name(arg, room.get("npcs", []), NPCS)
