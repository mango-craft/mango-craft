#!/usr/bin/env python3
"""Importa nel repository il dump del gioco scritto da /mango_dump (KubeJS, dalla 0.7.2).

Uso: python3 scripts/dump_importa.py <cartella del dump> <cartella versione>
     es. python3 scripts/dump_importa.py ~/copia/logs/mango-craft-dump 1.21.1

Il comando /mango_dump (script 1.21.1/pack/kubejs/server_scripts/mango_dump.js) scrive in logs/mango-craft-dump/
dell'istanza di prova: meta.json, effetti.json, pozioni.json, alambicco.json, oggetti.json e, dal formato 2, registri.json,
ricette.json, tag.json, tabelle.json, strutture.json (cosa contiene ognuno: il commento in testa allo script). Questo script li controlla
(formato, sezioni presenti, errori) e li riscrive **ordinati** in <versione>/data/dump/, così le differenze tra un dump
e il successivo si leggono nel diff. La base dati (scripts/botanypots_db.py) li legge da lì.

Il dump non lo rifà nessun workflow: si rilancia in gioco dopo ogni giro di aggiornamenti delle mod. La base dati
confronta le versioni delle mod nel dump con quelle dell'inventario e avvisa se il dump è vecchio.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DP = "pack/config/paxi/datapacks/matteo_tweaks/data"


def impronta_datapack(ver: Path) -> str:
    """sha256 di tutti i file del nostro datapack (percorso e contenuto): il dump vale per questo datapack. La base dati
    la confronta con il datapack attuale: se è cambiato, il confronto ricette/tag/tabelle con il gioco non blocca più."""
    h = hashlib.sha256()
    for f in sorted((ver / DP).rglob("*")):
        if f.is_file():
            h.update(f.relative_to(ver / DP).as_posix().encode()); h.update(b"\0"); h.update(f.read_bytes()); h.update(b"\0")
    return h.hexdigest()
SEZIONI = ("effetti", "pozioni", "alambicco", "oggetti", "registri", "ricette", "tag", "tabelle", "strutture")
FORMATO = 2


def ordina(nome: str, d):
    if nome in ("effetti", "pozioni", "oggetti"):
        return sorted(d, key=lambda r: r["id"])
    if nome == "alambicco":
        chiave = lambda m: json.dumps(m, sort_keys=True)  # noqa: E731
        return {"ingredienti": sorted(set(d.get("ingredienti") or [])),
                "miscele": sorted(d.get("miscele") or [], key=chiave),
                "ricette": sorted(d.get("ricette") or [], key=chiave)}
    if nome in ("registri", "ricette"):      # {registro o tipo: [id]}
        return {k: sorted(v) for k, v in sorted(d.items())}
    if nome == "tag":                        # {registro: {tag: [id] | numero}}
        return {r: {t: (sorted(v) if isinstance(v, list) else v) for t, v in sorted(tags.items())} for r, tags in sorted(d.items())}
    if nome == "tabelle":
        return sorted(d)
    if nome == "strutture":
        return {k: {**v, "strutture": sorted(v.get("strutture") or [], key=lambda e: e["struttura"])} for k, v in sorted(d.items())}
    return d


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    src = Path(argv[0]).expanduser()
    ver = Path(argv[1]) if Path(argv[1]).is_absolute() else ROOT / argv[1]
    dst = ver / "data" / "dump"
    meta = json.loads((src / "meta.json").read_text(encoding="utf-8"))
    if meta.get("formato") != FORMATO:
        print(f"formato del dump {meta.get('formato')} diverso da {FORMATO}: aggiornare questo script")
        return 1
    problemi = list(meta.get("errori") or [])
    for s in SEZIONI:
        if not (src / f"{s}.json").exists():
            problemi.append(f"{s}: file mancante")
    dst.mkdir(parents=True, exist_ok=True)
    meta["mod"] = dict(sorted((meta.get("mod") or {}).items()))
    meta["datapack_sha256"] = impronta_datapack(ver)   # aggiunto dall'importatore, non dal gioco
    (dst / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    for s in SEZIONI:
        f = src / f"{s}.json"
        if f.exists():
            d = ordina(s, json.loads(f.read_text(encoding="utf-8")))
            (dst / f"{s}.json").write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"Dump del {meta.get('data')} importato in {dst}: {meta.get('file')}; mod: {len(meta['mod'])}")
    if problemi:
        print("Problemi del dump (da guardare prima di contarci):")
        for p in problemi:
            print(" -", p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
