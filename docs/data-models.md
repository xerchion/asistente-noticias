# Modelos de datos compartidos — asistente-noticias

> Fuente de verdad para estructuras de datos usadas en frontend y backend.
> Solo el Orquestador puede modificar este documento.
> Versión: 0.0.0 (bootstrap — definiciones placeholder)

---

## Noticia

Representa un artículo de noticias obtenido de cualquier fuente.

```
Noticia:
  title: string          — título del artículo
  summary: string        — resumen o extracto (puede ser vacío)
  url: string            — URL canónica del artículo
  source: string         — nombre de la fuente (ej. "Hacker News", "GNews")
  published_at: string   — fecha ISO 8601 (ej. "2024-01-15T10:30:00Z")
  lang: "es" | "en"     — idioma detectado o configurado
  topic: string?         — categoría temática (opcional)
```

---

## FuenteNoticia

Configuración de una fuente de noticias.

```
FuenteNoticia:
  id: string             — identificador único (ej. "hackernews-rss")
  name: string           — nombre legible
  type: "rss" | "gnews" | "newsdata"
  url: string            — URL del feed o base de la API
  lang: "es" | "en" | "both"
  topics: string[]       — categorías que cubre
  priority: integer      — orden de preferencia (1 = primera opción)
  enabled: boolean
```

---

## PreguntaUsuario

Estructura del input del usuario al endpoint `/ask`.

```
PreguntaUsuario:
  text: string           — texto de la pregunta (1–500 caracteres)
  lang: "es" | "en"     — idioma de la interfaz
  topic: string?         — categoría temática opcional
```

---

## RespuestaAsistente

Estructura de la respuesta del asistente desde `/ask`.

```
RespuestaAsistente:
  answer: string         — texto de la respuesta generada por el LLM
  sources: Noticia[]     — artículos usados como contexto
  lang: "es" | "en"     — idioma de la respuesta
  tokens_used: integer?  — tokens consumidos (solo en modo debug)
  cached: boolean?       — indica si la respuesta vino de caché
```

---

## Notas de implementación

- El backend usa Pydantic para validar `PreguntaUsuario` en la entrada
- El frontend consume `RespuestaAsistente` y mapea `sources` a la UI
- Los campos marcados con `?` son opcionales; el frontend no debe asumir su presencia
- `published_at` siempre en UTC, el frontend formatea según locale del usuario
