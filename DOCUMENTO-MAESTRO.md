# 🧠 DOCUMENTO MAESTRO — Mis Skills + Combos + Cadenas

> Todo lo que necesitás para trabajar con Kiro en una sola página.  
> Autor: paillamilm-blip | Última actualización: Septiembre 2026 · 115 skills en 12 segmentos

---

---

## 🏆 RANKING DE COMBOS Y LOOPS

> Reanálisis completo (modo *superpowers*) sobre las 115 skills reales, incluidas las
> nuevas de investigación/scraping/seguridad. Reemplaza los combos y cadenas viejos.
>
> **Combo** = secuencia lineal (A → B → C, una pasada).
> **Loop** = ciclo que se repite hasta cumplir una condición de salida (⟳).
>
> **Cómo se puntúa (0–100):** `Impacto` (cuánto resuelve) + `Frecuencia` (cuán seguido lo usarás) + `Palanca` (cuánto multiplica vs hacerlo suelto) − `Fricción` (setup/costo/riesgo).

---

### 🥇 TABLA MAESTRA — Top 15 rankeado

| # | Nombre | Tipo | Cadena de skills | Score | Segmento |
|---|--------|------|------------------|:-----:|----------|
| 1 | 🏗️ **CONSTRUIR** | combo | Office Hours → Autoplan → Spec → GSD+Incremental → Ultra Review → Ship | **95** | full-stack |
| 2 | 🔎 **INVESTIGAR** | combo | Agent Reach (leer web/redes) → ScrapeGraph (extraer JSON) → Superpowers (sintetizar) | **93** | research |
| 3 | 🎨 **OBRA MAESTRA** | combo⚙️ | taste → ui-ux-pro-max → impeccable → animate *(ya es skill real)* | **92** | diseño |
| 4 | 🐛 **CAZA-BUGS** ⟳ | loop | Investigate → Superpowers → fix (GSD) → QA → *si falla* ⟳ vuelve al fix | **90** | debugging |
| 5 | 🛡️ **PENTEST** ⟳ | loop | Strix (scan) → priorizar → fix → Strix (re-scan) → *hasta 0 críticas* ⟳ | **89** | seguridad |
| 6 | ⚡ **HACER-BIEN** ⟳ | loop | GSD+Ponytail → Verification-Before-Completion → *si no pasa* ⟳ ajustar | **88** | ejecución |
| 7 | 🧪 **TDD** ⟳ | loop | TDD (test rojo) → GSD (código) → test verde → *si rojo* ⟳ / refactor | **86** | testing |
| 8 | 🚀 **LANZAR** | combo | Ultra Review → CSO (security) → Shipping checklist → Ship → Land & Deploy | **85** | deploy |
| 9 | 📊 **PIPELINE DE DATOS** | combo | ScrapeGraph MCP → microsandbox (analizar) → html-anything (reporte) | **84** | automatización |
| 10 | 🔒 **BLINDAR** | combo | Context Mode → Careful → Security & Hardening → CSO → Ultra Review → Ship | **82** | seguridad |
| 11 | 🎨 **DISEÑO** ⟳ | loop | Design Shotgun → Impeccable → UI Verification → *si no matchea* ⟳ Impeccable | **81** | diseño |
| 12 | 🧹 **LIMPIAR** | combo | Ponytail Audit → Code Simplification → Ponytail Review → Ultra Review → Retro | **79** | calidad |
| 13 | 👀 **VIGILANCIA** ⟳ | loop | ScrapeGraph monitor → *detecta cambio* → notifica → ⟳ (job programado) | **77** | automatización |
| 14 | 📣 **COMUNICAR** | combo | Ship → Marketing Brief → Social Copy → Blog Post → Newsletter | **75** | marketing |
| 15 | 🧬 **PERFIL** | combo | [pegar CV] → ADN Digital → Impeccable (portfolio) → Ship | **72** | producto |

⚙️ = ya existe como skill ejecutable (`03-diseno/obra-maestra`), no hay que recrearla.
⟳ = loop (se repite hasta la condición de salida).

---

### 🔥 Los 5 que más vas a usar (día a día)

| Combo | Frase para Kiro | Cuándo |
|-------|-----------------|--------|
| ⚡ **HACER** | `"Hacelo: [tarea]"` | 80% de las tareas |
| 🔎 **INVESTIGAR** | `"Investigá [tema] en internet y resumí"` | Antes de decidir/construir algo |
| 🎨 **OBRA MAESTRA** | `"OBRA MAESTRA [pantalla]"` | Cualquier UI que tiene que verse pro |
| 🔍 **REVISAR + LANZAR** | `"Ultra review y ship it"` | Cerrar un PR con calidad |
| 🐛 **CAZA-BUGS** | `"Investigá y arreglá [error]"` | Bug que no cede a la primera |

