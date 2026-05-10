# Delivery: Fase 0 — Backend

## Resumen

Entorno base del backend configurado y verificado. El servidor arranca
correctamente, las variables de entorno se cargan desde `.env` y el
linter no reporta errores.

## Archivos modificados

- `backend/requirements.txt` — dependencias fijadas con versiones exactas
- `backend/app/config.py` — carga de settings via pydantic-settings
- `backend/app/main.py` — FastAPI app con CORS y endpoint `/health`
- `backend/ruff.toml` — configuración del linter ruff

## Criterios de aceptación

- [x] `uvicorn app.main:app --reload` arranca sin errores ✅
- [x] `GET /health` responde `{"status":"ok","version":"0.1.0"}` ✅
- [x] `.env` cargado correctamente por pydantic-settings ✅
- [x] `ruff check app/` sin errores ✅

## Notas para el Orquestador

- El archivo `backend/.env` es local y no se commitea (está en .gitignore)
- Las API keys (Groq, GNews, NewsData) permanecen vacías — se rellenarán
  en las fases correspondientes (6 y 5)
- `docs_url` de FastAPI se desactiva en producción automáticamente
  via `settings.env`
- `ruff.toml` usa formato nativo (no `[tool.ruff]`) para ruff standalone

## Tests

No hay tests en Fase 0 (el endpoint /health se testea en Fase 2).
