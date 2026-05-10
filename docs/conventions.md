# Convenciones del proyecto — asistente-noticias

> Documento de referencia para todos los subagentes.
> Solo el Orquestador puede modificarlo.

---

## Código backend (Python)

- **Estilo:** PEP8 estricto. Linter: `ruff` (o `flake8` como alternativa).
- **Type hints:** obligatorios en todas las funciones públicas.
- **Docstrings:** una línea en funciones públicas; formato Google style si se extiende.
- **Imports:** agrupados (stdlib → third-party → local), ordenados con `isort`.
- **Nombres:** `snake_case` para variables y funciones, `PascalCase` para clases.
- **Constantes:** `UPPER_SNAKE_CASE`.
- **Comentarios:** en inglés, solo cuando el "por qué" no es obvio.

---

## Código frontend (JavaScript)

- **Estilo:** no hay linter obligatorio en v1; seguir convenciones de `prettier` manualmente.
- **Sintaxis:** ES2020+, módulos nativos si el navegador lo soporta.
- **Nombres:** `camelCase` para variables y funciones, `PascalCase` para clases/constructores.
- **Constantes de módulo:** `UPPER_SNAKE_CASE`.
- **Comentarios:** en inglés, solo cuando el "por qué" no es obvio.
- **DOM:** IDs y clases en `kebab-case`.

---

## HTML / CSS

- **HTML:** semántico (usar `<main>`, `<nav>`, `<section>`, `<article>` apropiadamente).
- **CSS:** metodología BEM para clases nuevas. Variables CSS para colores y tipografía.
- **Responsive:** mobile-first. Breakpoints: 320px, 768px, 1280px.
- **Accesibilidad:** `alt` en imágenes, `aria-label` en controles sin texto visible,
  contraste mínimo WCAG AA (4.5:1 texto normal).

---

## Commits

Todos los commits llevan prefijo del agente responsable:

```
[orchestrator] descripción
[frontend] descripción
[backend] descripción
[security] descripción
[testing] descripción
[improvement] descripción
```

- Descripción en **imperativo**, en español o inglés (consistente dentro de un PR).
- Máximo 72 caracteres en la primera línea.
- Cuerpo opcional para contexto adicional.

Ejemplos válidos:
```
[backend] add /health endpoint with version field
[frontend] implementar selector de idioma ES/EN
[testing] añadir fixtures para modelo Noticia
```

---

## Ramas

- Una rama por fase: `fase-N-descripcion`
- Ejemplos: `fase-0-entorno-base`, `fase-2-backend-health`
- Solo el Orquestador fusiona hacia `main`
- Nunca trabajar directamente en `main`

---

## Documentación

- Documentación de proyecto y comentarios en documentos: **español**
- Comentarios en código fuente: **inglés**
- Mensajes de UI hacia el usuario: **español o inglés según `lang`**
- Nombres de variables, funciones, clases: **inglés**

---

## Variables de entorno

- Definir siempre en `.env.example` al añadir una nueva variable
- Nunca con valores reales en el repositorio
- Acceder en el backend vía módulo de configuración (`app/config.py`)
- Nunca leer `os.environ` directamente fuera de `config.py`

---

## Gestión de dependencias

- Backend: `requirements.txt` con versiones fijadas (`==`)
- Frontend: sin gestor de paquetes en v1 (vanilla, sin build step)
- Toda dependencia nueva requiere aprobación del Orquestador
- Documentar el motivo de cada dependencia en un comentario en `requirements.txt`
