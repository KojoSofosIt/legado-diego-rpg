"""Terminal display utilities."""
from __future__ import annotations
import textwrap

WRAP = 76
COLOR = True

_R  = "\033[0m"
_B  = "\033[1m"
_D  = "\033[2m"
_CY = "\033[36m"
_YL = "\033[33m"
_GR = "\033[32m"
_RD = "\033[31m"
_MG = "\033[35m"


def _c(*codes: str) -> str:
    return "".join(codes) if COLOR else ""


def wrap(text: str) -> str:
    lines = []
    for para in text.splitlines():
        if para.strip():
            lines.append(textwrap.fill(para.strip(), width=WRAP))
        else:
            lines.append("")
    return "\n".join(lines)


class UI:
    def titulo(self) -> None:
        print(f"\n{'=' * 60}")
        print(f"  {_c(_B, _YL)}El Legado de Diego: Guardianes del Mictlán{_c(_R)}")
        print(f"  {_c(_D)}Vía RPG — Exploración Libre{_c(_R)}")
        print(f"{'=' * 60}\n")
        print(wrap(
            "Eres el heredero de Diego Xólotl de Guzmán. "
            "Las puertas del Mictlán se han debilitado de nuevo. "
            "Explora el pueblo y las barrancas, recoge las reliquias de tu abuelo "
            "y enfrenta a las criaturas del inframundo."
        ))
        print(f"\n{_c(_D)}Escribe 'ayuda' para ver los comandos.{_c(_R)}\n")

    def describe_room(self, room: dict, player) -> None:
        from content.world_data import ITEMS, CREATURES, NPCS
        print(f"\n{_c(_B, _CY)}[ {room['name']} ]{_c(_R)}")
        print(wrap(room.get("description", "")))

        visible_items = [
            i for i in room.get("items", [])
            if i not in player.picked_up
        ]
        if visible_items:
            names = [ITEMS[i]["name"] for i in visible_items if i in ITEMS]
            if names:
                print(f"\n{_c(_YL)}Objetos:{_c(_R)} {', '.join(names)}")

        alive = [
            c for c in room.get("creatures", [])
            if c not in player.defeated
        ]
        if alive:
            names = [CREATURES[c]["name"] for c in alive if c in CREATURES]
            print(f"\n{_c(_RD)}¡Criaturas!:{_c(_R)} {', '.join(names)}")

        npcs = room.get("npcs", [])
        if npcs:
            names = [NPCS[n]["name"] for n in npcs if n in NPCS]
            print(f"\n{_c(_GR)}Personajes:{_c(_R)} {', '.join(names)}")

        exits = list(room.get("exits", {}).keys())
        locked = list(room.get("locked_exits", {}).keys())
        all_exits = exits + [f"{d}*" for d in locked]
        if all_exits:
            print(f"\n{_c(_D)}Salidas: {', '.join(all_exits)}  (* requiere condición){_c(_R)}")

    def msg(self, text: str, color: str = "") -> None:
        prefix = _c(color) if color else ""
        suffix = _c(_R) if color else ""
        print(f"{prefix}{wrap(text)}{suffix}")

    def status(self, player) -> None:
        from content.world_data import ITEMS
        print(f"\n{_c(_B)}─── Estado del Jugador ───{_c(_R)}")
        print(f"  HP : {self._bar(player.hp, player.max_hp, _GR)} {player.hp}/{player.max_hp}")
        print(f"  ESP: {self._bar(player.esp, 20, _YL)} {player.esp}/20")
        print(f"  NAH: {self._bar(player.nah, 20, _MG)} {player.nah}/20")
        w = player.equipped_weapon
        wname = ITEMS[w]["name"] if w and w in ITEMS else "ninguna (puños, daño 2)"
        print(f"  Equipado: {wname}")
        if player.inventory:
            names = [ITEMS[i]["name"] if i in ITEMS else i for i in player.inventory]
            print(f"  Mochila: {', '.join(names)}")
        else:
            print(f"  Mochila: vacía")

    def help(self) -> None:
        cmds = [
            ("n / s / e / o",          "Moverse (norte/sur/este/oeste)"),
            ("mirar  (m)",              "Describir la sala actual"),
            ("examinar <objeto>  (x)",  "Examinar objeto, criatura o rasgo"),
            ("tomar <objeto>",          "Recoger un objeto"),
            ("soltar <objeto>",         "Dejar un objeto"),
            ("inventario  (i)",         "Ver mochila y estado"),
            ("equipar <arma/escudo>",   "Equipar arma o escudo"),
            ("usar <objeto>",           "Usar objeto (curación, ritual)"),
            ("atacar [criatura]",       "Iniciar combate"),
            ("hablar <personaje>",      "Hablar con un personaje"),
            ("estado",                  "Ver estadísticas"),
            ("guardar [slot]  (g)",     "Guardar partida (slot 1 por defecto)"),
            ("cargar [slot]",           "Cargar partida guardada"),
            ("ayuda",                   "Esta ayuda"),
            ("salir",                   "Salir del juego"),
        ]
        print(f"\n{_c(_B)}─── Comandos ───{_c(_R)}")
        for cmd, desc in cmds:
            print(f"  {_c(_CY)}{cmd:<28}{_c(_R)} {desc}")

    def combat_header(self, creature: dict) -> None:
        print(f"\n{_c(_B, _RD)}⚔  COMBATE: {creature['name']}  ⚔{_c(_R)}")
        print(wrap(creature.get("combat_desc", creature["description"])))

    def combat_status(self, player, creature: dict, c_hp: int) -> None:
        p_bar = self._bar(player.hp, player.max_hp, _GR)
        c_bar = self._bar(c_hp, creature["hp"], _RD)
        cname = creature["name"][:16]
        print(f"\n  Tú            HP {p_bar} {player.hp}/{player.max_hp}")
        print(f"  {cname:<14}  HP {c_bar} {c_hp}/{creature['hp']}")

    def _bar(self, cur: int, mx: int, color: str) -> str:
        filled = max(0, int((cur / max(mx, 1)) * 10))
        bar = "█" * filled + "░" * (10 - filled)
        return f"{_c(color)}{bar}{_c(_R)}"
