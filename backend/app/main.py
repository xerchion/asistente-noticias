from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.config import settings
from app.routes.news import router as news_router

app = FastAPI(
    title="Asistente de Noticias API",
    version="0.1.0",
    docs_url="/docs" if settings.env == "development" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins.split(","),
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


app.include_router(news_router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "fase": 2}


class EchoRequest(BaseModel):
    texto: str
    idioma: str


@app.post("/echo")
async def echo(body: EchoRequest) -> EchoRequest:
    return body
