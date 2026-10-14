#!/usr/bin/env python3
"""
preparar-kiro-skills.py — Genera .kiro/skills/ listo para usar en Kiro.

Fuente de verdad: kiro-skills/NN-segmento/... (organizado por segmento).
Salida:           .kiro/skills/<nombre>/SKILL.md  (plano, un nivel, como exige Kiro)

Reglas que aplica (docs: https://kiro.dev/docs/skills y /docs/web/cloud-configuration):
  - Cada carpeta con SKILL.md (incluidas sub-skills de paraguas como strix/firecrawl)
    pasa a ser una skill de primer nivel.
  - `name` del frontmatter = nombre de la carpeta (minúsculas, números y guiones, <=64).
  - `description` obligatoria (<=1024 caracteres).
  - Solo archivos de texto, máximo 25 archivos por skill, <=4 MB por archivo
    (límites de Settings > Sync en Kiro Web). Los archivos que no caben se listan en
    ARCHIVOS-EXTRA.md con su enlace directo en GitHub para que el agente los descargue.
  - Se omiten plantillas *.tmpl (no se usan en tiempo de ejecución).

Uso:
  python3 scripts/preparar-kiro-skills.py          # regenera .kiro/skills/
  python3 scripts/preparar-kiro-skills.py --check  # solo valida, no escribe
"""
from __future__ import annotations

import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "kiro-skills")
OUT = os.path.join(ROOT, ".kiro", "skills")
RAW = "https://raw.githubusercontent.com/paillamilm-blip/mis-skills/main/"

MAX_FILES = 25
MAX_BYTES = 4_000_000
MAX_DESC = 1024
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Sub-skills con nombre genérico: se les antepone el nombre del paraguas.
PREFIJAR = {"agent-browser"}
# Casos donde el SKILL.md vive en una subcarpeta pero representa a la skill completa.
SKILL_COMPLETA = {"leankg": "skills/usage"}


def es_skill_md(nombre: str) -> bool:
    return nombre.lower() == "skill.md"


def es_texto(ruta: str) -> bool:
    try:
        with open(ruta, "rb") as f:
            datos = f.read()
        if b"\0" in datos:
            return False
        datos.decode("utf-8")
        return True
    except (UnicodeDecodeError, OSError):
        return False


def descubrir():
    """Devuelve lista de (nombre_salida, segmento, carpeta_skill, carpeta_contenido, skill_md)."""
    skills = []
    for seg in sorted(os.listdir(SRC)):
        seg_p = os.path.join(SRC, seg)
        if not os.path.isdir(seg_p):
            continue
        for top in sorted(os.listdir(seg_p)):
            top_p = os.path.join(seg_p, top)
            if not os.path.isdir(top_p):
                continue
            if top in SKILL_COMPLETA:
                md_dir = os.path.join(top_p, SKILL_COMPLETA[top])
                md = next(f for f in os.listdir(md_dir) if es_skill_md(f))
                skills.append((top, seg, top_p, top_p, os.path.join(md_dir, md)))
                continue
            for dp, dn, fn in os.walk(top_p):
                dn.sort()
                md = next((f for f in fn if es_skill_md(f)), None)
                if not md:
                    continue
                if dp == top_p:
                    nombre = top
                else:
                    base = os.path.basename(dp)
                    nombre = f"{top}-{base}" if top in PREFIJAR else base
                skills.append((nombre, seg, dp, dp, os.path.join(dp, md)))
    return skills


def archivos_de(carpeta: str, skill_md: str, otras_skills: set[str]):
    """Archivos de la skill, sin entrar en sub-skills anidadas."""
    res = []
    for dp, dn, fn in os.walk(carpeta):
        dn[:] = sorted(d for d in dn if os.path.join(dp, d) not in otras_skills and d != ".git")
        for f in sorted(fn):
            p = os.path.join(dp, f)
            if p == skill_md or f.endswith(".tmpl") or f == ".DS_Store":
                continue
            res.append(p)
    return res


