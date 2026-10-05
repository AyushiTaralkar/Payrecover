from fastapi import FastAPI
from app.voice.websocket import router as voice_router
from app.database.db import Base, engine
from app.database import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="PayRecover",
    description="AI-powered autopay recovery agent",
    version="0.1.0",
)

app.include_router(voice_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PayRecover",
        "version": "0.1.0",
    }