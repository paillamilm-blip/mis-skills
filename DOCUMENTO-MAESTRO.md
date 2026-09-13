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

### 🥇 TABLA MAESTRA — Top 10

| # | Nombre | Tipo | Cadena de skills | Score | Segmento |
|---|--------|------|------------------|:-----:|----------|
| 1 | 🏗️ **CONSTRUIR** | combo | Office Hours → Autoplan → Spec → GSD+Incremental → Ultra Review → Ship | **95** | full-stack |
| 2 | 🔎 **INVESTIGAR** | combo | Agent Reach (leer web/redes) → ScrapeGraph (extraer JSON) → Superpowers (sintetizar) | **93** | research |
| 3 | 🎨 **OBRA MAESTRA** | combo⚙️ | taste → ui-ux-pro-max → impeccable → animate *(ya es skill real)* | **92** | diseño |
| 4 | 🐛 **CAZA-BUGS** ⟳ | loop | Investigate → Superpowers → fix (GSD) → QA → *si falla* ⟳ vuelve al fix | **90** | debugging |
| 5 | 🛡️ **CONTROL** ⟳ | loop | Buscar fallas de seguridad con Strix → arreglar la más grave → volver a escanear → repetir hasta que no queden fallas graves | **89** | seguridad |
| 6 | ⚡ **CERO DEFECTOS** ⟳ | loop | Hacer la tarea rápido y simple → revisar si de verdad quedó terminada → si falta algo, corregir y volver a revisar hasta que esté OK | **88** | ejecución |
| 7 | 🧪 **TDD** ⟳ | loop | Primero escribir la prueba (falla) → escribir el código para que pase → limpiar el código → repetir con la siguiente parte | **86** | testing |
| 8 | 🚀 **LANZAR** | combo | Revisar el código a fondo → chequear seguridad → repasar checklist de release → publicar → verificar que funcione en producción | **85** | deploy |
| 9 | 📊 **PIPELINE DE DATOS** | combo | Sacar datos de una web → procesarlos en un entorno seguro → armar un informe visual listo para leer | **84** | automatización |
| 10 | 🧹 **LIMPIAR** ⟳ | loop | Escanear qué sobra (Ponytail Audit) → simplificar (Code Simplification) → revisar que no quedó bloat (Ponytail Review) → *si todavía hay deuda* ⟳ → cerrar con Retro | **83** | calidad |

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

### 📖 El ranking explicado (en simple)

Los **loops** ⟳ se repiten hasta cumplir una condición de salida (le decís la meta y Kiro itera solo); los **combos** son una sola pasada. Abajo, el ciclo de cada loop y la explicación de los que tienen más jerga.

```
🐛 CAZA-BUGS    → arreglar → probar         REPITE hasta que el test pasa
🛡️ CONTROL      → buscar fallas → arreglar   REPITE hasta que no queden fallas graves
🧪 TDD          → escribir código → probar   REPITE hasta que todo pasa
⚡ CERO DEFECTOS → hacer → revisar            REPITE hasta que quedó bien terminado
🧹 LIMPIAR      → simplificar → revisar       REPITE hasta que no queda código de más
```

**#5 🛡️ CONTROL — "control de calidad de seguridad: buscá y tapá los agujeros"**
Un *pentest* es simular un ataque para encontrar vulnerabilidades. La herramienta **Strix** revisa tu app como lo haría un hacker, te dice qué encontró (ordenado por gravedad), arreglás lo más grave, y **vuelve a revisar**. Se repite hasta que no queden fallas críticas.
> `"Loop de pentest sobre CausasPro hasta cerrar las fallas graves"` → Kiro escanea, arregla, re-escanea y te reporta cada vuelta. ⚠️ Solo sobre proyectos tuyos.

