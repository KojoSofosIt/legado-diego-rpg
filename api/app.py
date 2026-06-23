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
from src.challenge import ChallengeEngine
from src.commands import CommandParser, DIRECTION_MAP
from src.save import save_game, load_game, list_saves
from src.ending_resolver import EndingResolver
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
    challenge_engine: ChallengeEngine
    command_parser: CommandParser
    in_combat: bool = False
    combat_creature_id: Optional[str] = None
    combat_c_hp: int = 0
    in_challenge: bool = False
    challenge_id: Optional[str] = None
    challenge_phase: Optional[str] = None
    last_accessed: float = field(default_factory=time.time)


_sessions: dict[str, GameSession] = {}


def _make_session() -> tuple[str, GameSession]:
    sid = uuid.uuid4().hex[:10]
    player = Player()
    world = World()
    ui = UI()
    combat = CombatEngine(player, ui)
    challenge = ChallengeEngine(player, ui)
    parser = CommandParser(player, world, ui, combat, challenge)
    sess = GameSession(player=player, world=world, ui=ui,
                       combat_engine=combat, challenge_engine=challenge,
                       command_parser=parser)
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


def _base_resp(sess: GameSession, out: str, extra: str = "") -> dict:
    return {
        "output": out + extra,
        "game_over": sess.player.game_over,
        "in_combat": sess.in_combat,
        "in_challenge": sess.in_challenge,
    }


