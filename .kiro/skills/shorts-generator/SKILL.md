---
name: shorts-generator
description: Generar Shorts/Reels/TikTok verticales 9:16 con IA usando ShortsFlow (shorts-generator) — recorte de videos largos o de YouTube, explicativos con Manim, datos curiosos, top 5, doblaje, voz IA/clonada, subtítulos animados estilo Hormozi con Remotion, música con ducking y servidor MCP. Usar cuando se pida un video corto vertical para redes o subtítulos animados.
---
# Shorts Generator (ShortsFlow AI Studio)

Fuente: [ghost1412/shorts-generator](https://github.com/ghost1412/shorts-generator) · MIT ([LICENSE](./LICENSE))
Guía original para agentes (inglés): [AGENTS.md](./AGENTS.md).

## Instalación (Mac)

Requiere Python 3.12+, Node 18+ (para Remotion) y FFmpeg.

```bash
git clone --depth 1 https://github.com/ghost1412/shorts-generator.git
cd shorts-generator
chmod +x setup.sh && ./setup.sh
```

Archivo `.env` (no subir a Git):

```env
GEMINI_API_KEY=tu_clave
PEXELS_API_KEY=tu_clave       # videos de fondo de stock
HF_API_KEY=tu_clave           # opcional
```

## Recetas

```bash
# Explicativo animado con Manim (vertical por defecto)
python3 main.py --mode EXPLAINER --prompt "Cómo funciona la reputación en Ómicron" --skip-upload

# Cortar 3 shorts de un video largo, con subtítulos animados
python3 main.py --source_video "https://www.youtube.com/watch?v=ID" --extract_mode shorts \
  --clip_count 3 --smart_crop --tighten --use_remotion --caption_style HORMOZI

# Datos curiosos con voz, zoom y música que baja cuando se habla
python3 main.py --mode FACTS --category "productividad" --enable_zoom --auto_ducking --use_remotion

# Doblar un video al español
python3 main.py --mode DUB --source_video "clip.mp4" --target_lang es --use_remotion

# Horizontal para YouTube
python3 main.py --mode EXPLAINER --prompt "Tema" --aspect_ratio 16:9

# Interfaz gráfica
python3 gui_app.py
```

## Opciones útiles

| Opción | Valores |
|--------|---------|
| `--mode` | `EXPLAINER`, `FACTS`, `STORY`, `TOP_5`, `CHAT_STORY`, `PODCAST`, `DUB`, `WYR`, `RANK_IT`, `EMOJI_GUESS`, `NEWS` |
| `--caption_style` | `HORMOZI`, `GLOW_BOX`, `BOUNCE`, `MINIMAL` (requiere `--use_remotion`) |
| `--aspect_ratio` | `9:16`, `16:9`, `1:1`, `4:5` |
| `--tts_provider` / `--clone_voice` | ElevenLabs, EdgeTTS, VoiceStudio · `--clone_voice muestra.wav` |
| `--llm_provider` | Gemini, Ollama, DeepSeek, Groq, Anthropic, OpenRouter |
| `--video_filter` | `dynamic`, `cyberpunk`, `teal_orange`, `cinematic_warm`, `moody_dark`… |
| `--batch_file` | lista de temas (uno por línea) para generar en lote |

## Servidor MCP (para que un agente IA genere shorts solo)

```bash
python3 mcp_server.py
```

Herramientas: `generate_short`, `extract_clips`, `generate_social_package` (título/descripción
para YouTube, TikTok y Reels), `get_render_status`.

## Reglas

1. Nunca subir `.mp4` ni binarios a Git; las salidas van en `sessions/`.
2. Subtítulos verticales: resolución 1080×1920, posición `y_pos` por defecto 1150.
3. Si no hay videos de fondo locales, debe funcionar el respaldo de Pexels.
4. Para videos educativos con fórmulas o diagramas propios, generar la escena con
   [`../manim/`](../manim/SKILL.md) + [`../manim-voiceover/`](../manim-voiceover/SKILL.md) y usar este repo para
   el formato vertical, subtítulos animados y publicación.
