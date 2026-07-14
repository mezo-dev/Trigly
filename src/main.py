from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from src.database import Base, engine
import logging


logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    logger.info("Trigly is starting up... tables ready!")

    yield

    logger.info("Trigly is shutting down...")




app = FastAPI(
    title="Trigly",
    description="A lightweight scheduling engine for triggering external API calls on a schedule.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health", tags=["Health"])
def health_check(request: Request):
    return {"status": "200-OK", "service": "Trigly!"}