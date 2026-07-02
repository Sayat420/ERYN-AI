from __future__ import annotations

from pathlib import Path


def execute(command: str) -> str:
    target = command.replace("file", "", 1).replace("files", "", 1).strip()
    if not target:
        return "Tell me which file or folder to inspect."

    path = Path(target)
    if path.exists():
        if path.is_dir():
            return f"Folder exists: {path}"
        return f"File exists: {path}"

    return f"Path not found: {target}"
