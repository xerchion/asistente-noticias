from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

_D = "2026-05-10"

_RSS_ARTICLES = [
    {
        "titulo": "RSS Noticia 1",
        "resumen": "resumen rss",
        "url": "https://rss.example.com/1",
        "fuente": "Xataka",
        "fecha": f"{_D}T12:00:00",
    },
    {
        "titulo": "RSS Noticia 2",
        "resumen": "resumen rss 2",
        "url": "https://rss.example.com/2",
        "fuente": "Genbeta",
        "fecha": f"{_D}T11:00:00",
    },
]
_GNEWS_ARTICLES = [
    {
        "titulo": "GNews Noticia",
        "resumen": "resumen gnews",
        "url": "https://gnews.example.com/1",
        "fuente": "TechNews",
        "fecha": f"{_D}T10:00:00",
    },
]
_NEWSDATA_ARTICLES = [
    {
        "titulo": "NewsData Noticia",
        "resumen": "resumen newsdata",
        "url": "https://newsdata.example.com/1",
        "fuente": "techblog",
        "fecha": f"{_D}T09:00:00",
    },
]


def _mock_all_sources(rss=None, gnews=None, newsdata=None):
    rss = rss if rss is not None else _RSS_ARTICLES
    gnews = gnews if gnews is not None else _GNEWS_ARTICLES
    newsdata = newsdata if newsdata is not None else _NEWSDATA_ARTICLES

    return (
        patch("app.routes.news_unified.fetch_rss", return_value=rss),
        patch(
            "app.routes.news_unified.fetch_gnews",
            new_callable=AsyncMock,
            return_value=gnews,
        ),
        patch(
            "app.routes.news_unified.fetch_newsdata",
            new_callable=AsyncMock,
            return_value=newsdata,
        ),
    )


def test_endpoint_news_devuelve_articulos():
    p_rss, p_gnews, p_newsdata = _mock_all_sources()
    with p_rss, p_gnews, p_newsdata:
        response = client.get("/news")

    assert response.status_code == 200
    data = response.json()
    assert "articulos" in data
    assert "total" in data
    assert "lang" in data
    assert "topic" in data
    assert "fuentes_activas" in data
    assert data["total"] == len(data["articulos"])
    assert data["total"] > 0


def test_deduplicacion():
    dup_url = "https://shared.example.com/dup"
    rss = [
        {
            "titulo": "A",
            "resumen": "",
            "url": dup_url,
            "fuente": "RSS",
            "fecha": f"{_D}T12:00:00",
        }
    ]
    gnews = [
        {
            "titulo": "B",
            "resumen": "",
            "url": dup_url,
            "fuente": "GNews",
            "fecha": f"{_D}T11:00:00",
        }
    ]
    newsdata = [
        {
            "titulo": "C",
            "resumen": "",
            "url": "https://unique.example.com/c",
            "fuente": "ND",
            "fecha": f"{_D}T10:00:00",
        }
    ]

    p_rss, p_gnews, p_newsdata = _mock_all_sources(
        rss=rss, gnews=gnews, newsdata=newsdata
    )
    with p_rss, p_gnews, p_newsdata:
        response = client.get("/news")

    data = response.json()
    urls = [a["url"] for a in data["articulos"]]
    assert len(urls) == len(set(urls)), "Hay URLs duplicadas"
    assert dup_url in urls
    assert data["total"] == 2


def test_fuentes_activas():
    p_rss, p_gnews, p_newsdata = _mock_all_sources(gnews=[])
    with p_rss, p_gnews, p_newsdata:
        response = client.get("/news")

    data = response.json()
    assert "gnews" not in data["fuentes_activas"]
    assert "rss" in data["fuentes_activas"]
    assert "newsdata" in data["fuentes_activas"]


def test_limit():
    rss = [
        {
            "titulo": f"Art {i}",
            "resumen": "",
            "url": f"https://rss.example.com/{i}",
            "fuente": "RSS",
            "fecha": f"{_D}T{10 + i:02d}:00:00",
        }
        for i in range(10)
    ]
    gnews = [
        {
            "titulo": f"GNews {i}",
            "resumen": "",
            "url": f"https://gnews.example.com/{i}",
            "fuente": "GN",
            "fecha": f"{_D}T{i:02d}:00:00",
        }
        for i in range(5)
    ]

    p_rss, p_gnews, p_newsdata = _mock_all_sources(
        rss=rss, gnews=gnews, newsdata=[]
    )
    with p_rss, p_gnews, p_newsdata:
        response = client.get("/news?limit=5")

    data = response.json()
    assert data["total"] == 5
    assert len(data["articulos"]) == 5
