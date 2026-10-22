#!/usr/bin/env python3
"""Controlla i vasi di Botany Pots del datapack contro i .jar veri (non contro l'inventario).

Uso: python3 scripts/vasi_verifica_jar.py <cartella mods> [--pack CARTELLA] [--lungo]

Si lancia dove stanno i jar (es. sul PC di Matteo, in sola lettura: non scrive niente). Per ogni coltura e
terreno scritti da `botanypots_genera.py` (e a mano) controlla nei jar:
- il blocco esiste (file `blockstates/`, oppure voce di lingua);
- il seme e i raccolti scritti a mano esistono (modello dell'oggetto, oppure voce di lingua);
- il terreno ha un oggetto, e le voci dell'etichetta `botanypots:soil/dirt` esistono;
- gli alberi di `alberi/` (copiati da Botany Trees): la loro tabella del bottino esiste nel datapack e i suoi oggetti nei jar;
- per le colture senza raccolto scritto (Botany Pots lo ricava dalla tabella del bottino del blocco): la tabella
  esiste e, con il vaso **senza attrezzo** (impostazione predefinita di Botany Pots), dà almeno un oggetto.
  Le tabelle che chiedono le cesoie o un incantesimo non danno niente senza attrezzo: la coltura va scritta con
  un raccolto diretto (`1.21.1/data/vasi/coltura_raccolto_custom.csv`).

Il giudizio sulle tabelle è statico (non sostituisce `/botanypots debug` in gioco): le condizioni che non sa
valutare le conta come soddisfatte e le elenca come «incerte» con `--lungo`.
Esce con 1 se trova un nome mancante o una coltura che non darebbe niente.
"""
import argparse
import glob
import json
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DP = "config/paxi/datapacks/matteo_tweaks/data"
ABILITA_VUOTA = ("neoforge:can_item_perform_ability", "forge:can_tool_perform_action", "can_item_perform_ability")


class Jar:
    def __init__(self, cartella: Path):
        self.n = 0
        self.ns = defaultdict(list)  # namespace -> [(zip, nomi)]
        for p in sorted(cartella.glob("*.jar")):
            try:
                z = zipfile.ZipFile(p)
                nomi = set(z.namelist())
            except (zipfile.BadZipFile, OSError) as e:
                print(f"ILLEGGIBILE {p.name}: {e}")
                continue
            self.n += 1
            visti = set()
            for n in nomi:
                parti = n.split("/")
                if len(parti) > 2 and parti[0] in ("assets", "data") and parti[1] not in visti:
                    visti.add(parti[1])
                    self.ns[parti[1]].append((z, nomi))
        self._lang = {}

    def leggi(self, ns: str, chiave: str):
        for z, nomi in self.ns.get(ns, ()):
            if chiave in nomi:
                return json.loads(z.read(chiave).decode("utf-8-sig"))
        return None

    def esiste(self, ns: str, chiave: str) -> bool:
        return any(chiave in nomi for _, nomi in self.ns.get(ns, ()))

    def lang(self, ns: str) -> dict:
        if ns not in self._lang:
            d = {}
            for z, nomi in self.ns.get(ns, ()):
                k = f"assets/{ns}/lang/en_us.json"
                if k in nomi:
                    try:
                        d.update(json.loads(z.read(k).decode("utf-8-sig")))
                    except ValueError:
                        pass
            self._lang[ns] = d
        return self._lang[ns]

    def blockstate(self, i: str):
        ns, p = i.split(":")
        return self.leggi(ns, f"assets/{ns}/blockstates/{p}.json")

    def blocco(self, i: str) -> bool:
        ns, p = i.split(":")
        return self.blockstate(i) is not None or f"block.{ns}.{p}" in self.lang(ns)

    def oggetto(self, i: str) -> bool:
        ns, p = i.split(":")
        return (ns == "minecraft" or self.esiste(ns, f"assets/{ns}/models/item/{p}.json")
                or self.esiste(ns, f"assets/{ns}/items/{p}.json")
                or f"item.{ns}.{p}" in self.lang(ns) or f"block.{ns}.{p}" in self.lang(ns))

    def loot(self, i: str):
        ns, p = i.split(":")
        for base in ("loot_table", "loot_tables"):
            t = self.leggi(ns, f"data/{ns}/{base}/blocks/{p}.json")
            if t is not None:
                return t
        return None

    def loot_per_id(self, tid: str) -> bool:
        ns, p = tid.split(":")
        return self.esiste(ns, f"data/{ns}/loot_table/{p}.json") or self.esiste(ns, f"data/{ns}/loot_tables/{p}.json")


