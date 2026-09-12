#!/usr/bin/env bash
#
# contar-skills.sh — Recuento oficial de skills de IA del repo mis-skills.
#
# Criterio oficial: una "skill" = una carpeta de NIVEL SUPERIOR dentro de un
# segmento (kiro-skills/NN-segmento/<skill>/) que contenga algún SKILL.md en su
# árbol. Es la unidad que se copia/instala; las sub-skills internas (p. ej.
# agent-browser/core, firecrawl/firecrawl-build) NO se cuentan por separado.
#
# Uso:
#   ./scripts/contar-skills.sh          # tabla por segmento + total
#
set -euo pipefail

# Directorio raíz del repo (padre de scripts/)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIRO="$ROOT/kiro-skills"

if [[ ! -d "$KIRO" ]]; then
  echo "No se encontró $KIRO" >&2
  exit 1
fi

total=0
printf '%-28s %s\n' "SEGMENTO" "SKILLS"
printf '%-28s %s\n' "----------------------------" "------"

for seg in "$KIRO"/*/; do
  seg_name="$(basename "$seg")"
  n=0
  for sub in "$seg"*/; do
    [[ -d "$sub" ]] || continue
    if find "$sub" -iname 'skill.md' -print -quit | grep -q .; then
      n=$((n + 1))
    fi
  done
  printf '%-28s %s\n' "$seg_name" "$n"
  total=$((total + n))
done

printf '%-28s %s\n' "----------------------------" "------"
printf '%-28s %s\n' "TOTAL" "$total"
