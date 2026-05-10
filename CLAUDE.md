# CLAUDE.md — Instrucciones para el Orquestador

> Claude Code lee este archivo automáticamente al inicio de cada sesión.
> Contiene las reglas globales del proyecto `asistente-noticias`.

---

## Visión del producto

Asistente web de noticias tecnológicas por voz. El usuario habla al micrófono,
el sistema busca noticias relevantes (RSS + APIs gratuitas), genera un resumen
con un LLM (Groq / Llama 3.3 70B) y lo responde también por voz. Soporta
español e inglés, funciona en móvil y desktop sin instalación.

---

## Stack tecnológico

| Capa       | Tecnología                                  |
|------------|---------------------------------------------|
| Frontend   | HTML5 / CSS3 / Vanilla JS, Web Speech API   |
| Backend    | Python 3.11+, FastAPI, Uvicorn              |
| LLM        | Groq API (Llama 3.3 70B)                    |
| Noticias   | RSS (feedparser), GNews API, NewsData API   |
| Despliegue | GitHub Pages (frontend), Render (backend)   |

---

## Subagentes y cuándo delegar

| Subagente    | Delegar cuando…                                              |
|--------------|--------------------------------------------------------------|
| FRONTEND     | Cambios en HTML/CSS/JS, Web Speech API, UI responsive        |
| BACKEND      | Endpoints FastAPI, servicios de noticias o LLM, config       |
| SECURITY     | Auditorías, secretos, CORS, rate limiting, OWASP             |
| TESTING      | Tests unit/integración/e2e, fixtures, cobertura              |
| IMPROVEMENT  | Métricas, retrospectivas, optimizaciones, backlog            |

Los subagentes están definidos en `.claude/agents/`. Para delegar, usa el
comando `/agents` o referencia el agente por nombre en tu sesión.

---

## Convenciones de commits

Todos los commits llevan prefijo del agente que realizó el cambio:

```
[orchestrator] descripción
[frontend] descripción
[backend] descripción
[security] descripción
[testing] descripción
[improvement] descripción
```

---

## Estrategia de ramas

- Una rama por fase: `fase-N-descripcion`
- Ejemplo: `fase-0-entorno-base`, `fase-1-frontend-voz`
- La rama activa es la fuente de verdad para el trabajo en curso
- Solo el Orquestador fusiona ramas hacia `main`

---

## Reglas globales

1. **No añadir dependencias** sin aprobación explícita del Orquestador.
   Toda dependencia nueva debe justificarse y registrarse.

2. **No modificar contratos** en `/docs` ni esquemas en `/shared`
   sin autorización del Orquestador. Estos son la fuente de verdad.

3. **No abrir `.env` nunca.** Las variables de entorno se referencian
   por nombre. Usar `.env.example` para documentar las necesarias.

4. **No mezclar zonas.** Cada agente trabaja exclusivamente en su zona.
   Ver `/agents/[NOMBRE].md` para los límites de cada uno.

5. **Handoff obligatorio.** Al completar una tarea, el agente escribe un
   resumen en `/agents/handoffs/fase-N-[agente]-delivery.md`.

6. **Tests antes de marcar como hecho.** Ninguna tarea se considera
   completada sin que los tests relevantes pasen.

---

## Referencias

- [ROADMAP.md](./ROADMAP.md) — fases, entregables y criterios de aceptación
- [agents/ORCHESTRATOR.md](./agents/ORCHESTRATOR.md) — rol detallado del Orquestador
- [docs/architecture.md](./docs/architecture.md) — arquitectura del sistema
- [docs/api-contract.md](./docs/api-contract.md) — contrato de endpoints (fuente de verdad)
- [docs/conventions.md](./docs/conventions.md) — convenciones de código
