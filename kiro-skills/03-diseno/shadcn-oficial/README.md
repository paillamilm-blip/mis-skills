# shadcn/ui — Skills oficiales

> Fuente: [github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui) → carpeta `skills/` · Licencia MIT (ver [LICENSE.md](./LICENSE.md)).
> Copiadas sin modificar. Este README es la única pieza agregada (atribución en español).

Son las skills que el propio equipo de shadcn mantiene para agentes de IA. Sirven para
construir la **web de captación** con componentes shadcn + Tailwind siguiendo las reglas
oficiales (no "a ojo").

| Sub-skill | Para qué |
|-----------|----------|
| [`shadcn/`](./shadcn/SKILL.md) | Agregar, buscar, componer, estilizar y depurar componentes shadcn. Incluye reglas de estilo, formularios, íconos, composición, chat, CLI, MCP, registries y design system |
| [`migrate-radix-to-base/`](./migrate-radix-to-base/SKILL.md) | Migrar componentes de Radix UI a Base UI (mapeo de props, clases y patrones) |

## Cuándo usarla

- Proyecto con `components.json` (o que vas a iniciar con `npx shadcn@latest init`).
- Pedidos tipo: *"agrega un formulario de contacto con shadcn"*, *"arma la sección de precios con Card + Tabs"*.

## Diferencia con `ui-styling`

`ui-styling` es una guía general (shadcn + Radix + Tailwind + dark mode).
`shadcn-oficial` son las reglas **oficiales y actualizadas** del equipo shadcn (CLI, presets,
registries, MCP). Si hay conflicto, manda esta.

## Instalar en un proyecto

```bash
cp -r kiro-skills/03-diseno/shadcn-oficial/shadcn mi-proyecto/.kiro/skills/
```
