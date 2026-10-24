#!/usr/bin/env python3
"""Genera le voci e i listini del mercato di Farming for Blockheads nel datapack matteo_tweaks, dalle regole in CSV.

Uso: python3 scripts/mercato_genera.py <cartella versione> [--dry-run] [--verifica] [--report FILE]

A differenza di botanypots_genera.py, questo script non rilegge i CSV: interroga la base dati delle piante
(scripts/botanypots_db.py, che si rifà da sola se inventario, datapack o CSV sono cambiati) e scrive ciò che le
viste MERCATO_PIANO_VOCE e MERCATO_PIANO_PRESET dicono di scrivere. Le regole stanno in <versione>/data/mercato/:
- mercato_base.csv            origine (overworld, nether, end…) e intervallo di rarità → moneta e quantità base
- rarita_mercato_settings.csv classe di rarità (anagrafica in <versione>/data/rarita.csv) → moltiplicatore
- mercato_mod_custom.csv      mod (slug) → origine e classe predefinite di tutte le sue piante
- mercato_tipo_custom.csv     tipo di piantabile (seme, alberello, vegetazione…) → categoria, si vende o no
- mercato_voce_custom.csv     eccezioni per oggetto: categoria, origine, classe, escluso
- mercato_preset_custom.csv   listini delle mod da riscrivere con il nostro prezzo, o da accendere/spegnere
Prezzo = quantità base × moltiplicatore, per eccesso; sopra 64, blocchi per eccesso (il pagamento è uno stack
in uno slot: MarketMenu di FFB 21.1.14). Priorità delle regole: oggetto > tipo > mod.

Cosa scrive, sotto <versione>/pack/config/paxi/datapacks/matteo_tweaks/data/:
- matteo_tweaks/recipe/market/<namespace>/<oggetto>.json     una voce per riga di MERCATO_PIANO_VOCE,
  con la condizione `neoforge:item_exists` sull'oggetto
- matteo_tweaks/market_presets/<origine>_<classe>.json       un listino nostro per ogni coppia usata
- <namespace>/market_presets/<nome>.json                     i listini delle mod riscritti **allo stesso percorso**
  del file originale (Paxi carica il datapack sopra alle mod), da mercato_preset_custom.csv

Queste cartelle sono dello script: i .json si cancellano e si riscrivono a ogni esecuzione (i readme restano).
--verifica non scrive: confronta i file che scriverebbe con quelli nel datapack ed esce con 1 se differiscono.
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from botanypots_db import DP, NOSTRO, BotanyPotsDB  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TIPO = "farmingforblockheads:market"


def voce(oggetto: str, categoria: str, preset: str) -> dict:
    return {"neoforge:conditions": [{"type": "neoforge:item_exists", "item": oggetto}],
            "type": TIPO, "category": categoria, "preset": preset, "result": {"item": oggetto}}


def preset(pagamento: str, quantita: int, acceso: int) -> dict:
    d = {"payment": {"ingredient": {"item": pagamento}, "count": int(quantita)}}
    if not acceso:
        d["enabled"] = False
    return d


def piano(db: BotanyPotsDB) -> tuple[dict[Path, dict], list[str]]:
    """I file da scrivere (percorso relativo a data/ → contenuto) e i motivi di ciò che si salta."""
    file, saltati = {}, []
    for r in db.query("SELECT * FROM MERCATO_PIANO_VOCE ORDER BY oggetto_id"):
        ns, nome = r["oggetto_id"].split(":")
        file[Path(NOSTRO) / "recipe" / "market" / ns / f"{nome}.json"] = voce(r["oggetto_id"], r["categoria_id"], r["preset_id"])
    for r in db.query("SELECT * FROM MERCATO_PIANO_PRESET ORDER BY tipo, preset_id"):
        if not r["pagamento_id"]:
            saltati.append(f"preset {r['preset_id']}: senza prezzo (origine o classe non in MERCATO_PREZZO, e nessun file originale)")
            continue
        ns, nome = r["preset_id"].split(":")
        p = Path(ns) / "market_presets" / f"{nome}.json"
        if p in file:
            saltati.append(f"preset {r['preset_id']}: doppione")
            continue
        file[p] = preset(r["pagamento_id"], r["quantita"], r["acceso"])
    return file, saltati


def esistenti(data: Path) -> dict[Path, dict]:
    out = {}
    for f in [*(data / NOSTRO / "recipe" / "market").glob("**/*.json"), *data.glob("*/market_presets/*.json")]:
        out[f.relative_to(data)] = json.loads(f.read_text(encoding="utf-8"))
    return out


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
    file, saltati = piano(db)
    vecchi = esistenti(data)

    righe = [f"Voci: {sum(1 for p in file if p.parts[1] == 'recipe')} · listini nostri: "
             f"{sum(1 for p in file if p.parts[0] == NOSTRO and p.parts[1] == 'market_presets')} · listini delle mod riscritti: "
             f"{sum(1 for p in file if p.parts[0] != NOSTRO)} · saltati: {len(saltati)}"]
    per_mod = Counter(p.parts[3] for p in file if p.parts[1] == "recipe")
    righe.append("Voci per namespace: " + ", ".join(f"{m} {n}" for m, n in per_mod.most_common()))
    senza = db.query("SELECT slug, count(*) AS n FROM MERCATO_CANDIDATO WHERE escluso IS NULL AND (origine IS NULL OR classe IS NULL) GROUP BY slug ORDER BY n DESC")
    if senza:
        righe.append("Candidati senza regola (mod non in mercato_mod_custom.csv): " + ", ".join(f"{r['slug']} {r['n']}" for r in senza))
    righe += [f"Saltato: {s}" for s in saltati]
    diff = sorted({p for p in file if vecchi.get(p) != file[p]} | (set(vecchi) - set(file)))
    testo = "\n".join(righe)
    print(testo)
    if a.report:
        a.report.write_text(testo + "\n", encoding="utf-8")
    if a.verifica:
        if diff:
            print(f"Il datapack del mercato NON corrisponde alle regole: {len(diff)} file diversi, mancanti o di troppo "
                  "(rilanciare scripts/mercato_genera.py):")
            for p in diff[:30]:
                print(" -", p.as_posix())
            return 1
        print(f"Datapack del mercato coerente con le regole: {len(file)} file.")
        return 0
    if a.dry_run:
        print(f"(dry-run) file da scrivere o cambiare: {len(diff)}")
        return 0
    for p in set(vecchi) - set(file):
        (data / p).unlink()
    for p, d in file.items():
        f = data / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    # cartelle rimaste vuote
    for d in sorted({(data / p).parent for p in set(vecchi) - set(file)}, key=lambda x: -len(x.parts)):
        if d.exists() and not any(d.iterdir()):
            d.rmdir()
    print(f"Scritti {len(file)} file ({len(diff)} cambiati).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
