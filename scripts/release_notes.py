#!/usr/bin/env python3
"""Note di una release: la voce del changelog più l'elenco delle mod CurseForge.

Uso: python3 scripts/release_notes.py <cartella pack> <changelog> <versione>
(il changelog di una versione di Minecraft è <MC>/docs/0401-changelog.md)

Le mod CurseForge non entrano nel .mrpack pubblico: qui vengono elencate con
il link al file esatto, così si possono scaricare a mano se si usa il .mrpack.
"""
import sys
import tomllib
from pathlib import Path


def changelog_section(changelog: Path, version: str) -> str:
    lines = changelog.read_text(encoding="utf-8").splitlines()
    out, inside = [], False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().startswith(version)
            if inside:
                continue
        if inside:
            out.append(line)
    return "\n".join(out).strip() or "_Nessuna voce nel changelog per questa versione._"


def curseforge_mods(pack: Path) -> list[str]:
    rows = []
    for p in sorted(pack.rglob("*.pw.toml")):
        d = tomllib.loads(p.read_text(encoding="utf-8"))
        if d.get("download", {}).get("mode") != "metadata:curseforge":
            continue
        cf = d.get("update", {}).get("curseforge", {})
        slug = p.name[: -len(".pw.toml")]
        url = f"https://www.curseforge.com/minecraft/mc-mods/{slug}/files/{cf.get('file-id')}"
        rows.append(f"| {d.get('name')} | `{d.get('filename')}` | [file {cf.get('file-id')}]({url}) |")
    return rows


def main(pack_dir: str, changelog: str, version: str) -> None:
    pack = Path(pack_dir)
    print(changelog_section(Path(changelog), version))
    rows = curseforge_mods(pack)
    if rows:
        print()
        print("### Mod solo CurseForge (non incluse nel .mrpack)")
        print()
        print("Con un'istanza collegata al repository le scarica packwiz-installer. "
              "Se usi il `.mrpack`, scaricale a mano e mettile nella cartella `mods`:")
        print()
        print("| Mod | File | Link |")
        print("|---|---|---|")
        print("\n".join(rows))
    print()
    print("Installazione e istanze: vedi `docs/0101-installazione.md` nel repository.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    main(*sys.argv[1:])
