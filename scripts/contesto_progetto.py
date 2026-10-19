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


def current_version_file(mc):
    """Il file della versione in corso: quello con stato 🔧 (in lavorazione), altrimenti il primo 📋 (pianificata)."""
    files = sorted((ROOT / mc / "lavoro" / "versioni").glob("v*.md"),
                   key=lambda f: [int(x) for x in re.findall(r"\d+", f.stem)])
    for mark in ("🔧", "📋"):
        for f in files:
            m = re.search(r"^\*\*Stato\*\*: (.*)$", f.read_text(encoding="utf-8"), flags=re.M)
            if m and m.group(1).startswith(mark):
                return f
    return None


def version_summary(mc, f):
    """Stato, obiettivo e domande ancora da decidere del file della versione in corso."""
    text = f.read_text(encoding="utf-8")
    title = text.split("\n", 1)[0].lstrip("# ").strip()
    stato = re.search(r"^\*\*Stato\*\*: (.*)$", text, flags=re.M).group(1)
    link = f"{REPO_URL}/{mc}/lavoro/versioni/{f.name}"
    out = [f"### {title}", f"**Stato**: {stato}", "",
           section(text, "1. Obiettivo") or "", "",
           "**Da decidere**", "", section(text, "Da decidere", level=3) or "(niente)", "",
           f"Valutazioni, lavoro e prove: [{f.name}]({link})."]
    return "\n".join(out)


def sheets_index(mc):
    """Tabella delle schede di mod-knowledge, con i link al repository."""
    text = read(f"{mc}/mod-knowledge/README.md")
    base = f"{REPO_URL}/{mc}/mod-knowledge/"
    rows = [l for l in text.split("\n") if l.startswith("|")]
    return re.sub(r"\]\(([^)/]+\.md)\)", lambda m: f"]({base}{m.group(1)})", "\n".join(rows))


def main():
    mc = sys.argv[1] if len(sys.argv) > 1 else "1.21.1"
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                         capture_output=True, text=True).stdout.strip() or "?"
    agents = read("AGENTS.md")
    bug = read(f"{mc}/docs/0402-bug-report.md")

    cur = current_version_file(mc)
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
        "## 4. Versione in corso e ultima versione\n\n" + (version_summary(mc, cur) + "\n\n" if cur else "")
        + "### Ultima versione rilasciata\n\n" + demote(first_entry(read(f"{mc}/docs/0401-changelog.md")), 1),
        "## 5. Mod nel pack, per tema\n\n⏳ = approvata, non ancora nel pack. Ruolo, licenza e note di ogni mod: "
        f"[0301-mod]({REPO_URL}/{mc}/docs/0301-mod.md).\n\n" + mod_list(read(f"{mc}/docs/0301-mod.md")),
        "## 6. Cose da non rompere\n\n" + section(read(f"{mc}/docs/0303-note-tecniche.md"), "Cose da non rompere"),
        "## 7. Problemi aperti\n\n### Da correggere da noi\n\n" + section(bug, "🔧")
        + "\n\n### Da verificare in gioco\n\n" + section(bug, "🔍")
        + f"\n\nGli altri (problemi delle mod, risolti): [0402-bug-report]({REPO_URL}/{mc}/docs/0402-bug-report.md).",
        "## 8. Temi aperti\n\n" + demote(body(read(f"{mc}/lavoro/0503-temi-aperti.md")), 1),
        "## 9. Mod candidate\n\n" + body(read(f"{mc}/lavoro/0601-mod-candidate.md")),
        "## 10. Schede delle mod e dei temi\n\nConoscenza verificata, con data e fonti (cartella `mod-knowledge`).\n\n" + sheets_index(mc),
        "## 11. Dove trovare il resto\n\nUn file per versione in "
        f"[lavoro/versioni]({REPO_URL.replace('/blob/', '/tree/')}/{mc}/lavoro/versioni); risultati grezzi delle ricerche in "
        f"[ai-agents/stage]({REPO_URL.replace('/blob/', '/tree/')}/ai-agents/stage).\n\n" + "\n".join(index),
    ]
    print("\n\n".join(parts).rstrip() + "\n")


if __name__ == "__main__":
    main()
