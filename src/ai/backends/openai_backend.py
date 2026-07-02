from __future__ import annotations

from openai import OpenAI


class OpenAIBackend:
    def __init__(self, api_key: str, model: str, temperature: float = 0.7) -> None:
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1" if api_key.startswith("sk-or-") else None,
        )

    def create_chat_completion(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful, professional assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature,
            max_tokens=800,
        )

        return response.choices[0].message.content.strip()

    def set_model(self, model_name: str) -> None:
        self.model = model_name
