#!/usr/bin/env bash
# Salva con un commit i file che i workflow rigenerano (indice, metafile, inventario)
# e lo manda sul ramo corrente, riprovando se nel frattempo il ramo è andato avanti.
# Uso: bash scripts/ci_commit.sh "<messaggio>" ["<descrizione>"]
set -euo pipefail
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A -- '*/pack' '*/data/inventario'
if git diff --cached --quiet; then
  echo "Niente da salvare."
  exit 0
fi
if [ $# -ge 2 ] && [ -n "$2" ]; then
  git commit -q -m "$1" -m "$2"
else
  git commit -q -m "$1"
fi
for i in 1 2 3; do
  if git push -q; then exit 0; fi
  git pull -q --rebase
done
echo "Push non riuscito"; exit 1
