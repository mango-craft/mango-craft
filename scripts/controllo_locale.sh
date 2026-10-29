#!/usr/bin/env bash
# Controlli del pack da fare in locale prima di un push su dev: gli stessi di ci_pack.sh, senza l'inventario
# (che scarica tutti i jar: lo rifà il workflow) e senza packwiz (l'indice lo scrive packwiz_index.py).
# Uso: bash scripts/controllo_locale.sh <cartella pack>     es. bash scripts/controllo_locale.sh 1.21.1/pack
set -uo pipefail
PACK="$1"
VER="$(dirname "$PACK")"
INV="$VER/data/inventario"
status=0
python3 scripts/packwiz_index.py "$PACK" || status=1
python3 scripts/check_pack.py "$PACK" || status=1
python3 scripts/check_ids.py "$PACK" "$INV" --report "$INV/controllo.md" > /dev/null || status=1
if [ -f "$VER/data/vasi/coltura_custom.csv" ]; then
  python3 scripts/botanypots_genera.py "$VER" --verifica || status=1
  python3 scripts/botanypots_db.py "$VER" refresh > /dev/null || status=1
fi
if [ -f "$VER/data/mercato/mercato_base.csv" ]; then
  python3 scripts/mercato_genera.py "$VER" --verifica || status=1
fi
if [ -f "$VER/data/pozioni/pozione_custom.csv" ]; then
  python3 scripts/pozioni_genera.py "$VER" --verifica || status=1
fi
if [ $status -eq 0 ]; then echo "Controllo locale: tutto a posto ($INV/controllo.md aggiornato)"; else echo "Controllo locale: qualcosa è fallito (vedi sopra)"; fi
exit $status
