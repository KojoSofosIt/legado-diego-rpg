"""FastAPI web server for legadoDiegoRPG."""
from __future__ import annotations
import contextlib
import io
import sys
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Ensure project root is on the path regardless of where uvicorn is launched from
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from src.player import Player
from src.world import World
from src.ui import UI
from src.combat import CombatEngine
from src.commands import CommandParser
from src.save import save_game, load_game, list_saves
from content.world_data import CREATURES

app = FastAPI(title="El Legado de Diego RPG")

# ── Session store ─────────────────────────────────────────────────────────────

SESSION_TTL = 7200  # 2 hours


@dataclass
class GameSession:
    player: Player
    world: World
    ui: UI
    combat_engine: CombatEngine
    command_parser: CommandParser
    in_combat: bool = False
    combat_creature_id: Optional[str] = None
    combat_c_hp: int = 0
    last_accessed: float = field(default_factory=time.time)


_sessions: dict[str, GameSession] = {}


def _make_session() -> tuple[str, GameSession]:
    sid = uuid.uuid4().hex[:10]
    player = Player()
    world = World()
    ui = UI()
    combat = CombatEngine(player, ui)
    parser = CommandParser(player, world, ui, combat)
    sess = GameSession(player=player, world=world, ui=ui,
                       combat_engine=combat, command_parser=parser)
    _sessions[sid] = sess
    return sid, sess


def _get(sid: str) -> GameSession:
    sess = _sessions.get(sid)
    if not sess:
        raise HTTPException(404, "Sesión no encontrada. Inicia una nueva partida.")
    now = time.time()
    if now - sess.last_accessed > SESSION_TTL:
        del _sessions[sid]
        raise HTTPException(410, "Sesión expirada. Inicia una nueva partida.")
    sess.last_accessed = now
    return sess


def _cap(fn, *args, **kwargs) -> str:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args, **kwargs)
    return buf.getvalue()

# ── Pydantic request models ───────────────────────────────────────────────────


class CmdReq(BaseModel):
    session_id: str
    command: str


class SaveReq(BaseModel):
    session_id: str
    slot: int = 1


class LoadReq(BaseModel):
    session_id: str
    slot: int

# ── Routes ────────────────────────────────────────────────────────────────────


@app.get("/", response_class=HTMLResponse)
def index():
    return (ROOT / "static" / "index.html").read_text(encoding="utf-8")


@app.post("/api/new")
def new_game():
    sid, sess = _make_session()
    out = _cap(sess.ui.titulo) + _cap(sess.ui.describe_room,
               sess.world.get_room(sess.player.position), sess.player)
    return {"session_id": sid, "output": out, "game_over": False, "in_combat": False}


@app.post("/api/command")
def command(req: CmdReq):
    sess = _get(req.session_id)
    raw = req.command.strip()
    if not raw:
        return {"output": "", "game_over": False, "in_combat": sess.in_combat}

    # ── Active combat: route to combat engine ──────────────────────────────
    if sess.in_combat:
        out, new_hp, done, won = sess.combat_engine.turn_web(
            sess.combat_creature_id, sess.combat_c_hp, raw
        )
        sess.combat_c_hp = new_hp
        if done:
            sess.in_combat = False
            sess.combat_creature_id = None
            sess.combat_c_hp = 0
        return {"output": out, "game_over": sess.player.game_over,
                "in_combat": sess.in_combat}

    verb = raw.lower().split()[0]

    # ── Attack: intercept so we don't block on input() ─────────────────────
    if verb in ("atacar", "ataque", "attack"):
        arg = raw.split(None, 1)[1].lower() if len(raw.split(None, 1)) > 1 else ""
        room = sess.world.get_room(sess.player.position)
        alive = [c for c in room.get("creatures", []) if c not in sess.player.defeated]
        if not alive:
            return {"output": "  No hay criaturas aquí para atacar.\n",
                    "game_over": False, "in_combat": False}
        cid = alive[0]
        if arg:
            cid = sess.command_parser._match_name(arg, alive, CREATURES) or cid
        out, c_hp = sess.combat_engine.init_web(cid)
        sess.in_combat = True
        sess.combat_creature_id = cid
        sess.combat_c_hp = c_hp
        return {"output": out, "game_over": False, "in_combat": True}

    # ── Save/load: handled at API layer to avoid input() prompts ───────────
    if verb in ("guardar", "save", "g"):
        parts = raw.split()
        slot = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
        try:
            path = save_game(sess.player, slot=slot)
            return {"output": f"  Partida guardada en slot {slot}. ({path.name})\n",
                    "game_over": False, "in_combat": False}
        except Exception as exc:
            return {"output": f"  Error al guardar: {exc}\n",
                    "game_over": False, "in_combat": False}

    if verb in ("cargar", "load"):
        parts = raw.split()
        if len(parts) < 2 or not parts[1].isdigit():
            saves = list_saves()
            if not saves:
                return {"output": "  No hay partidas guardadas.\n",
                        "game_over": False, "in_combat": False}
            lines = "\n─── Partidas guardadas ───\n"
            for s in saves:
                lines += (f"  [{s['slot']}] HP {s['hp']}/{s['max_hp']}  "
                          f"Sala: {s['position']}  ({s['saved_at']})\n")
            lines += "\nEscribe: cargar <número de slot>\n"
            return {"output": lines, "game_over": False, "in_combat": False}
        slot = int(parts[1])
        try:
            loaded = load_game(slot=slot)
        except FileNotFoundError as exc:
            return {"output": f"  {exc}\n", "game_over": False, "in_combat": False}
        except Exception as exc:
            return {"output": f"  Error al cargar: {exc}\n",
                    "game_over": False, "in_combat": False}
        sess.player.__dict__.update(loaded.__dict__)
        out = (f"  Partida cargada (slot {slot}).\n" +
               _cap(sess.ui.describe_room,
                    sess.world.get_room(sess.player.position), sess.player))
        return {"output": out, "game_over": False, "in_combat": False}

    # ── Quit: no input() needed in web ────────────────────────────────────
    if verb in ("salir", "quit", "exit", "q"):
        return {"output": "  Guarda tu partida con 'guardar' antes de cerrar la pestaña.\n",
                "game_over": False, "in_combat": False}

    # ── Normal commands: capture stdout ───────────────────────────────────
    out = _cap(sess.command_parser.execute, raw)
    return {"output": out, "game_over": sess.player.game_over, "in_combat": False}


@app.get("/api/saves/{session_id}")
def get_saves(session_id: str):
    _get(session_id)
    saves = list_saves()
    return {"saves": [
        {"slot": s["slot"], "position": s["position"],
         "hp": s["hp"], "max_hp": s["max_hp"], "saved_at": s["saved_at"]}
        for s in saves
    ]}


@app.post("/api/save")
def api_save(req: SaveReq):
    sess = _get(req.session_id)
    try:
        path = save_game(sess.player, slot=req.slot)
        return {"ok": True, "message": f"Guardado en slot {req.slot} ({path.name})"}
    except Exception as exc:
        raise HTTPException(500, str(exc))


@app.post("/api/load")
def api_load(req: LoadReq):
    sess = _get(req.session_id)
    try:
        loaded = load_game(slot=req.slot)
    except FileNotFoundError as exc:
        raise HTTPException(404, str(exc))
    except Exception as exc:
        raise HTTPException(500, str(exc))
    sess.player.__dict__.update(loaded.__dict__)
    out = _cap(sess.ui.describe_room,
               sess.world.get_room(sess.player.position), sess.player)
    return {"ok": True, "output": f"  Partida cargada (slot {req.slot}).\n" + out}