def valori_stato(bs) -> dict:
    """Valori possibili di ogni proprietà, letti dal blockstate."""
    d = defaultdict(set)
    if not bs:
        return d
    for k in bs.get("variants", {}):
        for p in k.split(","):
            if "=" in p:
                a, b = p.split("=", 1)
                d[a].add(b)

    def giro(x):
        if isinstance(x, dict):
            for kk, vv in x.items():
                if kk in ("OR", "AND"):
                    for y in vv:
                        giro(y)
                else:
                    for o in str(vv).split("|"):
                        d[kk].add(o)

    for m in bs.get("multipart", []):
        giro(m.get("when", {}))
    return d


def stato_raccolto(sv: dict) -> dict:
    """Come Botany Pots: età massima, bacche presenti."""
    st = {}
    if "age" in sv:
        try:
            st["age"] = str(max(int(x) for x in sv["age"]))
        except ValueError:
            pass
    if "berries" in sv:
        st["berries"] = "true"
    return st


def condizione(c: dict, st: dict, sv: dict, note: set) -> bool:
    """Valuta una condizione con il vaso senza attrezzo. Ciò che non sa valutare conta come vero (e va in `note`)."""
    t = c.get("condition", "").replace("minecraft:", "")
    if t == "survives_explosion":
        return True
    if t == "inverted":
        return not condizione(c["term"], st, sv, note)
    if t == "any_of":
        return any(condizione(x, st, sv, note) for x in c["terms"])
    if t == "all_of":
        return all(condizione(x, st, sv, note) for x in c["terms"])
    if t in ("random_chance", "random_chance_with_enchanted_bonus", "table_bonus"):
        return True
    if t == "match_tool":
        note.add("attrezzo")
        return not c.get("predicate")
    if t in ABILITA_VUOTA:
        note.add("attrezzo")
        return False
    if t == "block_state_property":
        for k, v in c.get("properties", {}).items():
            if isinstance(v, dict):
                continue
            if k in st:
                if st[k] != str(v):
                    return False
            elif k in sv:
                note.add(f"incerta: {k}={v}")
                if str(v) not in sv[k]:
                    return False
            else:
                return False
        return True
    note.add(f"incerta: condizione {t}")
    return True


def voci(es: list, st, sv, note, out: set) -> None:
    for e in es:
        if not all(condizione(c, st, sv, note) for c in e.get("conditions", [])):
            continue
        t = e.get("type", "").replace("minecraft:", "")
        if t == "item":
            out.add(e["name"])
        elif t == "alternatives":
            for ch in e.get("children", []):
                tmp = set()
                voci([ch], st, sv, note, tmp)
                if tmp:
                    out |= tmp
                    break
        elif t in ("group", "sequence"):
            voci(e.get("children", []), st, sv, note, out)
        elif t == "tag":
            out.add("#" + e["name"])
        elif t == "loot_table":
            out.add("tabella:" + str(e.get("value") or e.get("name")))


def nomi_oggetto(x, out: set) -> None:
    """Tutti gli oggetti nominati in una tabella del bottino."""
    if isinstance(x, dict):
        if x.get("type") == "minecraft:item" and "name" in x:
            out.add(x["name"])
        for v in x.values():
            nomi_oggetto(v, out)
    elif isinstance(x, list):
        for v in x:
            nomi_oggetto(v, out)


def blocchi_aspetto(display) -> list:
    """I blocchi nominati nell'aspetto (display) di una coltura."""
    out = []
    if isinstance(display, dict):
        bs = display.get("block_state")
        if isinstance(bs, dict) and bs.get("block"):
            out.append(bs["block"])
        for v in display.values():
            out += blocchi_aspetto(v)
    elif isinstance(display, list):
        for v in display:
            out += blocchi_aspetto(v)
    return out


