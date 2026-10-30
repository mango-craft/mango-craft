#!/usr/bin/env python3
"""Confronta i log del gioco di due avvii: quali avvisi ed errori sono nuovi e quali sono spariti.

Uso: python3 scripts/log_confronta.py <log nuovo> <log vecchio> [--tutti]
     es. python3 scripts/log_confronta.py <istanza>/logs/latest.log <istanza>/logs/2026-10-24-6.log.gz

È la prova di uscita di ogni versione («nel log nessun errore nuovo grave», AGENTS.md sezione 5): il log nuovo è quello
dell'istanza di prova con la versione da far uscire, quello vecchio un log della versione precedente (i file `.log.gz`
si leggono direttamente). Ogni riga WARN/ERROR/FATAL diventa una «firma» (livello, logger, messaggio con i numeri
sostituiti da #, troncato), così le ripetizioni e i valori che cambiano a ogni avvio non contano. Stampa le firme nuove
con quante volte compaiono e le sparite (le prime 40, tutte con --tutti). Ogni nuova è da leggere: innocua (va in B14),
problema nuovo (codice `Bnn` nel bug report) o errore grave (blocca l'uscita). Esce con 1 se ci sono firme nuove.
Solo libreria standard.
"""
import gzip
import re
import sys
from pathlib import Path

RIGA = re.compile(r"\[[^\]]+\] \[([^\]]*)/(\w+)\] \[([^\]]*)\]: (.*)")
LIVELLI = {"ERROR", "WARN", "FATAL"}


def firme(path: Path) -> dict[str, int]:
    apri = gzip.open if path.suffix == ".gz" else open
    out: dict[str, int] = {}
    with apri(path, "rt", encoding="utf-8", errors="replace") as f:
        for riga in f:
            m = RIGA.match(riga)
            if not m:
                continue
            _thread, livello, logger, msg = m.groups()
            if livello not in LIVELLI:
                continue
            chiave = f"{livello} [{logger}] " + normalizza(msg)[:200]
            out[chiave] = out.get(chiave, 0) + 1
    return out


def normalizza(msg: str) -> str:
    """Toglie dal messaggio ciò che cambia a ogni avvio: UUID, indirizzi e hash esadecimali, numeri."""
    msg = re.sub(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", "<uuid>", msg, flags=re.I)
    msg = re.sub(r"@[0-9a-f]+\b", "@<hex>", msg, flags=re.I)
    msg = re.sub(r"\b0x[0-9a-f]+\b|\b(?=[0-9a-f]*\d)[0-9a-f]{12,}\b", "<hex>", msg, flags=re.I)
    return re.sub(r"\d+(\.\d+)?", "#", msg)


def main(argv: list[str]) -> int:
    tutti = "--tutti" in argv
    argv = [a for a in argv if a != "--tutti"]
    if len(argv) != 2:
        print(__doc__)
        return 2
    nuovo, vecchio = firme(Path(argv[0])), firme(Path(argv[1]))
    nuove = sorted(set(nuovo) - set(vecchio))
    sparite = sorted(set(vecchio) - set(nuovo))
    print(f"Firme WARN/ERROR distinte: ora {len(nuovo)}, prima {len(vecchio)}")
    print(f"\nNUOVE: {len(nuove)}")
    for x in nuove if tutti else nuove[:40]:
        print(f"+ {nuovo[x]} x {x}")
    print(f"\nSPARITE: {len(sparite)}")
    for x in sparite if tutti else sparite[:40]:
        print(f"- {x}")
    if not tutti and (len(nuove) > 40 or len(sparite) > 40):
        print("\n(elenco troncato a 40: --tutti per vederle tutte)")
    return 1 if nuove else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
