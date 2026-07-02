from __future__ import annotations

from datetime import datetime


def execute(command: str) -> str:
    return f"Today is {datetime.now().strftime('%A, %d %B %Y')}."
