#!/usr/bin/env python3
"""Rigenera index.toml e l'hash dell'indice in pack.toml, come `packwiz refresh`.

Uso: python3 scripts/packwiz_index.py 1.21.1/pack

Serve dove packwiz non è installato (es. in locale).
Nelle GitHub Actions gira comunque `packwiz refresh`, che è la fonte di verità:
se il risultato differisce, la build lo corregge con un commit automatico.
"""
import fnmatch
import hashlib
import re
import sys
import tomllib
from pathlib import Path

# Stesse esclusioni di default di packwiz (core/index.go, ignoreDefaults)
IGNORE_DEFAULTS = [".git/**", ".gitattributes", ".gitignore", ".DS_Store",
                   "/*.zip", "*.mrpack", "packwiz.exe", "packwiz"]


def load_ignore(root: Path):
    patterns = list(IGNORE_DEFAULTS)
    f = root / ".packwizignore"
    if f.exists():
        patterns += [l.strip() for l in f.read_text(encoding="utf-8").splitlines()
                     if l.strip() and not l.startswith("#")]
    return patterns


def ignored(rel: str, patterns) -> bool:
    for p in patterns:
        anchored = p.startswith("/")
        pat = p.lstrip("/")
        if pat.endswith("/**"):
            base = pat[:-3]
            if rel == base or rel.startswith(base + "/"):
                return True
            continue
        if anchored:
            if fnmatch.fnmatchcase(rel, pat):
                return True
        else:
            name = rel.rsplit("/", 1)[-1]
            if fnmatch.fnmatchcase(name, pat) or fnmatch.fnmatchcase(rel, pat) \
                    or rel.startswith(pat + "/"):
                return True
    return False


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(pack_dir: str) -> None:
    root = Path(pack_dir)
    pack = root / "pack.toml"
    text = pack.read_text(encoding="utf-8")
    m = re.search(r'^\s*file\s*=\s*"([^"]+)"', text.split("[index]", 1)[1], re.M)
    index_name = m.group(1) if m else "index.toml"
    patterns = load_ignore(root)
    skip = {"pack.toml", index_name, ".packwizignore"}
    # I flag "preserve = true" (installa solo se manca) vanno conservati, come fa packwiz
    preserve = set()
    old = root / index_name
    if old.exists():
        for f in tomllib.loads(old.read_text(encoding="utf-8")).get("files", []):
            if f.get("preserve"):
                preserve.add(f["file"])
    files = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if rel in skip or ignored(rel, patterns):
            continue
        files.append(rel)
    files.sort()
    out = ['hash-format = "sha256"', ""]
    for rel in files:
        out.append("[[files]]")
        out.append(f'file = "{rel}"')
        out.append(f'hash = "{sha256(root / rel)}"')
        if rel.endswith(".pw.toml"):
            out.append("metafile = true")
        if rel in preserve:
            out.append("preserve = true")
        out.append("")
    (root / index_name).write_text("\n".join(out), encoding="utf-8")
    new_hash = sha256(root / index_name)
    text = re.sub(r'(\[index\][^\[]*?hash\s*=\s*")[0-9a-f]*(")', rf"\g<1>{new_hash}\g<2>", text, flags=re.S)
    pack.write_text(text, encoding="utf-8")
    print(f"{len(files)} file nell'indice, hash {new_hash[:12]}…")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1.21.1/pack")
