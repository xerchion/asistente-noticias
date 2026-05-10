import asyncio

from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.services.news.gnews import fetch_gnews
from app.services.news.newsdata import fetch_newsdata
from app.services.news.rss import fetch_rss

router = APIRouter(tags=["news"])

TOPIC_MAP: dict[str, dict[str, str]] = {
    "tecnologia": {"es": "technology", "en": "technology"},
    "ia":         {"es": "technology", "en": "technology"},
    "moviles":    {"es": "technology", "en": "technology"},
    "seguridad":  {"es": "technology", "en": "technology"},
    "ciencia":    {"es": "science",    "en": "science"},
    "gaming":     {"es": "entertainment", "en": "entertainment"},
    "startups":   {"es": "business",   "en": "business"},
}

_DEFAULT_TOPIC = "technology"


class Article(BaseModel):
    titulo: str
    resumen: str
    url: str
    fuente: str
    fecha: str


class UnifiedNewsResponse(BaseModel):
    articulos: list[Article]
    total: int
    lang: str
    topic: str
    fuentes_activas: list[str]


def _resolve_api_topic(topic: str, lang: str) -> str:
    mapping = TOPIC_MAP.get(topic.lower())
    if not mapping:
        return _DEFAULT_TOPIC
    lang_key = "en" if lang == "en" else "es"
    return mapping.get(lang_key, _DEFAULT_TOPIC)


@router.get("/news", response_model=UnifiedNewsResponse)
async def get_unified_news(
    lang: str = Query(default="es", pattern="^(es|en|all)$"),
    topic: str = Query(default="tecnologia"),
    limit: int = Query(default=15, ge=1, le=30),
) -> UnifiedNewsResponse:
    api_lang = "en" if lang == "en" else "es"
    api_topic = _resolve_api_topic(topic, api_lang)

    rss_articles, gnews_articles, newsdata_articles = await asyncio.gather(
        asyncio.to_thread(fetch_rss, lang=lang, limit=limit),
        fetch_gnews(lang=api_lang, topic=api_topic, limit=limit),
        fetch_newsdata(lang=api_lang, topic=api_topic, limit=limit),
    )

    fuentes_activas: list[str] = []
    seen_urls: set[str] = set()
    merged: list[dict] = []

    source_map = [
        ("rss", rss_articles),
        ("gnews", gnews_articles),
        ("newsdata", newsdata_articles),
    ]

    for source_name, articles in source_map:
        added = False
        for article in articles:
            url = article.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                merged.append(article)
                added = True
        if added:
            fuentes_activas.append(source_name)

    merged.sort(key=lambda a: a.get("fecha", ""), reverse=True)
    merged = merged[:limit]

    return UnifiedNewsResponse(
        articulos=merged,
        total=len(merged),
        lang=lang,
        topic=topic,
        fuentes_activas=fuentes_activas,
    )
