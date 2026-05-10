from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Asistente de Noticias API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "fase": 2}


class EchoRequest(BaseModel):
    texto: str
    idioma: str


@app.post("/echo")
async def echo(body: EchoRequest) -> EchoRequest:
    return body
