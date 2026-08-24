# 🏭 gstack — Software Factory de Garry Tan (CEO de Y Combinator)

> "Una sola persona con IA puede construir lo que antes requería un equipo de 20."  
> Fuente: [github.com/garrytan/gstack](https://github.com/garrytan/gstack) | Licencia: MIT

---

## 🤔 ¿Qué es gstack?

**gstack** es la fábrica de software personal de Garry Tan (CEO de Y Combinator). Convierte un agente de IA en un **equipo virtual completo**:

- 🧑‍💼 **CEO** que repiensa el producto
- 👷 **Eng Manager** que bloquea la arquitectura
- 🎨 **Diseñador** que detecta AI slop
- 🔍 **Reviewer** que encuentra bugs de producción
- 🌐 **QA Lead** que abre un browser real
- 🛡️ **CSO** que corre auditorías OWASP + STRIDE
- 🚀 **Release Engineer** que shipea el PR

**Resultado real de Garry:** 810× más productivo que en 2013. 3 servicios en producción + 40 features en 60 días, a medio tiempo.

---

## 📊 Resumen de Skills

| Categoría | Skills | Para qué |
|-----------|--------|----------|
| 🧠 Estrategia & Planning | 6 | Office hours, CEO/Eng/Design/DevEx review, autoplan |
| 🚀 Ship & Deploy | 4 | Review, ship, land-and-deploy, canary |
| 🛡️ Seguridad | 3 | CSO, guard, freeze/unfreeze |
| 🧪 QA & Testing | 3 | QA, qa-only, benchmark |
| 🎨 Diseño | 4 | Consultation, HTML, review, shotgun |
| 🔍 Debugging | 2 | Investigate, retro |
| 📝 Documentación | 3 | Generate, release, learn |
| 🌐 Browser & Scraping | 2 | Browse, scrape |
| 🛠️ Utilidades | 6 | Spec, careful, pair-agent, diagram, context-save/restore, skillify |

**Total: ~33 skills | 373 archivos**

---

## 🧠 Estrategia & Planning

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Office Hours** | [`office-hours/`](./office-hours/) | Sesión estilo YC: brainstorm, "¿vale la pena construir esto?", pensar en grande. |
| **Plan CEO Review** | [`plan-ceo-review/`](./plan-ceo-review/) | Revisión como fundador/CEO: estrategia, scope, visión más amplia. |
| **Plan Eng Review** | [`plan-eng-review/`](./plan-eng-review/) | Revisión como eng manager: arquitectura, implementación, riesgos técnicos. |
| **Plan Design Review** | [`plan-design-review/`](./plan-design-review/) | Revisión de diseñador: UX, visual, dimensiones de calidad (0-10). |
| **Plan DevEx Review** | [`plan-devex-review/`](./plan-devex-review/) | Revisión de developer experience: ergonomía, DX, facilidad de uso. |
| **Autoplan** | [`autoplan/`](./autoplan/) | Pipeline automático: corre CEO + Eng + Design + DevEx review en secuencia. |

---

## 🚀 Ship & Deploy

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Review** | [`review/`](./review/) | Pre-landing review: SQL safety, LLM trust boundaries, side effects. |
| **Ship** | [`ship/`](./ship/) | Workflow completo: merge base, tests, review, bump VERSION, CHANGELOG, PR. |
| **Land and Deploy** | [`land-and-deploy/`](./land-and-deploy/) | Merge y deploy a producción con verificación. |
| **Canary** | [`canary/`](./canary/) | Deploy canary: verificar en producción con subset de tráfico. |

---

## 🛡️ Seguridad

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **CSO** | [`cso/`](./cso/) | Chief Security Officer: OWASP Top 10, STRIDE, secrets archaeology, supply chain. |
| **Guard** | [`guard/`](./guard/) | Modo guardián: previene cambios peligrosos. |
| **Freeze / Unfreeze** | [`freeze/`](./freeze/) [`unfreeze/`](./unfreeze/) | Congelar/descongelar deploys (code freeze). |

---

## 🧪 QA & Testing

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **QA** | [`qa/`](./qa/) | QA completo: testea + encuentra bugs + los arregla + commitea fix + re-verifica. |
| **QA Only** | [`qa-only/`](./qa-only/) | Solo testing, sin arreglar (reporta los bugs). |
| **Benchmark** | [`benchmark/`](./benchmark/) | Benchmarking de performance. |

---

## 🎨 Diseño

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Design Consultation** | [`design-consultation/`](./design-consultation/) | Consultoría de diseño: investiga landscape, propone design system completo. |
| **Design HTML** | [`design-html/`](./design-html/) | Genera diseños en HTML real (no mockups). |
| **Design Review** | [`design-review/`](./design-review/) | Revisión de diseño de una implementación existente. |
| **Design Shotgun** | [`design-shotgun/`](./design-shotgun/) | Múltiples variantes de diseño rápidas para comparar. |

---

## 🔍 Debugging & Retrospectiva

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Investigate** | [`investigate/`](./investigate/) | Debugging sistemático con root cause analysis. |
| **Retro** | [`retro/`](./retro/) | Retrospectiva post-incidente o post-sprint. |

---

## 📝 Documentación & Aprendizaje

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Document Generate** | [`document-generate/`](./document-generate/) | Genera documentación del código/proyecto. |
| **Document Release** | [`document-release/`](./document-release/) | Release notes profesionales. |
| **Learn** | [`learn/`](./learn/) | Gestión de learnings del proyecto. |

---

## 🌐 Browser & Scraping

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Browse** | [`browse/`](./browse/) | Navegación web automatizada para research/testing. |
| **Scrape** | [`scrape/`](./scrape/) | Web scraping estructurado. |

---

## 🛠️ Utilidades

| Skill | Carpeta | Para qué sirve |
|-------|---------|----------------|
| **Spec** | [`spec/`](./spec/) | Crear especificaciones técnicas. |
| **Careful** | [`careful/`](./careful/) | Modo cuidadoso: extra verificación antes de cambios. |
| **Pair Agent** | [`pair-agent/`](./pair-agent/) | Pair programming con segundo agente. |
| **Diagram** | [`diagram/`](./diagram/) | Genera diagramas (arquitectura, flujos, etc.). |
| **Context Save/Restore** | [`context-save/`](./context-save/) [`context-restore/`](./context-restore/) | Guardar/restaurar contexto entre sesiones. |
| **Skillify** | [`skillify/`](./skillify/) | Convierte un workflow en skill (como Skill Creator). |

---

## 🏛️ Filosofía "Builder Ethos" (3 principios)

### 1. 🌊 Boil the Ocean
> "Completar todo cuesta casi nada con IA. No hay excusa para atajos."

| Tarea | Equipo humano | Con IA | Compresión |
|-------|--------------|--------|-----------|
| Boilerplate | 2 días | 15 min | ~100× |
| Tests | 1 día | 15 min | ~50× |
| Feature | 1 semana | 30 min | ~30× |
| Bug fix | 4 horas | 15 min | ~20× |
| Arquitectura | 2 días | 4 horas | ~5× |

### 2. 🔍 Search Before Building
> "¿Ya existe esto? Buscá antes de construir."

3 capas: Tried & True → New & Popular → First Principles.

### 3. 👑 User Sovereignty
> "La IA recomienda. El usuario decide. Siempre."

---

## 🔗 Fuente

- **Repo original:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Autor:** [Garry Tan](https://x.com/garrytan) — CEO de Y Combinator
- **Licencia:** MIT
- **Versión:** 1.68.3.0
