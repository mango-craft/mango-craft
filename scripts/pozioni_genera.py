#!/usr/bin/env python3
"""Genera la lista nera degli amuleti di pozione di Apotheosis nel datapack matteo_tweaks, dalle regole in CSV.

Uso: python3 scripts/pozioni_genera.py <cartella versione> [--dry-run] [--verifica] [--report FILE]

Come mercato_genera.py, interroga la base dati (scripts/botanypots_db.py, che si rifà da sola se inventario, datapack o
CSV sono cambiati) e scrive ciò che la vista POZIONE_LISTA_NERA dice di scrivere. La regola sta in
<versione>/data/pozioni/pozione_custom.csv: una riga per pozione (pozione_id), `varianti` = tutte (la regola vale per
tutte le varianti lunghe e forti della stessa pozione) o questa (solo lei, e vince sulla famiglia), `amuleto` = 0 (in
lista nera) o 1 (ammessa: serve per riammettere una variante di una famiglia in lista nera), `motivo`.

Cosa scrive, sotto <versione>/pack/config/paxi/datapacks/matteo_tweaks/data/:
- apotheosis/tags/potion/potion_charm_blacklist.json   le pozioni della lista nera, ognuna con "required": false
  (togliere una mod non dà errori). L'etichetta di Apotheosis è vuota: la nostra si aggiunge (niente "replace").
  Con la lista vuota il file non c'è.

Il file è dello script: si cancella e si riscrive a ogni esecuzione (il readme della cartella resta).
--verifica non scrive: confronta il file che scriverebbe con quello nel datapack ed esce con 1 se differisce.
Regole di Apotheosis 8.9.0 (sorgente, PotionCharmItem.isValidPotion): l'amuleto si fa solo con pozioni di un solo
effetto, non istantaneo, e non nell'etichetta; tema 1.21.1/theme-knowledge/pozioni.md.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from botanypots_db import DP, BotanyPotsDB  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FILE = Path("apotheosis") / "tags" / "potion" / "potion_charm_blacklist.json"


def piano(db: BotanyPotsDB) -> tuple[dict[Path, dict], list]:
    righe = db.query("SELECT * FROM POZIONE_LISTA_NERA ORDER BY pozione_id")
    if not righe:
        return {}, []
    return {FILE: {"values": [{"id": r["pozione_id"], "required": False} for r in righe]}}, righe


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("versione", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="non scrive niente, stampa solo il rapporto")
    ap.add_argument("--verifica", action="store_true", help="non scrive: esce con 1 se il datapack differisce dal piano")
    ap.add_argument("--report", type=Path)
    a = ap.parse_args()
    ver = a.versione if a.versione.is_absolute() else ROOT / a.versione
    data = ver / DP
    db = BotanyPotsDB(ver)
    file, righe = piano(db)
    f = data / FILE
    vecchio = {FILE: json.loads(f.read_text(encoding="utf-8"))} if f.exists() else {}

    famiglie = {r["famiglia"] for r in righe}
    dedotte = [r["pozione_id"] for r in righe if r["dedotta"]]
    testo = "\n".join([f"Lista nera degli amuleti: {len(righe)} pozioni in {len(famiglie)} famiglie"]
                      + [f"- {r['pozione_id']} ({r['nome'] or 'gioco base'}): {r['motivo']}" for r in righe]
                      + ([f"Nomi dedotti dalla traduzione, da confermare in gioco: {', '.join(dedotte)}"] if dedotte else []))
    print(testo)
    if a.report:
        a.report.write_text(testo + "\n", encoding="utf-8")
    diverso = vecchio != file
    if a.verifica:
        if diverso:
            print("La lista nera degli amuleti NON corrisponde alle regole (rilanciare scripts/pozioni_genera.py).")
            return 1
        print("Lista nera degli amuleti coerente con le regole.")
        return 0
    if a.dry_run:
        print("(dry-run) file da cambiare:", 1 if diverso else 0)
        return 0
    if not file:
        if f.exists():
            f.unlink()
        print("Lista nera vuota: nessun file.")
        return 0
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(file[FILE], indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"Scritto {FILE.as_posix()} ({'cambiato' if diverso else 'uguale'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
