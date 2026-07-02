from __future__ import annotations

import subprocess


def execute(command: str) -> str:
    text = command.replace("clipboard", "", 1).strip()
    if not text:
        try:
            result = subprocess.check_output(["powershell", "-NoProfile", "-Command", "Get-Clipboard"], text=True)
            return result.strip() or "Clipboard is empty."
        except Exception:
            return "Clipboard is empty or unavailable."
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", f"Set-Clipboard -Value '{text}'"], check=True)
        return f"Saved to clipboard: {text}"
    except Exception:
        return "Unable to write to clipboard."
