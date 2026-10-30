#!/usr/bin/env bash
# Tutti i controlli di un pack: indice, controllo del pack, inventario, controllo dei nomi,
# generatori (--verifica) e base dati. Rifà i file generati (indice, inventario, controllo.md):
# in locale vanno nel commit; il Controllo pack li rifà e fallisce se il commit non li aveva.
# Uso: bash scripts/ci_pack.sh <cartella pack> [--locale]
#   senza --locale l'indice lo scrive packwiz (nel PATH, nelle Actions): fa da verifica
#   indipendente; con --locale lo scrive packwiz_index.py, che dà lo stesso risultato.
# L'inventario scarica solo i jar cambiati (serve la rete). Esegue tutti i passi anche se uno
# fallisce e alla fine esce con errore se almeno uno è fallito.
set -uo pipefail
PACK="$1"
VER="$(dirname "$PACK")"
INV="$VER/data/inventario"
status=0
if [ "${2:-}" = --locale ]; then
  python3 scripts/packwiz_index.py "$PACK" || status=1
else
  (cd "$PACK" && packwiz refresh) || status=1
fi
python3 scripts/check_pack.py "$PACK" || status=1
python3 scripts/inventory.py "$PACK" "$INV" || status=1
python3 scripts/check_ids.py "$PACK" "$INV" --report "$INV/controllo.md" > /dev/null || status=1
# Vasi di Botany Pots: i file generati devono corrispondere alle regole
if [ -f "$VER/data/vasi/coltura_custom.csv" ]; then
  python3 scripts/botanypots_genera.py "$VER" --verifica || status=1
fi
# Base dati (piante, mercato, pozioni, confronto con il gioco): si mostrano solo
# i controlli falliti (❌) e gli avvisi che hanno trovato qualcosa (⚠️)
if [ -f "$VER/data/rarita.csv" ]; then
  if out=$(python3 scripts/botanypots_db.py "$VER" refresh 2>&1); then
    grep -E '^(❌|⚠)' <<< "$out" || true
  else
    echo "$out"
    status=1
  fi
fi
# Mercato e lista nera degli amuleti: i file generati devono corrispondere alle regole
# (leggono la base dati appena rifatta)
if [ -f "$VER/data/mercato/mercato_base.csv" ]; then
  python3 scripts/mercato_genera.py "$VER" --verifica || status=1
fi
if [ -f "$VER/data/pozioni/pozione_custom.csv" ]; then
  python3 scripts/pozioni_genera.py "$VER" --verifica || status=1
fi
exit $status
