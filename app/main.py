import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi import Request
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


from fastapi.responses import Response
@app.post("/twiml")
@app.get("/twiml")
def twiml():
    twiml_response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather
        input="speech"
        action="https://YOUR-NGROK-URL/process-speech"
        method="POST"
        speechTimeout="auto"
        language="en-IN"
    >
        <Say language="en-IN">
            Hello. This is PayRecover.
            Your scheduled autopay payment has failed.
            Would you like me to retry the payment?
        </Say>
    </Gather>

    <Say language="en-IN">
        I didn't hear a response. Goodbye.
    </Say>
</Response>
"""

    return Response(
        content=twiml_response,
        media_type="application/xml",
    )