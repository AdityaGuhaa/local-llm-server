from fastapi import FastAPI

from app.api.chat import router as chat_router

app = FastAPI(
    title="Local LLM Server",
    description="Private self-hosted LLM backend",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Local LLM server is running"
    }


app.include_router(chat_router)
