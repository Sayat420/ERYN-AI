from __future__ import annotations

from typing import Any


class GoogleBackend:
    def __init__(self, api_key: str, model: str, temperature: float = 0.7) -> None:
        try:
            from google.generativeai import initialize, ChatCompletion
        except ImportError as exc:
            raise ImportError(
                "Google Generative AI package is not installed. Install `google-generativeai` to use Gemini backend."
            ) from exc

        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.initialize = initialize
        self.ChatCompletion = ChatCompletion
        self.initialize(api_key=api_key)

    def create_chat_completion(self, prompt: str) -> str:
        response = self.ChatCompletion.create(
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
        )

        if hasattr(response, "result") and response.result:
            return response.result[0].content[0].text.strip()

        return ""

    def set_model(self, model_name: str) -> None:
        self.model = model_name
