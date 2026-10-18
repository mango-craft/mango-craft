#!/usr/bin/env python3
"""Genera il context.md per il progetto Claude "Minecraft modpack" (la bacheca su claude.ai).

Il file è un riassunto ricavato dai documenti del repository, che restano l'unica fonte:
non si scrive a mano e non si modifica nel progetto, si rigenera.

Uso: python3 scripts/contesto_progetto.py <versione MC> > context.md   (es. 1.21.1)
"""
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/mango-craft/mango-craft/blob/dev"


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def body(text):
    """Toglie il titolo e la prima riga di presentazione del documento."""
    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip()


def section(text, title, level=2):
    """Contenuto di una sezione (titolo che inizia con `title`), senza il titolo."""
    mark = "#" * level + " "
    out, inside = [], False
    for line in text.split("\n"):
        if line.startswith(mark):
            if inside:
                break
            inside = line[len(mark):].startswith(title)
            continue
        if inside and re.match(r"#{1,%d} " % (level - 1), line):
            break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def demote(text, by=1):
    return re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + by) + " ", text, flags=re.M)


def mod_list(text):
    """Per ogni tema di 0301, i nomi delle mod: nelle tabelle i grassetti della prima cella che ne ha,
    negli elenchi le righe del tipo "**Nome** (…) — descrizione"."""
    out = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        title, _, rest = block.partition("\n")
        title = re.sub(r"\s*\(.*\)$", "", title.strip())
        if title in ("Piattaforma", "Librerie"):
            continue
        names = []
        for line in rest.split("\n"):
            found = []
            if line.startswith("|") and not line.startswith("|---"):
                for cell in line.strip("|").split("|"):
                    found = [b for b in re.findall(r"\*\*([^*]+)\*\*", cell)
                             if not b.startswith(("Dalla", "Prevista"))]
                    if found:
                        break
            else:
                m = (re.match(r"\s*- \*\*([^*]+)\*\*(?:\s*\([^)]*\))?\s*(?:⚠️\s*)?—", line)
                     or re.match(r"\*\*([^*]+)\*\*\s*\([^)]*\)\s*—", line))
                if m:
                    found = [m.group(1)]
            for name in found:
                name = name.strip() + (" ⏳" if "⏳" in line else "")
                if name not in names:
                    names.append(name)
        if names:
            out.append(f"- **{title}**: " + " · ".join(names))
    return "\n".join(out)


def first_entry(changelog):
    parts = re.split(r"^## ", changelog, flags=re.M)
    return "### " + parts[1].strip() if len(parts) > 1 else ""


def index_table(readme, base):
    rows = []
    for line in readme.split("\n"):
        m = re.match(r"\| \*\*(\d{4})\*\* \| \[([^\]]+)\]\(([^)]+)\) \| (.*?) \| (.*?) \|$", line)
        if m:
            code, name, link, what, kind = m.groups()
            rows.append(f"| {code} | [{name}]({REPO_URL}/{base}/{link}) | {what} | {kind} |")
    return rows


def main():
    mc = sys.argv[1] if len(sys.argv) > 1 else "1.21.1"
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                         capture_output=True, text=True).stdout.strip() or "?"
    agents = read("AGENTS.md")
    bug = read(f"{mc}/docs/0402-bug-report.md")

    index = ["| Codice | Documento | Contenuto | Tipo |", "|---|---|---|---|"]
    index += index_table(read("docs/README.md"), "docs")
    index += index_table(read(f"{mc}/docs/README.md"), f"{mc}/docs")
    index += index_table(read(f"{mc}/lavoro/README.md"), f"{mc}/lavoro")

    parts = [
        "# Mango Craft — context.md",
        f"_Generato il {date.today().strftime('%d/%m/%Y')} dal repository "
        f"[mango-craft]({REPO_URL.rsplit('/blob', 1)[0]}) (ramo `dev`, commit `{sha}`) con "
        f"`scripts/contesto_progetto.py`. È un riassunto: la fonte sono i documenti del repository. "
        f"Non modificarlo qui, si rigenera._",
        "## 1. Il progetto\n\n" + demote(body(read("docs/0001-progetto.md")), 1),
        "## 2. Come rispondere\n\n" + section(agents, "2. Come rispondere"),
        "## 3. Stato e piano\n\n" + demote(body(read(f"{mc}/lavoro/0501-piano.md")), 1),
        "## 4. Ultima versione\n\n" + first_entry(read(f"{mc}/docs/0401-changelog.md")),
        "## 5. Mod nel pack, per tema\n\n⏳ = approvata, non ancora nel pack. Ruolo, licenza e note di ogni mod: "
        f"[0301-mod]({REPO_URL}/{mc}/docs/0301-mod.md).\n\n" + mod_list(read(f"{mc}/docs/0301-mod.md")),
        "## 6. Cose da non rompere\n\n" + section(read(f"{mc}/docs/0303-note-tecniche.md"), "Cose da non rompere"),
        "## 7. Problemi aperti\n\n### Da correggere da noi\n\n" + section(bug, "🔧")
        + "\n\n### Da verificare in gioco\n\n" + section(bug, "🔍")
        + f"\n\nGli altri (problemi delle mod, risolti): [0402-bug-report]({REPO_URL}/{mc}/docs/0402-bug-report.md).",
        "## 8. Mod candidate\n\n" + body(read(f"{mc}/lavoro/0601-mod-candidate.md")),
        "## 9. Dove trovare il resto\n\n" + "\n".join(index),
    ]
    print("\n\n".join(parts).rstrip() + "\n")


if __name__ == "__main__":
    main()
