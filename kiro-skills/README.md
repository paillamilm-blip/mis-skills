# 🧠 Kiro Skills — Biblioteca Completa

> 86 skills organizadas en 11 segmentos para desarrollo asistido por IA.  
> 3 fuentes: propias + [Addy Osmani](https://github.com/addyosmani/agent-skills) + [Garry Tan / gstack](https://github.com/garrytan/gstack)

---

## 📚 Guías Rápidas

| Documento | Para qué |
|-----------|----------|
| [⚡ COMANDOS.md](./COMANDOS.md) | Referencia rápida: qué decirle al agente para activar cada skill |
| [🔥 COMBINACIONES.md](./COMBINACIONES.md) | Los mejores combos por situación (15 recetas) |
| [📖 GUIA_COMPLETA.md](./GUIA_COMPLETA.md) | Descripción detallada de cada skill con tips |

---

## 🗂️ Estructura por Segmentos

| # | Segmento | Skills | Carpeta | Para qué |
|---|----------|--------|---------|----------|
| 01 | 🧠 **Estrategia** | 15 | [`01-estrategia/`](./01-estrategia/) | Pensar, planificar, especificar, validar |
| 02 | 🚀 **Ejecución** | 14 | [`02-ejecucion/`](./02-ejecucion/) | Modos de trabajo: rápido, simple, cuidadoso |
| 03 | 🎨 **Diseño** | 15 | [`03-diseno/`](./03-diseno/) | UI/UX, marca, animaciones, landing pages |
| 04 | 🔍 **Código y Calidad** | 7 | [`04-codigo-calidad/`](./04-codigo-calidad/) | Reviews, simplificación, APIs |
| 05 | 🧪 **Testing y QA** | 10 | [`05-testing-qa/`](./05-testing-qa/) | Tests, debugging, performance, retros |
| 06 | 🛡️ **Seguridad** | 5 | [`06-seguridad/`](./06-seguridad/) | Auditorías, hardening, protección |
| 07 | 🚀 **Deploy y Ship** | 7 | [`07-deploy-ship/`](./07-deploy-ship/) | CI/CD, releases, versioning |
| 08 | 🤖 **Automatización** | 3 | [`08-automatizacion/`](./08-automatizacion/) | Browser automation, scraping |
| 09 | 📝 **Documentación** | 6 | [`09-documentacion/`](./09-documentacion/) | Docs, ADRs, diagramas, release notes |
| 10 | 🛠️ **Utilidades** | 5 | [`10-utilidades/`](./10-utilidades/) | Meta-skills, APIs, memoria de código |
| 11 | 🧬 **Producto** | 1 | [`11-producto/`](./11-producto/) | Skills específicas del negocio |

**Total: 86 skills | 757 archivos | 3 fuentes**

---

## ⚡ Top 10 Comandos del Día a Día

```
"Hacelo"                    → Ejecutar rápido (GSD)
"Modo superpowers"          → Calidad máxima
"Ponytail"                  → Solución más simple
"Ultra review"              → Code Review 6 dimensiones
"Ship it"                   → Workflow completo de release
"QA test this"              → Testing en browser real
"Office hours"              → Brainstorm estilo YC
"Autoplan"                  → Pipeline CEO+Eng+Design review
"Security audit"            → CSO (OWASP + STRIDE)
"Dame variantes de diseño"  → Design Shotgun
```

---

## 🔥 Top 5 Combos

| # | Combo | Para qué |
|---|-------|----------|
| 1 | `GSD + Ponytail` | 80% de las tareas diarias — rápido y simple |
| 2 | `Context Mode → Careful → Ultra Review` | Cambios que no pueden fallar |
| 3 | `Ultra Review → Ship it` | PR rápido con calidad garantizada |
| 4 | `Taste Skill → Impeccable → Animate` | UI que se ve increíble |
| 5 | `Autoplan → GSD → Ultra Review → Ship` | Feature completa end-to-end |

→ Ver los 15 combos completos en [COMBINACIONES.md](./COMBINACIONES.md)

---

## 🏗️ Cómo instalar skills en un proyecto

```bash
# Clonar la biblioteca
git clone https://github.com/paillamilm-blip/mis-skills.git

# Copiar un segmento completo
cp -r mis-skills/kiro-skills/01-estrategia/* mi-proyecto/.kiro/skills/

# O copiar skills individuales
cp -r mis-skills/kiro-skills/02-ejecucion/gsd/ mi-proyecto/.kiro/skills/
cp -r mis-skills/kiro-skills/03-diseno/impeccable/ mi-proyecto/.kiro/skills/
```

---

## 📊 Fuentes y Licencias

| Fuente | Autor | Skills | Licencia |
|--------|-------|--------|----------|
| Propias | [@paillamilm-blip](https://github.com/paillamilm-blip) | 29 | Personal |
| [agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani (Google) | 24 | MIT |
| [gstack](https://github.com/garrytan/gstack) | Garry Tan (Y Combinator) | 33 | MIT |
