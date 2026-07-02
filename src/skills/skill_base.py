from __future__ import annotations

from typing import Any

from src.skills.permission_manager import has_permission


class SkillBase:
    def __init__(self, name: str, permission: str | None = None, reason: str | None = None) -> None:
        self.name = name
        self.permission = permission
        self.reason = reason

    def can_execute(self) -> bool:
        if not self.permission:
            return True
        return has_permission(self.permission, self.reason)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("Skill must implement execute()")
