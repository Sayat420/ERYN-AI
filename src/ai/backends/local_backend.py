from __future__ import annotations


class LocalBackend:
    def __init__(self, model_name: str = "local") -> None:
        self.model_name = model_name
        self.model = model_name

    def create_chat_completion(self, prompt: str) -> str:
        prompt_text = (prompt or "").strip()
        if not prompt_text:
            return "I’m running in offline mode. Add a valid API key in the environment to enable cloud responses."

        return (
            "I’m running in offline mode. I can still help with basic guidance, but "
            f"cloud responses are unavailable until a valid API key is configured. You asked: {prompt_text}"
        )

    def set_model(self, model_name: str) -> None:
        self.model = model_name
