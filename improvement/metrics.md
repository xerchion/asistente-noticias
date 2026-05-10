# Métricas del proyecto — asistente-noticias

> Mantenido por el agente IMPROVEMENT.
> Actualizar al final de cada fase con datos reales.

---

## Métricas de rendimiento

| Métrica                    | Descripción                                      | Objetivo  |
|----------------------------|--------------------------------------------------|-----------|
| Latencia `/ask` (p50)      | Tiempo medio de respuesta del endpoint /ask      | < 3s      |
| Latencia `/ask` (p95)      | Percentil 95 de latencia                         | < 5s      |
| Latencia `/news` (p50)     | Tiempo medio de respuesta de /news               | < 1s      |
| Tokens LLM por petición    | Tokens consumidos en prompt + completion         | < 2000    |
| Caché hit rate (noticias)  | % de peticiones servidas desde caché             | > 60%     |
| Caché hit rate (LLM)       | % de respuestas LLM servidas desde caché         | > 30%     |
| Tasa de error `/ask`       | % de peticiones que resultan en error 5xx        | < 1%      |
| Tasa de error `/news`      | % de peticiones que resultan en error 5xx        | < 1%      |

---

## Métricas de calidad de código

| Métrica              | Descripción                        | Objetivo |
|----------------------|------------------------------------|----------|
| Cobertura backend    | % de líneas cubiertas por tests    | ≥ 85%    |
| Cobertura frontend   | % de funciones cubiertas           | ≥ 70%    |
| Deuda técnica        | Issues de linter sin resolver      | 0        |

---

## Métricas de uso de APIs externas

| Métrica                     | Descripción                               |
|-----------------------------|-------------------------------------------|
| Llamadas a Groq / día       | Para monitorizar límites del plan gratuito|
| Llamadas a GNews / día      | Para monitorizar cuota gratuita           |
| Llamadas a NewsData / día   | Para monitorizar cuota gratuita           |
| Llamadas a RSS / hora       | Para evitar bloqueos de feeds             |

---

## Registro de mediciones por fase

| Fase | Fecha | Latencia /ask p50 | Tokens/req | Caché hit | Notas |
|------|-------|-------------------|------------|-----------|-------|
| —    | —     | —                 | —          | —         | Pendiente implementación |
