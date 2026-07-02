from __future__ import annotations

import json
from pathlib import Path

CONTACTS_FILE = Path(__file__).resolve().parents[1] / ".." / "data" / "contacts.json"


def _load_contacts() -> list[dict[str, str]]:
    if not CONTACTS_FILE.exists():
        return []
    try:
        return json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_contacts(contacts: list[dict[str, str]]) -> None:
    CONTACTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONTACTS_FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")


def execute(command: str) -> str:
    text = command.replace("contact", "", 1).replace("contacts", "", 1).strip()
    if not text:
        contacts = _load_contacts()
        if contacts:
            return "Saved contacts: " + ", ".join(item.get("name", "") for item in contacts if item.get("name"))
        return "No contacts saved yet."

    contacts = _load_contacts()
    contacts.append({"name": text})
    _save_contacts(contacts)
    return f"Saved contact: {text}"
