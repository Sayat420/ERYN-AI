from typing import Any

from config.config import AI_BACKEND
from src.ai.router import get_ai_backend


class ChatAssistant:
    def __init__(self) -> None:
        self.backend = None
        self.error: str | None = None
        self.backend_name = AI_BACKEND

        try:
            self.backend = get_ai_backend(self.backend_name)
        except Exception as exc:
            self.error = f"Failed to initialize AI backend: {exc}"

        if not self.backend and not self.error:
            self.error = (
                "No AI backend could be initialized. "
                "Check AI_BACKEND and AI_API_KEY configuration."
            )

    def ask(self, prompt: str) -> str:
        if self.error:
            return self.error

        if not prompt:
            return "Please ask me a question."

        if not self.backend:
            return "AI backend is unavailable."

        try:
            return self.backend.create_chat_completion(prompt)
        except Exception as exc:
            return f"AI backend error: {exc}"

    def set_backend(self, backend_name: str) -> str:
        try:
            self.backend = get_ai_backend(backend_name)
            self.backend_name = backend_name
            self.error = None
            return f"Switched to {backend_name}."
        except Exception as exc:
            self.error = f"Failed to switch backend: {exc}"
            return self.error

    def set_model(self, model_name: str) -> str:
        if not self.backend:
            return "AI backend is not initialized."

        if hasattr(self.backend, "set_model"):
            try:
                self.backend.set_model(model_name)
                return f"Model changed to {model_name}."
            except Exception as exc:
                return f"Failed to change model: {exc}"

        if hasattr(self.backend, "model"):
            setattr(self.backend, "model", model_name)
            return f"Model changed to {model_name}."

        return "Current backend does not support direct model switching."

    def get_status(self) -> str:
        if self.error:
            return self.error

        if not self.backend:
            return "AI backend is unavailable."

        backend_name = getattr(self.backend, "__class__", type(self.backend)).__name__
        model = getattr(self.backend, "model", "n/a")
        return f"Backend: {backend_name}, model: {model}."


assistant = ChatAssistant()