---

### ⟳ Los Loops explicados (lo nuevo)

Un loop no termina en un paso: **se repite hasta cumplir una condición de salida**. Le decís la meta y Kiro itera solo.

```
🐛 CAZA-BUGS    → repite fix→test   HASTA que el test pasa
🛡️ PENTEST      → repite scan→fix   HASTA 0 vulnerabilidades críticas
🧪 TDD          → repite código→test HASTA que todo está verde
🎨 DISEÑO       → repite diseño→QA   HASTA que matchea la spec visual
⚡ HACER-BIEN   → repite hasta que Verification-Before-Completion da OK
👀 VIGILANCIA   → repite en el tiempo (job programado) vigilando cambios
```

**Cómo dispararlos:** `"Loop de pentest sobre CausasPro hasta cerrar las críticas"` — Kiro corre Strix, arregla, re-escanea, y repite reportándote cada vuelta hasta la condición.

---

### 🗺️ Mapa de decisión rápida

```
¿Qué necesito?
│
├── 💡 PENSAR ────────── Office Hours → Autoplan
├── 🔎 INVESTIGAR ────── Agent Reach → ScrapeGraph → Superpowers
├── ⚡ HACER RÁPIDO ──── GSD + Ponytail
├── 🏗️ CONSTRUIR ─────── Office Hours → Spec → GSD → Ship
├── 🎨 DISEÑAR ───────── OBRA MAESTRA (o DISEÑO ⟳ si querés iterar)
├── 🐛 DEBUGGEAR ─────── CAZA-BUGS ⟳
├── 🛡️ ASEGURAR ──────── PENTEST ⟳ (Strix) / BLINDAR
├── 📊 DATOS ─────────── ScrapeGraph MCP → sandbox → reporte
├── 🚀 DEPLOYAR ──────── LANZAR (Ultra Review → CSO → Ship)
└── 📣 COMUNICAR ─────── Marketing Brief → Social → Blog
```

### Cómo funciona un combo o loop paso a paso:

```
Vos: "CONSTRUIR: sistema de pagos"
Kiro: [paso 1] → te muestra resultado → esperás
Vos: "Dale" / "Sí" / "Siguiente"
Kiro: [paso 2] → ... hasta completar

Vos: "CAZA-BUGS: el login falla intermitente"
Kiro: investiga → arregla → testea → si falla, vuelve a arreglar (⟳)
      → te reporta cada vuelta hasta que el test pasa.
```

---

---

## 🎚️ REGULADOR DE INTENSIDAD

| Decís | Kiro hace |
|-------|-----------|
| `"Hacelo"` | Rápido, sin preguntas |
| `"Hacelo con cuidado"` | Rápido pero verifica dos veces |
| `"Superpowers: [tarea]"` | Análisis profundo, opciones, vos elegís |

---

## 🗣️ FEEDBACK RÁPIDO

| Decís | Qué pasa |
|-------|----------|
| `"Más simple"` | Simplifica todo |
| `"No me gusta, otra opción"` | Cambia de approach |
| `"Solo hacelo, no expliques"` | Cero texto, puro resultado |
| `"Para, pensemos"` | Freno y analizamos juntos |

---

---

## 🟢 16 SKILLS ACTIVAS en Sistema Ómicron

> Estas funcionan AUTOMÁTICAS. No tenés que pensar en ellas.

| # | Skill | Qué hace en una frase |
|---|-------|-----------------------|
| 1 | **GSD** | Ejecuta rápido sin preguntas |
| 2 | **QA Skill** | Aprende de errores y no los repite |
| 3 | **Ponytail** | Fuerza la solución más simple |
| 4 | **Verification** | Verifica antes de decir "listo" |
| 5 | **Incremental** | Entrega de a pasos |
| 6 | **Impeccable** | UI nivel award-winning |
| 7 | **Design System** | Tokens y consistencia visual |
| 8 | **Animate** | Animaciones con propósito |
| 9 | **Code Review Ultra** | Auditoría 6 dimensiones |
| 10 | **Shipping & Launch** | Checklist pre-deploy |
| 11 | **Security & Hardening** | Protege datos y auth |
| 12 | **ADN Digital** | CV → perfil JSON del gemelo |
| 13 | **Superpowers** | Análisis profundo, calidad máxima |
| 14 | **Office Hours** | Validar ideas |
| 15 | **Ship** | Workflow: tests → PR → release |
| 16 | **Sinergia** | Verifica que todo esté conectado |

