#!/usr/bin/env python3
"""Converte un pacchetto Modrinth (.mrpack) nella cartella packwiz del pack.

Uso: python3 scripts/import_mrpack.py <file.mrpack> <cartella pack> [nomi.json]

- Ogni file in `files[]` diventa un metafile `<cartella>/<slug>.pw.toml`
  (mods/, resourcepacks/…) con URL, hash sha512 e dati di aggiornamento Modrinth.
- Il contenuto di `overrides/` viene copiato così com'è nella cartella del pack.
- `nomi.json` (facoltativo) è una lista di oggetti con project_id, slug e name:
  serve a dare ai metafile il nome del progetto invece di quello del file.

Usato una volta per importare la 0.1.1; resta qui per poter rifare il passaggio.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

URL_RE = re.compile(r"^https://cdn\.modrinth\.com/data/([A-Za-z0-9]+)/versions/([A-Za-z0-9]+)/")


def toml_str(value: str) -> str:
    # Le stringhe JSON sono stringhe TOML "basic" valide
    return json.dumps(value, ensure_ascii=False)


def metafile(name: str, filename: str, url: str, sha512: str, pid: str, vid: str, side: str) -> str:
    return (
        f"name = {toml_str(name)}\n"
        f"filename = {toml_str(filename)}\n"
        f"side = {toml_str(side)}\n"
        "\n"
        "[download]\n"
        f"url = {toml_str(url)}\n"
        'hash-format = "sha512"\n'
        f'hash = "{sha512}"\n'
        "\n"
        "[update]\n"
        "[update.modrinth]\n"
        f'mod-id = "{pid}"\n'
        f'version = "{vid}"\n'
    )


def side_of(env: dict) -> str:
    client = env.get("client", "required") != "unsupported"
    server = env.get("server", "required") != "unsupported"
    if client and server:
        return "both"
    return "client" if client else "server"


def main(mrpack: str, pack_dir: str, names_file: str | None = None) -> None:
    root = Path(pack_dir)
    names = {}
    if names_file:
        for m in json.loads(Path(names_file).read_text(encoding="utf-8")):
            names[m["project_id"]] = m
    z = zipfile.ZipFile(mrpack)
    index = json.loads(z.read("modrinth.index.json"))
    used = set()
    for f in index["files"]:
        folder, filename = f["path"].rsplit("/", 1)
        url = f["downloads"][0]
        m = URL_RE.match(url)
        if not m:
            raise SystemExit(f"URL non Modrinth, da gestire a mano: {url}")
        pid, vid = m.groups()
        info = names.get(pid, {})
        slug = info.get("slug") or filename.rsplit(".", 1)[0].lower()
        name = info.get("name") or filename
        target = root / folder / f"{slug}.pw.toml"
        if target in used:
            raise SystemExit(f"Slug duplicato: {target}")
        used.add(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(metafile(name, filename, url, f["hashes"]["sha512"], pid, vid,
                                   side_of(f.get("env", {}))), encoding="utf-8")
    copied = 0
    for n in z.namelist():
        if n.startswith("overrides/") and not n.endswith("/"):
            out = root / n[len("overrides/"):]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(z.read(n))
            copied += 1
    deps = index.get("dependencies", {})
    print(f"{len(used)} metafile, {copied} file di override; versioni: {deps}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    main(*sys.argv[1:4])
