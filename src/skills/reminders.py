from __future__ import annotations

from datetime import datetime
from pathlib import Path
import json

REMINDERS_FILE = Path(__file__).resolve().parents[1] / ".." / "data" / "reminders.json"


def _load_reminders() -> list[dict[str, str]]:
    if not REMINDERS_FILE.exists():
        return []
    try:
        return json.loads(REMINDERS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_reminders(reminders: list[dict[str, str]]) -> None:
    REMINDERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    REMINDERS_FILE.write_text(json.dumps(reminders, indent=2), encoding="utf-8")


def execute(command: str) -> str:
    text = command.replace("reminder", "", 1).replace("reminders", "", 1).strip()
    if not text:
        return "Tell me what to remember."

    reminders = _load_reminders()
    reminders.append({"text": text, "created_at": datetime.now().isoformat()})
    _save_reminders(reminders)
    return f"Reminder saved: {text}"
