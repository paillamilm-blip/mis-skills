# 🧠 Guía Completa de Mis Kiro Skills

> Qué hace cada skill, cuándo usarla, y cómo sacarle el máximo provecho.

---

## 🗺️ Mapa Mental — ¿Qué skill uso para qué?

```
¿Qué necesito hacer?
│
├── 💻 PROGRAMAR
│   ├── Quiero ir rápido sin preguntas ──────────► GSD
│   ├── Necesito calidad máxima ─────────────────► Superpowers
│   ├── Quiero un plan antes de actuar ──────────► Context Mode
│   ├── No quiero repetir errores ───────────────► QA Skill
│   └── Quiero la solución más simple ───────────► Ponytail
│
├── 🔍 REVISAR CÓDIGO
│   ├── Revisión rápida (bugs, edge cases) ──────► Code Review
│   └── Auditoría profunda (seguridad, perf) ────► Code Review Ultra
│
├── 🎨 DISEÑAR
│   ├── Landing page con gusto ──────────────────► Taste Skill
│   ├── UI nivel director/award-winning ─────────► Impeccable
│   ├── Componentes shadcn/Tailwind ─────────────► UI Styling
│   ├── Elegir paletas/fonts/estilos ────────────► UI/UX Pro Max
│   ├── Crear animaciones ───────────────────────► Animate
│   ├── Banners para redes/ads ──────────────────► Banner Design
│   ├── Logo + identidad corporativa ────────────► Design / Brand
│   ├── Tokens de diseño (3 capas) ──────────────► Design System
│   ├── Presentaciones HTML ─────────────────────► Slides
│   └── Verificar UI vs spec ────────────────────► UI Verification
│
├── 🤖 AUTOMATIZAR
│   └── Browser automation + scraping ───────────► Nova Act
│
├── 🧬 PRODUCTO
│   └── Construir ADN Digital desde CV ──────────► ADN Digital
│
├── 📚 REFERENCIA
│   ├── Buscar APIs gratuitas ───────────────────► Public APIs
│   └── Indexar/navegar codebase ────────────────► Codebase Memory
│
└── 🛠️ META (sobre las skills mismas)
    ├── Crear nuevas skills ─────────────────────► Skill Creator
    └── Recordar cosas entre sesiones ───────────► Claude Mem
```

---

## ⚡ EJECUCIÓN Y PRODUCTIVIDAD

---

### 1. 🚀 GSD (Get Stuff Done)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Modo ejecución rápida. Menos charla, más acción. Implementa sin pedir confirmación. |
| **Cuándo usarla** | Cuando tenés claro qué querés y solo necesitás que se haga YA |
| **Cómo activarla** | Di: "modo GSD", "hacelo", "dale", "implementalo" |

**💡 Máximo provecho:**
- Úsala para tareas bien definidas: "GSD: crea un componente Card con imagen, título y botón"
- No la uses cuando necesitás explorar opciones — ahí mejor Superpowers
- Combinala con Context Mode cuando la tarea es grande: planificás primero, luego "GSD" para ejecutar

**⚠️ No usar cuando:** No sabés exactamente qué querés, o es algo crítico que necesita análisis.

---

### 2. 🧠 Claude Mem (Memoria + Tracking)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Memoria persistente entre sesiones + tracking de progreso en tareas multi-paso |
| **Cuándo usarla** | Cuando querés que la IA recuerde decisiones, preferencias o contexto |
| **Cómo activarla** | Comandos: "Recordá que...", "Qué sabés de...", "Olvidá..." |

**💡 Máximo provecho:**
- "Recordá que uso tabs de 2 espacios y prefiero const sobre let"
- "Recordá que el proyecto usa Supabase, no Firebase"
- "Qué sabés de mis preferencias de diseño?"
- Automáticamente descompone tareas grandes en checklists con tracking

**⚠️ Nota:** En Kiro la memoria ya se maneja con learnings, pero esta skill estructura el tracking de ejecución.

---

### 3. 🎯 Context Mode (Protocolo de 4 Fases)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Fuerza análisis antes de actuar: Análisis → Plan → Confirmación → Ejecución |
| **Cuándo usarla** | Cambios complejos, refactors, o cuando no querés que se rompa nada |
| **Cómo activarla** | Activo por defecto antes de cambios al codebase |

**💡 Máximo provecho:**
- Ideal para refactors grandes: "Context Mode: quiero reorganizar los servicios en módulos"
- Te muestra QUÉ archivos se tocan, QUÉ puede romperse, y pide confirmación
- Combinación killer: Context Mode (planificar) → GSD (ejecutar el plan)