---

---

## 📚 BIBLIOTECA COMPLETA (115 skills en 12 segmentos)

> Guardadas en github.com/paillamilm-blip/mis-skills  
> Copiás la que necesitás, la usás, la sacás.  
> Conteo oficial = carpetas de skill de nivel superior. Recuento: `scripts/contar-skills.sh`.

### 01 — Estrategia (14)

| Skill | Qué hace |
|-------|----------|
| Superpowers | Calidad máxima, razonamiento profundo |
| Context Mode | Analizar → Planificar → Confirmar → Ejecutar |
| Office Hours | Brainstorm estilo YC |
| Plan CEO Review | Revisar visión de producto |
| Plan Eng Review | Revisar arquitectura |
| Plan Design Review | Scoring UX 0-10 |
| Plan DevEx Review | ¿Es fácil para otros devs? |
| Autoplan | CEO+Eng+Design review automático |
| Spec-Driven Dev | Spec antes de codear |
| Planning & Breakdown | Dividir en tareas |
| Idea Refine | Idea vaga → concepto concreto |
| Interview Me | Preguntas hasta entender bien |
| Doubt-Driven Dev | Verificación adversarial |

### 02 — Ejecución (15)

| Skill | Qué hace |
|-------|----------|
| GSD | Hacer sin preguntar |
| Claude Mem | Memoria persistente |
| Incremental | De a pasos |
| Source-Driven | Basado en docs oficiales |
| Ponytail | Lo más simple (YAGNI) |
| Ponytail Audit | Escanear repo buscando bloat |
| Ponytail Review | Review anti-complejidad |
| Ponytail Debt | Tracking de shortcuts |
| Careful | Extra verificación |
| Pair Agent | Pair programming |
| Context Save | Guardar sesión |
| Context Restore | Recuperar sesión |

### 03 — Diseño (16)

| Skill | Qué hace |
|-------|----------|
| Impeccable | UI extraordinaria (18 comandos, 4 modos) |
| Taste Skill | Landing anti-genérica |
| Design | Logos, CIP, banners, íconos |
| Design System | Tokens 3 capas |
| Brand | Identidad de marca completa |
| Banner Design | 22 estilos × todas las plataformas |
| Slides | Presentaciones HTML + Chart.js |
| UI Styling | shadcn + Tailwind + dark mode |
| UI/UX Pro Max | 192 paletas, 84 estilos, 74 fonts |
| UI Verification | Verificar UI vs spec |
| Animate | Motion filosofía Emil Kowalski |
| Frontend UI Eng | Accesible + responsive |
| Design Consultation | Research + propuesta completa |
| Design Review | Auditoría de diseño |
| Design Shotgun | Múltiples variantes rápidas |

### 04 — Código y Calidad (8)

| Skill | Qué hace |
|-------|----------|
| Code Review Ultra | Auditoría 6 dimensiones |
| Code Review & Quality | Review multi-eje |
| Code Simplification | Refactoring para claridad |
| Review (gstack) | Pre-landing con 7 specialists |
| DevEx Review | ¿Es ergonómico? |
| API & Interface Design | APIs REST/GraphQL estables |
| Receiving Code Review | Recibir feedback con rigor |
| Requesting Code Review | Pedir review estructurado |

### 05 — Testing y QA (12)

| Skill | Qué hace |
|-------|----------|
| QA Skill | Aprende de cada error |
| TDD | Tests primero |
| Debugging & Recovery | Root cause sistemático |
| Browser Testing | Testing en browser real |
| QA (gstack) | Testea + arregla + verifica |
| QA Only | Solo reporta |
| Investigate | Root cause profundo |
| Benchmark | Medir performance |
| Retro | Retrospectiva |
| Performance Opt | Web Vitals, profiling |
| Verification Before Completion | Verificar antes de "listo" |
| Systematic Debugging | Método obra (276K⭐) |

### 06 — Seguridad (6)

| Skill | Qué hace |
|-------|----------|
| Security & Hardening | Input, auth, GDPR |
| CSO | OWASP + STRIDE + supply chain |
| Guard | Previene cambios peligrosos |
| Freeze | Congelar deploys |
| Unfreeze | Descongelar |
| **Strix** | Pentesting autónomo con IA — 9 sub-skills (pentest, OWASP Top 10, autofix, CI). Valida con PoC real |

### 07 — Deploy y Ship (8)

