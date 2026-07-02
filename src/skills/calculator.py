from __future__ import annotations

import re


def _safe_eval(expression: str) -> float:
    expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)
    return eval(expression, {"__builtins__": {}}, {})


def execute(command: str) -> str:
    match = re.search(r"calculate\s+(.*)", command.lower())
    if not match:
        return "Try saying: calculate 2 + 2"

    expression = match.group(1).strip()
    try:
        result = _safe_eval(expression)
        return f"The result is {result}."
    except Exception:
        return "I could not evaluate that expression."