**⚠️ No usar cuando:** Son cambios triviales (typos, estilos menores) — ahí GSD es mejor.

---

### 4. 🦸 Superpowers (Modo Experto)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Maximiza calidad, profundidad y completitud. Razonamiento multidimensional. |
| **Cuándo usarla** | Decisiones de arquitectura, problemas complejos, cuando necesitás la MEJOR solución |
| **Cómo activarla** | "Modo superpowers", o cuando necesitás análisis profundo |

**💡 Máximo provecho:**
- "Superpowers: ¿Cuál es la mejor forma de manejar auth en esta app?"
- "Superpowers: analiza este error de performance y dame 3 opciones con trade-offs"
- Te da el POR QUÉ de cada decisión, no solo el código
- Anticipa problemas futuros antes de que aparezcan

**⚠️ No usar cuando:** Solo necesitás ejecutar algo rápido — ahí GSD.

---

### 5. 🏭 Skill Creator

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Transforma flujos de trabajo repetitivos en skills reutilizables |
| **Cuándo usarla** | Cuando repetís el mismo proceso y querés automatizarlo |
| **Cómo activarla** | "Creá una skill para..." + describe tu flujo |

**💡 Máximo provecho:**
- "Skill Creator: siempre que creo un endpoint hago X, Y, Z — convertilo en skill"
- "Skill Creator: mi proceso de deploy es..." → te genera una skill documentada
- Las skills creadas van a `.kiro/skills/` y se activan automáticamente

---

## 🔍 REVISIÓN DE CÓDIGO

---

### 6. 🏆 Code Review Ultra

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | 2 niveles: Review (rápida) + Ultra Review (auditoría completa de 6 dimensiones) |
| **Cuándo usarla** | Antes de merge a main, antes de deploy a prod, o cuando querés calidad garantizada |
| **Cómo activarla** | "Review" (rápida) o "Ultra Review" (profunda) |

**💡 Máximo provecho:**
- **Review** → antes de cada PR: busca bugs, edge cases, imports muertos
- **Ultra Review** → antes de deploy: seguridad, performance, arquitectura, accesibilidad
- Te da un scorecard de 6 dimensiones con nota
- Formato priorizado: 🔴 Crítico → 🟡 Medio → 🟢 Bajo

**Combo ideal:** Code Review Ultra ANTES del merge + QA Skill para aprender de lo que encuentra.

---

### 7. 📋 Code Review (Legacy)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Revisión estándar para React + TypeScript + Vite + Supabase |
| **Cuándo usarla** | Revisión día a día, menos formal que Ultra |
| **Nota** | Usa Code Review Ultra en su lugar — es la versión evolucionada |

---

## 🎨 DISEÑO Y UI/UX

---

### 8. 🎨 Design (Skill Unificada)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Logos (55 estilos), CIP completo, slides, banners, iconos, fotos sociales |
| **Cuándo usarla** | Cualquier tarea de diseño visual |
| **Cómo activarla** | "Diseñá un logo para...", "Creá un CIP para...", "Generá un ícono..." |

**💡 Máximo provecho:**
- Tiene routing inteligente: le decís qué necesitás y enruta a la sub-skill correcta
- Genera prompts para Gemini AI cuando necesita imágenes
- CIP = Corporate Identity Program: 50 entregables de marca completos

---

### 9. 🏗️ Design System

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Tokens de 3 capas (Primitive → Semantic → Component), CSS variables, Tailwind theme |
| **Cuándo usarla** | Cuando necesitás consistencia visual sistematizada |
| **Cómo activarla** | "Creá tokens de diseño para...", "Design system para..." |

**💡 Máximo provecho:**
- Define tokens UNA vez y úsalos en todo el proyecto
- Genera archivos de tokens JSON, CSS variables y config de Tailwind
- Incluye specs de componentes con estados y variantes

---

### 10. 🏷️ Brand

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Voz de marca, identidad visual, frameworks de mensajería, gestión de assets |
| **Cuándo usarla** | Cuando necesitás definir o mantener una identidad de marca coherente |
| **Cómo activarla** | "Definí la voz de marca para...", "Revisá consistencia de marca" |

**💡 Máximo provecho:**
- Crea brand guidelines completas desde cero
- Verifica que tus contenidos sean consistentes con la marca
- Incluye checklist de aprobación y reglas de uso de logo

---

