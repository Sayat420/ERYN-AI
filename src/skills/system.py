from __future__ import annotations

import platform
import os


def execute(command: str) -> str:
    if "info" in command.lower():
        return f"System: {platform.platform()}"
    if "pwd" in command.lower() or "directory" in command.lower():
        return f"Current directory: {os.getcwd()}"
    return "System skill ready. Try: system info"
