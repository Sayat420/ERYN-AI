from __future__ import annotations


def execute(command: str) -> str:
    text = command.replace("alarm", "", 1).strip()
    if not text:
        return "Say the time for the alarm, for example: alarm 7:30"
    return f"Alarm set for {text}."
