from __future__ import annotations

import webbrowser


def execute(command: str) -> str:
    query = command.replace("youtube", "", 1).strip()
    if not query:
        return "What would you like to watch on YouTube?"
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"Opening YouTube search for: {query}"
