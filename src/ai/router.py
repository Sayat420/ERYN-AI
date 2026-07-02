from typing import Protocol

from config.config import (
    AI_BACKEND,
    AI_API_KEY,
    AI_ANTHROPIC_MODEL,
    AI_ANTHROPIC_MODELS,
    AI_ANTHROPIC_TEMPERATURE,
    AI_GOOGLE_MODEL,
    AI_GOOGLE_MODELS,
    AI_GOOGLE_TEMPERATURE,
    AI_OPENAI_MODEL,
    AI_OPENAI_MODELS,
    AI_OPENAI_TEMPERATURE,
    SUPPORTED_AI_BACKENDS,
)
from src.ai.backends.local_backend import LocalBackend
from src.ai.backends.openai_backend import OpenAIBackend


class AIBase(Protocol):
    def create_chat_completion(self, prompt: str) -> str:
        ...

    def set_model(self, model_name: str) -> None:
        ...


def _select_model(primary: str | None, fallback_list: list[str], default: str) -> str:
    if primary:
        return primary
    if fallback_list:
        return fallback_list[0]
    return default


def _normalize_backend_name(backend_name: str | None = None) -> str:
    name = (backend_name or AI_BACKEND or "openai").lower().strip()
    aliases = {
        "chatgpt": "openai",
        "gpt": "openai",
        "openai": "openai",
        "claude": "anthropic",
        "anthropic": "anthropic",
        "google": "google",
        "gemini": "google",
        "google gemini": "google",
        "google gemini pro": "google",
        "local": "local",
        "offline": "local",
    }
    return aliases.get(name, name)


def get_ai_backend(backend_name: str | None = None) -> AIBase:
    selected_backend = _normalize_backend_name(backend_name)
    if selected_backend not in SUPPORTED_AI_BACKENDS:
        selected_backend = "openai"

    if selected_backend == "local" or not AI_API_KEY:
        return LocalBackend()

    if selected_backend == "github":
        try:
            from src.ai.backends.github_backend import GitHubBackend
        except ImportError as exc:
            raise ImportError(
                "GitHub Models support is not available because the required package is missing. "
                "Install `requests` or choose a different backend."
            ) from exc

        model = _select_model(AI_OPENAI_MODEL, AI_OPENAI_MODELS, "openai/gpt-4.1")
        return GitHubBackend(AI_API_KEY, model, AI_OPENAI_TEMPERATURE)

    if selected_backend == "anthropic":
        try:
            from src.ai.backends.anthropic_backend import AnthropicBackend
        except ImportError as exc:
            raise ImportError(
                "Anthropic support is not available because the required package is missing. "
                "Install `anthropic` or choose OpenAI/Google backend."
            ) from exc

        model = _select_model(AI_ANTHROPIC_MODEL, AI_ANTHROPIC_MODELS, "claude-3.5")
        return AnthropicBackend(AI_API_KEY, model, AI_ANTHROPIC_TEMPERATURE)

    if selected_backend == "google":
        try:
            from src.ai.backends.google_backend import GoogleBackend
        except ImportError as exc:
            raise ImportError(
                "Google Gemini support is not available because the required package is missing. "
                "Install `google-generativeai` or choose OpenAI/Anthropic backend."
            ) from exc

        model = _select_model(AI_GOOGLE_MODEL, AI_GOOGLE_MODELS, "gemini-pro")
        return GoogleBackend(AI_API_KEY, model, AI_GOOGLE_TEMPERATURE)

    model = _select_model(AI_OPENAI_MODEL, AI_OPENAI_MODELS, "gpt-4o")
    return OpenAIBackend(AI_API_KEY, model, AI_OPENAI_TEMPERATURE)
