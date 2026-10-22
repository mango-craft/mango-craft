#!/usr/bin/env python3
"""Genera i file di Botany Pots del datapack matteo_tweaks dalle nostre regole (i CSV in <versione>/data/vasi/).

Uso: python3 scripts/botanypots_genera.py <cartella versione> [--dry-run] [--report FILE]

Le regole (una tabella per cosa, caricate anche nella base dati di scripts/botanypots_db.py):
- terreno_rarita.csv            terreno → classe di rarità (bonus in rarita_pots_settings.csv), motivo
- terreno_tag_custom.csv      terreno → tag `botanypots:soil/*` in cui lo mettiamo
- coltura_custom.csv          una coltura da scrivere: seme, tempo, blocchi richiesti, grafica, note
- coltura_tag_custom.csv      coltura → tag ammessi (uno per riga, ne basta uno; nessuna riga = soil/dirt)
- coltura_raccolto_custom.csv coltura → raccolto (oggetti con quantità e probabilità, o una tabella del bottino)

Cosa scrive, sotto <versione>/pack/config/paxi/datapacks/matteo_tweaks/data/:
- matteo_tweaks/recipe/botanypots/<mod>/crop/<nome>.json   una coltura per riga di coltura_custom
- matteo_tweaks/recipe/botanypots/<mod>/soil/<nome>.json   un terreno per riga di terreno_rarita senza file originale;
  se il terreno ha già un file di una mod e la classe gli dà un bonus diverso, il file si scrive **allo stesso
  percorso del file originale** (botanypots/recipe/…), che così lo sostituisce (Paxi carica il datapack sopra alle mod)
- botanypots/tags/item/soil/<nome>.json                   un tag per ogni tag di terreno_tag_custom

Le cartelle <mod>/ sotto recipe/botanypots/ e i tag botanypots:soil/* sono dello script: si cancellano e si
riscrivono a ogni esecuzione. Non si toccano `crop/`, `soil/` e `alberi/` (scritti a mano).
Si salta, con il motivo nel rapporto, ciò che l'inventario non conosce (blocco, seme, raccolto o terreno inesistente).
"""
import argparse
import csv
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DP = "pack/config/paxi/datapacks/matteo_tweaks/data"
MIEI = ("crop", "soil", "alberi")  # cartelle scritte a mano, non si toccano


def carica_inventario(inv: Path):
    blocks, items, originali = set(), set(), {}
    for f in [inv / "minecraft.json", *sorted((inv / "mods").glob("*.json"))]:
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        blocks.update(d.get("blocks", {}))
        items.update(d.get("items", {}))
        for r in d.get("botanypots") or []:
            if r.get("type") in ("botanypots:soil", "botanypots:block_derived_soil"):
                ogg = r["input"]["item"] if r.get("input") else r.get("block")
                originali[ogg] = r
    return blocks, items, originali


def leggi_csv(p: Path) -> list[dict]:
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cond(blocchi: list[str]) -> dict:
    return {"bookshelf:load_conditions": [{"type": "bookshelf:block_exists", "values": blocchi}]}


def scrivi_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def numero(s: str):
    return int(s) if s.isdigit() else float(s)


