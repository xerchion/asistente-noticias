# Arquitectura del sistema — asistente-noticias

> Documento vivo. Mantenido por el Orquestador.
> Última actualización: bootstrap inicial.

---

## Diagrama textual

```
┌─────────────────────────────────────────────────────┐
│                     USUARIO                         │
│              (navegador web, móvil/PC)               │
└────────────────────┬────────────────────────────────┘
                     │ voz / texto
                     ▼
┌─────────────────────────────────────────────────────┐
│                   FRONTEND                          │
│         HTML5 + CSS3 + Vanilla JS                   │
│                                                     │
│  ┌─────────────────┐  ┌──────────────────────────┐  │
│  │ Web Speech API  │  │   UI Components          │  │
│  │ SpeechRecog.    │  │   (selector idioma,      │  │
│  │ SpeechSynth.    │  │    historial, temática)  │  │
│  └─────────────────┘  └──────────────────────────┘  │
└────────────────────┬────────────────────────────────┘
                     │ HTTP/JSON (fetch API)
                     │ POST /ask  GET /news  GET /health
                     ▼
┌─────────────────────────────────────────────────────┐
│                   BACKEND                           │
│              Python 3.11 + FastAPI                  │
│                                                     │
│  ┌──────────────┐  ┌────────────┐  ┌─────────────┐  │
│  │   Routes     │  │  Services  │  │   Config    │  │
│  │  /health     │  │  news/     │  │  env vars   │  │
│  │  /ask        │  │  llm/      │  │  CORS       │  │
│  │  /news       │  │            │  │  rate limit │  │
│  └──────────────┘  └────────────┘  └─────────────┘  │
└────────┬───────────────────┬────────────────────────┘
         │                   │
         ▼                   ▼
┌─────────────────┐  ┌──────────────────────────────┐
│   GROQ API      │  │   APIs DE NOTICIAS           │
│  (LLM Llama 3)  │  │                              │
│                 │  │  ┌──────────┐ ┌───────────┐  │
│  - Generación   │  │  │  RSS     │ │  GNews    │  │
│    de resúmenes │  │  │ feedpars.│ │  NewsData │  │
│  - Chat context │  │  └──────────┘ └───────────┘  │
└─────────────────┘  └──────────────────────────────┘
```

---

## Decisiones técnicas clave

### Por qué Vanilla JS (sin framework)

- El proyecto es un SPA simple con pocas vistas; un framework añadiría complejidad innecesaria.
- Web Speech API se integra directamente con el DOM sin capas intermedias.
- Cero dependencias de build en frontend → despliegue trivial en GitHub Pages.

### Por qué FastAPI

- Tipado nativo con Pydantic, ideal para contratos de API compartidos con el frontend.
- Async nativo para llamadas concurrentes a Groq y APIs de noticias.
- Documentación automática (OpenAPI) sin trabajo extra.

### Por qué Groq (no OpenAI)

- Plan gratuito con límite generoso para desarrollo y uso personal.
- Latencia muy baja gracias a hardware especializado (LPU).
- Llama 3.3 70B es de código abierto, sin lock-in.

### Por qué RSS + APIs gratuitas (no solo una fuente)

- RSS es gratuito e ilimitado; APIs gratuitas tienen límites de peticiones.
- Estrategia de fallback: si una fuente falla, otra cubre.
- Diversidad de fuentes = mejor cobertura temática.

---

## Flujo de datos principal

```
1. Usuario habla → SpeechRecognition → texto
2. Frontend → POST /ask {texto, idioma, tematica}
3. Backend → busca noticias relevantes (RSS/GNews/NewsData)
4. Backend → construye prompt con noticias + pregunta
5. Backend → Groq API (Llama 3.3 70B) → respuesta en texto
6. Backend → respuesta JSON al frontend
7. Frontend → SpeechSynthesis → reproduce respuesta en voz
```

---

## Consideraciones de seguridad

- API keys solo en variables de entorno del servidor (nunca en frontend)
- CORS restringido a orígenes conocidos
- Rate limiting por IP en todos los endpoints
- Validación de inputs con Pydantic antes de enviar al LLM
- Ver `/security/checklist.md` para detalles completos
