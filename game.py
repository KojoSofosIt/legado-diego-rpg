#!/usr/bin/env python3
"""El Legado de Diego RPG — entry point.

© 2026 Kevin Jiménez Olea. Todos los derechos reservados.
El Legado de Diego: Guardianes del Mictlán
Queda prohibida la reproducción, distribución o uso comercial
sin autorización expresa del autor.
"""
from __future__ import annotations
import sys
import os

# Allow running from the legadoDiegoRPG/ directory directly
sys.path.insert(0, os.path.dirname(__file__))

from src.player import Player
from src.world import World
from src.ui import UI
from src.combat import CombatEngine
from src.challenge import ChallengeEngine
from src.commands import CommandParser


def main() -> None:
    ui = UI()
    ui.titulo()

    player = Player(start_room="altar_diego")
    world = World()
    combat = CombatEngine(player, ui)
    challenge = ChallengeEngine(player, ui)
    parser = CommandParser(player, world, ui, combat, challenge)

    # Describe starting room
    room = world.get_room(player.position)
    ui.describe_room(room, player)

    while not player.game_over:
        try:
            raw = input(f"\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print("¡Hasta pronto!")
            break

        if raw:
            parser.execute(raw)


if __name__ == "__main__":
    main()
