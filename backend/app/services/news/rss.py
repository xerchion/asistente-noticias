import html
import re
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime

import feedparser

socket.setdefaulttimeout(5)

RSS_FEEDS: dict[str, list[tuple[str, str]]] = {
    "es": [
        ("https://feeds.weblogssl.com/xataka/all", "Xataka"),
        ("https://feeds.weblogssl.com/genbeta", "Genbeta"),
        ("https://www.elespanol.com/omicrono/rss/", "Omicrono"),
    ],
    "en": [
        ("https://feeds.feedburner.com/TechCrunch", "TechCrunch"),
        ("https://www.theverge.com/rss/index.xml", "The Verge"),
        ("https://feeds.arstechnica.com/arstechnica/technology", "Ars Technica"),
        ("https://hnrss.org/frontpage", "Hacker News"),
    ],
}

_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(text: str) -> str:
    text = _TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return " ".join(text.split())


def _parse_date(entry: object) -> str:
    parsed = getattr(entry, "published_parsed", None)
    if parsed:
        try:
            return datetime(*parsed[:6], tzinfo=UTC).isoformat()
        except Exception:
            pass
    return ""


def _fetch_feed(url: str, source: str) -> list[dict]:
    try:
        feed = feedparser.parse(url, agent="asistente-noticias/1.0")
        articles = []
        for entry in feed.entries:
            link = getattr(entry, "link", "") or ""
            if not link:
                continue
            titulo = (getattr(entry, "title", "") or "").strip()
            raw = (
                getattr(entry, "summary", "")
                or getattr(entry, "description", "")
                or ""
            )
            resumen = _strip_html(raw)[:300]
            articles.append(
                {
                    "titulo": titulo,
                    "resumen": resumen,
                    "url": link,
                    "fuente": source,
                    "fecha": _parse_date(entry),
                }
            )
        return articles
    except Exception:
        return []


def fetch_rss(lang: str = "es", limit: int = 10) -> list[dict]:
    if limit > 20:
        limit = 20

    if lang == "all":
        feeds = RSS_FEEDS["es"] + RSS_FEEDS["en"]
    else:
        feeds = RSS_FEEDS.get(lang, RSS_FEEDS["es"])

    all_articles: list[dict] = []
    seen_urls: set[str] = set()

    with ThreadPoolExecutor(max_workers=len(feeds)) as executor:
        futures = {
            executor.submit(_fetch_feed, url, source): source
            for url, source in feeds
        }
        for future in as_completed(futures, timeout=10):
            try:
                for article in future.result(timeout=6):
                    if article["url"] not in seen_urls:
                        seen_urls.add(article["url"])
                        all_articles.append(article)
            except Exception:
                pass

    all_articles.sort(key=lambda a: a["fecha"], reverse=True)
    return all_articles[:limit]
