---
inclusion: always
---

# Skills Activas para Productos Digitales

Este archivo define las skills que se activan automáticamente para generar productos digitales.

## 🎯 Estrategia y Planificación

| Skill | Uso |
|-------|-----|
| `/office-hours` | Brainstorming y definición de producto estilo Y Combinator |
| `/spec-driven-development` | Especificaciones formales antes de codificar |
| `/plan-eng-review` | Revisión técnica del plan por ingeniero senior |
| `/autoplan` | Pipeline automático CEO+Eng+Design (recomendado para producción) |

## 🎨 Diseño y UI/UX

| Skill | Uso |
|-------|-----|
| `/frontend-ui-engineering` | Interfaces de producción, accesibles, responsivas |
| `/design` | Design system completo (brand, tokens, UI, logo, CIP, slides) |
| `/ui-ux-pro-max` | Intelligence con 84+ estilos, 192+ paletas, 98+ patrones UX |
| `/design-system` | Token architecture, component specifications, CSS variables |
| `/impeccable` | Diseño frontend de nivel award para landing pages |

## 🔧 Código y Calidad

| Skill | Uso |
|-------|-----|
| `/api-and-interface-design` | Diseño de APIs REST/GraphQL estables |
| `/code-review-and-quality` | Revisión multi-eje de código |
| `/code-review-ultra` | Auditoría exhaustiva (seguridad, performance, arquitectura) |

## 🧪 Testing y QA

| Skill | Uso |
|-------|-----|
| `/qa` | QA sistemático + corrección automática de bugs |
| `/browser-testing-with-devtools` | Pruebas en navegador real (Chrome DevTools) |
| `/test-driven-development` | Desarrollo guiado por tests |
| `/performance-optimization` | Optimización de performance |

## 🛡️ Seguridad

| Skill | Uso |
|-------|-----|
| `/security-and-hardening` | Hardening contra vulnerabilidades (auth, input, storage) |
| `/cso` | Chief Security Officer mode (OWASP, STRIDE) |

## 🚀 Deploy y Lanzamiento

| Skill | Uso |
|-------|-----|
| `/ship` | Workflow completo: tests, bump VERSION, CHANGELOG, PR |
| `/land-and-deploy` | Deploy workflow con canary monitoring |
| `/ci-cd-and-automation` | Automatización de CI/CD pipelines |

## 📝 Documentación

| Skill | Uso |
|-------|-----|
| `/documentation-and-adrs` | Documentación y decisiones arquitectónicas (ADR) |
| `/diagram` | Diagramas visuales (Mermaid, Excalidraw) |

## 🏃 Ejecución Rápida (Opcional)

| Skill | Uso |
|-------|-----|
| `/gsd` | "Get Stuff Done" - modo rápido, menos charla, más acción |
| `/ponytail` | Solución más simple que funcione (evita over-engineering) |

## 🎯 Comandos Diarios Recomendados

| Comando | Para qué |
|---------|----------|
| `Office hours` | Brainstorming de ideas de producto |
| `Especifica esto` | Crear especificación formal |
| `Auto-review` | Pipeline completo de revisiones |
| `Hazlo` | Modo GSD rápido |
| `QA test this` | Testing sistemático |
| `Security audit` | Revisión de seguridad |
| `Ship it` | Deploy completo |

## 🔁 Workflow Recomendado

**Flow Completo (Producción):**
```
/office-hours → /spec-driven-development → /autoplan
→ /frontend-ui-engineering + /design
→ /code-review-and-quality → /qa
→ /security-and-hardening → /ship
```

**Flow Rápido (MVP):**
```
/gsd → /frontend-ui-engineering → /qa → /ship
```

---

## 📌 Notas

- Este archivo se puede editar manualmente para agregar/quitar skills
- Las skills se activan automáticamente cuando coinciden con tu solicitud
- Puedes invocar manualmente usando `/nombre-de-skill`
- Para regenerar el catálogo, corre `python3 scripts/preparar-kiro-skills.py`
