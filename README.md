# asistente-noticias

Asistente de noticias tecnológicas por voz, construido como monorepo multi-agente.

## Visión del producto

Aplicación web responsive que permite al usuario consultar noticias tecnológicas
por voz (Web Speech API), obtener resúmenes generados por un LLM (Groq / Llama 3),
y recibir la respuesta también por voz. Soporta español e inglés configurables.

## Stack tecnológico

| Capa       | Tecnología                                  |
|------------|---------------------------------------------|
| Frontend   | HTML5 / CSS3 / JavaScript, Web Speech API   |
| Backend    | Python 3.11+, FastAPI, Uvicorn              |
| LLM        | Groq API (Llama 3.3 70B)                    |
| Noticias   | RSS (feedparser), GNews API, NewsData API   |
| Despliegue | GitHub Pages (frontend), Render (backend)   |

## Estado actual

> Estructura inicial creada. Pendiente Fase 0: preparación del entorno y configuración base.

## Documentación

- [CLAUDE.md](./CLAUDE.md) — instrucciones para Claude Code (Orquestador)
- [ROADMAP.md](./ROADMAP.md) — fases del proyecto y criterios de aceptación
- [agents/](./agents/) — documentación detallada de cada subagente
- [docs/](./docs/) — arquitectura, contratos de API, modelos de datos y convenciones

## Estructura del repositorio

```
asistente-noticias/
├── frontend/        # HTML/CSS/JS, Web Speech API
├── backend/         # Python/FastAPI, servicios LLM y noticias
├── security/        # Auditorías, políticas, checklists OWASP
├── testing/         # Estrategia, e2e, integración, fixtures
├── improvement/     # Métricas, retrospectivas, backlog
├── shared/          # Esquemas y traducciones compartidas
├── ops/             # Deploy y CI
├── docs/            # Contratos y arquitectura (fuente de verdad)
└── agents/          # Documentación de cada subagente
```

## Subagentes

| Agente       | Zona principal          | Prefijo de commit  |
|--------------|-------------------------|--------------------|
| ORCHESTRATOR | Raíz, docs, contratos   | `[orchestrator]`   |
| FRONTEND     | /frontend               | `[frontend]`       |
| BACKEND      | /backend                | `[backend]`        |
| SECURITY     | /security               | `[security]`       |
| TESTING      | /testing                | `[testing]`        |
| IMPROVEMENT  | /improvement            | `[improvement]`    |
