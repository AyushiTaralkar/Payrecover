import asyncio
import os
import ngrok
from dotenv import load_dotenv

load_dotenv()


async def main():
    token = os.getenv("NGROK_AUTHTOKEN")

    listener = await ngrok.forward(
        "localhost:8000",
        authtoken=token,
    )

    print("PUBLIC URL:", listener.url())

    await asyncio.Event().wait()


asyncio.run(main())