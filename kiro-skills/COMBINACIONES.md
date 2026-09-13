# 🏆 Ranking de Combos y Loops — Máximo Poder

> Reanálisis completo (modo **superpowers**) sobre las **115 skills reales**, incluidas las
> nuevas de investigación/scraping/seguridad (Agent Reach, ScrapeGraphAI, ScrapeGraph MCP, Strix).
> Reemplaza la lista de combos anterior.

---

## 🧩 Conceptos

- **Combo** = secuencia lineal de skills (A → B → C, una sola pasada).
- **Loop** ⟳ = ciclo que se **repite hasta cumplir una condición de salida** (ej: `fix → test → si falla, volver al fix`). Le decís la meta; Kiro itera solo y te reporta cada vuelta.
- **Combo-skill** ⚙️ = ya existe como skill ejecutable (no hay que recrearla): `obra-maestra`, `automatizar-web`, `clonar`.

**Puntuación (0–100):** `Impacto` + `Frecuencia` + `Palanca` (cuánto multiplica vs hacerlo suelto) − `Fricción` (setup/costo/riesgo).

---

## 📊 TABLA MAESTRA — Ranking

| # | Nombre | Tipo | Cadena de skills | Score |
|---|--------|------|------------------|:-----:|
| 1 | 🏗️ **CONSTRUIR** | combo | Office Hours → Autoplan → Spec → GSD+Incremental → Ultra Review → Ship | **95** |
| 2 | 🔎 **INVESTIGAR** | combo | Agent Reach → ScrapeGraph → Superpowers (síntesis) | **93** |
| 3 | 🎨 **OBRA MAESTRA** | combo ⚙️ | taste → ui-ux-pro-max → impeccable → animate | **92** |
| 4 | 🐛 **CAZA-BUGS** | loop ⟳ | Investigate → Superpowers → fix → QA → *si falla* ⟳ | **90** |
| 5 | 🛡️ **PENTEST** | loop ⟳ | Strix scan → priorizar → fix → re-scan → *hasta 0 críticas* ⟳ | **89** |
| 6 | ⚡ **HACER-BIEN** | loop ⟳ | GSD+Ponytail → Verification-Before-Completion → *si no pasa* ⟳ | **88** |
| 7 | 🧪 **TDD** | loop ⟳ | test rojo → código → test verde → *si rojo* ⟳ / refactor | **86** |
| 8 | 🚀 **LANZAR** | combo | Ultra Review → CSO → Shipping checklist → Ship → Land & Deploy | **85** |
| 9 | 📊 **PIPELINE DE DATOS** | combo | ScrapeGraph MCP → microsandbox → html-anything | **84** |
| 10 | 🔒 **BLINDAR** | combo | Context Mode → Careful → Security & Hardening → CSO → Ultra Review → Ship | **82** |
| 11 | 🎨 **DISEÑO** | loop ⟳ | Design Shotgun → Impeccable → UI Verification → *si no matchea* ⟳ | **81** |
| 12 | 🧹 **LIMPIAR** | combo | Ponytail Audit → Code Simplification → Ponytail Review → Ultra Review → Retro | **79** |
| 13 | 👀 **VIGILANCIA** | loop ⟳ | ScrapeGraph monitor → *detecta cambio* → notifica → ⟳ | **77** |
| 14 | 📣 **COMUNICAR** | combo | Ship → Marketing Brief → Social Copy → Blog Post → Newsletter | **75** |
| 15 | 🧬 **PERFIL** | combo | [CV] → ADN Digital → Impeccable (portfolio) → Ship | **72** |

---

## 🔝 Los detallados (Top 6)

### 1 — 🏗️ CONSTRUIR (combo · 95)
> Proyecto o feature grande, de la idea a producción.
```
Office Hours → Autoplan → Spec → GSD + Incremental → Ultra Review → Ship
```
**Comando:** `"CONSTRUIR: [qué]"` · **Cuándo:** feature nueva, módulo, sistema completo.

### 2 — 🔎 INVESTIGAR (combo · 93) 🆕
> Traer info real de internet y sintetizarla. Desbloquea las skills nuevas.
```
Agent Reach (leer web/YouTube/Reddit/Twitter) → ScrapeGraph (extraer JSON) → Superpowers (sintetizar)
```
**Comando:** `"Investigá [tema] en internet y resumí"` · **Cuándo:** research de mercado, comparar herramientas, ver qué dicen de un producto, due diligence.

