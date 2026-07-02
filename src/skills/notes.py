from __future__ import annotations

from pathlib import Path

NOTES_FILE = Path(__file__).resolve().parents[1] / ".." / "data" / "notes.txt"


def execute(command: str) -> str:
    text = command.replace("note", "", 1).replace("notes", "", 1).strip()
    if not text:
        return "What should I save in your notes?"

    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with NOTES_FILE.open("a", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return f"Saved to notes: {text}"
