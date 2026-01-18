from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ollama_client import OllamaClient

router = APIRouter()

client = OllamaClient()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat/")
def chat(request: ChatRequest):
    print("🔥 /chat endpoint HIT")
    print("Prompt:", request.prompt)

    result = client.generate(request.prompt)

    if result is None:
        raise HTTPException(status_code=500, detail="LLM generation failed")

    return {"response": result}
