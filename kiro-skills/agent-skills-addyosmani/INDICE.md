# 🧰 Agent Skills — by Addy Osmani

> Colección de skills profesionales para agentes de código de [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).  
> Licencia: MIT

---

## 📊 Resumen

| Categoría | Skills | Enfoque |
|-----------|--------|---------|
| 🏗️ Planificación | 4 | Specs, tareas, ideas, entrevistas |
| 💻 Desarrollo | 4 | TDD, incremental, source-driven, frontend |
| 🔍 Calidad | 4 | Review, simplificación, debugging, doubt-driven |
| 🚀 Deploy | 4 | CI/CD, shipping, git workflow, deprecation |
| 🛡️ Robustez | 3 | Seguridad, observabilidad, performance |
| 🎯 Especialidades | 5 | APIs, browser testing, docs, context, meta-skill |

**Total: 24 skills | 83 archivos**

---

## 🏗️ Planificación y Diseño

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 1 | **Spec-Driven Development** | [`spec-driven-development/`](./spec-driven-development/) | Crea especificaciones ANTES de codear. Descompone requirements vagos en capability maps. |
| 2 | **Planning & Task Breakdown** | [`planning-and-task-breakdown/`](./planning-and-task-breakdown/) | Divide trabajo grande en tareas ordenadas e implementables. Estima scope. |
| 3 | **Idea Refine** | [`idea-refine/`](./idea-refine/) | Refina ideas vagas en conceptos accionables. Pensamiento divergente → convergente. |
| 4 | **Interview Me** | [`interview-me/`](./interview-me/) | Extrae lo que realmente querés (no lo que decís). Preguntas 1 a 1 hasta 95% confianza. |

---

## 💻 Desarrollo

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 5 | **Test-Driven Development** | [`test-driven-development/`](./test-driven-development/) | Escribe tests primero, después código. Prueba que funciona antes de avanzar. |
| 6 | **Incremental Implementation** | [`incremental-implementation/`](./incremental-implementation/) | Entrega cambios incrementalmente, nunca todo de golpe. |
| 7 | **Source-Driven Development** | [`source-driven-development/`](./source-driven-development/) | Basa cada decisión en documentación oficial. Código citado y actualizado. |
| 8 | **Frontend UI Engineering** | [`frontend-ui-engineering/`](./frontend-ui-engineering/) | UIs accesibles, responsive, production-quality. No se ve "hecho por IA". |

---

## 🔍 Calidad y Revisión

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 9 | **Code Review & Quality** | [`code-review-and-quality/`](./code-review-and-quality/) | Review multi-eje antes de merge. |
| 10 | **Code Simplification** | [`code-simplification/`](./code-simplification/) | Refactoring para claridad sin cambiar comportamiento. |
| 11 | **Debugging & Error Recovery** | [`debugging-and-error-recovery/`](./debugging-and-error-recovery/) | Debugging sistemático: root cause, no adivinanzas. |
| 12 | **Doubt-Driven Development** | [`doubt-driven-development/`](./doubt-driven-development/) | Review adversarial de cada decisión no-trivial. Verificar > debuggear después. |

---

## 🚀 Deploy y Operaciones

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 13 | **CI/CD & Automation** | [`ci-cd-and-automation/`](./ci-cd-and-automation/) | Setup de pipelines, quality gates, deployment strategies. |
| 14 | **Shipping & Launch** | [`shipping-and-launch/`](./shipping-and-launch/) | Checklist pre-launch, monitoring, staged rollout, rollback strategy. |
| 15 | **Git Workflow & Versioning** | [`git-workflow-and-versioning/`](./git-workflow-and-versioning/) | Commits, branches, releases, semver, changelogs. |
| 16 | **Deprecation & Migration** | [`deprecation-and-migration/`](./deprecation-and-migration/) | Migrar o retirar sistemas viejos de forma segura. |

---

## 🛡️ Robustez y Performance

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 17 | **Security & Hardening** | [`security-and-hardening/`](./security-and-hardening/) | Hardening contra vulnerabilidades. Input, auth, GDPR, datos. |
| 18 | **Observability & Instrumentation** | [`observability-and-instrumentation/`](./observability-and-instrumentation/) | Logging, métricas, tracing, alerting en producción. |
| 19 | **Performance Optimization** | [`performance-optimization/`](./performance-optimization/) | Core Web Vitals, N+1 queries, profiling, optimización. |

---

## 🎯 Especialidades

| # | Skill | Carpeta | Para qué sirve |
|---|-------|---------|----------------|
| 20 | **API & Interface Design** | [`api-and-interface-design/`](./api-and-interface-design/) | Diseño de APIs estables (REST, GraphQL, contratos entre módulos). |
| 21 | **Browser Testing with DevTools** | [`browser-testing-with-devtools/`](./browser-testing-with-devtools/) | Testing en browser real via Chrome DevTools MCP. DOM, network, performance. |
| 22 | **Documentation & ADRs** | [`documentation-and-adrs/`](./documentation-and-adrs/) | Documenta decisiones arquitecturales y cambios para el futuro. |
| 23 | **Context Engineering** | [`context-engineering/`](./context-engineering/) | Optimiza el setup de contexto del agente. Rules files, memoria. |
| 24 | **Using Agent Skills** | [`using-agent-skills/`](./using-agent-skills/) | Meta-skill: cómo descubrir y usar todas las demás skills. |

---

## 🚀 Cómo usarlas

### En Kiro (`.kiro/skills/`)
```bash
# Copiar una skill individual
cp -r agent-skills-addyosmani/spec-driven-development/ mi-proyecto/.kiro/skills/

# Copiar todas
cp -r agent-skills-addyosmani/*/skill.md mi-proyecto/.kiro/skills/
```

### En Claude (`.claude/commands/` o CLAUDE.md)
Las skills también vienen con formato compatible para Claude Code. Ver `CLAUDE.md` en esta carpeta.

### En otros agentes
Cada carpeta tiene un `skill.md` que funciona como prompt universal.

---

## 🔗 Fuente

- **Repo original:** [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **Autor:** [Addy Osmani](https://github.com/addyosmani) (Google Chrome team)
- **Licencia:** MIT
