from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/voice")
async def voice_websocket(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            print("Twilio:", message)

    except Exception as e:
        print("WebSocket closed:", e)