def normalizar_frontmatter(texto: str, nombre: str) -> tuple[str, list[str]]:
    errores = []
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", texto, re.S)
    if not m:
        errores.append("sin frontmatter")
        return texto, errores
    fm = m.group(1)
    if re.search(r"^name:", fm, re.M):
        fm = re.sub(r"^name:.*$", f"name: {nombre}", fm, count=1, flags=re.M)
    else:
        fm = f"name: {nombre}\n" + fm
    # Descripciones cortas (estilo gstack) + lista `triggers:` → sumar los triggers a la
    # descripción, porque Kiro activa las skills comparando el pedido con la descripción.
    t = re.search(r"^triggers:\s*\n((?:[ \t]+-[^\n]*\n?)+)", fm + "\n", re.M)
    linea = re.search(r"^description:[ \t]*([^\s>|].*)$", fm, re.M)
    if t and linea:
        trig = [x.strip().strip('"\'') for x in re.findall(r"-\s*(.+)", t.group(1))]
        base = linea.group(1).strip().strip('"\'').rstrip(".")
        nueva = f"{base}. Use when the user says: " + "; ".join(trig) + "."
        if len(nueva) <= MAX_DESC:
            nueva = nueva.replace("\\", "\\\\").replace('"', '\\"')
            fm = fm[: linea.start()] + f'description: "{nueva}"' + fm[linea.end():]
    # Largo aproximado de la descripción (línea simple o bloque YAML).
    d = re.search(r"^description:[ \t]*(.*?)(?=^\S[^\n]*:|\Z)", fm, re.S | re.M)
    if not d or not d.group(1).strip():
        errores.append("sin description")
    else:
        desc = re.sub(r"^[>|][-+]?\s*", "", d.group(1).strip())
        desc = re.sub(r"\s+", " ", desc).strip().strip('"\'')
        if len(desc) > MAX_DESC:
            errores.append(f"description de {len(desc)} caracteres (> {MAX_DESC})")
    return f"---\n{fm}\n---\n" + texto[m.end():], errores


SEGMENTOS = {
    "01-estrategia": "🧠 01 — Estrategia",
    "02-ejecucion": "🚀 02 — Ejecución",
    "03-diseno": "🎨 03 — Diseño",
    "04-codigo-calidad": "🔍 04 — Código y Calidad",
    "05-testing-qa": "🧪 05 — Testing y QA",
    "06-seguridad": "🛡 06 — Seguridad",
    "07-deploy-ship": "🚀 07 — Deploy y Ship",
    "08-automatizacion": "🤖 08 — Automatización",
    "09-documentacion": "📝 09 — Documentación",
    "10-utilidades": "🛠 10 — Utilidades",
    "11-producto": "🧬 11 — Producto",
    "12-marketing-content": "📣 12 — Marketing y Content",
}


