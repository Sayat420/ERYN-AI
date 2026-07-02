from __future__ import annotations

import webbrowser


def execute(command: str) -> str:
    location = command.replace("map", "", 1).replace("maps", "", 1).strip()
    if not location:
        return "Which place would you like to view on the map?"
    webbrowser.open(f"https://www.google.com/maps/search/{location}")
    return f"Opening map for: {location}"