### 11. 🖼️ Banner Design

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | 22 estilos de art direction para banners de redes sociales, ads, web, print |
| **Cuándo usarla** | Necesitás un banner/cover/header para cualquier plataforma |
| **Cómo activarla** | "Diseñá un banner para LinkedIn", "Banner para Facebook evento" |

**💡 Máximo provecho:**
- Especificá plataforma + estilo: "Banner glassmorphism para YouTube"
- Soporta: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, print
- Estilos: minimalist, gradient, bold typography, photo-based, neon, 3D, retro, etc.

---

### 12. 📊 Slides

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Presentaciones HTML estratégicas con Chart.js, design tokens, copywriting |
| **Cuándo usarla** | Necesitás una presentación profesional |
| **Cómo activarla** | "Creá slides sobre [tema] [cantidad]" |

**💡 Máximo provecho:**
- Genera presentaciones en HTML puro (no PowerPoint) con diseño premium
- Incluye gráficos con Chart.js automáticos
- Aplica fórmulas de copywriting para cada slide
- Las slides son responsive y se pueden deployar como web

---

### 13. 🎭 UI Styling (shadcn + Tailwind)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Componentes con shadcn/ui + Radix UI + Tailwind CSS, theming, dark mode |
| **Cuándo usarla** | Implementar UI components accesibles y estilizados |
| **Cómo activarla** | "Creá un [componente] con shadcn" |

**💡 Máximo provecho:**
- Genera componentes accesibles (ARIA) automáticamente
- Configuración de dark mode incluida
- Personalización de temas y colores
- Incluye scripts para agregar componentes shadcn al proyecto

---

### 14. 📐 UI/UX Pro Max (Base de Datos de Diseño)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | DB searchable: 84 estilos, 192 paletas, 74 font pairings, 192 product types, 98 UX guidelines |
| **Cuándo usarla** | Cuando necesitás inspiración o decisiones de diseño fundamentadas |
| **Cómo activarla** | "Qué paleta va para un SaaS B2B?", "Font pairing para editorial" |

**💡 Máximo provecho:**
- "¿Qué estilo visual funciona para [tipo de producto]?"
- "Necesito un color palette para [industria/vibe]"
- "¿Qué guidelines UX aplican para [formularios/dashboards/etc]?"
- Soporta 22 stacks: React, Next.js, Vue, Svelte, Flutter, SwiftUI, etc.
- Tiene datos de motion, charts, iconos y performance

---

### 15. ✅ UI Verification

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Verifica que la UI live matchee la spec de diseño + ejecuta user flows |
| **Cuándo usarla** | QA visual — asegurar que lo implementado es lo diseñado |
| **Cómo activarla** | "Verificá que esta UI cumple con el diseño" |

**💡 Máximo provecho:**
- Compara CSS real vs spec de diseño
- Ejecuta flows de usuario vía Nova Act con escenarios Gherkin
- Genera reporte con screenshots anotadas
- 5 categorías: visual style, components, accessibility, project rules, platform conventions

---

### 16. 👅 Taste Skill (Anti-Slop)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Landing pages con "gusto" real. Anti-AI: evita que se vea genérico/templated |
| **Cuándo usarla** | Landing pages, portfolios, redesigns que NO se vean "hechos por IA" |
| **Cómo activarla** | Para cualquier landing/portfolio/redesign |

**💡 Máximo provecho:**
- Primero "lee la sala": infiere vibe, audiencia, contexto
- Tiene 3 dials ajustables + 60+ items de pre-flight check
- Anti-defaults: evita purple gradients, centered hero over dark mesh, three equal cards
- Ideal para: tu portfolio personal, landing de producto, sitio de freelance

---

### 17. ✨ Animate

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Construye animaciones desde cero con filosofía Emil Kowalski |
| **Cuándo usarla** | Cuando algo necesita movimiento: transiciones, micro-interactions, entrances |
| **Cómo activarla** | "Animá este componente", "Agregá motion a...", "Transición para..." |

**💡 Máximo provecho:**
- Sigue una secuencia estricta: ¿Debe animarse? → ¿Propósito? → ¿Herramienta? → ¿Curva?
- Elige la herramienta más simple: CSS > WAAPI > Motion library
- Incluye reduced motion y hover gating automáticamente
- Tiene tabla de curvas y duraciones exactas (no inventa valores)

---

### 18. 💎 Impeccable

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Diseño UI nivel director de diseño award-winning. 18 commands, 4 modos. |
| **Cuándo usarla** | Cuando querés resultado de nivel EXTRAORDINARIO |
| **Cómo activarla** | Para cualquier tarea de diseño/UI frontend |

