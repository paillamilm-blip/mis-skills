# ✅ Usar tus skills en cualquier chat de Kiro

Tus skills ya están empaquetadas en la carpeta **`.kiro/skills/`** de este repositorio:
**140 skills**, cada una en su propia carpeta, en el formato que exige Kiro.
El índice con todas está en [CATALOGO-KIRO.md](./CATALOGO-KIRO.md).

> ¿Por qué 140 y no 118? El conteo oficial (118) toma las skills "paraguas" como una sola,
> por ejemplo Strix o el Motor de Videos. Kiro necesita cada sub-skill por separado, así que aquí aparecen todas.

## Opción A — Chats sobre este repo (automático)

En un chat de Kiro que abre el repo `mis-skills`, Kiro lee `.kiro/skills/` solo. No tienes que hacer nada.

## Opción B — Todos tus chats, con cualquier repo (recomendado, se hace 1 vez)

Así las skills quedan en tu cuenta de Kiro y funcionan también en Sistema-omicrom y en cualquier otro proyecto.

**1. Baja la última versión a tu Mac.** Copia y pega en la Terminal:

```bash
cd ~/Downloads && ( [ -d mis-skills ] || git clone https://github.com/paillamilm-blip/mis-skills.git ) && cd mis-skills && git checkout main && git pull origin main && open .kiro
```

El último comando (`open .kiro`) abre una ventana de Finder. Adentro verás la carpeta **`skills`**.

**2. Súbela a Kiro Web:**
1. Abre https://app.kiro.dev/settings/cloud-config, o en Kiro Web ve a **Settings → Sync**.
2. **Arrastra la carpeta `skills`** desde el Finder al recuadro de subida.
3. Revisa la lista. Todas deberían aparecer como **New**.
4. Presiona **Upload N files**.

**3. Comprueba que quedaron:** en **Settings → Skills** deberías ver las 140.

Desde ese momento, todos los chats nuevos de Kiro Web las tienen disponibles.
Si quieres usarlas también en Kiro en tu computador, activa en la misma página
**"Apply your cloud configuration to local sessions"**.

## Cómo se usan en un chat

- **Automático:** pide la tarea con tus palabras, por ejemplo *"hazme un short vertical sobre X"*. Kiro elige la skill cuya descripción coincide con tu pedido.
- **Directo:** escribe `/` + el nombre de la skill, por ejemplo `/gsd`, `/obra-maestra`, `/manim-voiceover`… (los nombres están en el [catálogo](./CATALOGO-KIRO.md)).
- Para ver qué skills tiene cargadas un chat, escribe `/context show`.

## Cuando agregues o cambies skills

1. La skill se crea o edita en `kiro-skills/NN-segmento/` (ahí sigue el orden por segmentos).
2. Se regenera el paquete y el catálogo con:
   ```bash
   python3 scripts/preparar-kiro-skills.py
   ```
3. Se vuelve a subir la carpeta `skills` en **Settings → Sync**. Las que cambiaron aparecen
   como **Update** y vienen sin marcar, así que hay que marcarlas para reemplazarlas.

> Puedes pedirle a Kiro que haga los pasos 1 y 2 por ti. Tú solo haces el paso 3.

## Límites de Kiro (ya resueltos en el paquete)

Kiro acepta **hasta 25 archivos de texto por skill**. Hay 9 skills grandes que traen más:
`browse`, `ui-styling`, `ui-ux-pro-max`, `design`, `impeccable`, `design-system`, `shadcn`,
`reglas-cursor-web` y `manim-animation-agent`. Para esas, el paquete lleva lo esencial y un archivo
`ARCHIVOS-EXTRA.md` con el enlace directo a cada archivo que faltó. Así el agente lo
descarga solo cuando la tarea lo necesita.
