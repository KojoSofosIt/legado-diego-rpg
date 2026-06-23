"""Turn-based combat engine."""
from __future__ import annotations
import io
import contextlib
import random
from content.world_data import ITEMS, CREATURES
from src.ui import _c, _GR, _RD, _YL, _R, _B, _D


class CombatEngine:
    def __init__(self, player, ui) -> None:
        self.player = player
        self.ui = ui

    def run(self, creature_id: str) -> bool:
        """Run combat. Returns True if player won, False if fled or dead."""
        template = CREATURES[creature_id]
        c_hp = template["hp"]

        self.ui.combat_header(template)

        while c_hp > 0 and self.player.hp > 0:
            self.ui.combat_status(self.player, template, c_hp)

            usable = self._usable_items()
            self._print_options(usable)

            try:
                raw = input(f"\n{_c(_GR)}>{_c(_R)} ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return False

            action, item_id = self._parse(raw, usable)

            if action == "attack":
                dmg = self._player_dmg(creature_id)
                c_hp -= dmg
                wname = (ITEMS[self.player.equipped_weapon]["name"]
                         if self.player.equipped_weapon else "tus manos")
                print(f"\n  {_c(_YL)}Atacas con {wname}: {dmg} de daño.{_c(_R)}")

            elif action == "item" and item_id:
                dealt = self._use_item(item_id, creature_id)
                c_hp -= dealt

            elif action == "flee":
                if random.random() < 0.55:
                    print(f"\n  {_c(_D)}Logras escapar.{_c(_R)}")
                    return False
                print(f"\n  {_c(_RD)}No puedes escapar.{_c(_R)}")

            else:
                print(f"  {_c(_D)}Elige a, h, o el número de un objeto.{_c(_R)}")
                continue

            # Creature counterattack
            if c_hp > 0:
                cdmg = self._creature_dmg(template)
                self.player.take_damage(cdmg)
                print(f"  {_c(_RD)}{template['name']} te ataca: {cdmg} daño."
                      f"  (HP {self.player.hp}/{self.player.max_hp}){_c(_R)}")

        if self.player.hp <= 0:
            print(f"\n{_c(_B, _RD)}☠  Fuiste derrotado por {template['name']}.{_c(_R)}")
            print("Tu historia termina aquí.")
            self.player.game_over = True
            return False

        print(f"\n{_c(_B, _GR)}✓  Derrotaste a {template['name']}.{_c(_R)}")
        self.player.defeated.add(creature_id)

        for loot_id in template.get("loot", []):
            if loot_id not in self.player.inventory:
                self.player.add_item(loot_id)
                print(f"  Encuentras: {_c(_YL)}{ITEMS[loot_id]['name']}{_c(_R)}.")

        return True

    # ── helpers ──────────────────────────────────────────────────────────────

    def _usable_items(self) -> list[str]:
        return [
            i for i in self.player.inventory
            if ITEMS.get(i, {}).get("type") in ("healing", "ritual")
        ]

    def _print_options(self, usable: list[str]) -> None:
        w = self.player.equipped_weapon
        dmg_hint = f"~{ITEMS[w]['damage']} daño" if w and w in ITEMS else "~2 daño"
        print(f"\n  [a] Atacar ({dmg_hint})")
        for idx, iid in enumerate(usable, 1):
            item = ITEMS[iid]
            if item["type"] == "healing":
                hint = f"+{item['healing']} HP"
            else:
                hint = f"~{item.get('combat_bonus', 0)} daño ritual"
            print(f"  [{idx}] Usar {item['name']} ({hint})")
        print(f"  [h] Huir")

    def _parse(self, raw: str, usable: list[str]) -> tuple[str, str | None]:
        if raw in ("a", "atacar", "attack"):
            return "attack", None
        if raw in ("h", "huir", "flee", "escape"):
            return "flee", None
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(usable):
                return "item", usable[idx]
        except ValueError:
            for iid in usable:
                if raw in ITEMS[iid]["name"].lower() or raw in iid:
                    return "item", iid
        return "unknown", None

    def _player_dmg(self, creature_id: str) -> int:
        w = self.player.equipped_weapon
        base = ITEMS[w].get("damage", 2) if w and w in ITEMS else 2
        if w and ITEMS.get(w, {}).get("weakness_bonus_vs") == creature_id:
            base = int(base * 1.5)
        defense = CREATURES[creature_id].get("defense", 0)
        return max(1, base - defense + random.randint(-1, 2))

    def _creature_dmg(self, template: dict) -> int:
        atk = template.get("attack", 4)
        shield_def = 0
        w = self.player.equipped_weapon
        if w and ITEMS.get(w, {}).get("type") == "shield":
            shield_def = ITEMS[w].get("defense", 0)
        return max(1, atk + random.randint(-2, 2) - shield_def)

    def _use_item(self, item_id: str, creature_id: str) -> int:
        item = ITEMS[item_id]
        itype = item["type"]

        if itype == "healing":
            gained = self.player.heal(item.get("healing", 10))
            self.player.remove_item(item_id)
            print(f"\n  {_c(_GR)}Usas {item['name']}. +{gained} HP "
                  f"({self.player.hp}/{self.player.max_hp}){_c(_R)}")
            return 0

        if itype == "ritual":
            default_msg = f"Usas {item['name']}."
            print(f"\n  {_c(_YL)}{item.get('use_msg', default_msg)}{_c(_R)}")
            base = item.get("combat_bonus", 0)
            if item.get("weakness_bonus_vs") == creature_id:
                base = int(base * 1.5)
            dmg = max(1, base + random.randint(-1, 2))
            print(f"  Causa {dmg} de daño.")
            return dmg

        return 0

    # ── web API methods ───────────────────────────────────────────────────────

    def init_web(self, creature_id: str) -> tuple[str, int]:
        """Start web combat. Returns (display_text, initial_c_hp)."""
        template = CREATURES[creature_id]
        c_hp = template["hp"]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.ui.combat_header(template)
            self.ui.combat_status(self.player, template, c_hp)
            self._print_options(self._usable_items())
        return buf.getvalue(), c_hp

    def turn_web(self, creature_id: str, c_hp: int, raw: str) -> tuple[str, int, bool, bool]:
        """Process one web combat turn. Returns (output, new_c_hp, done, won)."""
        template = CREATURES[creature_id]
        buf = io.StringIO()
        won = False

        with contextlib.redirect_stdout(buf):
            usable = self._usable_items()
            action, item_id = self._parse(raw.strip().lower(), usable)

            if action == "attack":
                dmg = self._player_dmg(creature_id)
                c_hp -= dmg
                wname = (ITEMS[self.player.equipped_weapon]["name"]
                         if self.player.equipped_weapon else "tus manos")
                print(f"\n  {_c(_YL)}Atacas con {wname}: {dmg} de daño.{_c(_R)}")

            elif action == "item" and item_id:
                dealt = self._use_item(item_id, creature_id)
                c_hp -= dealt

            elif action == "flee":
                if random.random() < 0.55:
                    print(f"\n  {_c(_D)}Logras escapar.{_c(_R)}")
                    return buf.getvalue(), c_hp, True, False
                print(f"\n  {_c(_RD)}No puedes escapar.{_c(_R)}")

            else:
                print(f"  {_c(_D)}Elige a, h, o el número de un objeto.{_c(_R)}")
                self.ui.combat_status(self.player, template, c_hp)
                self._print_options(self._usable_items())
                return buf.getvalue(), c_hp, False, False

            # Creature counterattack
            if c_hp > 0 and self.player.hp > 0:
                cdmg = self._creature_dmg(template)
                self.player.take_damage(cdmg)
                print(f"  {_c(_RD)}{template['name']} te ataca: {cdmg} daño."
                      f"  (HP {self.player.hp}/{self.player.max_hp}){_c(_R)}")

            done = c_hp <= 0 or self.player.hp <= 0

            if done:
                if c_hp <= 0 and self.player.hp > 0:
                    won = True
                    print(f"\n{_c(_B, _GR)}✓  Derrotaste a {template['name']}.{_c(_R)}")
                    self.player.defeated.add(creature_id)
                    for loot_id in template.get("loot", []):
                        if loot_id not in self.player.inventory:
                            self.player.add_item(loot_id)
                            print(f"  Encuentras: {_c(_YL)}{ITEMS[loot_id]['name']}{_c(_R)}.")
                else:
                    print(f"\n{_c(_B, _RD)}☠  Fuiste derrotado por {template['name']}.{_c(_R)}")
                    print("Tu historia termina aquí.")
                    self.player.game_over = True
            else:
                self.ui.combat_status(self.player, template, c_hp)
                self._print_options(self._usable_items())

        return buf.getvalue(), c_hp, done, won
