# Checklist de seguridad OWASP — asistente-noticias

> Mantenido por el agente SECURITY.
> Actualizar al inicio y al final de cada fase.

---

## Gestión de secretos

- [ ] API keys y secretos almacenados únicamente en variables de entorno
- [ ] `.env` en `.gitignore`, nunca commiteado
- [ ] `.env.example` con nombres de variables pero sin valores reales
- [ ] No hay secretos hardcodeados en el código fuente
- [ ] No hay secretos en logs de la aplicación

## CORS

- [ ] `ALLOWED_ORIGINS` configurado explícitamente (no `*` en producción)
- [ ] Headers CORS revisados y restrictivos
- [ ] Métodos HTTP permitidos limitados a los necesarios

## Rate Limiting

- [ ] Rate limiting activo en todos los endpoints públicos
- [ ] Límites definidos por IP y por endpoint
- [ ] Respuesta 429 correctamente formateada
- [ ] Rate limiting testeado

## Validación de input

- [ ] Todos los inputs del usuario validados con Pydantic (backend)
- [ ] Longitud máxima definida para campos de texto libre
- [ ] Tipos de datos validados antes de procesar
- [ ] Sanitización de queries antes de enviar a APIs externas

## Sanitización de output

- [ ] Respuestas del LLM no se inyectan en HTML sin escapar (frontend)
- [ ] URLs de noticias validadas antes de mostrar como enlaces
- [ ] Content Security Policy (CSP) configurada en el frontend

## HTTPS

- [ ] Producción usa HTTPS en ambas capas (frontend y backend)
- [ ] Redirección HTTP → HTTPS activa
- [ ] Certificado válido y no expirado

## Headers de seguridad (backend)

- [ ] `X-Content-Type-Options: nosniff`
- [ ] `X-Frame-Options: DENY`
- [ ] `Strict-Transport-Security` en producción
- [ ] `Referrer-Policy: strict-origin-when-cross-origin`

## Dependencias

- [ ] Dependencias de backend auditadas con `pip-audit` o `safety`
- [ ] Sin dependencias con CVEs conocidas de alta severidad
- [ ] Versiones fijadas en `requirements.txt`

## OWASP Top 10 (aplicable a este stack)

- [ ] A01 Broken Access Control — sin endpoints que exponen datos de otros usuarios
- [ ] A02 Cryptographic Failures — sin datos sensibles sin cifrar
- [ ] A03 Injection — inputs validados, no se construyen queries con concatenación
- [ ] A05 Security Misconfiguration — CORS, headers y entorno revisados
- [ ] A06 Vulnerable Components — dependencias auditadas
- [ ] A09 Logging/Monitoring — sin secretos en logs, errores manejados