def raccolto_senza_attrezzo(lt: dict, st, sv, note) -> set:
    out = set()
    for p in lt.get("pools", []):
        if all(condizione(c, st, sv, note) for c in p.get("conditions", [])):
            voci(p.get("entries", []), st, sv, note, out)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mods", type=Path, help="cartella con i .jar")
    ap.add_argument("--pack", type=Path, default=ROOT / "1.21.1" / "pack")
    ap.add_argument("--lungo", action="store_true", help="elenca anche le colture con condizioni incerte")
    a = ap.parse_args()

    bp = a.pack / DP / "matteo_tweaks" / "recipe" / "botanypots"
    colture = [(f, json.loads(f.read_text(encoding="utf-8"))) for f in sorted([*bp.glob("**/crop/*.json"), *bp.glob("alberi/**/*.json")])]
    tabelle = a.pack / DP / "matteo_tweaks" / "loot_table"
    terreni = [(f, json.loads(f.read_text(encoding="utf-8"))) for f in sorted(bp.glob("**/soil/*.json"))]
    jar = Jar(a.mods)
    print(f"jar letti: {jar.n} · namespace: {len(jar.ns)}")

    errori = defaultdict(list)
    incerte = []
    n_derivate = n_scritte = 0
    for f, d in colture:
        nome = f.relative_to(bp).as_posix()
        b = d.get("block")  # le colture libere (graticci) non hanno un blocco proprio: si controlla l'aspetto
        for bl in ([b] if b else []) + blocchi_aspetto(d.get("display")):
            if not jar.blocco(bl):
                errori["blocco non trovato nei jar"].append(f"{nome}: {bl}")
        if not b and not d.get("drops"):
            errori["coltura senza blocco e senza raccolto scritto"].append(nome)
        seme = d.get("input", {}).get("item") if isinstance(d.get("input"), dict) else None
        if seme and not jar.oggetto(seme):
            errori["seme non trovato nei jar"].append(f"{nome}: {seme}")
        if d.get("drops"):
            n_scritte += 1
            for dr in d["drops"]:
                if dr.get("type") == "botanypots:items":
                    for it in dr["items"]:
                        if not jar.oggetto(it["result"]["id"]):
                            errori["raccolto scritto non trovato nei jar"].append(f"{nome}: {it['result']['id']}")
                elif dr.get("type") == "botanypots:loot_table":
                    ns, p = dr["table_id"].split(":")
                    if ns == "matteo_tweaks":  # tabella nostra (alberi copiati da Botany Trees): esiste, e i suoi oggetti pure
                        tf = tabelle / f"{p}.json"
                        if not tf.exists():
                            errori["tabella del bottino nostra non trovata"].append(f"{nome}: {dr['table_id']}")
                        else:
                            ogg = set()
                            nomi_oggetto(json.loads(tf.read_text(encoding="utf-8")), ogg)
                            for o in sorted(ogg):
                                if not jar.oggetto(o):
                                    errori["oggetto di una tabella nostra non trovato nei jar"].append(f"{p}: {o}")
                    elif not jar.loot_per_id(dr["table_id"]):
                        errori["tabella del bottino scritta non trovata"].append(f"{nome}: {dr['table_id']}")
            continue
        n_derivate += 1
        lt = jar.loot(b)
        if lt is None:
            errori["raccolto derivato: il blocco non ha una tabella del bottino"].append(f"{nome}: {b}")
            continue
        sv = valori_stato(jar.blockstate(b))
        note = set()
        dato = raccolto_senza_attrezzo(lt, stato_raccolto(sv), sv, note)
        if not dato:
            motivo = "chiede le cesoie o un incantesimo" if "attrezzo" in note else "condizioni sullo stato"
            errori[f"non darebbe niente nel vaso senza attrezzo ({motivo})"].append(f"{nome}: {b}")
        elif any(n.startswith("incerta") for n in note):
            incerte.append(f"{nome}: {sorted(n for n in note if n.startswith('incerta'))}")
    for f, d in terreni:
        nome = f.relative_to(bp).as_posix()
        if not jar.blocco(d["block"]):
            errori["terreno: blocco non trovato nei jar"].append(f"{nome}: {d['block']}")
        if not jar.oggetto(d["block"]):
            errori["terreno: il blocco non ha un oggetto"].append(f"{nome}: {d['block']}")
    tag = a.pack / DP / "botanypots" / "tags" / "item" / "soil" / "dirt.json"
    n_tag = 0
    if tag.exists():
        for v in json.loads(tag.read_text(encoding="utf-8"))["values"]:
            i = v["id"] if isinstance(v, dict) else v
            n_tag += 1
            if not jar.oggetto(i):
                errori["etichetta botanypots:soil/dirt: oggetto non trovato"].append(i)

    print(f"colture: {len(colture)} (raccolto ricavato dalla tabella del blocco: {n_derivate}, scritto a mano: {n_scritte}) · "
          f"terreni: {len(terreni)} · voci dell'etichetta dirt: {n_tag}")
    if not errori:
        print("PROBLEMI: nessuno")
    for k, v in errori.items():
        print(f"\n## {k} ({len(v)})")
        for x in v:
            print("-", x)
    if incerte:
        print(f"\nColture con condizioni incerte (da provare in gioco): {len(incerte)}" + ("" if a.lungo else " (--lungo per l'elenco)"))
        if a.lungo:
            for x in incerte:
                print("-", x)
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
