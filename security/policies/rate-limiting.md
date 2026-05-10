# Política de rate limiting

## Política

Todos los endpoints públicos tienen rate limiting por IP para prevenir
abuso y proteger los límites de las APIs externas (Groq, GNews, NewsData).

## Implementación esperada

1. Librería: `slowapi` (wrapper de `limits` para FastAPI)
2. Límites por defecto por IP:
   - `POST /ask` — 20 peticiones / hora
   - `GET /news` — 60 peticiones / hora
   - `GET /health` — sin límite
3. Respuesta al superar límite: HTTP 429 con `Retry-After` header
4. Almacenamiento de contadores: en memoria (desarrollo), Redis (producción si escala)

## Checks

- [ ] Rate limiting activo en `/ask` y `/news`
- [ ] Respuesta 429 incluye `Retry-After`
- [ ] Test de rate limit incluido en la suite de tests
- [ ] Límites documentados en `/docs/api-contract.md`
- [ ] Límites revisados al añadir nuevas fuentes de noticias o LLMs
