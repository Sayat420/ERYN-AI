from __future__ import annotations

from typing import Any


class AnthropicBackend:
    def __init__(self, api_key: str, model: str, temperature: float = 0.7) -> None:
        try:
            from anthropic import Anthropic, AI_PROMPT, HUMAN_PROMPT
        except ImportError as exc:
            raise ImportError(
                "Anthropic package is not installed. Install `anthropic` to use Claude backend."
            ) from exc

        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.AI_PROMPT = AI_PROMPT
        self.HUMAN_PROMPT = HUMAN_PROMPT
        self.client = Anthropic(api_key=api_key)

    def create_chat_completion(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=f"{self.HUMAN_PROMPT} {prompt} {self.AI_PROMPT}",
            max_tokens_to_generate=800,
            temperature=self.temperature,
        )

        return response.output.strip()

    def set_model(self, model_name: str) -> None:
        self.model = model_name
