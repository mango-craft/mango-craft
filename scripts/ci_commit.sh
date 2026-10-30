#!/usr/bin/env bash
# Salva con un commit i file che i workflow di aggiunta mod rigenerano (metafile, indice,
# inventario) e lo manda sul ramo corrente, riprovando se nel frattempo il ramo è andato avanti.
# Solo nelle GitHub Actions: in locale i commit si fanno a mano, con il proprio nome.
# Uso: bash scripts/ci_commit.sh "<messaggio>" ["<descrizione>"]
set -euo pipefail
if [ -z "${GITHUB_ACTIONS:-}" ]; then
  echo "ci_commit.sh gira solo nelle GitHub Actions" >&2
  exit 1
fi
# Il nome del bot solo per questi comandi: la configurazione del repository non cambia
bot=(-c user.name="github-actions[bot]" -c user.email="41898282+github-actions[bot]@users.noreply.github.com")
for d in */pack */data/inventario; do
  if [ -e "$d" ]; then git add -A -- "$d"; fi
done
if git diff --cached --quiet; then
  echo "Niente da salvare."
  exit 0
fi
msg=(-m "$1")
if [ $# -ge 2 ] && [ -n "$2" ]; then msg+=(-m "$2"); fi
git "${bot[@]}" commit -q "${msg[@]}"
for tentativo in 1 2 3; do
  if git push -q; then exit 0; fi
  if [ "$tentativo" -eq 3 ]; then break; fi
  if ! git "${bot[@]}" pull -q --rebase; then
    git rebase --abort || true
    echo "Il ramo è andato avanti con modifiche agli stessi file: rilanciare il workflow" >&2
    exit 1
  fi
done
echo "Push non riuscito" >&2
exit 1
