---
name: manim-voiceover
description: Agregar voz en off con IA (Gemini, ElevenLabs, OpenAI, Azure, gTTS) o grabada con micrófono a videos Manim, sincronizando animaciones con el audio palabra a palabra y generando subtítulos automáticamente. Usar cuando un video Manim necesite narración, voz IA, doblaje a otro idioma o subtítulos.
---

# Manim Voiceover

Fuente: [ManimCommunity/manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) · MIT ([LICENSE](./LICENSE)) · Docs: https://voiceover.manim.community

## Instalación

```bash
pip install --upgrade "manim-voiceover[gemini,gtts]"
# Otros extras: elevenlabs, openai, azure, recorder (micrófono), translate (DeepL), transcribe (Whisper), all
```

Para Gemini, crear `.env` en la carpeta del proyecto (nunca subirlo a Git):

```env
GEMINI_API_KEY=tu_clave
```

## Escena con voz IA (Gemini, voz en español)

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gemini import GeminiService

class Explicacion(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GeminiService(voice="Kore"))

        circulo = Circle()
        with self.voiceover(text="Este círculo se dibuja mientras hablo.") as tracker:
            self.play(Create(circulo), run_time=tracker.duration)

        with self.voiceover(text="Y ahora se convierte en un cuadrado.") as tracker:
            self.play(Transform(circulo, Square()), run_time=tracker.duration)
```

Alternativa gratis y sin clave: `GTTSService(lang="es", tld="cl")`.

## Renderizar

```bash
manim -pql escena.py Explicacion --disable_caching      # borrador
manim -qh escena.py Explicacion --disable_caching       # final
manim -qh -r 1080,1920 escena.py Explicacion --disable_caching   # vertical
```

> `--disable_caching` es **obligatorio** con esta librería (bug conocido de Manim).

## Sincronizar con palabras exactas (bookmarks)

```python
with self.voiceover(text="Primero <bookmark mark='A'/>el registro y luego <bookmark mark='B'/>el pago.") as tracker:
    self.wait_until_bookmark("A")
    self.play(FadeIn(paso1), run_time=tracker.time_until_bookmark("B", limit=1))
    self.wait_until_bookmark("B")
    self.play(FadeIn(paso2))
```

Con voces grabadas o servicios sin marcas de tiempo, instalar el extra `transcribe` y pasar
`transcription_model="base"` al servicio (usa Whisper).

## Subtítulos

Cada bloque `self.voiceover(...)` crea un subtítulo automáticamente: al renderizar aparece un
archivo `.srt` junto al `.mp4`. Para desactivarlo: `self.set_speech_service(servicio, create_subcaption=False)`.

## Servicios disponibles

| Servicio | Clase | Necesita |
|----------|-------|----------|
| Gemini TTS (recomendado) | `GeminiService(voice="Kore")` | `GEMINI_API_KEY` |
| ElevenLabs | `ElevenLabsService(voice_name=...)` | `ELEVEN_API_KEY` |
| OpenAI | `OpenAIService(voice="alloy")` | `OPENAI_API_KEY` |
| Azure | `AzureService(voice="es-CL-CatalinaNeural")` | clave Azure |
| gTTS | `GTTSService(lang="es")` | internet, gratis |
| pyttsx3 | `PyTTSX3Service()` | offline |
| Micrófono | `RecorderService()` | extra `recorder` + `brew install portaudio` |

## Ejemplos incluidos (oficiales)

- [`ejemplos/gtts-example.py`](./ejemplos/gtts-example.py) — básico gratis.
- [`ejemplos/bookmark-example.py`](./ejemplos/bookmark-example.py) — sincronía por palabra/sílaba.
- [`ejemplos/voiceover-demo.py`](./ejemplos/voiceover-demo.py) — demo completa.
- [`ejemplos/recorder-example.py`](./ejemplos/recorder-example.py) — grabar tu propia voz.
