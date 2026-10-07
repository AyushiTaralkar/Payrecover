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
        action="https://hamstring-acquire-acrobat.ngrok-free.dev/process-speech"
        method="POST"
        speechTimeout="auto"
        language="en-IN"
    >
        <Say language="en-IN">
            Hello! This is PayRecover. Your autopay payment failed.
            Please say yes if you want to retry the payment.
        </Say>
    </Gather>

    <Say>
        I didn't hear a response. Goodbye.
    </Say>
</Response>
"""

    return Response(
        content=twiml_response,
        media_type="application/xml",
    )
@app.post("/process-speech")
async def process_speech(request: Request):
    form = await request.form()
    speech = form.get("SpeechResult", "").lower()

    if "yes" in speech or "retry" in speech:
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>
        Okay. I have your confirmation. The payment retry will now be processed.
    </Say>
</Response>
"""
    elif "no" in speech:
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>
        No problem. I will not retry the payment.
    </Say>
</Response>
"""
    else:
        response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>
        Sorry, I didn't understand your response.
    </Say>
</Response>
"""

    return Response(
        content=response,
        media_type="application/xml",
    )