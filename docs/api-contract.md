# Contrato de API — asistente-noticias

> Este contrato es la fuente de verdad.
> Frontend y Backend deben respetarlo.
> Solo el Orquestador puede modificarlo.
> Versión: 0.0.0 (bootstrap — pendiente implementación)

---

## Base URL

- Desarrollo: `http://localhost:8000`
- Producción: (pendiente, se actualizará en Fase 9)

---

## Autenticación

No requerida en v1. Los endpoints son públicos con rate limiting por IP.

---

## Endpoints

### GET /health

> Estado del servicio.

**Respuesta 200:**
```json
{
  "status": "ok",
  "version": "string"
}
```

---

### POST /ask

> Envía una pregunta del usuario y recibe una respuesta del asistente.

**Request body:**
```json
{
  "text": "string",
  "lang": "es | en",
  "topic": "string (opcional)"
}
```

**Respuesta 200:**
```json
{
  "answer": "string",
  "sources": [
    {
      "title": "string",
      "url": "string",
      "published_at": "string (ISO 8601)"
    }
  ],
  "lang": "es | en"
}
```

**Respuesta 422:** input inválido (Pydantic)
**Respuesta 429:** rate limit superado
**Respuesta 503:** servicio externo no disponible

---

### GET /news

> Obtiene noticias recientes, opcionalmente filtradas.

**Query params:**
- `lang` (string, opcional, default: `es`) — idioma: `es` | `en`
- `q` (string, opcional) — búsqueda por keyword
- `topic` (string, opcional) — categoría temática
- `limit` (integer, opcional, default: `5`, max: `20`)

**Respuesta 200:**
```json
{
  "items": [
    {
      "title": "string",
      "summary": "string",
      "url": "string",
      "source": "string",
      "published_at": "string (ISO 8601)"
    }
  ],
  "total": "integer",
  "lang": "es | en"
}
```

**Respuesta 503:** ninguna fuente de noticias disponible

---

## Códigos de error estándar

| Código | Significado                                  |
|--------|----------------------------------------------|
| 200    | OK                                           |
| 400    | Petición malformada                          |
| 422    | Error de validación (campo inválido)         |
| 429    | Demasiadas peticiones (rate limit)           |
| 503    | Servicio externo no disponible               |

---

## Notas de versioning

- El contrato se versiona con el campo `version` en `/health`
- Cambios breaking requieren aprobación del Orquestador
- Cambios no-breaking (campos opcionales nuevos) se documentan aquí con fecha
