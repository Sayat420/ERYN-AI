import importlib
import os
import unittest
from unittest.mock import patch


class AIBackendConfigTests(unittest.TestCase):
    def test_local_backend_provides_offline_response_without_api_key(self):
        with patch.dict(os.environ, {"AI_BACKEND": "openai", "AI_API_KEY": ""}, clear=False):
            import config.config as config_module
            import src.ai.router as router_module

            config_module = importlib.reload(config_module)
            router_module = importlib.reload(router_module)

            backend = router_module.get_ai_backend("openai")
            prompt = "Summarize the weather in one sentence."
            response = backend.create_chat_completion(prompt)

            self.assertIn("offline", response.lower())
            self.assertNotIn("Set AI_API_KEY", response)
            self.assertIn("weather", response.lower())


if __name__ == "__main__":
    unittest.main()
