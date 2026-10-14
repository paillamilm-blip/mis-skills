# 🎬 Motor de Videos — Manim + voz IA + subtítulos

Skill paraguas (cuenta como **1**, igual que Strix o Firecrawl) con 5 sub-skills para generar
videos explicativos animados con voz y subtítulos, en horizontal (YouTube) o vertical (Shorts/Reels/TikTok).

## El flujo completo

```
Guion (video-script) → Escenas Manim (manim) → Voz IA sincronizada (manim-voiceover)
   → Subtítulos .srt automáticos → Formato vertical + subtítulos animados (shorts-generator)
```

| Sub-skill | Qué hace | Fuente | Licencia |
|-----------|----------|--------|----------|
| [manim/](./manim/SKILL.md) | Motor de animación en Python (texto, fórmulas, gráficos, 3D) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | MIT |
| [manim-voiceover/](./manim-voiceover/SKILL.md) | Voz IA (Gemini, ElevenLabs, OpenAI, Azure, gTTS) sincronizada palabra a palabra + subtítulos | [ManimCommunity/manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) | MIT |
| [manim-animation-agent/](./manim-animation-agent/SKILL.md) | Pipeline de agente: tema → plan de escenas → código Manim → auto-corrección de errores. Incluye sus 36 prompts | [ManojINaik/manimAnimationAgent](https://github.com/ManojINaik/manimAnimationAgent) | MIT |
| [shorts-generator/](./shorts-generator/SKILL.md) | Shorts 9:16 con subtítulos estilo Hormozi (Remotion), recorte inteligente, voz, música, servidor MCP | [ghost1412/shorts-generator](https://github.com/ghost1412/shorts-generator) | MIT |
| [manim-tutorial/](./manim-tutorial/SKILL.md) | Ruta de aprendizaje de Manim en 18 lecciones | [Elteoremadebeethoven/ManimCE-tutorial](https://github.com/Elteoremadebeethoven/ManimCE-tutorial) | Sin licencia → solo enlaces |

Además, [`reglas/`](./reglas/) trae reglas `.mdc` (CC0) de buenas prácticas para Python, FFmpeg,
FastAPI y OpenCV, tomadas de [sanjeed5/awesome-cursor-rules-mdc](https://github.com/sanjeed5/awesome-cursor-rules-mdc).

## Requisitos (en la Mac)

```bash
brew install python@3.12 ffmpeg cairo pango pkg-config
brew install --cask mactex-no-gui   # solo si vas a usar fórmulas LaTeX (MathTex/Tex)
pip install manim "manim-voiceover[gemini,gtts]"
```

## Notas

- Los repos de código grande (manim, shorts-generator, manimAnimationAgent) **no se copiaron
  enteros**: aquí van la guía, las piezas reutilizables (ejemplos, prompts, AGENTS.md) y la licencia.
  El código se instala con `pip` o `git clone` cuando se usa.
- El repo `Manim-Tutorial-Community-Edition` pedido no existe con ese nombre; el equivalente del
  mismo autor es `ManimCE-tutorial`. Como no declara licencia, no se copió su código.
