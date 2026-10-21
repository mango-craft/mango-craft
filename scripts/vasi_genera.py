#!/usr/bin/env python3
"""Genera le ricette dei vasi di Botany Pots (colture e terreni) per il datapack matteo_tweaks.

Uso: python3 scripts/vasi_genera.py <cartella pack> [--dry-run] [--report FILE]
                                     [--copertura FILE] [--aggiunte FILE] [--inventario DIR]

Dati di partenza (nel repository, da riguardare a ogni aggiornamento delle mod):
- 1.21.1/data/vasi/copertura.json: le piante delle mod e una bozza di ricetta per ognuna (17/10/2026);
- 1.21.1/data/vasi/aggiunte.json: terreni, colture scritte a mano, esclusioni (con il motivo).

Cosa scrive (tutto sotto <pack>/config/paxi/datapacks/matteo_tweaks/data/):
- matteo_tweaks/recipe/botanypots/<mod>/crop/<blocco>.json   una coltura per pianta scoperta
- matteo_tweaks/recipe/botanypots/<mod>/soil/<blocco>.json   un terreno per blocco
- botanypots/tags/item/soil/dirt.json                        i terreni "di terra", perché le colture di terra
                                                              li accettino (etichetta botanypots:soil/dirt)

Le cartelle <mod> sono di proprietà dello script: a ogni esecuzione si cancellano e si riscrivono. Le cartelle
`crop` e `soil` direttamente sotto botanypots/ sono scritte a mano (Ars Nouveau) e non si toccano.

Si salta (con il motivo nel rapporto) ciò che non si può scrivere sicuro: blocco o seme che non esiste
nell'inventario, pianta esclusa, terreno il cui blocco non ha un oggetto (Botany Pots non saprebbe cosa metterci).
Non copre: le piante già coperte da Botany Pots, Botany Trees, dalle mod o dal nostro datapack, gli alberi di
Bountiful Fares (da copiare dal sorgente di Botany Trees) e le 8 piante di Regions Unexplored con i nomi vecchi
(si riscrivono solo se la prova in gioco dice che non funzionano).
"""
import argparse
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "1.21.1" / "data"
DP = "config/paxi/datapacks/matteo_tweaks/data"
COVERAGE_DA_SCRIVERE = {"none", "bcl"}  # le altre sono già coperte, o si trattano a parte (alias, bt-unreleased)


def carica_inventario(inv: Path) -> tuple[set, set]:
    blocks, items = set(), set()
    files = [inv / "minecraft.json", *sorted((inv / "mods").glob("*.json"))]
    for f in files:
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        blocks.update(d.get("blocks", {}))
        items.update(d.get("items", {}))
    return blocks, items


def cond_blocco(block: str) -> dict:
    return {"bookshelf:load_conditions": [{"type": "bookshelf:block_exists", "values": [block]}]}


