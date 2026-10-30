#!/usr/bin/env python3
"""Sceglie le versioni Modrinth da aggiungere al pack, secondo le regole del repository.

Uso: python3 scripts/modrinth_resolve.py <cartella pack> <voce> [<voce> …]

Ogni voce può essere:
- `slug`                      → l'ultima **release** per la versione di Minecraft e il loader
                                del pack (se non c'è: l'ultima beta, poi l'ultima alpha);
                                per i pacchetti di shader il "loader" è Iris, per i resource
                                pack è "minecraft" (packwiz li mette nella cartella giusta);
- `slug@versione`             → quella versione esatta: id, oppure numero di versione
                                cercato tra quelle per Minecraft e loader del pack (lo
                                stesso numero può esistere per più loader);
- un link `https://modrinth.com/<tipo>/<slug>/version/<versione>` → come sopra;
- un id di versione di 8 caratteri.

Stampa una riga per voce, separata da tabulazioni:
id versione · slug · numero di versione · tipo (release/beta/alpha) · data · id progetto
Esce con errore se una voce non esiste o non è per Minecraft/loader del pack.
Serve la rete verso api.modrinth.com (nelle GitHub Actions o in locale).
"""
import json
import re
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.modrinth.com/v2"
USER_AGENT = "mango-craft (github.com/mango-craft/mango-craft)"
ORDER = ("release", "beta", "alpha")
# Progetti che non sono mod: su Modrinth il campo "loaders" delle versioni indica altro
TYPE_LOADER = {"shader": "iris", "resourcepack": "minecraft", "datapack": "datapack"}


def api(path: str):
    req = urllib.request.Request(API + path, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def check(v: dict, mc: str, loader: str, entry: str) -> dict:
    if mc not in v.get("game_versions", []) or loader not in v.get("loaders", []):
        raise SystemExit(f"{entry}: la versione {v.get('version_number')} non è per {mc} + {loader} "
                         f"(è per {', '.join(v.get('game_versions', []))} / {', '.join(v.get('loaders', []))})")
    return v


def version_by_id(vid: str) -> dict | None:
    try:
        return api(f"/version/{vid}")
    except urllib.error.HTTPError:
        return None


def loader_for(project: dict, pack_loader: str) -> str:
    return TYPE_LOADER.get(project.get("project_type"), pack_loader)


def resolve(entry: str, mc: str, loader: str) -> dict:
    m = re.fullmatch(r"https://modrinth\.com/[a-z]+/([^/]+)/version/([^/?#]+)", entry)
    if m:
        entry_slug, wanted = m.group(1), urllib.parse.unquote(m.group(2))
    elif "@" in entry:
        entry_slug, wanted = entry.split("@", 1)
    elif re.fullmatch(r"[A-Za-z0-9]{8}", entry) and (v := version_by_id(entry)):
        # un id di versione (se tutto minuscolo potrebbe essere anche uno slug: si prova prima come id)
        return check(v, mc, loader_for(api(f"/project/{v['project_id']}"), loader), entry)
    else:
        entry_slug, wanted = entry, None
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", entry_slug):
        raise SystemExit(f"{entry}: slug non valido")
    try:
        project = api(f"/project/{entry_slug}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{entry}: progetto non trovato ({e.code})")
    loader = loader_for(project, loader)
    if wanted and re.fullmatch(r"[A-Za-z0-9]{8}", wanted):
        v = version_by_id(wanted)
        if v and v["project_id"] == project["id"]:
            return check(v, mc, loader, entry)
    q = urllib.parse.urlencode({"game_versions": json.dumps([mc]), "loaders": json.dumps([loader])})
    versions = api(f"/project/{project['id']}/version?{q}")
    if wanted:
        # numero di versione: solo tra quelle per Minecraft e loader del pack
        for v in versions:
            if v["version_number"] == wanted:
                return v
        raise SystemExit(f"{entry}: nessuna versione {wanted} per {mc} + {loader}")
    if not versions:
        raise SystemExit(f"{entry}: nessuna versione per {mc} + {loader}")
    versions.sort(key=lambda v: v["date_published"], reverse=True)
    for kind in ORDER:
        for v in versions:
            if v.get("version_type") == kind:
                return v
    return versions[0]


def main(pack_dir: str, entries: list[str]) -> None:
    pv = tomllib.loads((Path(pack_dir) / "pack.toml").read_text(encoding="utf-8"))["versions"]
    mc = pv["minecraft"]
    loader = next((l for l in ("neoforge", "fabric", "quilt", "forge") if l in pv), None)
    for entry in entries:
        v = resolve(entry.strip(), mc, loader)
        project = api(f"/project/{v['project_id']}")
        print("\t".join([v["id"], project["slug"], v["version_number"], v.get("version_type", "?"),
                         v["date_published"][:10], v["project_id"]]))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], [a for a in sys.argv[2:] if a.strip()])
