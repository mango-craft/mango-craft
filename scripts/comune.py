"""Costanti e funzioni usate da più script. Solo libreria standard.

Gli script si lanciano come `python3 scripts/<nome>.py`: la cartella scripts/ è nel percorso
di ricerca, quindi basta `from comune import …`.
"""
import hashlib
from pathlib import Path

# La cartella data/ del nostro datapack, dentro la cartella di una versione (es. 1.21.1/)
DATAPACK_DATA = "pack/config/paxi/datapacks/matteo_tweaks/data"


def impronta_datapack(data: Path) -> str:
    """sha256 dei file del datapack che il gioco legge (.json e .mcfunction, con il percorso; non i readme).

    Il dump del gioco vale per il datapack che aveva l'istanza: scripts/dump_importa.py salva questa impronta
    in meta.json e la base dati la confronta con quella attuale. Se sono diverse, i confronti con il gioco
    non bloccano finché non si rifà il dump.
    """
    h = hashlib.sha256()
    for f in sorted(data.rglob("*")):
        if f.is_file() and f.suffix in (".json", ".mcfunction"):
            h.update(f.relative_to(data).as_posix().encode())
            h.update(b"\0")
            h.update(f.read_bytes())
            h.update(b"\0")
    return h.hexdigest()
