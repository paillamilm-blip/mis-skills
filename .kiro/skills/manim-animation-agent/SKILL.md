---
name: manim-animation-agent
description: Pipeline de agente IA que convierte un tema en un video educativo Manim — planifica escenas, hace storyboard, diseña la implementación técnica y la narración, genera el código Manim y lo auto-corrige cuando falla el render. Usar cuando se pida "hazme un video explicativo sobre X" de punta a punta, o para generar/arreglar código Manim de forma confiable.
---
# Manim Animation Agent

Fuente: [ManojINaik/manimAnimationAgent](https://github.com/ManojINaik/manimAnimationAgent) · MIT ([LICENSE](./LICENSE))
Se copiaron sus **36 prompts** ([`prompts/`](./prompts/)); el código Python completo no (se clona si hace falta).

## El pipeline (seguir en este orden)

| Paso | Prompt a usar | Entrada → Salida |
|------|---------------|------------------|
| 1. Plan de escenas | [`prompt_scene_plan.txt`](./prompts/prompt_scene_plan.txt) | `{topic}`, `{description}` → lista de 3–7 escenas con propósito y layout |
| 2. Storyboard visual (por escena) | [`prompt_scene_vision_storyboard.txt`](./prompts/prompt_scene_vision_storyboard.txt) | escena → qué objetos aparecen, dónde y en qué orden |
| 3. Plan técnico | [`prompt_scene_technical_implementation.txt`](./prompts/prompt_scene_technical_implementation.txt) | storyboard → clases Manim, posiciones, tiempos |
| 4. Narración | [`prompt_scene_animation_narration.txt`](./prompts/prompt_scene_animation_narration.txt) | plan técnico → guion de voz sincronizado con cada animación |
| 5. Código | [`prompt_code_generation.txt`](./prompts/prompt_code_generation.txt) | todo lo anterior → archivo `.py` Manim (con `VoiceoverScene` si hay voz) |
| 6. Render | `manim -ql escena.py SceneN` | — |
| 7. Si falla | [`prompt_fix_error.txt`](./prompts/prompt_fix_error.txt) | `{error_message}`, `{manim_code}`, `{implementation_plan}` → código corregido. Repetir máx. 3 veces |
| 8. Revisión visual | [`prompt_visual_self_reflection.txt`](./prompts/prompt_visual_self_reflection.txt) | captura del frame → detectar textos encimados o fuera de pantalla |

Los `{placeholders}` se reemplazan con el contenido real antes de enviar el prompt al modelo
(en el proyecto original: Gemini 2.5 Flash vía LiteLLM).

## Material de apoyo (leer antes de generar código)

- [`prompt_manim_cheatsheet.txt`](./prompts/prompt_manim_cheatsheet.txt) — API de Manim CE resumida.
- [`prompt_best_practices.txt`](./prompts/prompt_best_practices.txt) — buenas prácticas de animación.
- [`prompt_teaching_framework.txt`](./prompts/prompt_teaching_framework.txt) — estructura pedagógica de un buen video.
- [`code_color_cheatsheet.txt`](./prompts/code_color_cheatsheet.txt), [`code_font_size.txt`](./prompts/code_font_size.txt), [`code_background.txt`](./prompts/code_background.txt), [`code_limit.txt`](./prompts/code_limit.txt) — restricciones de estilo (colores, tamaños, fondo, límites de pantalla).
- [`banned_reasonings.txt`](./prompts/banned_reasonings.txt) — excusas que el agente NO debe usar al corregir errores.

Prompts extra para variantes con RAG (búsqueda en documentación) y Tavily (búsqueda web):
`prompt_rag_query_generation_*.txt`, `prompt_tavily_*.txt`, `prompt_context_learning_*.txt`.

## Reglas clave del agente original

1. Planificar **antes** de escribir código (pasos 1–4 nunca se saltan).
2. Una clase `Scene` por escena; nombres `Scene1`, `Scene2`…
3. Respetar márgenes seguros y espaciado mínimo entre objetos.
4. Ante un error: leer el traceback completo, corregir la causa (no tapar el error), re-renderizar.
5. Guardar cada corrección exitosa como aprendizaje para no repetir el error.

## Usar el proyecto completo (opcional)

```bash
git clone --depth 1 https://github.com/ManojINaik/manimAnimationAgent.git
cd manimAnimationAgent && pip install -r requirements.txt
python generate_video.py --help
```

---
> 📦 **Si un archivo que cita esta skill no está en la carpeta**, búscalo en [ARCHIVOS-EXTRA.md](./ARCHIVOS-EXTRA.md): la documentación viene incluida ahí completa y los datos/código tienen su enlace directo para descargarlos.