**#6 ⚡ CERO DEFECTOS — "hacelo rápido, pero que quede terminado de verdad (right-first-time)"**
Es el modo "hacer las cosas" pero con un control de calidad al final: Kiro ejecuta la tarea de forma simple y directa, después **se autoverifica** (¿compila?, ¿cubre todo lo pedido?, ¿quedó algún cabo suelto?). Si detecta que falta algo, lo corrige y vuelve a verificar. Sale del loop recién cuando está realmente listo.
> `"CERO DEFECTOS: agregá el botón de exportar a PDF"` → lo implementa, se revisa a sí mismo, corrige lo que falte, y recién ahí te dice "listo".

**#7 🧪 TDD — "escribí la prueba antes que el código"**
TDD = *Test-Driven Development* (desarrollo guiado por pruebas). El orden se invierte: primero escribís una prueba de lo que querés (que **falla** porque el código todavía no existe) → escribís el código mínimo para que la prueba **pase** → limpiás el código → repetís con la siguiente parte. Así el código nace con una red de seguridad que avisa si algo se rompe más adelante. Ideal para lógica delicada (pagos, cálculos, el bot de CausasPro).
> `"TDD para la función que calcula el total con descuento"` → escribe el test, luego el código, hasta que todo pasa.

**#8 🚀 LANZAR — "publicar a producción sin que nada se rompa"**
Es el ritual de salida a producción, en orden: **revisar el código a fondo** (Ultra Review) → **chequear seguridad** (CSO: busca vulnerabilidades comunes) → repasar el **checklist de release** → **publicar** (ship) → **verificar que quedó funcionando** en producción. Es lo que hacés cuando un cambio importante ya está listo y no querés sorpresas.
> `"LANZAR"` (o `"Ultra review y ship it"`) → revisa, asegura, publica y confirma.

**#9 📊 PIPELINE DE DATOS — "de una web a un informe, automático"**
Une tres pasos en cadena: **sacar datos** de una página (ScrapeGraph) → **procesarlos** en un entorno aislado y seguro (microsandbox, para que ejecutar código no toque tu máquina) → **armar un informe visual** listo para leer (html-anything). Sirve para convertir datos dispersos de la web en un reporte terminado — muy alineado a tu meta de "reportes tipo Magnar" en CausasPro.
> `"PIPELINE: sacá los precios de esta página, analizalos y hacé un reporte"`.

**#10 🧹 LIMPIAR — "sacá lo que sobra hasta dejar el código limpio"**
Ataca la deuda técnica en ciclo: escanea el repo buscando código de más o duplicado (Ponytail Audit) → simplifica → revisa que no haya quedado nada innecesario (Ponytail Review). Si **todavía** encuentra bloat, **vuelve a pasar**; cierra con una retrospectiva de qué causó la deuda para no repetirla. Ideal cada 2-3 sprints o cuando un proyecto "se siente pesado".
> `"LIMPIAR el módulo de reportes de CausasPro"` → escanea, simplifica, re-revisa hasta que no queda código de más, y te dice qué aprendió.

---

### 🗺️ Mapa de decisión rápida

```
¿Qué necesito?
│
├── 💡 PENSAR ────────── Office Hours → Autoplan
├── 🔎 INVESTIGAR ────── Agent Reach → ScrapeGraph → Superpowers
├── ⚡ HACER RÁPIDO ──── GSD + Ponytail
├── 🏗️ CONSTRUIR ─────── Office Hours → Spec → GSD → Ship
├── 🎨 DISEÑAR ───────── OBRA MAESTRA
├── 🐛 DEBUGGEAR ─────── CAZA-BUGS ⟳
├── 🛡️ ASEGURAR ──────── CONTROL ⟳ (Strix)
├── 📊 DATOS ─────────── PIPELINE DE DATOS (ScrapeGraph MCP → sandbox → reporte)
├── 🧹 LIMPIAR ───────── LIMPIAR ⟳
└── 🚀 DEPLOYAR ──────── LANZAR (Ultra Review → CSO → Ship)
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
