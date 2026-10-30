#!/usr/bin/env bash
# Controlli da fare in locale prima di ogni push su dev: gli stessi del Controllo pack
# (ci_pack.sh), con l'indice scritto da packwiz_index.py. Aggiorna indice, inventario e
# controllo.md, che vanno nel commit: il Controllo pack fallisce se il commit non li ha.
# Uso: bash scripts/controllo_locale.sh <cartella pack>     es. bash scripts/controllo_locale.sh 1.21.1/pack
set -uo pipefail
PACK="$1"
INV="$(dirname "$PACK")/data/inventario"
if bash scripts/ci_pack.sh "$PACK" --locale; then
  echo "Controllo locale: tutto a posto (indice, inventario e $INV/controllo.md aggiornati: vanno nel commit)"
else
  echo "Controllo locale: qualcosa è fallito (vedi sopra)"
  exit 1
fi
