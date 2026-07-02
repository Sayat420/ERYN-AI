from __future__ import annotations

from config.config import AI_NAME, AI_BACKEND


def execute(command: str) -> str:
    return f"Assistant name: {AI_NAME}. Current backend: {AI_BACKEND}."
