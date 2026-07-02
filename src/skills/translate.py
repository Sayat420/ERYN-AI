from __future__ import annotations


def execute(command: str) -> str:
    text = command.replace("translate", "", 1).strip()
    if not text:
        return "Tell me what to translate."
    return f"Translation placeholder: {text}"
