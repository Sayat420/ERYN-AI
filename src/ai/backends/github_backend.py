from __future__ import annotations

import requests


class GitHubBackend:
    def __init__(self, api_key: str, model: str, temperature: float = 0.7) -> None:
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.base_url = "https://models.inference.ai.azure.com"

    def create_chat_completion(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "messages": [
                    {"role": "system", "content": "You are a helpful, professional assistant."},
                    {"role": "user", "content": prompt},
                ],
                "model": self.model,
                "temperature": self.temperature,
                "max_tokens": 800,
            },
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        return payload["choices"][0]["message"]["content"].strip()

    def set_model(self, model_name: str) -> None:
        self.model = model_name
