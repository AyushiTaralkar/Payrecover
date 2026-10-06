import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import Response

from app.database.db import Base, engine
from app.database import models
from app.voice.websocket import router as voice_router

load_dotenv()

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


@app.get("/twiml")
@app.post("/twiml")
def twiml():
    ngrok_url = os.getenv("NGROK_URL")

    if not ngrok_url:
        return Response(
            content="NGROK_URL is missing",
            status_code=500,
        )

    twiml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Connect>
        <ConversationRelay
            url="wss://{ngrok_url}/voice"
            welcomeGreeting="Hello! This is PayRecover. How can I help you today?"
        />
    </Connect>
</Response>"""

    return Response(
        content=twiml_response,
        media_type="application/xml",
    )