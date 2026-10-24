#!/usr/bin/env bash
# Controlli completi di un pack, usati da tutti i workflow che lo modificano.
# Uso: bash scripts/ci_pack.sh <cartella pack>
# Serve packwiz nel PATH e la rete (per l'inventario). Esegue tutti i passi anche se
# uno fallisce, così indice, inventario e rapporto vengono comunque aggiornati;
# alla fine esce con errore se almeno un passo è fallito.
set -uo pipefail
PACK="$1"
INV="$(dirname "$PACK")/data/inventario"
status=0
(cd "$PACK" && packwiz refresh) || status=1
python3 scripts/check_pack.py "$PACK" || status=1
python3 scripts/inventory.py "$PACK" "$INV" || status=1
python3 scripts/check_ids.py "$PACK" "$INV" --report "$INV/controllo.md" > /dev/null || status=1
# Vasi di Botany Pots: i file generati devono corrispondere alle regole, e la base dati deve passare i controlli
VER="$(dirname "$PACK")"
if [ -f "$VER/data/vasi/coltura_custom.csv" ]; then
  python3 scripts/botanypots_genera.py "$VER" --verifica || status=1
  python3 scripts/botanypots_db.py "$VER" refresh > /dev/null || status=1
fi
exit $status
