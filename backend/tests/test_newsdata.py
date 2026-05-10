import pytest
import respx
from httpx import Response

from app.services.news.newsdata import fetch_newsdata

_VALID_RESPONSE = {
    "results": [
        {
            "title": "Nuevo chip de Intel",
            "description": "Descripción de prueba newsdata",
            "link": "https://example.com/intel-chip",
            "source_id": "techblog",
            "pubDate": "2026-05-10T09:00:00+00:00",
        }
    ]
}


@pytest.mark.asyncio
async def test_fetch_newsdata_sin_api_key(monkeypatch):
    monkeypatch.setattr(
        "app.services.news.newsdata.settings.newsdata_api_key", ""
    )
    monkeypatch.delenv("NEWSDATA_API_KEY", raising=False)
    result = await fetch_newsdata()
    assert result == []


@pytest.mark.asyncio
@respx.mock
async def test_fetch_newsdata_respuesta_ok(monkeypatch):
    monkeypatch.setattr(
        "app.services.news.newsdata.settings.newsdata_api_key", "test-key"
    )
    respx.get("https://newsdata.io/api/1/news").mock(
        return_value=Response(200, json=_VALID_RESPONSE)
    )

    result = await fetch_newsdata(lang="es", topic="technology", limit=5)

    assert len(result) == 1
    article = result[0]
    assert article["titulo"] == "Nuevo chip de Intel"
    assert article["resumen"] == "Descripción de prueba newsdata"
    assert article["url"] == "https://example.com/intel-chip"
    assert article["fuente"] == "techblog"
    assert article["fecha"] == "2026-05-10T09:00:00+00:00"


@pytest.mark.asyncio
@respx.mock
async def test_fetch_newsdata_error_red(monkeypatch):
    import httpx

    monkeypatch.setattr(
        "app.services.news.newsdata.settings.newsdata_api_key", "test-key"
    )
    respx.get("https://newsdata.io/api/1/news").mock(
        side_effect=httpx.TimeoutException("timeout")
    )

    result = await fetch_newsdata()
    assert result == []
