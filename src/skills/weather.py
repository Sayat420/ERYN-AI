from __future__ import annotations

import requests


def execute(command: str) -> str:
    location = command.replace("weather", "", 1).strip()
    if not location:
        return "Tell me which city you want the weather for."

    try:
        response = requests.get(
            "https://wttr.in/{}?format=3".format(location),
            timeout=10,
        )
        response.raise_for_status()
        return response.text.strip() or "I could not get the weather right now."
    except Exception:
        return "I could not fetch the weather right now."
