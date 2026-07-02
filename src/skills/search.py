from __future__ import annotations

import requests


def execute(command: str) -> str:
    query = command.replace("search", "", 1).strip()
    if not query:
        return "What would you like me to search for?"

    try:
        response = requests.get(
            "https://duckduckgo.com/html/?q=" + requests.utils.quote(query),
            timeout=10,
        )
        response.raise_for_status()
        return f"I can search for: {query}."
    except Exception:
        return "Search is unavailable right now."