def descripcion_corta(skill_md: str) -> str:
    texto = open(skill_md, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---", texto, re.S)
    d = re.search(r"^description:[ \t]*(.*?)(?=^\S[^\n]*:|\Z)", m.group(1), re.S | re.M) if m else None
    if not d:
        return ""
    desc = re.sub(r"^[>|][-+]?\s*", "", d.group(1).strip())
    desc = re.sub(r"\s+", " ", desc).strip().strip('"\'').replace('\\"', '"').replace("|", "/")
    return desc if len(desc) <= 160 else desc[:157].rsplit(" ", 1)[0] + "…"


def escribir_catalogo(skills) -> None:
    lineas = [
        "# 📇 Catálogo de skills para Kiro",
        "",
        "> Generado por `scripts/preparar-kiro-skills.py` — no editar a mano.",
        f"> {len(skills)} skills instalables en `.kiro/skills/`. Úsalas por su nombre con `/nombre`",
        "> o simplemente pidiendo la tarea: Kiro activa la skill cuya descripción coincide.",
        "> Cómo instalarlas en todos tus chats: [INSTALAR-EN-KIRO.md](./INSTALAR-EN-KIRO.md).",
        "",
    ]
    for seg in SEGMENTOS:
        del_seg = [s for s in skills if s[1] == seg]
        if not del_seg:
            continue
        lineas += [f"## {SEGMENTOS[seg]} ({len(del_seg)})", "", "| Comando | Qué hace |", "|---------|----------|"]
        for nombre, _, _, _, md in del_seg:
            lineas.append(f"| [`/{nombre}`](./.kiro/skills/{nombre}/SKILL.md) | {descripcion_corta(md)} |")
        lineas.append("")
    with open(os.path.join(ROOT, "CATALOGO-KIRO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))


def main() -> int:
    solo_check = "--check" in sys.argv
    skills = descubrir()
    carpetas_skill = {s[2] for s in skills}
    problemas, avisos, nombres = [], [], {}

    if not solo_check:
        shutil.rmtree(OUT, ignore_errors=True)
        os.makedirs(OUT)

    for nombre, seg, carpeta, contenido, skill_md in skills:
        if not NAME_RE.match(nombre) or len(nombre) > 64:
            problemas.append(f"{nombre}: nombre inválido")
        if nombre in nombres:
            problemas.append(f"{nombre}: nombre duplicado ({nombres[nombre]} y {carpeta})")
            continue
        nombres[nombre] = carpeta

        texto = open(skill_md, encoding="utf-8").read()
        texto, errs = normalizar_frontmatter(texto, nombre)
        problemas += [f"{nombre}: {e}" for e in errs]

        otras = carpetas_skill - {carpeta}
        archivos = archivos_de(contenido, skill_md, otras)
        textos = [p for p in archivos if es_texto(p) and os.path.getsize(p) <= MAX_BYTES]
        excluidos = [p for p in archivos if p not in textos]

        # Si sobran archivos: priorizar los que SKILL.md menciona, luego los más cercanos.
        cupo = MAX_FILES - 1  # SKILL.md
        if len(textos) > cupo:
            cupo -= 1  # ARCHIVOS-EXTRA.md
            def prioridad(p):
                rel = os.path.relpath(p, contenido)
                citado = rel in texto or os.path.basename(p) in texto
                return (0 if citado else 1, rel.count(os.sep), os.path.getsize(p))
            textos.sort(key=prioridad)
            excluidos += textos[cupo:]
            textos = textos[:cupo]

        if excluidos:
            avisos.append(f"{nombre}: {len(excluidos)} archivo(s) fuera del paquete -> ARCHIVOS-EXTRA.md")
            texto = texto.rstrip() + (
                "\n\n---\n> 📦 Archivos adicionales de esta skill (datos, binarios o código) están en "
                "[ARCHIVOS-EXTRA.md](./ARCHIVOS-EXTRA.md) con su enlace directo para descargarlos.\n"
            )

        if solo_check:
            continue
        destino = os.path.join(OUT, nombre)
        os.makedirs(destino)
        with open(os.path.join(destino, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(texto)
        for p in textos:
            rel = os.path.relpath(p, contenido)
            os.makedirs(os.path.dirname(os.path.join(destino, rel)), exist_ok=True)
            shutil.copy2(p, os.path.join(destino, rel))
        if excluidos:
            lineas = [
                f"# Archivos extra de `{nombre}`\n",
                "No caben en el paquete de Kiro (máx. 25 archivos de texto por skill). "
                "Descárgalos solo si la tarea los necesita, por ejemplo:\n",
                "```bash\ncurl -fsSLO <enlace>\n```\n",
                "| Archivo | Enlace |",
                "|---------|--------|",
            ]
            for p in sorted(excluidos):
                rel = os.path.relpath(p, contenido)
                url = RAW + os.path.relpath(p, ROOT).replace(os.sep, "/").replace(" ", "%20")
                lineas.append(f"| `{rel}` | {url} |")
            with open(os.path.join(destino, "ARCHIVOS-EXTRA.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(lineas) + "\n")

    if not solo_check:
        escribir_catalogo(skills)

    print(f"Skills encontradas: {len(skills)}")
    for a in avisos:
        print("  aviso:", a)
    for p in problemas:
        print("  ERROR:", p)
    if not solo_check:
        print(f"Generado: {os.path.relpath(OUT, ROOT)}/ ({len(nombres)} skills)")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