**💡 Máximo provecho:**
- 4 modos según el tipo de página:
  - **Persuade** → Landings, marketing (atención + acción)
  - **Operate** → Apps, dashboards (eficiencia + consistencia)
  - **Read** → Docs, artículos (comprensión)
  - **Experience** → Portfolios, galerías (inmersión)
- 18 comandos: shape, audit, polish, animate, colorize, distill, harden, optimize...
- Resultado = producción real, no mockup

---

## 🤖 AUTOMATIZACIÓN

---

### 19. 🌐 Nova Act (Browser Automation)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | SDK de Amazon para automatizar browsers con IA: scraping, testing, workflows |
| **Cuándo usarla** | Web scraping, testing E2E, automatizar tareas repetitivas en el browser |
| **Cómo activarla** | "Automatizá [acción] en [sitio]", "Scrapeá datos de..." |

**💡 Máximo provecho:**
- 2 modos: API Key (desarrollo rápido) o AWS Credentials (producción)
- Puede explorar sitios interactivamente
- Genera tests E2E desde escenarios en lenguaje natural
- Reproduce bugs automáticamente
- Extrae datos estructurados de cualquier web

---

## 🧬 CORE DEL PRODUCTO

---

### 20. 🧬 ADN Digital Técnico

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Transforma CVs/certificados en un ADN Digital JSON estructurado para el Gemelo Digital |
| **Cuándo usarla** | Cuando un usuario sube su CV o documentos de acreditación a Sistema Ómicron |
| **Cómo activarla** | Pasale texto de un CV o certificado |

**💡 Máximo provecho:**
- Extrae TODA la info profesional y la conecta en sinergias
- Bucle de refinamiento hasta coherencia ≥ 9.2/10
- Nunca inventa información (fidelidad al texto fuente)
- Output = JSON puro, listo para el sistema

---

## 🐴 PONYTAIL (Anti Over-Engineering)

---

### 21-26. Suite Ponytail

| Skill | ¿Qué hace? | Cuándo usarla |
|-------|-------------|---------------|
| **Ponytail** | Fuerza la solución más simple que funcione (YAGNI) | Cualquier tarea de código |
| **Ponytail Audit** | Escanea TODO el repo buscando over-engineering | Cuando sentís que el proyecto está inflado |
| **Ponytail Review** | Code review enfocado en eliminar complejidad | Antes de merge |
| **Ponytail Debt** | Rastreo de shortcuts deliberados (`ponytail:` comments) | Gestión de deuda técnica |
| **Ponytail Gain** | Scoreboard de impacto: menos código, menos costo | Para medir el beneficio |
| **Ponytail Help** | Referencia rápida de todos los comandos | Cuando no te acordás |

**💡 Máximo provecho de Ponytail:**
- 3 intensidades: `lite` (suave), `full` (default), `ultra` (extremo)
- La escalera: ¿Necesita existir? → ¿Ya existe en el codebase? → ¿Stdlib? → ¿Feature nativa? → ¿Dep instalada? → Solo entonces escribir
- "Ponytail ultra: revisá este módulo" → te dice qué borrar sin miedo
- Combo: Ponytail Audit (encuentra el bloat) → Ponytail (simplifica)

---

## 📋 QA & APRENDIZAJE

---

### 27. 🎓 QA Skill (Aprende de Errores)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Registra cada error, lo categoriza, y consulta el historial antes de actuar |
| **Cuándo usarla** | Siempre activo — previene errores repetidos |
| **Cómo activarla** | Automático en errores. Manual: "qaskill", "qué errores he tenido" |

**💡 Máximo provecho:**
- Cada error se convierte en una **regla permanente**
- Antes de cada cambio hace un "pre-flight check" contra errores pasados
- Categorías: Tipos, Imports, API mismatch, Unused code, Naming, Config
- Es como tener un QA engineer que RECUERDA todo lo que salió mal

---

## 📚 REFERENCIA

---

### 28. 🌍 Public APIs (+1400 APIs)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Catálogo de +1400 APIs públicas gratuitas por categoría |
| **Cuándo usarla** | Cuando necesitás datos externos: clima, monedas, noticias, geo, etc. |
| **Cómo activarla** | "Qué API puedo usar para [funcionalidad]?" |

**💡 Máximo provecho:**
- "Necesito una API de clima gratuita" → te da opciones con pros/cons
- Categorías: Animales, Finanzas, Clima, Música, Gobierno, Geo, News, y muchas más
- Ahorrás horas de búsqueda de APIs

