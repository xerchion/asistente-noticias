# Política de gestión de secretos

## Política

Todos los secretos (API keys, tokens, contraseñas) se gestionan exclusivamente
mediante variables de entorno. Ningún secreto puede aparecer en el código fuente,
mensajes de commit, logs ni documentación del repositorio.

## Implementación esperada

1. Variables de entorno definidas en `.env.example` (solo nombres, sin valores)
2. Valores reales en `.env` local, nunca commiteado
3. En producción, variables configuradas en el panel del hosting (Render, GitHub)
4. Acceso a variables solo desde `backend/app/config.py`
5. Nunca usar `os.environ.get(...)` fuera del módulo de configuración

## Checks

- [ ] `.env` listado en `.gitignore`
- [ ] `git log --all --full-diff -p -- .env` no muestra contenido real
- [ ] `grep -r "API_KEY=" --include="*.py"` no devuelve valores hardcodeados
- [ ] Variables de producción configuradas fuera del repo
