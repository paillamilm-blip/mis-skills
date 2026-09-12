# ⚡ Comandos Rápidos — Referencia de las 115 Skills

> Copia y pega el comando exacto cuando trabajes con Kiro o cualquier agente IA.
> Organizado por segmento. Cada skill tiene: trigger, qué le decís, y cuándo usarla.
> Conteo verificado con `scripts/contar-skills.sh`.

---

## 📋 Índice de Segmentos

| # | Segmento | Skills | Para qué |
|---|----------|--------|----------|
| 01 | [Estrategia](#01--estrategia) | 14 | Pensar, planificar, especificar |
| 02 | [Ejecución](#02--ejecución) | 15 | Modos de trabajo y productividad |
| 03 | [Diseño](#03--diseño) | 16 | UI/UX, marca, visual |
| 04 | [Código y Calidad](#04--código-y-calidad) | 8 | Reviews y simplificación |
| 05 | [Testing y QA](#05--testing-y-qa) | 12 | Tests, debugging, performance |
| 06 | [Seguridad](#06--seguridad) | 6 | Hardening, auditorías, pentesting |
| 07 | [Deploy y Ship](#07--deploy-y-ship) | 8 | CI/CD, releases, deployment |
| 08 | [Automatización](#08--automatización) | 14 | Browser automation, scraping, acceso web |
| 09 | [Documentación](#09--documentación) | 6 | Docs, ADRs, diagramas |
| 10 | [Utilidades](#10--utilidades) | 4 | Meta-skills, APIs, memoria |
| 11 | [Producto](#11--producto) | 1 | Específico de Sistema Ómicron |
| 12 | [Marketing y Content](#12--marketing-y-content) | 11 | Briefs, blog, social, PRD |

---

## 01 — ESTRATEGIA

> 🧠 Pensar antes de actuar. Planificar. Validar ideas.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Superpowers** | `"Modo superpowers"` / `"Análisis profundo de..."` | Decisiones críticas, arquitectura, problemas complejos |
| 2 | **Superpowers Obra** | `"Superpowers obra"` | Variante con metodología obra para razonamiento máximo |
| 3 | **Context Mode** | `"Context mode"` / `"Analiza antes de cambiar"` | Antes de cualquier cambio complejo al codebase |
| 4 | **Office Hours** | `"Office hours"` / `"¿Vale la pena construir esto?"` | Brainstorm inicial, validar si algo merece tiempo |
| 5 | **Plan CEO Review** | `"Plan CEO review"` / `"Pensá más grande"` | Expandir scope, revisar estrategia de producto |
| 6 | **Plan Eng Review** | `"Plan eng review"` / `"Revisá la arquitectura"` | Validar que la implementación técnica sea sólida |
| 7 | **Plan Design Review** | `"Plan design review"` / `"Revisá el UX"` | Scoring 0-10 de cada dimensión de diseño |
| 8 | **Plan DevEx Review** | `"Plan devex review"` / `"¿Es fácil de usar para devs?"` | Developer experience, ergonomía de APIs |
| 9 | **Autoplan** | `"Autoplan"` / `"Corré todas las reviews"` | Pipeline automático: CEO+Eng+Design+DevEx |
| 10 | **Spec-Driven Dev** | `"Creá un spec para..."` / `"Especificá antes de codear"` | Formalizar requirements antes de implementar |
| 11 | **Planning & Breakdown** | `"Dividí esta tarea"` / `"Breakdown de..."` | Descomponer trabajo grande en pasos |
| 12 | **Idea Refine** | `"Refiná esta idea"` / `"Stress-test my plan"` | Ideas vagas → conceptos accionables |
| 13 | **Interview Me** | `"Interview me"` / `"Preguntame hasta entender"` | Extraer lo que realmente querés |
| 14 | **Doubt-Driven Dev** | `"Verificá esta decisión"` / `"Doubt mode"` | Review adversarial de decisiones no-triviales |

---

## 02 — EJECUCIÓN

> 🚀 Modos de trabajo. Velocidad vs profundidad.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **GSD** | `"Hacelo"` / `"Dale"` / `"Modo GSD"` | Ejecutar rápido, sin preguntas innecesarias |
| 2 | **Claude Mem** | `"Recordá que..."` / `"Qué sabés de..."` / `"Olvidá..."` | Memoria persistente + tracking de progreso |
| 3 | **Incremental Implementation** | `"De a poco"` / `"Entregá incrementalmente"` | Nunca entregar todo de golpe |
| 4 | **Source-Driven Dev** | `"Basate en la documentación oficial"` | Código fundamentado en docs oficiales |
| 5 | **Ponytail** | `"Ponytail"` / `"Lazy mode"` / `"Lo más simple"` | Forzar la solución más simple (YAGNI) |
| 6 | **Ponytail Audit** | `"Ponytail audit"` | Escanear TODO el repo buscando qué sobra |
| 7 | **Ponytail Review** | `"Ponytail review"` | Code review anti-overengineering |
| 8 | **Ponytail Debt** | `"Ponytail debt"` | Rastrear shortcuts deliberados |
| 9 | **Careful** | `"Modo careful"` / `"Extra verificación"` | Cuando un error sería costoso |
| 10 | **Pair Agent** | `"Pair conmigo"` / `"Pair programming"` | Sesión de pair programming con segundo agente |
| 11 | **Dispatching Parallel Agents** | `"Lanzá agentes en paralelo"` | Repartir trabajo independiente entre subagentes |
| 12 | **Subagent-Driven Dev** | `"Delegá a subagentes"` | Desarrollo orquestando subagentes |
| 13 | **Executing Plans** | `"Ejecutá el plan"` | Llevar a cabo un plan ya definido, paso a paso |
| 14 | **Context Save** | `"Guardá el contexto"` | Persistir estado de sesión actual |
| 15 | **Context Restore** | `"Restaurá el contexto"` | Recuperar sesión anterior |

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
| 16 | **Obra Maestra** (combo) | `"OBRA MAESTRA [qué diseñar]"` / `"Diseño pro"` | 🏆 Combo potenciado: taste + pro-max + impeccable + animate en 1 pipeline |

---

## 04 — CÓDIGO Y CALIDAD

> 🔍 Reviews, simplificación, APIs.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Code Review Ultra** | `"Ultra review"` / `"Revisión profunda"` | Auditoría 6 dimensiones (seguridad, perf, arq, etc.) |
| 2 | **Code Review & Quality** | `"Multi-axis review"` / `"Revisá este código"` | Revisión multi-eje antes de merge |
| 3 | **Code Simplification** | `"Simplificá esto"` / `"Refactoreá para claridad"` | Reducir complejidad sin cambiar comportamiento |
| 4 | **Review (gstack)** | `"Pre-landing review"` / `"Check my diff"` | SQL safety, LLM trust, side effects, specialists |
| 5 | **DevEx Review** | `"Developer experience review"` | ¿Es ergonómico para otros devs? |
| 6 | **API & Interface Design** | `"Diseñá esta API"` / `"Contratos entre módulos"` | REST, GraphQL, type contracts, boundaries |
| 7 | **Requesting Code Review** | `"Pedí review de este cambio"` | Preparar un cambio para que lo revisen bien |
| 8 | **Receiving Code Review** | `"Ayudame a procesar este review"` | Recibir e incorporar feedback con rigor |

---

## 05 — TESTING Y QA

> 🧪 Tests, debugging, performance, retrospectivas.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **QA Skill** | `"QA skill"` / `"Qué errores he tenido"` | Aprende de errores. Pre-flight antes de cambios. |
| 2 | **TDD** | `"Test first"` / `"TDD para..."` | Tests primero, código después |
| 3 | **Debugging & Recovery** | `"Debug esto"` / `"Root cause"` | Debugging sistemático, no adivinanzas |
| 4 | **Systematic Debugging** | `"Debugging sistemático"` | Método obra de root cause paso a paso |
| 5 | **Browser Testing** | `"Testeá en browser"` / `"Chrome DevTools"` | Testing con browser real via DevTools MCP |
| 6 | **QA (gstack)** | `"QA test this"` / `"Testeá y arreglá"` | QA completo: testea + encuentra + arregla + verifica |
| 7 | **QA Only** | `"Solo testear, no arreglar"` | Reporta bugs sin tocar el código |
| 8 | **Investigate** | `"Investigá este bug"` / `"Root cause analysis"` | Debugging profundo con RCA |
| 9 | **Benchmark** | `"Benchmark de performance"` | Medir performance con datos |
| 10 | **Retro** | `"Retro del sprint"` / `"Retrospectiva"` | Análisis post-mortem o post-feature |
| 11 | **Performance Opt** | `"Optimizá performance"` / `"Core Web Vitals"` | Web Vitals, N+1, profiling, lazy loading |
| 12 | **Verification Before Completion** | `"Verificá antes de dar por listo"` | Chequeo final antes de decir "terminado" |

---

## 06 — SEGURIDAD

> 🛡️ Protección, auditorías, hardening, pentesting.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Security & Hardening** | `"Hardening de seguridad"` / `"Revisá inputs"` | Input validation, auth, GDPR, datos sensibles |
| 2 | **CSO** | `"Security audit"` / `"OWASP review"` / `"CSO mode"` | Auditoría COMPLETA: OWASP, STRIDE, supply chain |
| 3 | **Guard** | `"Guard mode"` / `"Protegé de cambios peligrosos"` | Prevenir cambios que puedan romper cosas |
| 4 | **Freeze** | `"Freeze"` / `"Code freeze"` | Congelar deploys (antes de release importante) |
| 5 | **Unfreeze** | `"Unfreeze"` / `"Descongelá"` | Descongelar después del freeze |
| 6 | **Strix** | `"Pentest con Strix"` / `"Buscá vulnerabilidades"` / `"OWASP Top 10"` | Pentesting autónomo con IA que valida con PoC real (9 sub-skills) |

---

## 07 — DEPLOY Y SHIP

> 🚀 Releases, CI/CD, versioning, deployment.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Shipping & Launch** | `"Checklist pre-deploy"` / `"Preparar launch"` | Checklist completo antes de producción |
| 2 | **CI/CD & Automation** | `"Setup CI/CD"` / `"Pipeline para..."` | Configurar pipelines y quality gates |
| 3 | **Git Workflow & Versioning** | `"Semver bump"` / `"Changelog"` / `"Git flow"` | Commits, branches, releases, tags |
| 4 | **Deprecation & Migration** | `"Deprecar [X]"` / `"Migrar de [A] a [B]"` | Retirar sistemas viejos de forma segura |
| 5 | **Ship (gstack)** | `"Ship it"` / `"Creá PR"` / `"Push to main"` | Workflow: tests→review→version→changelog→PR |
| 6 | **Land & Deploy** | `"Deploy"` / `"Merge y deploy"` | Merge + verificación en producción |
| 7 | **Canary** | `"Canary deploy"` / `"Deploy gradual"` | Deploy con subset de tráfico primero |
| 8 | **Finishing a Branch** | `"Terminá esta rama"` / `"Integrá el trabajo"` | Integrar trabajo completado de una rama |

---

## 08 — AUTOMATIZACIÓN

> 🤖 Browser automation, web scraping, clonación, acceso a internet, workflows.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **AUTOMATIZAR-WEB** ⚡ | `"AUTOMATIZAR [tarea]"` / `"EXTRAER / LLENAR / MONITOREAR / GRABAR"` | **POWER SUITE**: 4 skills + 8 capacidades combinadas |
| 2 | **Agent-Browser** | `"Navegá / clickeá / extraé con el browser"` | CLI browser automation (navegar, click, extraer, grabar) |
| 3 | **Nova Act** | `"Automatizá [acción] en [sitio]"` | SDK Amazon: automation con IA, testing E2E |
| 4 | **Browse** | `"Navegá a [URL]"` / `"Abrí en browser"` | Navegación web automatizada para research |
| 5 | **Scrape** | `"Scrape [sitio]"` / `"Extraé datos de..."` | Web scraping estructurado |
| 6 | **CLONAR** ⚡ | `"CLONAR [url]"` / `"Cloná este sitio"` | **COMBO**: Fiel (fuente real) o Recrear (Next.js moderno) |
| 7 | **AI Website Cloner** | `"Clone website"` / `"Pixel-perfect clone"` | Reconstruir sitio en Next.js moderno con builders AI |
| 8 | **Web Clone (Fiel)** | `"Clonar fielmente"` / `"Mirror site"` | Extraer código fuente real, sin alucinaciones IA |
| 9 | **HTML-Anything** | `"Generá un HTML/reporte/presentación"` | Generar HTML profesional sandboxed |
| 10 | **MicroSandbox** | `"Ejecutá esto en sandbox"` | Correr código en microVMs aisladas |
| 11 | **Firecrawl** | `"Firecrawl scrape/search/interact/build"` | Suite Firecrawl: web→Markdown, buscar, clicks/forms, integrar datos |
| 12 | **ScrapeGraph-AI** | `"Scrapear con IA"` / `"Extraé datos estructurados"` | Librería Python: describís qué querés → JSON (sin selectores) |
| 13 | **ScrapeGraph MCP** | `"Conectá scrapegraph por MCP"` / `"Convertí web a markdown"` | ScrapeGraph vía MCP: scrape/extract/search/crawl/monitor gestionado por API |
| 14 | **Agent Reach** | `"Investigá X en internet"` / `"Resumí este video/tweet/repo"` | Ojos de internet: leer/buscar en 15 plataformas sin APIs de pago |

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
| 1 | **Skill Creator** | `"Creá una skill para..."` / `"Skillify este proceso"` | Convertir un workflow en skill reutilizable |
| 2 | **Codebase Memory** | `"Indexá el codebase"` / `"Mapa del código"` | Navegar repos grandes instantáneamente |
| 3 | **Public APIs** | `"Qué API para [X]?"` | Catálogo +1400 APIs gratuitas |
| 4 | **LeanKG** | `"Knowledge graph del código"` | Grafo de conocimiento del codebase |

---

## 11 — PRODUCTO

> 🧬 Skills específicas del negocio.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **ADN Digital** | `"Procesá este CV"` / `[pegar texto de CV]` | Transformar CV en ADN Digital JSON (Sistema Ómicron) |

---

## 12 — MARKETING Y CONTENT

> 📣 De un PR a contenido de lanzamiento: briefs, blog, redes, PRD.

| # | Skill | Comando / Trigger | Cuándo usar |
|---|-------|-------------------|-------------|
| 1 | **Marketing Brief** | `"Marketing brief de este PR"` | Brief profesional desde un PR / feature |
| 2 | **Marketing Pipeline** | `"Marketing pipeline"` | Flujo completo de lanzamiento (brief→posts→blog) |
| 3 | **Blog Post** | `"Escribí un blog post sobre..."` | Artículo SEO-optimizado |
| 4 | **Social Copy** | `"Posts para Twitter/LinkedIn"` | Copy para redes sociales |
| 5 | **Newsletter** | `"Newsletter de lanzamiento"` | Email de anuncio |
| 6 | **Video Script** | `"Guión de video de producto"` | Script de video demo/producto |
| 7 | **YouTube Copy** | `"Título + descripción de YouTube"` | Metadata optimizada de YouTube |
| 8 | **To PRD** | `"Convertí esto en un PRD"` | Product Requirements Document |
| 9 | **Changelog** | `"Changelog de estos cambios"` | Historial de cambios profesional |
| 10 | **Presentation** | `"Deck técnico con Slidev"` | Presentación técnica |
| 11 | **Teach Me** | `"Creá un curso/tutorial de..."` | Generar cursos o tutoriales |

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
