---
name: manim-tutorial
description: Ruta de aprendizaje de Manim Community Edition en 18 lecciones (de Elteoremadebeethoven) — configuración de render, animaciones, posiciones, textos, transformaciones, gráficos 2D/3D, updaters, cámara. Usar cuando haya que aprender o enseñar Manim paso a paso, o buscar un ejemplo concreto de una técnica.
---
# Manim Tutorial (Community Edition)

Fuente: [Elteoremadebeethoven/ManimCE-tutorial](https://github.com/Elteoremadebeethoven/ManimCE-tutorial)
— autor del canal "Theorem of Beethoven", referente de Manim en español.

> ⚠ El repo no declara licencia, por eso **no se copió su código**: aquí está el índice con
> enlaces directos. Para tenerlo local: `git clone --depth 1 https://github.com/Elteoremadebeethoven/ManimCE-tutorial.git`
>
> El nombre pedido originalmente (`Manim-Tutorial-Community-Edition`) no existe; este es el repo equivalente del mismo autor.

## Lecciones

Base: `https://github.com/Elteoremadebeethoven/ManimCE-tutorial/blob/main/`

| # | Lección | Aprendes | Archivo |
|---|---------|----------|---------|
| 1 | Configuración de render | calidad, resolución, fps, fondo | `_01_render_settings.py` |
| 2 | Animaciones básicas | `Create`, `Write`, `FadeIn`, `run_time` | `_02_basic_animations.py` |
| 3 | Posiciones | `to_edge`, `next_to`, `shift`, `move_to` | `_03_basic_positions.py` |
| 4 | Propiedades y grupos | colores, grosor, `VGroup` | `_04_properties_and_groups.py` |
| 5 | Tex y textos | `Text`, `Tex`, `MathTex` | `_05_basic_tex_and_texts.py` |
| 6 | Textos como arreglos | animar partes de una fórmula | `_06_tex_and_texts_as_arrays.py` |
| 7 | Transformaciones | `Transform`, `ReplacementTransform` | `_07_transformations.py` |
| 8 | Gráficos 2D | `Axes`, `plot`, áreas | `_08_basic_2D_graphs.py` |
| 9 | Gráficos 3D | `ThreeDScene`, superficies | `_09_basic_3D_graphs.py` |
| 10 | Importar recursos | imágenes, SVG | `_10_import_assets.py` |
| 11 | Updaters básicos | `add_updater`, `always_redraw` | `_11_basic_updaters.py` |
| 12 | Updaters con alpha | animaciones paramétricas | `_12_alpha_updaters.py` |
| 13 | Métodos `.animate` | encadenar cambios | `_13_animate methods.py` |
| 14 | Updaters con `dt` | movimiento continuo en el tiempo | `_14_dt_updaters.py` |
| 15 | Animaciones en grupo | `LaggedStart`, `AnimationGroup` | `_15_group_animations.py` |
| 16 | Clases propias | crear Mobjects reutilizables | `_16_custom_classes.py` |
| 17 | Cámara móvil | `MovingCameraScene`, zoom/paneo | `_17_moving_camera.py` |
| 18 | Cámara con zoom | `ZoomedScene`, lupa | `_18_zoomed_camera.py` |

## Cómo usarla

- **Aprender:** seguir las lecciones en orden, renderizando cada archivo con `manim -pql archivo.py`.
- **Resolver algo puntual:** buscar en la tabla la técnica y abrir el archivo como ejemplo.
- La referencia rápida de la API está en [`../manim/SKILL.md`](../manim/SKILL.md).
