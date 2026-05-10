# ROADMAP — asistente-noticias

Estrategia de ramas: una rama por fase → `fase-N-descripcion`

---

## Fase 0 — Preparación del entorno y configuración base

**Objetivo:** Tener el entorno de desarrollo listo y la configuración base del proyecto.

**Entregables:**
- Variables de entorno configuradas (`.env` local desde `.env.example`)
- `requirements.txt` con dependencias iniciales de FastAPI
- Servidor de desarrollo backend arrancando (`uvicorn`)
- Script de arranque del proyecto documentado

**Criterios de aceptación:**
- [ ] `uvicorn app.main:app --reload` arranca sin errores
- [ ] `.env` cargado correctamente por la app
- [ ] Linter (ruff / flake8) configurado y sin errores

---

## Fase 1 — Frontend mínimo con voz (Web Speech API)

**Objetivo:** Página HTML funcional que capture y reproduzca voz en el navegador.

**Entregables:**
- `index.html` con botón de micrófono
- Integración de `SpeechRecognition` y `SpeechSynthesis`
- UI responsive (móvil, tablet, PC)
- Selector de idioma ES/EN

**Criterios de aceptación:**
- [ ] El navegador reconoce voz y muestra transcripción en pantalla
- [ ] La respuesta de texto se lee en voz alta
- [ ] Layout funciona en pantallas desde 320px

---

## Fase 2 — Backend FastAPI con endpoints health y echo

**Objetivo:** API base con endpoints mínimos y estructura limpia.

**Entregables:**
- `GET /health` → `{"status": "ok"}`
- `POST /echo` → devuelve el texto enviado
- CORS configurado para el frontend local
- Tests unitarios de los endpoints

**Criterios de aceptación:**
- [ ] Los dos endpoints responden correctamente
- [ ] CORS permite peticiones desde `localhost`
- [ ] Tests pasan con cobertura ≥ 80%

---

## Fase 3 — Integración front-back (envío y recepción de texto)

**Objetivo:** El frontend envía texto al backend y muestra la respuesta.

**Entregables:**
- Frontend hace `fetch` a `POST /ask` con el texto del usuario
- Backend responde con un texto de prueba (echo enriquecido)
- Manejo de errores de red en el frontend

**Criterios de aceptación:**
- [ ] El flujo completo funciona en local
- [ ] Errores de red se muestran al usuario
- [ ] Tests de integración front-back pasan

---

## Fase 4 — Noticias vía RSS (feedparser)

**Objetivo:** El backend obtiene noticias reales desde fuentes RSS tecnológicas.

**Entregables:**
- Servicio `news/rss.py` con feedparser
- Fuentes configurables (Hacker News, TechCrunch, El País Tecnología)
- Endpoint `GET /news?lang=es&limit=5`
- Caché en memoria (TTL 10 min)

**Criterios de aceptación:**
- [ ] Endpoint devuelve al menos 5 noticias reales
- [ ] Fuentes configurables por idioma
- [ ] Caché reduce llamadas externas

---

## Fase 5 — Noticias vía APIs gratuitas (GNews, NewsData)

**Objetivo:** Complementar RSS con APIs de noticias que permiten búsqueda por tema.

**Entregables:**
- Servicio `news/gnews.py` y `news/newsdata.py`
- Endpoint `GET /news?q=inteligencia+artificial`
- Fallback automático entre fuentes (RSS → GNews → NewsData)
- Rotación de API keys configurable

**Criterios de aceptación:**
- [ ] Al menos una fuente API funcional con cuenta gratuita
- [ ] Fallback funciona si una fuente falla
- [ ] API keys nunca expuestas en logs ni código

---

## Fase 6 — Integración LLM Groq (Llama 3.3 70B)

**Objetivo:** El asistente genera resúmenes y respuestas usando LLM.

**Entregables:**
- Servicio `llm/groq.py` con cliente Groq
- `POST /ask` recibe pregunta → busca noticias → genera respuesta con LLM
- Prompts en ES y EN según idioma del usuario
- Streaming opcional de la respuesta

**Criterios de aceptación:**
- [ ] Respuesta coherente a preguntas sobre noticias tech
- [ ] Latencia < 5s en condiciones normales
- [ ] Manejo de errores de la API Groq (rate limit, timeout)

---

## Fase 7 — UI completa

**Objetivo:** Interfaz pulida con todas las funcionalidades de UX previstas.

**Entregables:**
- Selector de idioma (ES/EN) persistente
- Selector de temática (tecnología, IA, ciberseguridad…)
- Historial de consultas en sesión
- Indicadores visuales de carga y error
- Diseño accesible (ARIA, contraste WCAG AA)

**Criterios de aceptación:**
- [ ] UX fluida en móvil y desktop
- [ ] Historial persiste durante la sesión
- [ ] Accesibilidad auditada con axe o Lighthouse ≥ 90

---

## Fase 8 — Optimización y caché

**Objetivo:** Reducir latencia y uso de tokens del LLM.

**Entregables:**
- Caché de respuestas LLM (mismo input → mismo output, TTL 5 min)
- Caché de noticias por fuente y query (TTL 10 min)
- Métricas básicas: latencia, tokens usados, caché hit rate
- Límites de rate por IP (backend)

**Criterios de aceptación:**
- [ ] Caché hit en segunda consulta idéntica
- [ ] Latencia media < 2s con caché
- [ ] Rate limiting activo (100 req/hora por IP)

---

## Fase 9 — Despliegue

**Objetivo:** Aplicación accesible públicamente.

**Entregables:**
- Frontend desplegado en GitHub Pages
- Backend desplegado en Render (free tier)
- Variables de entorno configuradas en producción
- URL pública documentada en README

**Criterios de aceptación:**
- [ ] URL pública del frontend accesible desde móvil
- [ ] Backend responde en producción
- [ ] No hay secretos en el repositorio

---

## Fase 10 — Extras opcionales

**Objetivo:** Funcionalidades avanzadas si el tiempo lo permite.

**Entregables (opcionales, priorizables):**
- PWA (Progressive Web App) con icono e instalación en móvil
- Podcast diario generado automáticamente (resumen del día en audio)
- Panel de métricas (dashboard simple con estadísticas de uso)
- Soporte multiusuario con sesiones
- Tests e2e con Playwright completos

**Criterios de aceptación:**
- [ ] Cada extra tiene sus propios criterios definidos antes de empezar
