from __future__ import annotations

import webbrowser


def execute(command: str) -> str:
    target = command.replace("browser", "", 1).replace("internet", "", 1).strip()
    if not target:
        return "What page would you like to open?"

    webbrowser.open(target if target.startswith(("http://", "https://")) else f"https://{target}")
    return f"Opened: {target}"
