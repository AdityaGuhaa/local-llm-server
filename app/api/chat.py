from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ollama_client import OllamaClient

router = APIRouter(prefix="/chat", tags=["chat"])

client = OllamaClient()


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = client.generate(request.prompt)

    if result is None:
        raise HTTPException(status_code=500, detail="LLM generation failed")

    return ChatResponse(response=result)
