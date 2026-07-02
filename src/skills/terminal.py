from __future__ import annotations

import os
import subprocess


def execute(command: str) -> str:
    text = command.replace("terminal", "", 1).strip()
    if not text:
        return "Tell me the command to run."

    try:
        result = subprocess.run(
            text,
            shell=True,
            capture_output=True,
            text=True,
            timeout=20,
            cwd=os.getcwd(),
        )
        output = result.stdout.strip() or result.stderr.strip() or "Command completed."
        return output[:1000]
    except Exception as exc:
        return f"Terminal command failed: {exc}"
