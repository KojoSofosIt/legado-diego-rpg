"""Save / load player progress to JSON files."""
from __future__ import annotations
import json
import os
from datetime import datetime
from pathlib import Path

from src.player import Player

SAVES_DIR = Path(__file__).parent.parent / "saves"
SCHEMA_VERSION = 1


def _saves_dir() -> Path:
    SAVES_DIR.mkdir(exist_ok=True)
    return SAVES_DIR


def save_game(player: Player, slot: int = 1) -> Path:
    data = {
        "schema_version": SCHEMA_VERSION,
        "saved_at": datetime.now().isoformat(timespec="seconds"),
        "position": player.position,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "esp": player.esp,
        "nah": player.nah,
        "inventory": player.inventory,
        "equipped_weapon": player.equipped_weapon,
        "picked_up": sorted(player.picked_up),
        "defeated": sorted(player.defeated),
        "npc_spoken": sorted(player.npc_spoken),
        "flags": sorted(player.flags),
    }
    path = _saves_dir() / f"save_{slot:02d}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def load_game(slot: int = 1) -> Player:
    path = _saves_dir() / f"save_{slot:02d}.json"
    if not path.exists():
        raise FileNotFoundError(f"No existe la partida en el slot {slot}.")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version", 0) != SCHEMA_VERSION:
        raise ValueError("Versión de guardado incompatible.")
    p = Player(start_room=data["position"])
    p.hp             = data["hp"]
    p.max_hp         = data["max_hp"]
    p.esp            = data["esp"]
    p.nah            = data["nah"]
    p.inventory      = data["inventory"]
    p.equipped_weapon = data.get("equipped_weapon")
    p.picked_up      = set(data.get("picked_up", []))
    p.defeated       = set(data.get("defeated", []))
    p.npc_spoken     = set(data.get("npc_spoken", []))
    p.flags          = set(data.get("flags", []))
    return p


def list_saves() -> list[dict]:
    result = []
    for path in sorted(_saves_dir().glob("save_*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            slot = int(path.stem.split("_")[1])
            result.append({
                "slot": slot,
                "path": path,
                "position": data.get("position", "?"),
                "hp": data.get("hp", "?"),
                "max_hp": data.get("max_hp", "?"),
                "saved_at": data.get("saved_at", "?"),
            })
        except Exception:
            pass
    return result
