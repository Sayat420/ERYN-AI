from __future__ import annotations

from src.skills.permission_manager import has_permission
from voice import speak, listen


def ask_voice_access() -> bool:
    return has_permission(
        "voice_recording",
        "I need permission to listen to your voice commands. May I proceed?",
    )


def ask_text_access() -> bool:
    return has_permission(
        "read_files",
        "I need permission to read text input or files. May I proceed?",
    )
