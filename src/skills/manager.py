from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path
from typing import Any

from src.skills.permission_manager import has_permission

SKILL_MAPPING = {
    "search": "search",
    "weather": "weather",
    "translate": "translate",
    "email": "email",
    "music": "music",
    "play music": "music",
    "notes": "notes",
    "note": "notes",
    "file": "file_manager",
    "files": "file_manager",
    "browser": "internet",
    "internet": "internet",
    "wifi": "wifi",
    "bluetooth": "bluetooth",
    "camera": "camera",
    "screenshot": "screenshot",
    "reminder": "reminders",
    "task": "tasks",
    "terminal": "terminal",
    "system": "system",
    "settings": "settings",
    "media": "media",
    "calculator": "calculator",
    "calendar": "calendar",
    "contacts": "contacts",
    "phone": "phone",
    "security": "security",
    "map": "maps",
    "youtube": "youtube",
    "github": "github",
    "pdf": "pdf",
    "zip": "zip",
    "whatsapp": "whatsapp",
    "spotify": "spotify",
    "music": "music",
    "chat": "ai_chat",
}

SKILL_MODULE_PREFIX = "src.skills"


def _discover_skill_modules() -> set[str]:
    skills_path = Path(__file__).resolve().parent
    packages = set()
    for finder, name, ispkg in pkgutil.iter_modules([str(skills_path)]):
        if name.startswith("__"):
            continue
        packages.add(name)
    return packages


class SkillManager:
    def __init__(self) -> None:
        self.available_skills = _discover_skill_modules()

    def _find_skill_module(self, command: str) -> str | None:
        for keyword, module_name in SKILL_MAPPING.items():
            if keyword in command:
                if module_name in self.available_skills:
                    return module_name
        return None

    def _load_skill(self, module_name: str):
        try:
            return importlib.import_module(f"{SKILL_MODULE_PREFIX}.{module_name}")
        except ImportError:
            return None

    def dispatch(self, command: str) -> str | None:
        module_name = self._find_skill_module(command)
        if not module_name:
            return None

        if module_name in {"notes", "tasks", "reminders", "calculator", "search", "weather", "terminal", "system", "settings", "file_manager", "internet", "music", "github", "youtube", "maps", "media", "bluetooth", "camera", "screenshot", "wifi", "ai_chat", "browser", "web"}:
            pass
        elif not has_permission(module_name, f"Permission is required to use {module_name}."):
            return "Permission denied for that skill."

        skill_module = self._load_skill(module_name)
        if skill_module is None:
            return f"I found the {module_name} skill but it is not installed yet."

        if hasattr(skill_module, "execute"):
            return skill_module.execute(command)

        return f"The {module_name} skill is available, but it has no execute function yet."


skill_manager = SkillManager()
