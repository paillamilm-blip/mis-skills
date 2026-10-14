---
inclusion: always
---

# Mantener el paquete de skills

- La fuente de las skills es `kiro-skills/NN-segmento/`. No edites `.kiro/skills/` ni `CATALOGO-KIRO.md` a mano, porque se generan.
- Después de agregar o cambiar cualquier skill, corre `python3 scripts/preparar-kiro-skills.py`. Debe terminar sin `ERROR`. Commitea también `.kiro/skills/` y `CATALOGO-KIRO.md`.
- Cada skill nueva necesita un `SKILL.md` con frontmatter `name` (igual al nombre de la carpeta, en minúsculas y con guiones) y `description` de 1024 caracteres como máximo, que diga cuándo usarla.
- Actualiza los conteos (README, DOCUMENTO-MAESTRO, COMANDOS) con `scripts/contar-skills.sh`.
- Recuérdale al usuario que vuelva a subir `.kiro/skills` en Kiro Web → Settings → Sync (ver `INSTALAR-EN-KIRO.md`).
