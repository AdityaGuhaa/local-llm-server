from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router

app = FastAPI(
    title="Local LLM Server",
    description="Private self-hosted LLM backend",
    version="0.1.0",
)

# ✅ CORS (THIS FIXES iPhone / other devices)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates (HTML)
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def serve_ui(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Local LLM server is running",
    }


app.include_router(chat_router)
