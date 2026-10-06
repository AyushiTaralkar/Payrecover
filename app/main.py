from fastapi import FastAPI

from app.database.db import Base, engine
from app.database import models
from app.voice.websocket import router as voice_router


# Create database tables
Base.metadata.create_all(bind=engine)


# FastAPI application
app = FastAPI(
    title="PayRecover",
    description="AI-powered autopay recovery agent",
    version="0.1.0",
)


# Register voice WebSocket routes
app.include_router(voice_router)


# Health check
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PayRecover",
        "version": "0.1.0",
    }