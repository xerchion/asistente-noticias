# Estrategia de testing — asistente-noticias

> Mantenido por el agente TESTING.

---

## Pirámide de tests

```
        /\
       /  \          E2E (Playwright)
      / e2e\         — flujo completo usuario → respuesta
     /------\
    /        \       Integración
   / integrac.\      — frontend ↔ backend, contrato de API
  /------------\
 /              \    Unitarios
/   unit tests   \   — funciones backend (pytest), funciones JS
/------------------\
```

**Ratio objetivo:** 70% unitarios / 20% integración / 10% e2e

---

## Herramientas

| Nivel        | Herramienta     | Zona                       |
|--------------|-----------------|----------------------------|
| Unit backend | pytest          | /backend/tests/            |
| Unit frontend| JS nativo / vitest (si se aprueba) | /frontend/tests/ |
| Integración  | pytest + httpx  | /testing/integration/      |
| E2E          | Playwright      | /testing/e2e/              |

---

## Convenciones

- Fixtures compartidas en `/testing/fixtures/`
- Mocks de APIs externas (Groq, GNews) siempre en tests, nunca llamadas reales en CI
- Nombres de tests: `test_[what]_[when]_[expected]`
- Tests atómicos: un test = un comportamiento
- Sin `time.sleep` en tests (usar mocks de tiempo si es necesario)

---

## Objetivos de cobertura por fase

| Fase | Backend | Frontend |
|------|---------|----------|
| 0    | N/A     | N/A      |
| 1    | N/A     | básico   |
| 2    | ≥ 80%   | N/A      |
| 3    | ≥ 80%   | básico   |
| 4-6  | ≥ 85%   | básico   |
| 7-9  | ≥ 85%   | ≥ 70%    |

---

## CI (futuro, Fase 9)

- Los tests se ejecutan automáticamente en cada PR
- No se fusiona sin tests verdes
- Informe de cobertura publicado como artefacto