@app.post("/api/command")
def command(req: CmdReq):
    sess = _get(req.session_id)
    raw = req.command.strip()
    if not raw:
        return _base_resp(sess, "")

    # ── Active combat ──────────────────────────────────────────────────────
    if sess.in_combat:
        out, new_hp, done, won = sess.combat_engine.turn_web(
            sess.combat_creature_id, sess.combat_c_hp, raw
        )
        sess.combat_c_hp = new_hp
        if done:
            sess.in_combat = False
            sess.combat_creature_id = None
            sess.combat_c_hp = 0
        return _base_resp(sess, out)

    # ── Active challenge ───────────────────────────────────────────────────
    if sess.in_challenge:
        out, next_phase, completed = sess.challenge_engine.choose_web(
            sess.challenge_id, sess.challenge_phase, raw
        )
        if completed:
            sess.in_challenge = False
            cid = sess.challenge_id
            sess.challenge_id = None
            sess.challenge_phase = None
            # nivel9 routes to final room based on player choice flags
            if cid == "nivel9_trono":
                flags = sess.player.flags
                if "eleccion_final_a" in flags:
                    dest = "final_a"
                elif "eleccion_final_c" in flags:
                    dest = "final_c"
                else:
                    dest = "final_b"
                sess.player.position = dest
                out += _cap(sess.ui.describe_room,
                            sess.world.get_room(dest), sess.player)
            else:
                # Move player through the now-unlocked exit
                room = sess.world.get_room(sess.player.position)
                for gate in room.get("locked_exits", {}).values():
                    if gate.get("requires_challenge") == cid:
                        sess.player.position = gate["destination"]
                        out += _cap(sess.ui.describe_room,
                                    sess.world.get_room(sess.player.position), sess.player)
                        break
        else:
            sess.challenge_phase = next_phase
        return _base_resp(sess, out)

    parts = raw.lower().split()
    verb = parts[0]

    # ── Attack: intercept so we don't block on input() ─────────────────────
    if verb in ("atacar", "ataque", "attack"):
        arg = raw.split(None, 1)[1].lower() if len(raw.split(None, 1)) > 1 else ""
        room = sess.world.get_room(sess.player.position)
        alive = [c for c in room.get("creatures", []) if c not in sess.player.defeated]
        if not alive:
            return _base_resp(sess, "  No hay criaturas aquí para atacar.\n")
        cid = alive[0]
        if arg:
            cid = sess.command_parser._match_name(arg, alive, CREATURES) or cid
        out, c_hp = sess.combat_engine.init_web(cid)
        sess.in_combat = True
        sess.combat_creature_id = cid
        sess.combat_c_hp = c_hp
        return _base_resp(sess, out)

    # ── Movement: intercept challenge-locked exits ─────────────────────────
    direction = DIRECTION_MAP.get(verb)
    if direction:
        room = sess.world.get_room(sess.player.position)
        gate = room.get("locked_exits", {}).get(direction)
        if gate and "requires_challenge" in gate:
            cid = gate["requires_challenge"]
            done_flag = f"challenge_{cid}_done"
            if done_flag not in sess.player.flags:
                out, phase = sess.challenge_engine.init_web(cid)
                sess.in_challenge = True
                sess.challenge_id = cid
                sess.challenge_phase = phase
                return _base_resp(sess, out)
            # Already done — fall through to normal command handling

    # ── Save/load: handled at API layer to avoid input() prompts ───────────
    if verb in ("guardar", "save", "g"):
        slot = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
        try:
            path = save_game(sess.player, slot=slot)
            return _base_resp(sess, f"  Partida guardada en slot {slot}. ({path.name})\n")
        except Exception as exc:
            return _base_resp(sess, f"  Error al guardar: {exc}\n")

    if verb in ("cargar", "load"):
        if len(parts) < 2 or not parts[1].isdigit():
            saves = list_saves()
            if not saves:
                return _base_resp(sess, "  No hay partidas guardadas.\n")
            lines = "\n─── Partidas guardadas ───\n"
            for s in saves:
                lines += (f"  [{s['slot']}] HP {s['hp']}/{s['max_hp']}  "
                          f"Sala: {s['position']}  ({s['saved_at']})\n")
            lines += "\nEscribe: cargar <número de slot>\n"
            return _base_resp(sess, lines)
        slot = int(parts[1])
        try:
            loaded = load_game(slot=slot)
        except FileNotFoundError as exc:
            return _base_resp(sess, f"  {exc}\n")
        except Exception as exc:
            return _base_resp(sess, f"  Error al cargar: {exc}\n")
        sess.player.__dict__.update(loaded.__dict__)
        out = (f"  Partida cargada (slot {slot}).\n" +
               _cap(sess.ui.describe_room,
                    sess.world.get_room(sess.player.position), sess.player))
        return _base_resp(sess, out)

    if verb in ("salir", "quit", "exit", "q"):
        return _base_resp(sess, "  Guarda tu partida con 'guardar' antes de cerrar la pestaña.\n")

    # ── Normal commands: capture stdout ───────────────────────────────────
    out = _cap(sess.command_parser.execute, raw)

    # ── Post-command checks ────────────────────────────────────────────────
    room = sess.world.get_room(sess.player.position)
    extra = ""

    # Milestone: first visit to a story waypoint (not a full ending)
    milestone = room.get("milestone")
    if milestone and milestone not in sess.player.flags:
        sess.player.flags.add(milestone)
        if milestone == "acto1_completado":
            extra = (
                "\n\n══════════════════════════════════════════════════\n"
                "  ✦  ACTO I COMPLETADO — EL UMBRAL  ✦\n"
                "══════════════════════════════════════════════════\n\n"
                "Cruzaste el Chiconahuapan. El río del olvido queda atrás.\n"
                "Lo que Diego sufrió durante nueve niveles, tú lo empiezas ahora.\n\n"
                "El Mictlán tiene ocho niveles más.\n"
                "Tu legado continúa... [ norte → Tepectli Monamictlan ]\n\n"
                "[ Escribe 'guardar' para preservar tu partida ]\n"
            )
        elif milestone == "nivel2_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 2 superado — Tepectli Monamictlan  ✦\n"
                "──────────────────────────────────────────────────\n"
                "Las montañas que chocan quedan atrás. Adelante: Iztepetl.\n\n"
            )
        elif milestone == "nivel3_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 3 superado — Iztepetl  ✦\n"
                "──────────────────────────────────────────────────\n"
                "El cerro de obsidiana queda atrás. Sus cortes permanecen.\n"
                "Adelante: el viento que corta — Itzehecayan.\n\n"
            )
        elif milestone == "nivel4_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 4 superado — Itzehecayan  ✦\n"
                "──────────────────────────────────────────────────\n"
                "El viento de obsidiana queda atrás. El silencio duele.\n"
                "Adelante: el campo del olvido — Pancuecuetlacayan.\n\n"
            )
        elif milestone == "nivel5_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 5 superado — Pancuecuetlacayan  ✦\n"
                "──────────────────────────────────────────────────\n"
                "El campo del olvido no pudo borrarte. Sigues siendo quien eres.\n"
                "Adelante: la lluvia eterna — Temiminaloyan.\n\n"
            )
        elif milestone == "nivel6_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 6 superado — Temiminaloyan  ✦\n"
                "──────────────────────────────────────────────────\n"
                "El campo de flechas eternas queda atrás.\n"
                "Adelante: el corredor del frío — Itztlan.\n\n"
            )
        elif milestone == "nivel7_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 7 superado — Teyollocualoyan  ✦\n"
                "──────────────────────────────────────────────────\n"
                "Itzcuintli y la selva de sombras quedan atrás.\n"
                "Adelante: la oscuridad total — Apochcaloca.\n\n"
            )
        elif milestone == "nivel8_completado":
            extra = (
                "\n\n──────────────────────────────────────────────────\n"
                "  ✦  Nivel 8 superado — Apochcaloca  ✦\n"
                "──────────────────────────────────────────────────\n"
                "Las ilusiones no pudieron detenerte. La oscuridad cedió.\n"
                "Adelante: el trono de Mictlantecuhtli — Chicnauhmictlan.\n\n"
            )

    # True ending: room with ending_id → resolve and display
    if room.get("ending") and not sess.player.game_over:
        ending_id = room.get("ending_id", "final_b")
        extra += EndingResolver.full_text(ending_id)
        sess.player.game_over = True

    return _base_resp(sess, out, extra)


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
