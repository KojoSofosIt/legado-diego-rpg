"""Pure ending resolution — determines Final A / B / C based on player state."""
from __future__ import annotations

ENDINGS: dict[str, dict] = {
    "final_a": {
        "title": "Final A — El Sacrificio",
        "subtitle": "Camino del Guerrero",
        "body": (
            "Decides tomar el lugar de Diego. El Mictlán necesita un guardián\n"
            "con sangre española y nahua — tú serás el puente entre los mundos,\n"
            "no como vivo, sino como custodio eterno.\n\n"
            "Diego descansa. Tú vigilas.\n\n"
            "Xochitl cierra los ojos. El Chiconahuapan fluye al revés, como siempre.\n"
            "Y el mundo sigue — sin saber que lo cuidas."
        ),
    },
    "final_b": {
        "title": "Final B — El Balance",
        "subtitle": "Camino Dual",
        "body": (
            "Encuentras la tercera vía: ni sacrificio ni fuga.\n"
            "Las puertas se sellan con tu sangre dual, pero no te quedas.\n"
            "Vuelves al mundo mortal llevando el conocimiento del Mictlán.\n"
            "Diego queda libre. Las puertas, cerradas. Por ahora.\n\n"
            "Xochitl sonríe — es lo más humano que la has visto hacer.\n"
            "Diego asiente. Sois lo que él no pudo ser solo: un puente completo."
        ),
    },
    "final_c": {
        "title": "Final C — La Liberación",
        "subtitle": "Camino del Sabio",
        "body": (
            "Liberas a Diego con los cantos que él nunca conoció.\n"
            "El Mictlán acepta el equilibrio: las puertas se sellan con memoria\n"
            "viva, no con sangre. Diego y Xochitl descansan juntos.\n\n"
            "El mundo de los muertos y el de los vivos se separan en paz.\n"
            "Por primera vez en cincuenta años, nadie llora en las barrancas."
        ),
    },
}

_SEP = "══════════════════════════════════════════════════"


class EndingResolver:
    """Pure function: player state + riddle answer → ending_id."""

    @staticmethod
    def resolve(player, acertijo_choice: str | None = None) -> str:
        """
        Returns 'final_a', 'final_b', or 'final_c'.

        Priority order:
          1. Special narrative flags (highest precedence)
          2. Final riddle answer (Level 9 acertijo)
          3. Accumulated duality difference (esp vs nah)
        """
        esp = player.esp
        nah = player.nah
        flags = player.flags

        # ── 1. Flag overrides ──────────────────────────────────────────────────
        # "Compromiso de amor" — Xochitl fully reborn only in Final C
        if "compromiso_amor" in flags:
            return "final_c"

        # "Voluntad inquebrantable" on a warrior path → Final A
        if "voluntad_inquebrantable" in flags and esp >= 15:
            return "final_a"

        # ── 2. Final riddle (Level 9 acertijo) ────────────────────────────────
        # [3] "Porque no debería haber puertas" — dual answer → always Final B
        if acertijo_choice == "3":
            return "final_b"

        # [1] "Porque los vivos olvidan a los muertos" — remembrance / NAH
        if acertijo_choice == "1" and nah >= 14:
            return "final_c"

        # [4] "Porque el miedo crea las grietas" — warrior / ESP path
        if acertijo_choice == "4" and esp >= 14:
            return "final_a"

        # [2] "Porque los muertos envidian" — wrong answer, push toward sacrifice
        if acertijo_choice == "2":
            esp += 3  # virtual penalty: no side-effects on player object

        # ── 3. Duality difference ──────────────────────────────────────────────
        diff = esp - nah
        if diff >= 5:
            return "final_a"
        if diff <= -5:
            return "final_c"
        return "final_b"

    @staticmethod
    def full_text(ending_id: str) -> str:
        """Return the full formatted ending screen."""
        e = ENDINGS.get(ending_id)
        if not e:
            return f"\nFin desconocido: {ending_id}\n"
        return (
            f"\n{_SEP}\n"
            f"  ✦  {e['title']}  ✦\n"
            f"     {e['subtitle']}\n"
            f"{_SEP}\n\n"
            f"{e['body']}\n\n"
            f"{_SEP}\n"
            "  El Legado de Diego — Fin\n"
            f"{_SEP}\n"
        )

    @staticmethod
    def one_line(ending_id: str) -> str:
        e = ENDINGS.get(ending_id, {})
        return f"{e.get('title', ending_id)} — {e.get('subtitle', '')}"
