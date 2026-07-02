from __future__ import annotations

import re
from typing import Any

import config.permissions as permissions_config
from voice import listen, speak
from config.voice import VOICE_ENABLED

_permission_cache: dict[str, bool] = {}


def _normalize_answer(answer: str) -> str:
    return answer.strip().lower()


def _is_positive(answer: str) -> bool:
    return bool(re.search(r"\b(yes|y|sure|ok|okay|please do|go ahead|yes please|please)\b", answer.lower()))


def _get_permission_setting(permission_name: str) -> bool:
    setting_name = f"ALLOW_{permission_name.upper()}"
    return getattr(permissions_config, setting_name, False)


def ask_permission(permission_name: str, reason: str | None = None) -> bool:
    if permission_name in _permission_cache:
        return _permission_cache[permission_name]

    if _get_permission_setting(permission_name):
        _permission_cache[permission_name] = True
        return True

    prompt = (
        reason
        or f"I need your permission to access {permission_name.replace('_', ' ')}. Is that okay?"
    )

    if VOICE_ENABLED:
        speak(prompt)
        answer = listen() or ""
    else:
        answer = input(prompt + " (yes/no): ").strip()

    allowed = _is_positive(_normalize_answer(answer))
    _permission_cache[permission_name] = allowed

    if allowed:
        speak("Permission granted.")
    else:
        speak("Permission denied.")

    return allowed


def has_permission(permission_name: str, reason: str | None = None) -> bool:
    if permission_name in _permission_cache:
        return _permission_cache[permission_name]

    if permission_name in {"notes", "tasks", "reminders", "calculator", "search", "weather", "terminal", "system", "settings", "file_manager", "internet", "music", "github", "youtube", "maps", "media", "bluetooth", "camera", "screenshot", "wifi", "ai_chat", "browser", "web"}:
        _permission_cache[permission_name] = True
        return True

    if _get_permission_setting(permission_name):
        _permission_cache[permission_name] = True
        return True

    return ask_permission(permission_name, reason)