def scrivi_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="non scrive niente, stampa solo il rapporto")
    ap.add_argument("--report", type=Path, help="scrive il rapporto anche in questo file")
    ap.add_argument("--copertura", type=Path, default=DATA / "vasi" / "copertura.json")
    ap.add_argument("--aggiunte", type=Path, default=DATA / "vasi" / "aggiunte.json")
    ap.add_argument("--inventario", type=Path, default=DATA / "inventario")
    a = ap.parse_args()

    cov = json.loads(a.copertura.read_text(encoding="utf-8"))
    add = json.loads(a.aggiunte.read_text(encoding="utf-8"))
    blocks, items = carica_inventario(a.inventario)
    esclusi = add.get("esclusi", {})

    colture: dict[str, dict] = {}   # blocco -> ricetta
    origine: dict[str, str] = {}    # blocco -> mod (slug)
    da_provare: list[str] = []      # colture scritte con nomi non verificabili sul sorgente
    saltate: list[tuple[str, str, str]] = []  # (mod, blocco, motivo)

    def aggiungi(mod: str, ricetta: dict, verifica: bool = False) -> None:
        blocco = ricetta["block"]
        if blocco in esclusi:
            saltate.append((mod, blocco, "esclusa: " + esclusi[blocco])); return
        if blocco not in blocks:
            saltate.append((mod, blocco, "il blocco non esiste nell'inventario")); return
        seme = (ricetta.get("input") or {}).get("item")
        if seme and seme not in items:
            saltate.append((mod, blocco, f"il seme {seme} non esiste nell'inventario")); return
        if blocco in colture:
            saltate.append((mod, blocco, "doppione")); return
        colture[blocco] = ricetta
        origine[blocco] = mod
        if verifica:
            da_provare.append(blocco)

    for p in cov["plants"]:
        if p["coverage"] not in COVERAGE_DA_SCRIVERE:
            continue
        if p.get("prio") == "skip":
            saltate.append((p["mod"], p["block"], "esclusa nella bozza del 17/10: " + (p.get("special") or p.get("note") or "prio skip")))
            continue
        draft = p.get("recipe_draft")
        if not draft:
            if not p["block"].startswith("?"):  # i nomi da chiarire (Roaster's Delight) sono in aggiunte.json
                saltate.append((p["mod"], p["block"], "nessuna bozza"))
            continue
        aggiungi(p["mod"], draft)
    for c in add.get("colture", []):
        aggiungi(c["mod"], c["ricetta"], verifica=c.get("da_provare", False))

    terreni: list[dict] = []
    for t in add.get("terreni", []):
        b = t["block"]
        if b not in blocks:
            saltate.append((t["mod"], b, "terreno: il blocco non esiste nell'inventario")); continue
        if b not in items:
            saltate.append((t["mod"], b, "terreno: il blocco non ha un oggetto, Botany Pots non saprebbe cosa mettere nel vaso")); continue
        terreni.append(t)

    # --- scrittura
    bp = a.pack / DP / "matteo_tweaks" / "recipe" / "botanypots"
    tag = a.pack / DP / "botanypots" / "tags" / "item" / "soil" / "dirt.json"
    if not a.dry_run:
        if bp.exists():
            for d in bp.iterdir():
                if d.is_dir() and d.name not in ("crop", "soil"):
                    shutil.rmtree(d)
        for blocco, ric in colture.items():
            ns, nome = blocco.split(":")
            scrivi_json(bp / ns / "crop" / f"{nome}.json", ric)
        for t in terreni:
            ns, nome = t["block"].split(":")
            ric = {**cond_blocco(t["block"]), "type": "botanypots:block_derived_soil", "block": t["block"]}
            if t.get("growth_modifier"):
                ric["growth_modifier"] = t["growth_modifier"]
            scrivi_json(bp / ns / "soil" / f"{nome}.json", ric)
        dirt = sorted(t["block"] for t in terreni if t.get("terra"))
        if dirt:
            scrivi_json(tag, {"replace": False, "values": [{"id": b, "required": False} for b in dirt]})
        elif tag.exists():
            tag.unlink()

    # --- rapporto
    out = []
    per_mod = Counter(origine.values())
    out.append(f"Colture scritte: {len(colture)} · terreni: {len(terreni)} · saltate: {len(saltate)}")
    out.append("")
    out.append("Colture per mod: " + ", ".join(f"{m} {n}" for m, n in sorted(per_mod.items(), key=lambda x: (-x[1], x[0]))))
    if da_provare:
        out.append("")
        out.append("Da provare in gioco (nomi non verificabili sul sorgente): " + ", ".join(da_provare))
    if saltate:
        out.append("")
        out.append("Saltate:")
        for mod, blocco, motivo in sorted(saltate):
            out.append(f"- {mod} · {blocco}: {motivo}")
    testo = "\n".join(out) + "\n"
    print(testo, end="")
    if a.report:
        a.report.write_text(testo, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
