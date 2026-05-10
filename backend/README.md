# Backend — Asistente de Noticias

Servidor FastAPI base. Fase 2.

## Arrancar el servidor

```bash
cd backend
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Endpoints

| Método | Ruta      | Descripción                        |
|--------|-----------|------------------------------------|
| GET    | /health   | Estado del servidor                |
| POST   | /echo     | Devuelve el mismo body recibido    |
| GET    | /docs     | Documentación automática (Swagger) |

### GET /health

```json
{"status": "ok", "fase": 2}
```

### POST /echo

Request:
```json
{"texto": "hola", "idioma": "es-ES"}
```

Response:
```json
{"texto": "hola", "idioma": "es-ES"}
```

## Variables de entorno

Copia `.env.example` como `.env` y rellena los valores necesarios.

## Linter

```bash
ruff check .
```
