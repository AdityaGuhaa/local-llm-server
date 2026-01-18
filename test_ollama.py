from app.services.ollama_client import OllamaClient

client = OllamaClient()

prompt = "Explain what an API is in one sentence."

response = client.generate(prompt)

print("\n--- MODEL RESPONSE ---\n")
print(response)
