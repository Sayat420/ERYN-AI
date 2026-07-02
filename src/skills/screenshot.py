from __future__ import annotations

import pyautogui


def execute(command: str) -> str:
    try:
        image = pyautogui.screenshot()
        path = "data/screenshot.png"
        image.save(path)
        return f"Screenshot saved to {path}"
    except Exception as exc:
        return f"Could not capture screenshot: {exc}"
