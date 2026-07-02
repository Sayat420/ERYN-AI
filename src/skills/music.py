from __future__ import annotations

import webbrowser


def execute(command: str) -> str:
    query = command.replace("music", "", 1).replace("play", "", 1).strip()
    if not query:
        return "What music should I look up?"
    webbrowser.open(f"https://music.youtube.com/search?q={query}")
    return f"Looking up music for: {query}"
