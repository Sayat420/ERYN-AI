from __future__ import annotations

import webbrowser


def execute(command: str) -> str:
    query = command.replace("github", "", 1).strip()
    if not query:
        return "What GitHub repository or search term should I open?"
    webbrowser.open(f"https://github.com/search?q={query}")
    return f"Opening GitHub search for: {query}"
