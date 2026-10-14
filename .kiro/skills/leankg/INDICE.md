# 🧠 LeanKG — Knowledge Graph para Codebases

> Grafo de conocimiento enterprise-ready para agentes de IA. Multi-repo, −65% tokens, −85% tool calls.  
> Fuente: [github.com/FreePeak/LeanKG](https://github.com/FreePeak/LeanKG) | ⭐ 212 | Licencia: Apache 2.0

---

## 🤔 ¿Qué es LeanKG?

**LeanKG** es un servidor MCP que indexa tu codebase en un **grafo de conocimiento** (knowledge graph). Cuando le preguntás algo sobre el código, responde en milisegundos usando el grafo — sin leer archivos uno por uno.

### Resultado:
- **65% menos tokens** consumidos por sesión
- **85% menos tool calls** (no más grep masivos)
- **Sub-ms queries** sobre dependencias, funciones, impacto

---

## ⚡ Qué puede hacer

| Comando | Qué hace |
|---------|----------|
| `search_code` | Buscar cualquier elemento del código |
| `find_function` | Localizar una función por nombre |
| `query_file` | Encontrar archivos |
| `get_impact_radius` | ¿Qué se rompe si cambio ESTE archivo? |
| `get_dependencies` | ¿De qué depende este archivo? |
| `get_dependents` | ¿Quién usa este archivo? |
| `get_context` | Contexto completo de un archivo |
| `get_call_graph` | Cadena de llamadas |
| `get_tested_by` | ¿Qué tests cubren esto? |

---

## 🎯 Cómo te ayuda

| Situación | Sin LeanKG | Con LeanKG |
|-----------|-----------|------------|
| "¿Dónde está la función X?" | Grep en todo el repo | `find_function` → instantáneo |
| "¿Qué se rompe si cambio Y?" | Adivinar | `get_impact_radius` → lista exacta |
| "¿Quién usa este módulo?" | Buscar manualmente | `get_dependents` → grafo completo |
| "Dame contexto de este archivo" | Leer 20 archivos | `get_context` → todo junto, menos tokens |

---

## 🚀 Instalación

```bash
# Docker (lo más fácil)
curl -fsSL https://raw.githubusercontent.com/FreePeak/LeanKG/main/scripts/docker-up.sh | bash

# Para tu agente (Cursor, Claude, Kiro)
curl -fsSL https://raw.githubusercontent.com/FreePeak/LeanKG/main/scripts/install.sh | bash -s -- claude
```

---

## 🔗 Tech Stack

- **Rust** (performance)
- **CozoDB** (grafo)
- **tree-sitter** (parsing 158 lenguajes)
- **MCP** (integración con agentes)
- **pgvector** (embeddings opcionales)

---

## 💡 Cuándo usarlo

- Repos grandes (>50 archivos)
- Cuando necesitás entender dependencias
- Para calcular "blast radius" antes de refactors
- Onboarding en proyectos nuevos
- Reducir costos de tokens en sesiones largas
