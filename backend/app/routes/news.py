from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.services.news.rss import fetch_rss

router = APIRouter(prefix="/news", tags=["news"])


class Article(BaseModel):
    titulo: str
    resumen: str
    url: str
    fuente: str
    fecha: str


class NewsResponse(BaseModel):
    articulos: list[Article]
    total: int
    lang: str


@router.get("/rss", response_model=NewsResponse)
async def get_rss_news(
    lang: str = Query(default="es", pattern="^(es|en|all)$"),
    limit: int = Query(default=10, ge=1),
) -> NewsResponse:
    articulos = fetch_rss(lang=lang, limit=limit)
    return NewsResponse(articulos=articulos, total=len(articulos), lang=lang)
