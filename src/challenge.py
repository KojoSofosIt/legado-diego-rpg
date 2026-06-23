"""Narrative challenge engine — multi-phase choice sequences."""
from __future__ import annotations
import io
import contextlib
from content.world_data import CHALLENGES, ITEMS
from src.ui import _c, _GR, _YL, _CY, _D, _B, _R, _MG, wrap


class ChallengeEngine:
    """
    Drives branching narrative challenges (e.g. crossing the Tepectli mountains).

    A challenge is a dict from CHALLENGES with:
      - name, entry_text, start_phase
      - phases: { phase_id: { text, options: [...] } }

    Each option may:
      - requires_flag / requires_flag_any : conditional availability
      - sets_flag / sets_flags            : flags to add to player
      - esp_delta / nah_delta             : duality adjustment
      - grants_items                      : items to give player
      - next_phase                        : None = challenge complete
      - response_text                     : narrative text after choice
    """

    def __init__(self, player, ui) -> None:
        self.player = player
        self.ui = ui

    # ── Web interface (stateless turns) ───────────────────────────────────────

    def init_web(self, challenge_id: str) -> tuple[str, str]:
        """Start a challenge. Returns (output_text, first_phase_id)."""
        ch = CHALLENGES[challenge_id]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self._print_entry(ch)
            phase_id = ch["start_phase"]
            self._print_phase(ch, phase_id)
        return buf.getvalue(), phase_id

    def choose_web(
        self, challenge_id: str, phase_id: str, raw: str
    ) -> tuple[str, str | None, bool]:
        """
        Process one choice in the current phase.
        Returns (output, next_phase_id, completed).
        next_phase_id is None when the challenge is done.
        """
        ch = CHALLENGES[challenge_id]
        phase = ch["phases"][phase_id]
        buf = io.StringIO()
        completed = False
        next_phase: str | None = phase_id  # default: stay (bad input)

        with contextlib.redirect_stdout(buf):
            opt = self._find_option(phase, raw)
            if opt is None:
                available = [o for o in phase["options"] if self._available(o)]
                print(f"  {_c(_D)}Elige entre 1 y {len(available)}.{_c(_R)}")
                self._print_phase(ch, phase_id)
            else:
                next_phase = self._apply(challenge_id, ch, opt)
                completed = (next_phase is None)
                if not completed:
                    self._print_phase(ch, next_phase)
                else:
                    self._print_done()

        return buf.getvalue(), next_phase, completed

    # ── CLI interface (blocking) ───────────────────────────────────────────────

    def run(self, challenge_id: str) -> None:
        """Run a full challenge interactively (CLI mode)."""
        ch = CHALLENGES[challenge_id]
        self._print_entry(ch)
        phase_id: str | None = ch["start_phase"]

        while phase_id is not None:
            self._print_phase(ch, phase_id)
            phase = ch["phases"][phase_id]
            try:
                raw = input(f"\n{_c(_CY)}>{_c(_R)} ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return
            opt = self._find_option(phase, raw)
            if opt is None:
                available = [o for o in phase["options"] if self._available(o)]
                print(f"  {_c(_D)}Elige entre 1 y {len(available)}.{_c(_R)}")
                continue
            phase_id = self._apply(challenge_id, ch, opt)

        self._print_done()

    # ── Private helpers ────────────────────────────────────────────────────────

    def _print_entry(self, ch: dict) -> None:
        sep = "─" * 52
        print(f"\n{_c(_B, _CY)}{sep}{_c(_R)}")
        print(f"  {_c(_B)}{ch['name']}{_c(_R)}")
        print(f"{_c(_B, _CY)}{sep}{_c(_R)}\n")
        print(wrap(ch["entry_text"]))

    def _print_phase(self, ch: dict, phase_id: str) -> None:
        phase = ch["phases"][phase_id]
        print(f"\n{wrap(phase['text'])}")
        available = [o for o in phase["options"] if self._available(o)]
        for i, opt in enumerate(available, 1):
            print(f"  [{i}] {opt['label']}")

    def _print_done(self) -> None:
        sep = "─" * 52
        print(f"\n{_c(_B, _GR)}{sep}{_c(_R)}")
        print(f"  {_c(_GR)}✓  Desafío superado.{_c(_R)}")
        print(f"{_c(_B, _GR)}{sep}{_c(_R)}")

    def _available(self, opt: dict) -> bool:
        if req := opt.get("requires_flag"):
            if req not in self.player.flags:
                return False
        if reqs := opt.get("requires_flag_any"):
            if not any(f in self.player.flags for f in reqs):
                return False
        return True

    def _find_option(self, phase: dict, raw: str) -> dict | None:
        available = [o for o in phase["options"] if self._available(o)]
        try:
            idx = int(raw.strip()) - 1
            if 0 <= idx < len(available):
                return available[idx]
        except ValueError:
            pass
        return None

    def _apply(self, challenge_id: str, ch: dict, opt: dict) -> str | None:
        """Apply an option's effects. Returns next phase_id or None if done."""
        if text := opt.get("response_text"):
            print(f"\n{wrap(text)}")

        # Flags
        if flag := opt.get("sets_flag"):
            self.player.flags.add(flag)
        for f in opt.get("sets_flags", []):
            self.player.flags.add(f)

        # Duality
        esp_d = opt.get("esp_delta", 0)
        nah_d = opt.get("nah_delta", 0)
        if esp_d:
            self.player.esp = max(0, min(20, self.player.esp + esp_d))
        if nah_d:
            self.player.nah = max(0, min(20, self.player.nah + nah_d))
        if esp_d or nah_d:
            sign = lambda v: f"+{v}" if v > 0 else str(v)
            parts = []
            if esp_d:
                parts.append(f"{_c(_YL)}ESP {sign(esp_d)}{_c(_R)}")
            if nah_d:
                parts.append(f"{_c(_MG)}NAH {sign(nah_d)}{_c(_R)}")
            print(f"\n  {_c(_D)}[Dualidad: {', '.join(parts)}"
                  f"  →  ESP {self.player.esp} / NAH {self.player.nah}]{_c(_R)}")

        # Items
        for item_id in opt.get("grants_items", []):
            if item_id not in self.player.inventory:
                self.player.add_item(item_id)
                name = ITEMS.get(item_id, {}).get("name", item_id)
                print(f"  {_c(_YL)}Obtienes: {name}.{_c(_R)}")

        # Completion
        next_phase: str | None = opt.get("next_phase")
        if next_phase is None:
            self.player.flags.add(f"challenge_{challenge_id}_done")

        return next_phase
