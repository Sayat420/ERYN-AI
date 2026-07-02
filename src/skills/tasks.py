from __future__ import annotations

import json
from pathlib import Path

TASKS_FILE = Path(__file__).resolve().parents[1] / ".." / "data" / "tasks.json"


def _load_tasks() -> list[str]:
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_tasks(tasks: list[str]) -> None:
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    TASKS_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def execute(command: str) -> str:
    text = command.replace("task", "", 1).replace("tasks", "", 1).strip()
    if not text:
        return "Tell me the task to add."

    tasks = _load_tasks()
    tasks.append(text)
    _save_tasks(tasks)
    return f"Added task: {text}"
