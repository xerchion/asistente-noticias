# Política de CORS

## Política

El backend solo acepta peticiones de orígenes explícitamente permitidos.
No se usa `*` como origen permitido en producción.

## Implementación esperada

1. Lista de orígenes en `ALLOWED_ORIGINS` (variable de entorno)
2. Formato: URLs completas separadas por comas
   - Desarrollo: `http://localhost:5500,http://127.0.0.1:5500`
   - Producción: `https://[usuario].github.io`
3. FastAPI configurado con `CORSMiddleware` usando esta lista
4. Métodos HTTP permitidos: `GET, POST, OPTIONS`
5. Headers permitidos: `Content-Type`

## Checks

- [ ] `ALLOWED_ORIGINS` no contiene `*` en producción
- [ ] Petición desde origen no listado recibe 403
- [ ] Petición OPTIONS (preflight) responde correctamente
- [ ] Lista de orígenes revisada al cambiar de entorno
