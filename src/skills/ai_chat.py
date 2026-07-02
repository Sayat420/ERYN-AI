from __future__ import annotations

from src.ai.assistant import assistant


def execute(command: str) -> str:
    prompt = command.replace("chat", "", 1).strip()
    if not prompt:
        return "What would you like to chat about?"
    return assistant.ask(prompt)
