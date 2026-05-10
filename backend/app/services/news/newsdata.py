import os

import httpx

from app.config import settings

_BASE_URL = "https://newsdata.io/api/1/news"


async def fetch_newsdata(
    lang: str = "es", topic: str = "technology", limit: int = 10
) -> list[dict]:
    api_key = settings.newsdata_api_key or os.environ.get("NEWSDATA_API_KEY", "")
    if not api_key:
        return []

    params = {
        "language": lang,
        "category": topic,
        "apikey": api_key,
    }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(_BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
    except Exception:
        return []

    articles = []
    for item in (data.get("results") or [])[:limit]:
        url = item.get("link", "")
        if not url:
            continue
        articles.append(
            {
                "titulo": (item.get("title") or "").strip(),
                "resumen": (item.get("description") or "")[:300],
                "url": url,
                "fuente": item.get("source_id", "NewsData"),
                "fecha": item.get("pubDate", ""),
            }
        )

    return articles
