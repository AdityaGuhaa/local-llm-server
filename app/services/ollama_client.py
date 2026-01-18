import requests
from typing import Optional


class OllamaClient:
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "gpt-oss:20b",
        timeout: int = 300,
    ):
        self.base_url = base_url
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> Optional[str]:
        """
        Send a prompt to Ollama and return the generated response text.
        """

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get("response")

        except requests.exceptions.RequestException as e:
            print(f"[OllamaClient] Error communicating with Ollama: {e}")
            return None
