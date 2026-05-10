# Handoffs entre agentes

Este directorio almacena los briefs de inicio y las entregas de finalización
de cada tarea por fase y agente.

## Propósito

Los handoffs son la memoria compartida del equipo multi-agente. Permiten al
Orquestador revisar el trabajo entregado, y a los agentes saber qué ha hecho
cada uno antes de tomar el relevo.

## Convención de nombres de archivos

```
fase-N-[agente]-brief.md       — instrucciones del Orquestador al agente
fase-N-[agente]-delivery.md    — resumen de entrega del agente al Orquestador
```

### Ejemplos

```
fase-0-backend-brief.md
fase-0-backend-delivery.md
fase-1-frontend-brief.md
fase-1-frontend-delivery.md
fase-1-testing-delivery.md
```

## Formato de un brief

```markdown
# Brief: Fase N — [Agente]

## Tarea
[Descripción clara de lo que debe hacer]

## Contexto
[Qué ya existe, qué decisiones previas son relevantes]

## Criterios de aceptación
- [ ] criterio 1
- [ ] criterio 2

## Contratos relevantes
- [links a docs de referencia]

## Fecha límite / prioridad
[cuando aplique]
```

## Formato de una entrega (delivery)

```markdown
# Delivery: Fase N — [Agente]

## Resumen
[Qué se hizo]

## Archivos modificados
- path/to/file.py — descripción del cambio
- path/to/other.js — descripción del cambio

## Criterios de aceptación
- [x] criterio 1 ✅
- [x] criterio 2 ✅
- [ ] criterio 3 ⚠️ (motivo si no se cumplió)

## Notas para el Orquestador
[Cualquier cosa relevante: deuda técnica, decisiones tomadas, dependencias]

## Tests
[Estado de los tests relacionados]
```
