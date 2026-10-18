#!/usr/bin/env python3
"""Controlli sul pack packwiz e sul datapack. Esce con errore se qualcosa non va.

Uso: python3 scripts/check_pack.py 1.21.1/pack

Controlla:
- pack.toml: versioni di Minecraft e NeoForge, hash dell'indice;
- index.toml: ogni file presente e con l'hash giusto, nessun file in più o in meno;
- metafile (*.pw.toml): campi obbligatori, formato degli hash, nessun progetto doppio;
- nessun .jar nel repository;
- datapack: JSON validi e nomi tutti minuscoli dentro data/.
"""
import hashlib
import json
import sys
import tomllib
from pathlib import Path

HASH_LEN = {"sha1": 40, "sha256": 64, "sha512": 128, "md5": 32}
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def check_metafiles(root: Path) -> int:
    seen: dict[tuple, str] = {}
    count = 0
    for p in sorted(root.rglob("*.pw.toml")):
        rel = p.relative_to(root).as_posix()
        count += 1
        try:
            d = tomllib.loads(p.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as e:
            err(f"{rel}: TOML non valido ({e})")
            continue
        for key in ("name", "filename", "side", "download"):
            if key not in d:
                err(f"{rel}: manca '{key}'")
        if d.get("side") not in ("both", "client", "server"):
            err(f"{rel}: side non valido: {d.get('side')}")
        dl = d.get("download", {})
        fmt, h = dl.get("hash-format"), dl.get("hash", "")
        if fmt in HASH_LEN and len(h) != HASH_LEN[fmt]:
            err(f"{rel}: hash {fmt} di lunghezza {len(h)}")
        upd = d.get("update", {})
        if dl.get("mode") == "metadata:curseforge":
            cf = upd.get("curseforge", {})
            if not cf.get("project-id") or not cf.get("file-id"):
                err(f"{rel}: CurseForge senza project-id/file-id")
            key = ("curseforge", cf.get("project-id"))
        else:
            if not dl.get("url", "").startswith("https://"):
                err(f"{rel}: URL mancante o non https")
            mr = upd.get("modrinth", {})
            key = ("modrinth", mr.get("mod-id")) if mr else ("url", dl.get("url"))
        if key in seen:
            err(f"{rel}: stesso progetto di {seen[key]}")
        seen[key] = rel
    return count


def check_index(root: Path) -> None:
    pack = tomllib.loads((root / "pack.toml").read_text(encoding="utf-8"))
    versions = pack.get("versions", {})
    if "minecraft" not in versions or "neoforge" not in versions:
        err("pack.toml: servono le versioni di minecraft e neoforge")
    idx_info = pack.get("index", {})
    idx_path = root / idx_info.get("file", "index.toml")
    if hashlib.sha256(idx_path.read_bytes()).hexdigest() != idx_info.get("hash"):
        err("pack.toml: l'hash dell'indice non corrisponde (lanciare scripts/packwiz_index.py)")
    idx = tomllib.loads(idx_path.read_text(encoding="utf-8"))
    listed = {}
    for f in idx.get("files", []):
        listed[f["file"]] = f
        p = root / f["file"]
        if not p.exists():
            err(f"index.toml: file mancante {f['file']}")
            continue
        if hashlib.sha256(p.read_bytes()).hexdigest() != f["hash"]:
            err(f"index.toml: hash non aggiornato per {f['file']}")
    for p in root.rglob("*"):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            if rel not in listed and rel not in ("pack.toml", idx_path.name, ".packwizignore"):
                err(f"index.toml: file non elencato {rel}")


def check_repo_jars(repo: Path) -> None:
    for p in repo.rglob("*.jar"):
        if ".git" not in p.parts:
            err(f"file .jar nel repository: {p.relative_to(repo)}")


def check_datapacks(root: Path) -> int:
    n = 0
    base = root / "config" / "paxi" / "datapacks"
    if not base.exists():
        return 0
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(base).as_posix()
        parts = rel.split("/")
        if "data" in parts[1:2] and rel != rel.lower():
            err(f"datapack: nome con maiuscole dentro data/: {rel}")
        if p.suffix in (".json", ".mcmeta"):
            n += 1
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                err(f"datapack: JSON non valido {rel} ({e})")
    return n


def main(pack_dir: str) -> None:
    root = Path(pack_dir)
    repo = Path(__file__).resolve().parent.parent
    metas = check_metafiles(root)
    check_index(root)
    check_repo_jars(repo)
    jsons = check_datapacks(root)
    if errors:
        print(f"{len(errors)} problemi:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"OK: {metas} metafile, {jsons} JSON del datapack, indice coerente.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1.21.1/pack")
