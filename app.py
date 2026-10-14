import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="PNAI AI Agent", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:8000").split(","),
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "PNAI AI Agent"}

@app.post("/api/chat")
def chat(req: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="Server administrator must configure OPENAI_API_KEY.")
    try:
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        response = client.responses.create(
            model=model,
            instructions=(
                "You are PNAI, a helpful assistant. For Azure, GitHub, or cloud actions, "
                "explain steps and request explicit approval before any consequential change. "
                "Do not claim to have accessed external accounts unless a connected tool actually did so."
            ),
            input=req.message,
        )
        return {"reply": response.output_text}
    except Exception:
        # Do not return provider errors that might contain sensitive configuration.
        raise HTTPException(status_code=502, detail="AI request failed. Check server logs and API configuration.")


from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")
