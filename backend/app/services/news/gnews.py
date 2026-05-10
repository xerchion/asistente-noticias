import os

import httpx

from app.config import settings

_BASE_URL = "https://gnews.io/api/v4/top-headlines"


async def fetch_gnews(
    lang: str = "es", topic: str = "technology", limit: int = 10
) -> list[dict]:
    api_key = settings.gnews_api_key or os.environ.get("GNEWS_API_KEY", "")
    if not api_key:
        return []

    params = {
        "lang": lang,
        "topic": topic,
        "max": limit,
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
    for item in data.get("articles", []):
        url = item.get("url", "")
        if not url:
            continue
        articles.append(
            {
                "titulo": (item.get("title") or "").strip(),
                "resumen": (item.get("description") or "")[:300],
                "url": url,
                "fuente": item.get("source", {}).get("name", "GNews"),
                "fecha": item.get("publishedAt", ""),
            }
        )

    return articles
