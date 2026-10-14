---
name: manim
description: Crear animaciones explicativas en Python con Manim Community Edition (texto, fórmulas LaTeX, gráficos 2D/3D, transformaciones, cámara). Usar cuando se pida un video animado educativo/explicativo, una animación matemática o técnica, o renderizar escenas Manim en horizontal o vertical.
---

# Manim (Community Edition)

Fuente: [ManimCommunity/manim](https://github.com/ManimCommunity/manim) · MIT ([LICENSE](./LICENSE), [LICENSE.community](./LICENSE.community)) · Docs: https://docs.manim.community

## Instalación

```bash
brew install ffmpeg cairo pango pkg-config   # macOS
pip install manim
manim checkhealth
```

## Estructura mínima de una escena

```python
from manim import *

class Intro(Scene):
    def construct(self):
        titulo = Text("¿Qué es un token?", font_size=56)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP))
        caja = RoundedRectangle(corner_radius=0.3, width=4, height=2, color=BLUE)
        self.play(Create(caja))
        self.wait(1)
```

## Renderizar

| Objetivo | Comando |
|----------|---------|
| Borrador rápido (480p) y abrir | `manim -pql escena.py Intro` |
| Calidad media 720p | `manim -qm escena.py Intro` |
| Final 1080p 60fps | `manim -qh escena.py Intro` |
| 4K | `manim -qk escena.py Intro` |
| **Vertical 9:16 (Shorts/Reels)** | `manim -qh -r 1080,1920 escena.py Intro` |
| Todas las escenas del archivo | `manim -qh -a escena.py` |
| GIF | `manim -ql --format gif escena.py Intro` |

El video queda en `media/videos/<archivo>/<calidad>/<Escena>.mp4`.

## API esencial

- **Objetos:** `Text`, `MarkupText`, `MathTex` (requiere LaTeX), `Circle`, `Square`, `Rectangle`, `Arrow`, `Line`, `Dot`, `NumberPlane`, `Axes`, `BarChart`, `ImageMobject`, `SVGMobject`, `VGroup`.
- **Animaciones:** `Create`, `Write`, `FadeIn`, `FadeOut`, `Transform`, `ReplacementTransform`, `TransformMatchingTex`, `Indicate`, `Circumscribe`, `LaggedStart`, `AnimationGroup`, `mob.animate.<método>()`.
- **Posición:** `.to_edge(UP)`, `.to_corner(UL)`, `.next_to(otro, DOWN, buff=0.3)`, `.shift(2*RIGHT)`, `.move_to(ORIGIN)`, `VGroup(...).arrange(DOWN, buff=0.5)`.
- **Tiempo:** `self.play(..., run_time=2)`, `self.wait(1)`, `rate_func=smooth`.
- **Updaters:** `mob.add_updater(lambda m: m.next_to(punto, UP))`, `ValueTracker` + `always_redraw`.
- **Cámara:** `MovingCameraScene` (`self.camera.frame.animate.scale(0.5)`), `ThreeDScene` (`self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)`).
- **Subtítulos:** `self.add_subcaption("texto", duration=2)` → genera `.srt` junto al video.

## Reglas para que salga bien

1. **Una idea por escena.** Escenas cortas (10–40 s) que luego se concatenan.
2. **Zona segura:** no salir de ±7 en x y ±4 en y (horizontal). En vertical, reducir `font_size` y usar `arrange(DOWN)`.
3. **Limpiar antes de lo siguiente:** `FadeOut` de lo que ya no se usa; evita superposiciones.
4. **Colores con contraste** sobre fondo oscuro (`WHITE`, `YELLOW`, `BLUE`, `GREEN`); máximo 3–4 por escena.
5. **Sin LaTeX instalado → usar `Text`**, no `MathTex`/`Tex`.
6. Probar siempre con `-ql` y renderizar final con `-qh` solo al final.

## Archivos incluidos

- [`ejemplos/basic.py`](./ejemplos/basic.py) — escenas oficiales de ejemplo (`manim -pql ejemplos/basic.py SquareToCircle`).
- Cheatsheet extensa para agentes: [`../manim-animation-agent/prompts/prompt_manim_cheatsheet.txt`](../manim-animation-agent/prompts/prompt_manim_cheatsheet.txt).