def ricetta_coltura(c: dict, tags: list[dict], raccolti: list[dict]) -> dict:
    cid = c["coltura_id"]
    richiesti = c["richiesti"].split("|") if c["richiesti"] else [cid]
    libera = bool(c["richiesti"]) and cid not in richiesti  # senza blocco proprio (graticci)
    r = {**cond(richiesti), "type": "botanypots:crop" if libera else "botanypots:block_derived_crop"}
    if not libera:
        r["block"] = cid
    if c["seme"]:
        r["input"] = {"item": c["seme"]}
    if tags:
        ing = [{"type": "bookshelf:block_tag", "tag": t["tag"]} if t["ambito"] == "blocchi" else {"tag": t["tag"]}
               for t in sorted(tags, key=lambda t: int(t["ordine"]))]
        r["soil"] = ing[0] if len(ing) == 1 else {"type": "bookshelf:either", "ingredients": ing}
    if c["tempo"]:
        r["grow_time"] = int(c["tempo"])
    if c["display_blocco"]:  # uno o più blocchi (separati da |), ognuno con il suo spostamento facoltativo (x,y,z)
        blocchi = c["display_blocco"].split("|")
        offset = c["display_offset"].split("|") if c["display_offset"] else [""] * len(blocchi)
        lista = []
        for b, o in zip(blocchi, offset):
            d = {"type": "botanypots:simple", "block_state": {"block": b}}
            if o:
                d["options"] = {"offset": [numero(x) for x in o.split(",")]}
            lista.append(d)
        r["display"] = lista[0] if len(lista) == 1 and not c["display_offset"] else lista
    if c["rotazione"]:
        r["render_options"] = {"rotation": c["rotazione"]}
    if raccolti:
        gruppi = defaultdict(list)
        for x in raccolti:
            gruppi[int(x["gruppo"])].append(x)
        drops = []
        for g in sorted(gruppi):
            righe = gruppi[g]
            if righe[0]["tipo"] == "tabella":
                drops.append({"type": "botanypots:loot_table", "table_id": righe[0]["id"]})
            else:
                items = []
                for x in righe:
                    it = {"result": {"id": x["id"], "count": int(x["count"] or 1)}}
                    if x["chance"]:
                        it["chance"] = float(x["chance"])
                    items.append(it)
                drops.append({"type": "botanypots:items", "items": items})
        r["drops"] = drops
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("versione", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="non scrive niente, stampa solo il rapporto")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--verifica", action="store_true",
                    help="non scrive: confronta i file che scriverebbe con quelli nel datapack ed esce con 1 se differiscono")
    a = ap.parse_args()
    ver = a.versione if a.versione.is_absolute() else ROOT / a.versione
    vasi = ver / "data" / "vasi"
    blocks, items, originali = carica_inventario(ver / "data" / "inventario")

    classi = {r["classe"]: r for r in leggi_csv(vasi / "rarita_pots_settings.csv")}
    rarita = leggi_csv(vasi / "terreno_rarita.csv")
    ttag = leggi_csv(vasi / "terreno_tag_custom.csv")
    colture = leggi_csv(vasi / "coltura_custom.csv")
    ctag, cracc = defaultdict(list), defaultdict(list)
    for t in leggi_csv(vasi / "coltura_tag_custom.csv"):
        ctag[t["coltura_id"]].append(t)
    for x in leggi_csv(vasi / "coltura_raccolto_custom.csv"):
        cracc[x["coltura_id"]].append(x)

    saltate: list[tuple[str, str]] = []
    file_colture: dict[Path, dict] = {}
    for c in colture:
        cid = c["coltura_id"]
        richiesti = c["richiesti"].split("|") if c["richiesti"] else [cid]
        manca = [b for b in richiesti if b not in blocks]
        if manca:
            saltate.append((cid, f"blocco inesistente: {', '.join(manca)}")); continue
        if c["seme"] and c["seme"] not in items:
            saltate.append((cid, f"seme inesistente: {c['seme']}")); continue
        manca = [b for b in c["display_blocco"].split("|") if b and b not in blocks]
        if manca:
            saltate.append((cid, f"blocco della grafica inesistente: {', '.join(manca)}")); continue
        manca = [x["id"] for x in cracc[cid] if x["tipo"] == "oggetto" and x["id"] not in items]
        if manca:
            saltate.append((cid, f"raccolto inesistente: {', '.join(manca)}")); continue
        ns, nome = cid.split(":")
        p = Path(ns) / "crop" / f"{nome}.json"
        if p in file_colture:
            saltate.append((cid, "doppione")); continue
        file_colture[p] = ricetta_coltura(c, ctag[cid], cracc[cid])

    file_terreni: dict[Path, dict] = {}   # relativi a matteo_tweaks/recipe/botanypots/
    sostituzioni: dict[Path, dict] = {}   # relativi a data/ (stesso percorso del file originale)
    for r in rarita:
        t = r["terreno_id"]
        if t not in items:
            saltate.append((t, "terreno: oggetto inesistente")); continue
        if r["classe"] not in classi:
            saltate.append((t, f"terreno: classe sconosciuta {r['classe']}")); continue
        cl = classi[r["classe"]]
        crescita, resa = float(cl["crescita"]), float(cl["resa"])
        orig = originali.get(t)
        if orig is not None:
            if (float(orig.get("growth_modifier", 0)), float(orig.get("yield_modifier", 0))) == (crescita, resa):
                continue  # il file della mod dà già questo bonus
            ns, path = orig["id"].split(":", 1)
            ric = {k: v for k, v in orig.items() if k != "id"}
            ric.pop("growth_modifier", None); ric.pop("yield_modifier", None)
            if crescita:
                ric["growth_modifier"] = crescita
            if resa:
                ric["yield_modifier"] = resa
            sostituzioni[Path(ns) / "recipe" / f"{path}.json"] = ric
            continue
        if t not in blocks:
            saltate.append((t, "terreno: non è un blocco, serve un file scritto a mano")); continue
        ns, nome = t.split(":")
        ric = {**cond([t]), "type": "botanypots:block_derived_soil", "block": t}
        if crescita:
            ric["growth_modifier"] = crescita
        if resa:
            ric["yield_modifier"] = resa
        file_terreni[Path(ns) / "soil" / f"{nome}.json"] = ric

    tags: dict[str, list[str]] = defaultdict(list)
    for x in ttag:
        if x["ambito"] != "oggetti" or not x["tag"].startswith("botanypots:soil/"):
            saltate.append((x["terreno_id"], f"tag non gestito: {x['ambito']} {x['tag']}")); continue
        if x["terreno_id"] not in items:
            saltate.append((x["terreno_id"], "tag: oggetto inesistente")); continue
        tags[x["tag"]].append(x["terreno_id"])

    # --- scrittura
    data = ver / DP
    bp = data / "matteo_tweaks" / "recipe" / "botanypots"
    tagdir = data / "botanypots" / "tags" / "item" / "soil"
    attesi: dict[Path, dict] = {}  # percorso relativo a data/ -> contenuto
    for p, ric in file_colture.items():
        attesi[Path("matteo_tweaks/recipe/botanypots") / p] = ric
    for p, ric in file_terreni.items():
        attesi[Path("matteo_tweaks/recipe/botanypots") / p] = ric
    attesi.update(sostituzioni)
    for tag, terreni in tags.items():
        attesi[Path("botanypots/tags/item/soil") / f"{tag.split('/', 1)[1]}.json"] = {
            "replace": False, "values": [{"id": b, "required": False} for b in sorted(set(terreni))]}
    if a.verifica:
        presenti = set()
        for d in (bp.iterdir() if bp.exists() else []):
            if d.is_dir() and d.name not in MIEI:
                presenti |= {q.relative_to(data) for q in d.rglob("*.json")}
        if tagdir.exists():
            presenti |= {q.relative_to(data) for q in tagdir.glob("*.json")}
        for ns in {p.parts[0] for p in sostituzioni}:
            presenti |= {q.relative_to(data) for q in (data / ns / "recipe").rglob("*.json")} if (data / ns / "recipe").exists() else set()
        diversi = sorted(str(q) for q in presenti - set(attesi)) + sorted(str(q) for q in set(attesi) - presenti)
        diversi += sorted(str(q) for q in set(attesi) & presenti
                          if json.loads((data / q).read_text(encoding="utf-8")) != attesi[q])
        if diversi:
            print("File del datapack diversi da quelli generati dalle regole (rilanciare scripts/botanypots_genera.py):")
            print("\n".join(f"- {q}" for q in diversi))
            return 1
        print(f"Datapack dei vasi coerente con le regole: {len(attesi)} file.")
        return 0
    if not a.dry_run:
        if bp.exists():
            for d in bp.iterdir():
                if d.is_dir() and d.name not in MIEI:
                    shutil.rmtree(d)
        for ns in {p.parts[0] for p in sostituzioni}:
            if (data / ns / "recipe").exists():
                shutil.rmtree(data / ns / "recipe")
        if tagdir.exists():
            shutil.rmtree(tagdir)
        for p, ric in file_colture.items():
            scrivi_json(bp / p, ric)
        for p, ric in file_terreni.items():
            scrivi_json(bp / p, ric)
        for p, ric in sostituzioni.items():
            scrivi_json(data / p, ric)
        for tag, terreni in tags.items():
            nome = tag.split("/", 1)[1]
            scrivi_json(tagdir / f"{nome}.json", {"replace": False, "values": [{"id": b, "required": False} for b in sorted(set(terreni))]})

    # --- rapporto
    out = [f"Colture scritte: {len(file_colture)} · terreni nuovi: {len(file_terreni)} · file di mod sostituiti: {len(sostituzioni)} · tag: {len(tags)} · saltate: {len(saltate)}"]
    per_mod = Counter(p.parts[0] for p in file_colture)
    out.append("Colture per mod: " + ", ".join(f"{m} {n}" for m, n in sorted(per_mod.items(), key=lambda x: (-x[1], x[0]))))
    dp = [c["coltura_id"] for c in colture if c["da_provare"]]
    if dp:
        out.append("Da provare in gioco: " + ", ".join(dp))
    if sostituzioni:
        out.append("Sostituiti: " + ", ".join(str(p) for p in sostituzioni))
    if saltate:
        out.append("Saltate:")
        out += [f"- {c}: {m}" for c, m in sorted(saltate)]
    testo = "\n".join(out) + "\n"
    print(testo, end="")
    if a.report:
        a.report.write_text(testo, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
