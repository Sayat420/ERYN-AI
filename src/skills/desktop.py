from __future__ import annotations

import os


def execute(command: str) -> str:
    if "open" in command.lower() or "show" in command.lower():
        os.startfile(os.path.expanduser("~\Desktop"))
        return "Opened your desktop folder."
    return "Desktop skill ready."