### 3 — 🎨 OBRA MAESTRA (combo-skill · 92) ⚙️
> UI nivel award. Ya es una skill real que encadena las 4 fases.
```
taste (leer la sala) → ui-ux-pro-max (inteligencia) → impeccable (ejecutar) → animate (vida)
```
**Comando:** `"OBRA MAESTRA [pantalla]"` · **Cuándo:** landing, dashboard, portfolio, componente premium.

### 4 — 🐛 CAZA-BUGS (loop ⟳ · 90)
> Bug que no cede a la primera. Itera hasta que el test pasa.
```
Investigate → Superpowers (hipótesis) → fix (GSD) → QA
        ⟳ si el test falla, vuelve al fix con lo aprendido
```
**Comando:** `"CAZA-BUGS: [síntoma]"` · **Salida:** test en verde / causa raíz cerrada.

### 5 — 🛡️ PENTEST (loop ⟳ · 89) 🆕
> Seguridad ofensiva real con Strix. Itera hasta cerrar críticas.
```
Strix (scan) → priorizar por severidad → fix → Strix (re-scan)
        ⟳ hasta 0 vulnerabilidades críticas/altas
```
**Comando:** `"Loop de pentest sobre [proyecto] hasta cerrar las críticas"` · ⚠️ solo sobre lo tuyo.

### 6 — 📊 PIPELINE DE DATOS (combo · 84) 🆕
> Extraer → analizar → reportar, end-to-end.
```
ScrapeGraph MCP (extraer) → microsandbox (analizar en aislado) → html-anything (reporte visual)
```
**Comando:** `"PIPELINE: extraé [datos] de [fuente], analizá y generá reporte"`.

---

## 🔥 Top 5 del día a día

| # | Combo | Frase rápida | Situación |
|---|-------|--------------|-----------|
| 1 | **HACER** | `"Hacelo: [tarea]"` | 80% de las tareas |
| 2 | **INVESTIGAR** | `"Investigá [tema] y resumí"` | Antes de decidir/construir |
| 3 | **OBRA MAESTRA** | `"OBRA MAESTRA [pantalla]"` | UI que tiene que verse pro |
| 4 | **REVISAR+LANZAR** | `"Ultra review y ship it"` | Cerrar PR con calidad |
| 5 | **CAZA-BUGS** | `"Investigá y arreglá [error]"` | Bug difícil |

---

## 🗺️ Mapa de decisión rápida

```
¿Qué necesito?
│
├── 💡 PENSAR ────────── Office Hours → Autoplan
├── 🔎 INVESTIGAR ────── Agent Reach → ScrapeGraph → Superpowers
├── ⚡ HACER RÁPIDO ──── GSD + Ponytail
├── 🏗️ CONSTRUIR ─────── Office Hours → Spec → GSD → Ship
├── 🎨 DISEÑAR ───────── OBRA MAESTRA (o DISEÑO ⟳ para iterar)
├── 🐛 DEBUGGEAR ─────── CAZA-BUGS ⟳
├── 🛡️ ASEGURAR ──────── PENTEST ⟳ / BLINDAR
├── 📊 DATOS ─────────── ScrapeGraph MCP → sandbox → reporte
├── 🚀 DEPLOYAR ──────── LANZAR
└── 📣 COMUNICAR ─────── Marketing Brief → Social → Blog
```

---

## 💬 Cómo se ejecuta

```
Combo (lineal):
  Vos: "CONSTRUIR: sistema de pagos"
  Kiro: paso 1 → mostrás → "dale" → paso 2 → ... hasta terminar

Loop ⟳ (iterativo hasta condición):
  Vos: "CAZA-BUGS: el login falla intermitente"
  Kiro: investiga → arregla → testea
        → si falla, repite el fix con lo aprendido
        → te reporta cada vuelta HASTA que el test pasa.
```

> Los tres combos-skill ⚙️ (`obra-maestra`, `automatizar-web`, `clonar`) siguen viviendo como skills ejecutables en sus carpetas; este ranking solo documenta cómo y cuándo combinarlas.
