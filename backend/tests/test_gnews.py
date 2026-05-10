import pytest
import respx
from httpx import Response

from app.services.news.gnews import fetch_gnews

_VALID_RESPONSE = {
    "articles": [
        {
            "title": "AI avanza",
            "description": "Descripción de prueba",
            "url": "https://example.com/ai-avanza",
            "source": {"name": "TechNews"},
            "publishedAt": "2026-05-10T10:00:00Z",
        }
    ]
}


@pytest.mark.asyncio
async def test_fetch_gnews_sin_api_key(monkeypatch):
    monkeypatch.setattr("app.services.news.gnews.settings.gnews_api_key", "")
    monkeypatch.delenv("GNEWS_API_KEY", raising=False)
    result = await fetch_gnews()
    assert result == []


@pytest.mark.asyncio
@respx.mock
async def test_fetch_gnews_respuesta_ok(monkeypatch):
    monkeypatch.setattr(
        "app.services.news.gnews.settings.gnews_api_key", "test-key"
    )
    respx.get("https://gnews.io/api/v4/top-headlines").mock(
        return_value=Response(200, json=_VALID_RESPONSE)
    )

    result = await fetch_gnews(lang="es", topic="technology", limit=5)

    assert len(result) == 1
    article = result[0]
    assert article["titulo"] == "AI avanza"
    assert article["resumen"] == "Descripción de prueba"
    assert article["url"] == "https://example.com/ai-avanza"
    assert article["fuente"] == "TechNews"
    assert article["fecha"] == "2026-05-10T10:00:00Z"


@pytest.mark.asyncio
@respx.mock
async def test_fetch_gnews_error_red(monkeypatch):
    import httpx

    monkeypatch.setattr(
        "app.services.news.gnews.settings.gnews_api_key", "test-key"
    )
    respx.get("https://gnews.io/api/v4/top-headlines").mock(
        side_effect=httpx.TimeoutException("timeout")
    )

    result = await fetch_gnews()
    assert result == []
