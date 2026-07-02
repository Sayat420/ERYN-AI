from __future__ import annotations

import subprocess


def execute(command: str) -> str:
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "profiles"], text=True)
        return output.strip() or "No Wi-Fi profiles found."
    except Exception as exc:
        return f"Could not retrieve Wi-Fi profiles: {exc}"
