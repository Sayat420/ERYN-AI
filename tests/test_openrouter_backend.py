import unittest
from unittest.mock import patch

from src.ai.backends.openai_backend import OpenAIBackend


class OpenRouterBackendTests(unittest.TestCase):
    @patch("src.ai.backends.openai_backend.OpenAI")
    def test_openrouter_key_uses_openrouter_base_url(self, mock_openai):
        OpenAIBackend("sk-or-v1-test-key", "openai/gpt-4o-mini")

        self.assertTrue(mock_openai.called)
        _, kwargs = mock_openai.call_args
        self.assertEqual(kwargs["api_key"], "sk-or-v1-test-key")
        self.assertEqual(kwargs["base_url"], "https://openrouter.ai/api/v1")


if __name__ == "__main__":
    unittest.main()
