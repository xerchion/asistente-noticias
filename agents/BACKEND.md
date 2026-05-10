# Agente: BACKEND

## Rol

Desarrollar y mantener la API FastAPI: endpoints, servicios de noticias (RSS
y APIs externas) e integración con el LLM (Groq / Llama 3.3 70B).

## Alcance

El agente BACKEND es responsable de toda la lógica del servidor: definir e
implementar los endpoints de la API, los servicios de obtención de noticias
(feedparser, GNews, NewsData), el cliente Groq para generación de respuestas,
la configuración del entorno y el tratamiento de errores del lado servidor.

## Carpetas que SÍ puede modificar

- `/backend` — toda la zona: app/, requirements.txt, tests/

## Carpetas que NO puede modificar (solo lectura)

- `/docs` — lee los contratos, no los modifica
- `/agents`
- `/shared`
- `/frontend`
- `/security`
- `/testing` — los tests de integración y e2e los escribe TESTING
- `/improvement`
- `/ops`

## Contratos que respeta

- `/docs/api-contract.md` — define exactamente los endpoints a implementar
- `/docs/data-models.md` — modelos de datos que el backend devuelve
- `/docs/conventions.md` — PEP8, type hints, docstrings, commits

## Cómo entrega trabajo

- Commits con prefijo `[backend]`
- Trabaja en la rama de la fase activa (`fase-N-descripcion`)
- Al terminar tarea, escribe resumen en `/agents/handoffs/fase-N-backend-delivery.md`
- Marca criterios de aceptación cumplidos en el handoff

## Restricciones

- No toca código fuera de `/backend`
- No añade dependencias a `requirements.txt` sin aprobación del Orquestador
- No modifica contratos en `/docs` ni esquemas en `/shared`
- No expone secretos en logs, respuestas de API ni código fuente

## Definición de "hecho"

- [ ] Criterios de aceptación de la fase cumplidos
- [ ] Tests unitarios pasan (`pytest`)
- [ ] Sin errores de linter (ruff / flake8)
- [ ] Endpoints funcionando según `/docs/api-contract.md`
- [ ] Sin warnings de tipo (mypy si se usa)
- [ ] Documentación de nuevos endpoints actualizada
- [ ] Handoff escrito en `/agents/handoffs/`