| Skill | Qué hace |
|-------|----------|
| Shipping & Launch | Checklist pre-producción |
| CI/CD & Automation | Pipelines |
| Git Workflow | Commits, semver, changelog |
| Deprecation | Retirar sistemas viejos |
| Ship (gstack) | Workflow: tests → PR |
| Land & Deploy | Merge + verificación |
| Canary | Deploy gradual |
| Finishing Branch | Integrar trabajo completado |

### 08 — Automatización (14)

| Skill | Qué hace |
|-------|----------|
| **AUTOMATIZAR-WEB** | **POWER SUITE: 4 skills + 8 capacidades combinadas** |
| Agent-Browser | CLI browser automation (navegar, click, extraer, grabar) |
| Clonar | Replicar sitios (FIEL o RECREAR en Next.js) |
| MicroSandbox | Ejecutar código en microVMs aisladas (hardware virtualization) |
| HTML-Anything | Generar HTML profesional (75 skills × 9 superficies) |
| Nova Act | Browser automation con IA |
| Browse | Navegación web automatizada |
| Scrape | Web scraping |
| Firecrawl Build | Integrar datos web en tu app |
| Firecrawl Scrape | 1 página → Markdown |
| Firecrawl Search | Buscar web + contenido |
| Firecrawl Interact | Clicks, forms, login |
| **ScrapeGraph-AI** | Scraping con IA en Python: describís qué querés → JSON estructurado (sin selectores). 8 pipelines |
| **Agent Reach** | Ojos de internet: leer/buscar en 15 plataformas (web, YouTube, Reddit, Twitter, GitHub, RSS…) con un CLI, sin APIs de pago |
| **ScrapeGraph MCP** | ScrapeGraph vía Model Context Protocol: scrape/extract/search/crawl/monitor gestionado por API, sin infra local |

### 09 — Documentación (6)

| Skill | Qué hace |
|-------|----------|
| Documentation & ADRs | Registrar decisiones |
| Observability | Logging, métricas, alerting |
| Document Generate | Docs automáticos |
| Document Release | Release notes |
| Learn | Gestionar learnings |
| Diagram | Diagramas de arquitectura |

### 10 — Utilidades (4)

| Skill | Qué hace |
|-------|----------|
| Skill Creator | Convertir workflow en skill |
| Codebase Memory | Navegar repos grandes |
| Public APIs | +1400 APIs gratuitas |
| LeanKG | Knowledge graph del código |

### 11 — Producto (1)

| Skill | Qué hace |
|-------|----------|
| ADN Digital | CV → perfil JSON para el gemelo |

### 12 — Marketing y Content (11)

| Skill | Qué hace |
|-------|----------|
| Marketing Brief | Brief profesional desde un PR |
| Marketing Pipeline | Flujo completo de lanzamiento |
| Blog Post | Artículo SEO-optimizado |
| Social Copy | Posts Twitter/X + LinkedIn |
| Newsletter | Email de lanzamiento |
| Video Script | Guión de video producto |
| YouTube Copy | Título + descripción YouTube |
| To PRD | Product Requirements Document |
| Changelog | Historial de cambios pro |
| Presentation | Slidev deck técnico |
| Teach Me | Crear cursos/tutorials |

---

---

## 📊 FUENTES Y ESTRELLAS

| Fuente | ⭐ | Skills |
|--------|----|--------|
| obra/superpowers | 276,965 | 10 |
| Firecrawl | 171,686 | 5 |
| gstack (Garry Tan / YC) | 129,432 | 26 |
| UI/UX Pro Max | 120,492 | 1 |
| shadcn/ui (ref) | 121,998 | 1 |
| Ponytail | 109,534 | 4 |
| Agent Skills (Addy Osmani) | 89,430 | 17 |
| Impeccable (pbakaus) | 62,158 | 1 |
| Codebase Memory | 40,312 | 1 |
| Animate (Emil Kowalski) | 32,051 | 1 |
| Nova Act (Amazon) | 913 | 1 |
| LeanKG | 212 | 1 |
| Propias | — | 16 |
| AlemTuzlak (marketing) | 39 | 11 |
| usestrix/strix (pentesting IA) | — | 1 (9 sub-skills) |
| ScrapeGraphAI (scraping IA) | — | 1 |
| Agent Reach (Panniantong) | — | 1 |

---

---

## 🔑 REGLA DE ORO

```
COMBO  = tarea chica  → "HACER: ___"
CADENA = tarea grande → "CONSTRUIR: ___"

Las 16 skills activas trabajan solas.
Las 103 de biblioteca las copiás cuando necesitás.
```

---

## 📎 Links

- Repo skills: github.com/paillamilm-blip/mis-skills
- Sistema Ómicron: github.com/paillamilm-blip/Sistema-omicrom
- App live: sistema-omicrom.vercel.app