---

### 29. 🧠 Codebase Memory (MCP)

| Campo | Valor |
|-------|-------|
| **¿Qué hace?** | Indexa codebases en grafo de conocimiento. 158 lenguajes, consultas sub-ms |
| **Cuándo usarla** | Cuando necesitás navegar un codebase grande rápidamente |
| **Cómo activarla** | Servidor MCP — se configura y queda disponible |

**💡 Máximo provecho:**
- Indexa repositorios masivos en milisegundos
- Busca símbolos, traza dependencias, navega arquitectura
- 99% menos tokens que leer archivos uno por uno
- Ideal para onboarding en proyectos grandes

---

## 🏆 COMBOS RECOMENDADOS (Máximo Poder)

| Situación | Combo de Skills |
|-----------|----------------|
| **Proyecto nuevo desde cero** | Superpowers (arquitectura) → Design System (tokens) → GSD (implementar) |
| **Feature compleja** | Context Mode (plan) → GSD (ejecutar) → Code Review Ultra (validar) |
| **Landing page profesional** | Taste Skill + Impeccable + Animate |
| **Refactor seguro** | Context Mode → Ponytail Audit → QA Skill |
| **Deploy a producción** | Code Review Ultra → UI Verification → Ponytail Review |
| **Portfolio/CV digital** | ADN Digital + Impeccable (Experience mode) + Taste Skill |
| **Diseño de marca completo** | Brand → Design → Banner Design → Slides |
| **Debugging difícil** | Superpowers + QA Skill + Codebase Memory |
| **Aprender codebase nuevo** | Codebase Memory → Context Mode (resumen) |
| **Hacer TODO rápido** | GSD + Ponytail (full) — velocidad máxima, complejidad mínima |

---

## 📝 Cómo instalar una skill en cualquier proyecto

```bash
# 1. Cloná tu biblioteca (una vez)
git clone https://github.com/paillamilm-blip/mis-skills.git

# 2. Copiá las skills que necesités al proyecto
mkdir -p mi-proyecto/.kiro/skills
cp -r mis-skills/kiro-skills/gsd/ mi-proyecto/.kiro/skills/
cp -r mis-skills/kiro-skills/impeccable/ mi-proyecto/.kiro/skills/
cp -r mis-skills/kiro-skills/ponytail/ mi-proyecto/.kiro/skills/

# 3. Kiro las detecta automáticamente ✅
```

---

## ⚡ Quick Reference — Una línea por skill

| # | Skill | Una línea |
|---|-------|-----------|
| 1 | GSD | "Solo hacelo, rápido y completo" |
| 2 | Claude Mem | "Recordá esto para siempre" |
| 3 | Context Mode | "Analizá antes de tocar algo" |
| 4 | Superpowers | "Dame lo mejor que puedas" |
| 5 | Skill Creator | "Convertí mi proceso en skill" |
| 6 | Code Review Ultra | "Revisá esto como si fuera a producción" |
| 7 | Code Review | "Revisión rápida básica" |
| 8 | Design | "Diseñá cualquier cosa visual" |
| 9 | Design System | "Tokens + sistema de diseño" |
| 10 | Brand | "Identidad de marca completa" |
| 11 | Banner Design | "Banner para [plataforma]" |
| 12 | Slides | "Presentación profesional HTML" |
| 13 | UI Styling | "Componentes shadcn + Tailwind" |
| 14 | UI/UX Pro Max | "Inspiración + decisiones de diseño" |
| 15 | UI Verification | "¿La UI matchea el diseño?" |
| 16 | Taste Skill | "Landing anti-genérica con gusto" |
| 17 | Animate | "Animación precisa con propósito" |
| 18 | Impeccable | "UI nivel award-winning" |
| 19 | Nova Act | "Automatizá el browser con IA" |
| 20 | ADN Digital | "CV → perfil digital JSON" |
| 21 | Ponytail | "La solución más lazy que funcione" |
| 22 | Ponytail Audit | "¿Qué sobra en este repo?" |
| 23 | Ponytail Review | "Review anti-overengineering" |
| 24 | Ponytail Debt | "Track de shortcuts deliberados" |
| 25 | Ponytail Gain | "¿Cuánto ahorré?" |
| 26 | Ponytail Help | "Cheatsheet de ponytail" |
| 27 | QA Skill | "Aprendé de mis errores" |
| 28 | Public APIs | "API gratis para [X]" |
| 29 | Codebase Memory | "Mapa del codebase instantáneo" |
