import json

from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/voice")
async def voice_websocket(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)

            print("Twilio:", data)

            # Twilio sends a setup message when the connection starts
            if data.get("type") == "setup":
                await websocket.send_text(
                    json.dumps({
                        "type": "text",
                        "token": "Hi! This is PayRecover. How can I help you today?",
                        "last": True
                    })
                )

    except Exception as e:
        print("WebSocket closed:", e)