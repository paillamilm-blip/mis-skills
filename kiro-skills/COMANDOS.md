# ⚡ Comandos Rápidos — Referencia de las 86 Skills

> Copia y pega el comando exacto cuando trabajes con Kiro o cualquier agente IA.  
> Organizado por segmento. Cada skill tiene: trigger, qué le decís, y cuándo usarla.

---

## 📋 Índice de Segmentos

| # | Segmento | Skills | Para qué |
|---|----------|--------|----------|
| 01 | [Estrategia](#01--estrategia) | 15 | Pensar, planificar, especificar |
| 02 | [Ejecución](#02--ejecución) | 14 | Modos de trabajo y productividad |
| 03 | [Diseño](#03--diseño) | 15 | UI/UX, marca, visual |
| 04 | [Código y Calidad](#04--código-y-calidad) | 7 | Reviews y simplificación |
| 05 | [Testing y QA](#05--testing-y-qa) | 10 | Tests, debugging, performance |
| 06 | [Seguridad](#06--seguridad) | 5 | Hardening, auditorías, protección |
| 07 | [Deploy y Ship](#07--deploy-y-ship) | 7 | CI/CD, releases, deployment |
| 08 | [Automatización](#08--automatización) | 3 | Browser automation, scraping |
| 09 | [Documentación](#09--documentación) | 6 | Docs, ADRs, diagramas |
| 10 | [Utilidades](#10--utilidades) | 5 | Meta-skills, APIs, memoria |
| 11 | [Producto](#11--producto) | 1 | Específico de Sistema Ómicron |

---

## 01 — ESTRATEGIA

> 🧠 Pensar antes de actuar. Planificar. Validar ideas.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Superpowers** | `"Modo superpowers"` / `"Análisis profundo de..."` | Decisiones críticas, arquitectura, problemas complejos |
| 2 | **Context Mode** | `"Context mode"` / `"Analiza antes de cambiar"` | Antes de cualquier cambio complejo al codebase |
| 3 | **Office Hours** | `"Office hours"` / `"¿Vale la pena construir esto?"` | Brainstorm inicial, validar si algo merece tiempo |
| 4 | **Plan CEO Review** | `"Plan CEO review"` / `"Pensá más grande"` | Expandir scope, revisar estrategia de producto |
| 5 | **Plan Eng Review** | `"Plan eng review"` / `"Revisá la arquitectura"` | Validar que la implementación técnica sea sólida |
| 6 | **Plan Design Review** | `"Plan design review"` / `"Revisá el UX"` | Scoring 0-10 de cada dimensión de diseño |
| 7 | **Plan DevEx Review** | `"Plan devex review"` / `"¿Es fácil de usar para devs?"` | Developer experience, ergonomía de APIs |
| 8 | **Autoplan** | `"Autoplan"` / `"Corré todas las reviews"` | Pipeline automático: CEO+Eng+Design+DevEx |
| 9 | **Spec-Driven Dev** | `"Creá un spec para..."` / `"Especificá antes de codear"` | Formalizar requirements antes de implementar |
| 10 | **Planning & Breakdown** | `"Dividí esta tarea"` / `"Breakdown de..."` | Descomponer trabajo grande en pasos |
| 11 | **Idea Refine** | `"Refiná esta idea"` / `"Stress-test my plan"` | Ideas vagas → conceptos accionables |
| 12 | **Interview Me** | `"Interview me"` / `"Preguntame hasta entender"` | Extraer lo que realmente querés |
| 13 | **Spec (gstack)** | `"Spec técnica para..."` | Crear especificación técnica formal |
| 14 | **Doubt-Driven Dev** | `"Verificá esta decisión"` / `"Doubt mode"` | Review adversarial de decisiones no-triviales |
| 15 | **Context Engineering** | `"Optimizá el contexto"` / `"Setup de sesión"` | Configurar contexto óptimo para el agente |

---

## 02 — EJECUCIÓN

> 🚀 Modos de trabajo. Velocidad vs profundidad.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **GSD** | `"Hacelo"` / `"Dale"` / `"Modo GSD"` | Ejecutar rápido, sin preguntas innecesarias |
| 2 | **Claude Mem** | `"Recordá que..."` / `"Qué sabés de..."` / `"Olvidá..."` | Memoria persistente + tracking de progreso |
| 3 | **Incremental** | `"De a poco"` / `"Entregá incrementalmente"` | Nunca entregar todo de golpe |
| 4 | **Source-Driven** | `"Basate en la documentación oficial"` | Código fundamentado en docs oficiales |
| 5 | **Ponytail** | `"Ponytail"` / `"Lazy mode"` / `"Lo más simple"` | Forzar la solución más simple (YAGNI) |
| 6 | **Ponytail Audit** | `"Ponytail audit"` | Escanear TODO el repo buscando qué sobra |
| 7 | **Ponytail Review** | `"Ponytail review"` | Code review anti-overengineering |
| 8 | **Ponytail Debt** | `"Ponytail debt"` | Rastrear shortcuts deliberados |
| 9 | **Ponytail Gain** | `"Ponytail gain"` | Scoreboard: cuánto ahorraste |
| 10 | **Ponytail Help** | `"Ponytail help"` | Cheatsheet de todos los comandos ponytail |
| 11 | **Careful** | `"Modo careful"` / `"Extra verificación"` | Cuando un error sería costoso |
| 12 | **Pair Agent** | `"Pair conmigo"` / `"Pair programming"` | Sesión de pair programming con segundo agente |
| 13 | **Context Save** | `"Guardá el contexto"` | Persistir estado de sesión actual |
| 14 | **Context Restore** | `"Restaurá el contexto"` | Recuperar sesión anterior |

---

## 03 — DISEÑO

> 🎨 UI, UX, marca, identidad visual, animaciones.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Impeccable** | `"Diseñá [superficie]"` / `"UI nivel award"` | Diseño de nivel director. El más potente. |
| 2 | **Taste Skill** | `"Landing anti-slop"` / `"Con gusto"` | Landing pages que NO se ven hechas por IA |
| 3 | **Design** | `"Diseñá un logo"` / `"CIP para..."` / `"Ícono para..."` | Skill unificada: logos, CIP, banners, íconos |
| 4 | **Design System** | `"Tokens para..."` / `"Design system"` | Tokens 3 capas + CSS variables + Tailwind |
| 5 | **Brand** | `"Identidad de marca"` / `"Voz de marca"` | Brand guidelines, voz, assets |
| 6 | **Banner Design** | `"Banner para [plataforma]"` | 22 estilos × todas las plataformas |
| 7 | **Slides** | `"Presentación sobre [tema]"` | Slides HTML con Chart.js y copywriting |
| 8 | **UI Styling** | `"Componente [X] con shadcn"` | shadcn/ui + Radix + Tailwind + dark mode |
| 9 | **UI/UX Pro Max** | `"Paleta para..."` / `"Font pairing"` / `"Estilo para..."` | DB: 84 estilos, 192 paletas, 74 fonts |
| 10 | **UI Verification** | `"Verificá la UI contra el diseño"` | QA visual: ¿la UI matchea la spec? |
| 11 | **Animate** | `"Animá esto"` / `"Transición para..."` | Animaciones con filosofía Emil Kowalski |
| 12 | **Frontend UI Eng** | `"Hacelo accesible"` / `"Responsive + WCAG"` | Accesibilidad + responsive production-quality |
| 13 | **Design Consultation** | `"Consultá diseño para..."` / `"Design system from scratch"` | Research landscape + propuesta completa |
| 14 | **Design Review (gstack)** | `"Revisá el diseño de esta implementación"` | Auditoría de diseño sobre código existente |
| 15 | **Design Shotgun** | `"Dame variantes de diseño"` / `"Múltiples opciones"` | Genera varias opciones rápidas para comparar |

---

## 04 — CÓDIGO Y CALIDAD

> 🔍 Reviews, simplificación, APIs.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Code Review Ultra** | `"Ultra review"` / `"Revisión profunda"` | Auditoría 6 dimensiones (seguridad, perf, arq, etc.) |
| 2 | **Code Review** | `"Review rápido"` / `"Revisá este código"` | Revisión estándar: bugs, edge cases, imports |
| 3 | **Code Review & Quality** | `"Multi-axis review"` | Review multi-eje antes de merge (Addy) |
| 4 | **Code Simplification** | `"Simplificá esto"` / `"Refactoreá para claridad"` | Reducir complejidad sin cambiar comportamiento |
| 5 | **Review (gstack)** | `"Pre-landing review"` / `"Check my diff"` | SQL safety, LLM trust, side effects, specialists |
| 6 | **DevEx Review** | `"Developer experience review"` | ¿Es ergonómico para otros devs? |
| 7 | **API & Interface Design** | `"Diseñá esta API"` / `"Contratos entre módulos"` | REST, GraphQL, type contracts, boundaries |

---

## 05 — TESTING Y QA

> 🧪 Tests, debugging, performance, retrospectivas.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **QA Skill** | `"QA skill"` / `"Qué errores he tenido"` | Aprende de errores. Pre-flight antes de cambios. |
| 2 | **TDD** | `"Test first"` / `"TDD para..."` | Tests primero, código después |
| 3 | **Debugging & Recovery** | `"Debug esto"` / `"Root cause"` | Debugging sistemático, no adivinanzas |
| 4 | **Browser Testing** | `"Testeá en browser"` / `"Chrome DevTools"` | Testing con browser real via DevTools MCP |
| 5 | **QA (gstack)** | `"QA test this"` / `"Testeá y arreglá"` | QA completo: testea + encuentra + arregla + verifica |
| 6 | **QA Only** | `"Solo testear, no arreglar"` | Reporta bugs sin tocar el código |
| 7 | **Investigate** | `"Investigá este bug"` / `"Root cause analysis"` | Debugging profundo con RCA |
| 8 | **Benchmark** | `"Benchmark de performance"` | Medir performance con datos |
| 9 | **Retro** | `"Retro del sprint"` / `"Retrospectiva"` | Análisis post-mortem o post-feature |
| 10 | **Performance Opt** | `"Optimizá performance"` / `"Core Web Vitals"` | Web Vitals, N+1, profiling, lazy loading |

---

## 06 — SEGURIDAD

> 🛡️ Protección, auditorías, hardening.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Security & Hardening** | `"Hardening de seguridad"` / `"Revisá inputs"` | Input validation, auth, GDPR, datos sensibles |
| 2 | **CSO** | `"Security audit"` / `"OWASP review"` / `"CSO mode"` | Auditoría COMPLETA: OWASP, STRIDE, supply chain |
| 3 | **Guard** | `"Guard mode"` / `"Protegé de cambios peligrosos"` | Prevenir cambios que puedan romper cosas |
| 4 | **Freeze** | `"Freeze"` / `"Code freeze"` | Congelar deploys (antes de release importante) |
| 5 | **Unfreeze** | `"Unfreeze"` / `"Descongelá"` | Descongelar después del freeze |

---

## 07 — DEPLOY Y SHIP

> 🚀 Releases, CI/CD, versioning, deployment.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Shipping & Launch** | `"Checklist pre-deploy"` / `"Preparar launch"` | Checklist completo antes de producción |
| 2 | **CI/CD & Automation** | `"Setup CI/CD"` / `"Pipeline para..."` | Configurar pipelines y quality gates |
| 3 | **Git Workflow** | `"Semver bump"` / `"Changelog"` / `"Git flow"` | Commits, branches, releases, tags |
| 4 | **Deprecation & Migration** | `"Deprecar [X]"` / `"Migrar de [A] a [B]"` | Retirar sistemas viejos de forma segura |
| 5 | **Ship (gstack)** | `"Ship it"` / `"Creá PR"` / `"Push to main"` | Workflow: tests→review→version→changelog→PR |
| 6 | **Land & Deploy** | `"Deploy"` / `"Merge y deploy"` | Merge + verificación en producción |
| 7 | **Canary** | `"Canary deploy"` / `"Deploy gradual"` | Deploy con subset de tráfico primero |

---

## 08 — AUTOMATIZACIÓN

> 🤖 Browser automation, web scraping, workflows.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Nova Act** | `"Automatizá [acción] en [sitio]"` / `"Scrapeá datos"` | SDK Amazon: automation con IA, testing E2E |
| 2 | **Browse** | `"Navegá a [URL]"` / `"Abrí en browser"` | Navegación web automatizada para research |
| 3 | **Scrape** | `"Scrape [sitio]"` / `"Extraé datos de..."` | Web scraping estructurado |

---

## 09 — DOCUMENTACIÓN

> 📝 Docs, decisiones, release notes, diagramas.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Documentation & ADRs** | `"Documentá esta decisión"` / `"ADR para..."` | Registrar decisiones arquitecturales |
| 2 | **Observability** | `"Agregá logging"` / `"Métricas para..."` | Logging, métricas, tracing, alerting |
| 3 | **Document Generate** | `"Generá documentación"` | Documentación automática del código |
| 4 | **Document Release** | `"Release notes"` / `"Notas de versión"` | Release notes profesionales |
| 5 | **Learn** | `"Qué aprendimos"` / `"Learnings del proyecto"` | Gestionar learnings persistentes |
| 6 | **Diagram** | `"Diagrama de [arquitectura/flujo]"` | Generar diagramas visuales |

---

## 10 — UTILIDADES

> 🛠️ Meta-skills, APIs, memoria de código.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Skill Creator** | `"Creá una skill para..."` | Convertir un workflow en skill reutilizable |
| 2 | **Codebase Memory** | `"Indexá el codebase"` / `"Mapa del código"` | Navegar repos grandes instantáneamente |
| 3 | **Public APIs** | `"Qué API para [X]?"` | Catálogo +1400 APIs gratuitas |
| 4 | **Skillify** | `"Skillify este proceso"` | Convertir workflow en skill (versión gstack) |
| 5 | **Using Agent Skills** | `"Qué skill aplica aquí?"` | Meta-skill: descubrir la skill correcta |

---

## 11 — PRODUCTO

> 🧬 Skills específicas del negocio.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **ADN Digital** | `"Procesá este CV"` / `[pegar texto de CV]` | Transformar CV en ADN Digital JSON (Sistema Ómicron) |

---

## 🏃 Quick Reference — Los 10 comandos que más usarás

```
1. "Hacelo"                    → GSD (ejecutar rápido)
2. "Modo superpowers"          → Superpowers (calidad máxima)
3. "Ponytail"                  → Solución más simple
4. "Ultra review"              → Code Review Ultra
5. "Ship it"                   → Ship (workflow completo de release)
6. "QA test this"              → QA en browser real
7. "Office hours"              → Brainstorm estilo YC
8. "Autoplan"                  → Pipeline CEO+Eng+Design review
9. "Security audit"            → CSO (OWASP + STRIDE)
10. "Dame variantes de diseño" → Design Shotgun
```
