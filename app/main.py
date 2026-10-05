from fastapi import FastAPI

from app.database.db import Base, engine
from app.database import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="PayRecover",
    description="AI-powered autopay recovery agent",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PayRecover",
        "version": "0.1.0",
    }