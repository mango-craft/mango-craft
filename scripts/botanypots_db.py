#!/usr/bin/env python3
"""Base dati dei vasi di Botany Pots: terreni, colture, tag e le nostre scelte di rarità, in SQLite.

Uso:  python3 scripts/botanypots_db.py <cartella versione> refresh
      python3 scripts/botanypots_db.py <cartella versione> query "SELECT ..."
      python3 scripts/botanypots_db.py <cartella versione> analisi <nome>     (esegue mod-knowledge/botany-pots/query/<nome>.sql)
      python3 scripts/botanypots_db.py <cartella versione> tabelle | controlli

Da Python:  db = BotanyPotsDB("1.21.1"); db.query("SELECT ..."); db.analisi("nome"); db.refresh(); db.tabelle(); db.controlli()
`query` e `analisi` creano il database se non esiste o se inventario, datapack, CSV o questo script sono più
recenti (così non si lavora mai su dati vecchi). `refresh` lo ricostruisce da zero e lo sostituisce solo se
tutti i vincoli e i controlli passano. Modello, fatti verificati e query: 1.21.1/mod-knowledge/botany-pots/.

Fonti (si leggono direttamente, niente copie intermedie):
- <versione>/data/inventario/: ricette e tag di ogni jar (generato dai workflow), più minecraft.json e neoforge.json;
- <versione>/pack/config/paxi/datapacks/matteo_tweaks/data/: le nostre ricette e i nostri tag;
- <versione>/data/vasi/*.csv: le regole nostre, scritte a mano.
Il file <versione>/data/vasi/vasi.sqlite non va nel repository: si rigenera.

Tabelle (chiavi e vincoli nello SCHEMA qui sotto):
  anagrafiche   TAG, TERRENO, COLTURA
  file del vaso POTS_TERRENO, POTS_COLTURA, POTS_COLTURA_SEME, POTS_COLTURA_TAG   (chiave: ricetta + fonte)
  viste         POTS_TERRENO_VINCENTE, POTS_COLTURA_VINCENTE (il file che il gioco usa per ogni id; `avviso` se due jar
                portano lo stesso id, caso in cui l'ordine non è noto e non blocca)
  esplosa       TERRENO_TAG   (per ogni terreno, tutti i tag in cui sta, con il tag che lo elenca davvero)
  scelte        RARITA_POTS_SETTINGS, TERRENO_RARITA, TERRENO_TAG_CUSTOM, COLTURA_CUSTOM, COLTURA_TAG_CUSTOM,
                COLTURA_RACCOLTO_CUSTOM   (le regole nostre, lette anche da scripts/botanypots_genera.py)
                POTS_COMPATIBILITA   (terreno × coltura, dai file vincenti, con il tag che fa da ponte)

Regole lette nel sorgente di Botany Pots 21.1.44 e Bookshelf 21.1.81:
- il vaso cerca il file di terreno con l'oggetto nello slot del terreno e il file di coltura con l'oggetto nello
  slot del seme; la coltura cresce se il terreno sta in almeno uno dei tag del suo campo `soil` (vuoto = soil/dirt);
- i bonus (crescita, resa, luce) stanno nel file di terreno; il tempo e la resa base nel file di coltura;
- un tag di blocchi si confronta con l'oggetto di ogni blocco: qui l'oggetto ha sempre lo stesso nome del blocco
  (lo script si ferma se non è così);
- tra più file con lo stesso id vince il pacchetto più in alto: il nostro datapack (Paxi lo mette sopra a tutti).
"""
import csv
import glob
import json
import os
import sqlite3
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

DP = "pack/config/paxi/datapacks/matteo_tweaks/data"
NOSTRO = "matteo_tweaks"
TAG_DIRT = ("oggetti", "botanypots:soil/dirt")
TIPI_TERRENO = ("botanypots:soil", "botanypots:block_derived_soil")
TIPI_COLTURA = ("botanypots:crop", "botanypots:block_derived_crop")
# Seme delle colture ricavate da un blocco il cui oggetto ha un altro nome (Botany Pots usa block.asItem()).
# Verificati: vanilla nel codice del gioco, palma nel sorgente di Bountiful Fares, Rustic Delight sugli oggetti del jar.
SEMI_ECCEZIONI = {
    "minecraft:beetroots": "minecraft:beetroot_seeds", "minecraft:carrots": "minecraft:carrot",
    "minecraft:cave_vines": "minecraft:glow_berries", "minecraft:cocoa": "minecraft:cocoa_beans",
    "minecraft:melon_stem": "minecraft:melon_seeds", "minecraft:potatoes": "minecraft:potato",
    "minecraft:pumpkin_stem": "minecraft:pumpkin_seeds", "minecraft:sweet_berry_bush": "minecraft:sweet_berries",
    "rusticdelight:bell_peppers": "rusticdelight:bell_pepper_seeds", "rusticdelight:cotton": "rusticdelight:cotton_seeds",
    "bountifulfares:palm_sapling": "bountifulfares:coconut",
}

SCHEMA = """
CREATE TABLE TAG (
  tag_id   INTEGER PRIMARY KEY,
  ambito   TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  nome     TEXT NOT NULL,
  UNIQUE (ambito, nome)
);
CREATE TABLE TERRENO (
  terreno_id TEXT PRIMARY KEY,          -- l'oggetto che va nello slot del terreno
  mod        TEXT NOT NULL,
  stato      TEXT NOT NULL CHECK (stato IN ('in_vaso', 'candidato'))  -- candidato: nei tag delle colture, senza file
);
CREATE TABLE COLTURA (
  coltura_id TEXT PRIMARY KEY,          -- la pianta: il blocco; per le colture senza blocco, il seme
  mod        TEXT NOT NULL,
  stato      TEXT NOT NULL CHECK (stato IN ('in_vaso'))
);
CREATE TABLE POTS_TERRENO (
  ricetta_id TEXT NOT NULL,             -- id del file nel gioco, es. botanypots:farmersdelight/soil/rich_soil
  fonte      TEXT NOT NULL,             -- jar (slug) o matteo_tweaks
  strato     TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  terreno_id TEXT NOT NULL REFERENCES TERRENO,
  crescita   REAL NOT NULL DEFAULT 0,
  resa       REAL NOT NULL DEFAULT 0,
  luce       INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (ricetta_id, fonte)
);
CREATE TABLE POTS_COLTURA (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  strato     TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  coltura_id TEXT NOT NULL REFERENCES COLTURA,
  tempo      INTEGER NOT NULL DEFAULT 1200,  -- tick
  resa_base  REAL NOT NULL DEFAULT 1,
  scala_resa REAL NOT NULL DEFAULT 1,
  PRIMARY KEY (ricetta_id, fonte)
);
CREATE TABLE POTS_COLTURA_SEME (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  seme       TEXT NOT NULL,             -- l'oggetto che va nello slot del seme
  origine    TEXT NOT NULL CHECK (origine IN ('file', 'blocco', 'eccezione')),  -- da dove viene il nome
  PRIMARY KEY (ricetta_id, fonte, seme),
  FOREIGN KEY (ricetta_id, fonte) REFERENCES POTS_COLTURA
);
CREATE TABLE POTS_COLTURA_TAG (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  tag_id     INTEGER NOT NULL REFERENCES TAG,
  implicito  INTEGER NOT NULL CHECK (implicito IN (0, 1)),  -- 1: il file non scrive `soil`, vale soil/dirt
  PRIMARY KEY (ricetta_id, fonte, tag_id),
  FOREIGN KEY (ricetta_id, fonte) REFERENCES POTS_COLTURA
);
CREATE TABLE TERRENO_TAG (
  terreno_id     TEXT NOT NULL REFERENCES TERRENO,
  tag_id         INTEGER NOT NULL REFERENCES TAG,   -- il tag raggiunto
  tag_diretto_id INTEGER NOT NULL REFERENCES TAG,   -- il tag il cui file elenca il terreno (l'origine)
  livello        INTEGER NOT NULL,                  -- 0 = elencato direttamente
  da_noi         INTEGER NOT NULL CHECK (da_noi IN (0, 1)),  -- 1: esiste solo grazie al nostro datapack
  PRIMARY KEY (terreno_id, tag_id, tag_diretto_id)
);
CREATE TABLE RARITA_POTS_SETTINGS (
  classe   TEXT PRIMARY KEY,
  ordine   INTEGER NOT NULL UNIQUE,     -- 1 = la più facile da ottenere
  crescita REAL NOT NULL,
  resa     REAL NOT NULL
);
CREATE TABLE TERRENO_RARITA (
  terreno_id TEXT PRIMARY KEY REFERENCES TERRENO,
  classe     TEXT NOT NULL REFERENCES RARITA_POTS_SETTINGS,
  motivo     TEXT NOT NULL              -- come si ottiene
);
-- Le altre regole nostre (CSV a mano, lette da scripts/botanypots_genera.py): qui per le analisi.
CREATE TABLE TERRENO_TAG_CUSTOM (
  terreno_id TEXT NOT NULL REFERENCES TERRENO,
  ambito     TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  tag        TEXT NOT NULL,
  PRIMARY KEY (terreno_id, ambito, tag)
);
CREATE TABLE COLTURA_CUSTOM (
  coltura_id     TEXT PRIMARY KEY,      -- il blocco della pianta, o l'id del file per le colture senza blocco
  mod            TEXT NOT NULL,
  seme           TEXT,
  tempo          INTEGER,
  richiesti      TEXT,                  -- blocchi richiesti dalla condizione di caricamento, separati da |
  display_blocco TEXT,
  display_offset TEXT,
  rotazione      TEXT,
  da_provare     TEXT,
  nota           TEXT
);
CREATE TABLE COLTURA_TAG_CUSTOM (
  coltura_id TEXT NOT NULL REFERENCES COLTURA_CUSTOM,
  ordine     INTEGER NOT NULL,
  ambito     TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  tag        TEXT NOT NULL,
  PRIMARY KEY (coltura_id, ordine)
);
CREATE TABLE COLTURA_RACCOLTO_CUSTOM (
  coltura_id TEXT NOT NULL REFERENCES COLTURA_CUSTOM,
  gruppo     INTEGER NOT NULL,
  tipo       TEXT NOT NULL CHECK (tipo IN ('oggetto', 'tabella')),
  id         TEXT NOT NULL,
  count      INTEGER,
  chance     REAL,
  PRIMARY KEY (coltura_id, gruppo, id)
);
-- File vincenti: tra file con lo stesso id vince il nostro datapack (Paxi lo carica sopra a tutti). Se due jar
-- portano lo stesso id l'ordine non è noto: `avviso` = 1 e si tiene il primo per nome di fonte.
CREATE VIEW POTS_TERRENO_VINCENTE AS
  SELECT p.*, (SELECT count(*) FROM POTS_TERRENO q WHERE q.ricetta_id = p.ricetta_id AND q.strato = 'originale') > 1 AS avviso
  FROM POTS_TERRENO p
  WHERE p.fonte = (SELECT fonte FROM POTS_TERRENO q WHERE q.ricetta_id = p.ricetta_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
CREATE VIEW POTS_COLTURA_VINCENTE AS
  SELECT p.*, (SELECT count(*) FROM POTS_COLTURA q WHERE q.ricetta_id = p.ricetta_id AND q.strato = 'originale') > 1 AS avviso
  FROM POTS_COLTURA p
  WHERE p.fonte = (SELECT fonte FROM POTS_COLTURA q WHERE q.ricetta_id = p.ricetta_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
CREATE VIEW POTS_COMPATIBILITA AS
  SELECT tt.terreno_id, pc.coltura_id, pct.tag_id, MIN(tt.da_noi) AS da_noi
  FROM TERRENO_TAG tt
  JOIN POTS_COLTURA_TAG pct ON pct.tag_id = tt.tag_id
  JOIN POTS_COLTURA_VINCENTE pc ON pc.ricetta_id = pct.ricetta_id AND pc.fonte = pct.fonte
  GROUP BY tt.terreno_id, pc.coltura_id, pct.tag_id;
"""


class ErroreDati(Exception):
    pass


def _carica_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8-sig"))


class BotanyPotsDB:
    def __init__(self, versione: str | Path):
        self.ver = Path(versione)
        if not self.ver.is_absolute():
            self.ver = Path(__file__).resolve().parent.parent / self.ver
        self.inventario = self.ver / "data" / "inventario"
        self.datapack = self.ver / DP
        self.vasi = self.ver / "data" / "vasi"
        self.db_path = self.vasi / "vasi.sqlite"
        self.query_dir = self.ver / "mod-knowledge" / "botany-pots" / "query"

    # ---------------------------------------------------------------- uso
    def aggiornato(self) -> bool:
        """Vero se il database esiste ed è più recente di inventario, datapack e CSV delle regole."""
        if not self.db_path.exists():
            return False
        t = self.db_path.stat().st_mtime
        fonti = [*self.inventario.rglob("*.json"), *self.datapack.rglob("*.json"), *self.vasi.glob("*.csv"),
                 Path(__file__)]
        return all(f.stat().st_mtime <= t for f in fonti)

    def connetti(self) -> sqlite3.Connection:
        if not self.aggiornato():
            self.refresh()
        c = sqlite3.connect(self.db_path)
        c.execute("PRAGMA foreign_keys = ON")
        c.row_factory = sqlite3.Row
        return c

    def query(self, sql: str, params=()) -> list[sqlite3.Row]:
        with self.connetti() as c:
            return c.execute(sql, params).fetchall()

    def analisi(self, nome: str, params=()) -> list[sqlite3.Row]:
        """Esegue la query salvata in mod-knowledge/botany-pots/query/<nome>.sql."""
        p = self.query_dir / f"{nome}.sql"
        if not p.exists():
            disponibili = ", ".join(sorted(q.stem for q in self.query_dir.glob("*.sql")))
            raise FileNotFoundError(f"query {nome} non trovata in {self.query_dir} (disponibili: {disponibili})")
        return self.query(p.read_text(encoding="utf-8"), params)

    def tabelle(self) -> list[tuple[str, str, int]]:
        out = []
        with self.connetti() as c:
            for nome, tipo in c.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY type DESC, name"):
                n = c.execute(f'SELECT count(*) FROM "{nome}"').fetchone()[0]
                out.append((nome, "vista" if tipo == "view" else "tabella", n))
        return out

    def controlli(self, conn: sqlite3.Connection | None = None) -> list[tuple[str, bool, str]]:
        """Controlli di coerenza oltre ai vincoli: (nome, esito, dettaglio)."""
        c = conn or self.connetti()
        out = []

        def ctl(nome, sql, atteso=0, dettaglio=""):
            n = c.execute(sql).fetchone()[0]
            out.append((nome, n == atteso, f"{dettaglio or 'trovati'}: {n}"))

        out.append(("chiavi esterne valide", not c.execute("PRAGMA foreign_key_check").fetchall(), ""))
        ctl("un solo file vincente per terreno", "SELECT count(*) FROM (SELECT terreno_id FROM POTS_TERRENO_VINCENTE GROUP BY terreno_id HAVING count(*)>1)")
        ctl("un solo file vincente per coltura", "SELECT count(*) FROM (SELECT coltura_id FROM POTS_COLTURA_VINCENTE GROUP BY coltura_id HAVING count(*)>1)")
        ctl("un seme non trova due colture vincenti", "SELECT count(*) FROM (SELECT s.seme FROM POTS_COLTURA_SEME s JOIN POTS_COLTURA_VINCENTE p ON p.ricetta_id=s.ricetta_id AND p.fonte=s.fonte GROUP BY s.seme HAVING count(*)>1)")
        ctl("ogni coltura ha almeno un seme", "SELECT count(*) FROM POTS_COLTURA p WHERE NOT EXISTS (SELECT 1 FROM POTS_COLTURA_SEME s WHERE s.ricetta_id=p.ricetta_id AND s.fonte=p.fonte)")
        ctl("ogni coltura ha almeno un tag", "SELECT count(*) FROM POTS_COLTURA p WHERE NOT EXISTS (SELECT 1 FROM POTS_COLTURA_TAG t WHERE t.ricetta_id=p.ricetta_id AND t.fonte=p.fonte)")
        ctl("ogni coltura vincente ha almeno un terreno", "SELECT count(*) FROM POTS_COLTURA_VINCENTE p WHERE NOT EXISTS (SELECT 1 FROM POTS_COMPATIBILITA k WHERE k.coltura_id=p.coltura_id)")
        ctl("i terreni in_vaso hanno un file vincente", "SELECT count(*) FROM TERRENO t WHERE (stato='in_vaso') <> EXISTS (SELECT 1 FROM POTS_TERRENO_VINCENTE p WHERE p.terreno_id=t.terreno_id)")
        n = c.execute("SELECT count(*) FROM (SELECT ricetta_id FROM POTS_TERRENO_VINCENTE WHERE avviso UNION ALL SELECT ricetta_id FROM POTS_COLTURA_VINCENTE WHERE avviso)").fetchone()[0]
        out.append(("avviso: id portati da due jar (non blocca)", True, f"trovati: {n}"))
        if self._coppie_attese is not None:
            n = c.execute("SELECT count(*) FROM (SELECT DISTINCT terreno_id, coltura_id FROM POTS_COMPATIBILITA)").fetchone()[0]
            out.append(("coppie terreno-coltura = conteggio diretto sui file", n == self._coppie_attese, f"vista {n}, diretto {self._coppie_attese}"))
        if conn is None:
            c.close()
        return out

    # ---------------------------------------------------------------- costruzione
    _coppie_attese = None

    def refresh(self) -> list[tuple[str, bool, str]]:
        dati = self._leggi_fonti()
        fd, tmp = tempfile.mkstemp(suffix=".sqlite", dir=self.vasi)
        os.close(fd)
        try:
            c = sqlite3.connect(tmp)
            c.execute("PRAGMA foreign_keys = ON")
            c.executescript(SCHEMA)
            self._carica(c, dati)
            c.commit()
            esiti = self.controlli(c)
            c.close()
            falliti = [e for e in esiti if not e[1]]
            if falliti:
                raise ErroreDati("controlli falliti: " + "; ".join(f"{n} ({d})" for n, _, d in falliti))
            os.replace(tmp, self.db_path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        return esiti

    def _leggi_fonti(self) -> dict:
        items, blocks, mods = set(), set(), set()
        tag_voci = {"oggetti": defaultdict(list), "blocchi": defaultdict(list)}  # (fonte, voce, facoltativa)
        ricette = []
        files = [self.inventario / "minecraft.json", self.inventario / "neoforge.json", *sorted((self.inventario / "mods").glob("*.json"))]
        for f in files:
            if not f.exists():
                continue
            d = _carica_json(f)
            fonte = f.stem
            items |= set(d.get("items", {}))
            blocks |= set(d.get("blocks", {}))
            mods |= {m["modid"] for m in d.get("mods", [])}
            for amb, cat in (("oggetti", "tags/item"), ("blocchi", "tags/block")):
                for nome, vals in (d.get("tags", {}).get(cat) or {}).items():
                    for v in vals:
                        tag_voci[amb][nome].append((fonte, v.rstrip("?"), v.endswith("?")))
            for r in d.get("botanypots") or []:
                ricette.append({**r, "_fonte": fonte, "_strato": "originale"})
        if not items:
            raise ErroreDati(f"inventario vuoto o assente: {self.inventario}")
        # datapack: tag e ricette
        for f in self.datapack.glob("*/tags/*/**/*.json"):
            rel = f.relative_to(self.datapack).parts
            amb = {"item": "oggetti", "block": "blocchi"}.get(rel[2])
            if amb is None:
                continue
            d = _carica_json(f)
            if d.get("replace"):
                raise ErroreDati(f"tag con replace=true non previsto: {f}")
            nome = f"{rel[0]}:{'/'.join(rel[3:])[:-5]}"
            for v in d.get("values", []):
                vid, fac = (v, False) if isinstance(v, str) else (v["id"], not v.get("required", True))
                tag_voci[amb][nome].append((NOSTRO, vid, fac))
        for f in self.datapack.glob("*/recipe/**/*.json"):
            d = _carica_json(f)
            if str(d.get("type", "")) in TIPI_TERRENO + TIPI_COLTURA:
                rel = f.relative_to(self.datapack).parts
                d["id"] = f"{rel[0]}:{'/'.join(rel[2:])[:-5]}"
                ricette.append({**d, "_fonte": NOSTRO, "_strato": "nostro"})
        return {"items": items, "blocks": blocks, "mods": mods, "tag_voci": tag_voci, "ricette": ricette}

    # -- condizioni di caricamento
    @staticmethod
    def _caricabile(r: dict, items: set, blocks: set, mods: set) -> bool:
        for cnd in r.get("bookshelf:load_conditions", []):
            t, vals = cnd["type"], cnd.get("values", [])
            if t == "bookshelf:block_exists":
                if not all(v in blocks for v in vals):
                    return False
            elif t == "bookshelf:item_exists":
                if not all(v in items for v in vals):
                    return False
            else:
                raise ErroreDati(f"condizione non prevista {t} in {r['id']}")
        for cnd in r.get("neoforge:conditions", []):
            t = cnd["type"]
            if t == "neoforge:mod_loaded":
                if cnd["modid"] not in mods:
                    return False
            elif t == "neoforge:item_exists":
                if cnd["item"] not in items:
                    return False
            else:
                raise ErroreDati(f"condizione non prevista {t} in {r['id']}")
        return True

    # -- ingredienti
    @staticmethod
    def _tag_di_soil(ing, rid: str) -> list[tuple[str, str]]:
        """Le alternative del campo `soil`: lista di (ambito, nome del tag)."""
        if ing is None:
            return [TAG_DIRT]
        if isinstance(ing, list):
            return [x for i in ing for x in BotanyPotsDB._tag_di_soil(i, rid)]
        t = ing.get("type")
        if t is None and "tag" in ing:
            return [("oggetti", ing["tag"])]
        if t == "bookshelf:block_tag":
            tags = ing["tag"] if isinstance(ing["tag"], list) else [ing["tag"]]
            return [("blocchi", x) for x in tags]
        if t in ("bookshelf:either", "neoforge:compound"):
            return [x for i in ing.get("ingredients", ing.get("children", [])) for x in BotanyPotsDB._tag_di_soil(i, rid)]
        raise ErroreDati(f"forma di `soil` non prevista in {rid}: {json.dumps(ing)[:120]}")

    @staticmethod
    def _oggetti_di_input(ing, rid: str) -> list[str]:
        if isinstance(ing, list):
            return [x for i in ing for x in BotanyPotsDB._oggetti_di_input(i, rid)]
        if isinstance(ing, dict) and "item" in ing and ing.get("type") is None:
            return [ing["item"]]
        raise ErroreDati(f"forma di `input` non prevista in {rid}: {json.dumps(ing)[:120]}")

    def _carica(self, c: sqlite3.Connection, dati: dict) -> None:
        items, blocks, mods, tag_voci = dati["items"], dati["blocks"], dati["mods"], dati["tag_voci"]
        ricette = [r for r in dati["ricette"] if self._caricabile(r, items, blocks, mods)]
        terreni_r = [r for r in ricette if r["type"] in TIPI_TERRENO]
        colture_r = [r for r in ricette if r["type"] in TIPI_COLTURA]

        # file vincenti (stessa regola della vista): il datapack vince; tra jar, il primo per nome di fonte
        def vincenti(rs):
            best = {}
            for r in sorted(rs, key=lambda r: (r["_strato"] != "nostro", r["_fonte"])):
                best.setdefault(r["id"], r)
            return {(r["id"], r["_fonte"]) for r in best.values()}

        vinc_t, vinc_c = vincenti(terreni_r), vincenti(colture_r)

        # tag: quelli nominati dalle colture e tutto ciò che contengono
        nominati = set()
        for r in colture_r:
            nominati |= set(self._tag_di_soil(r.get("soil"), r["id"]))
        tag_ids, pila = {}, list(nominati)
        while pila:
            amb, nome = pila.pop()
            if (amb, nome) in tag_ids:
                continue
            tag_ids[(amb, nome)] = len(tag_ids) + 1
            for _f, v, _o in tag_voci[amb].get(nome, []):
                if v.startswith("#"):
                    pila.append((amb, v[1:]))
        c.executemany("INSERT INTO TAG VALUES (?,?,?)", [(i, a, n) for (a, n), i in tag_ids.items()])

        # esplosione: per ogni terreno, i tag che lo elencano (diretti) e tutti i loro antenati
        def madri(con_nostre: bool) -> dict[tuple, set]:
            m = defaultdict(set)
            for (amb, nome) in tag_ids:
                for f, v, _o in tag_voci[amb].get(nome, []):
                    if v.startswith("#") and (con_nostre or f != NOSTRO):
                        m[(amb, v[1:])].add((amb, nome))
            return m

        def diretti(con_nostre: bool) -> dict[str, set]:
            d = defaultdict(set)  # terreno -> {(ambito, nome)}
            for (amb, nome) in tag_ids:
                reg = items if amb == "oggetti" else blocks
                for f, v, fac in tag_voci[amb].get(nome, []):
                    if v.startswith("#") or (con_nostre is False and f == NOSTRO):
                        continue
                    if v not in reg:
                        if fac:
                            continue
                        raise ErroreDati(f"il tag {nome} ({amb}) elenca {v}, che non esiste")
                    if amb == "blocchi" and v not in items:
                        continue  # blocco senza oggetto con lo stesso nome: non può stare nello slot
                    d[v].add((amb, nome))
            return d

        def esplodi(con_nostre: bool) -> set[tuple]:
            m, d = madri(con_nostre), diretti(con_nostre)
            righe = set()  # (terreno, tag, tag_diretto, livello)
            for terreno, tags in d.items():
                for t0 in tags:
                    visti, fronte, liv = {t0}, [t0], 0
                    while fronte:
                        for t in fronte:
                            righe.add((terreno, t, t0, liv))
                        liv += 1
                        fronte = [p for t in fronte for p in m.get(t, ()) if p not in visti]
                        visti |= set(fronte)
                        if liv > 50:
                            raise ErroreDati(f"ciclo nei tag a partire da {t0}")
            return righe

        senza, con = esplodi(False), esplodi(True)
        esploso = {}
        for terreno, t, t0, liv in con:
            k = (terreno, t, t0)
            esploso[k] = min(liv, esploso.get(k, 99))
        senza_k = {(a, b, c0) for a, b, c0, _ in senza}

        # anagrafiche
        for r in terreni_r:
            ogg = r["input"]["item"] if r.get("input") else r["block"]
            if r.get("input") and r["input"].get("type"):
                raise ErroreDati(f"input del terreno non previsto in {r['id']}")
            if ogg not in items:
                raise ErroreDati(f"terreno {ogg} di {r['id']} non è un oggetto")
            r["_terreno"] = ogg
        vinc_terreni = {r["_terreno"] for r in terreni_r if (r["id"], r["_fonte"]) in vinc_t}
        tutti_terreni = vinc_terreni | {r["_terreno"] for r in terreni_r} | {k[0] for k in esploso}
        c.executemany("INSERT INTO TERRENO VALUES (?,?,?)",
                      [(t, t.split(":")[0], "in_vaso" if t in vinc_terreni else "candidato") for t in sorted(tutti_terreni)])
        for r in colture_r:
            if r.get("input"):
                semi, orig = self._oggetti_di_input(r["input"], r["id"]), "file"
            elif r["block"] in items:
                semi, orig = [r["block"]], "blocco"
            elif r["block"] in SEMI_ECCEZIONI:
                semi, orig = [SEMI_ECCEZIONI[r["block"]]], "eccezione"
            else:
                raise ErroreDati(f"seme sconosciuto per {r['id']} (blocco {r['block']})")
            for s in semi:
                if s not in items:
                    raise ErroreDati(f"seme {s} di {r['id']} non è un oggetto")
            r["_semi"], r["_orig"] = semi, orig
            r["_coltura"] = r.get("block") or semi[0]
        c.executemany("INSERT OR IGNORE INTO COLTURA VALUES (?,?,?)",
                      [(r["_coltura"], r["_coltura"].split(":")[0], "in_vaso") for r in colture_r])

        # file del vaso
        c.executemany("INSERT INTO POTS_TERRENO VALUES (?,?,?,?,?,?,?)", [
            (r["id"], r["_fonte"], r["_strato"], r["_terreno"], r.get("growth_modifier", 0), r.get("yield_modifier", 0),
             r.get("light_level", 0)) for r in terreni_r])
        c.executemany("INSERT INTO POTS_COLTURA VALUES (?,?,?,?,?,?,?)", [
            (r["id"], r["_fonte"], r["_strato"], r["_coltura"], r.get("grow_time", 1200), r.get("yield", 1),
             r.get("yield_scale", 1)) for r in colture_r])
        c.executemany("INSERT INTO POTS_COLTURA_SEME VALUES (?,?,?,?)",
                      [(r["id"], r["_fonte"], s, r["_orig"]) for r in colture_r for s in r["_semi"]])
        righe = set()
        for r in colture_r:
            for amb, nome in self._tag_di_soil(r.get("soil"), r["id"]):
                righe.add((r["id"], r["_fonte"], tag_ids[(amb, nome)], int(r.get("soil") is None)))
        c.executemany("INSERT INTO POTS_COLTURA_TAG VALUES (?,?,?,?)", sorted(righe))
        c.executemany("INSERT INTO TERRENO_TAG VALUES (?,?,?,?,?)", [
            (t, tag_ids[tag], tag_ids[t0], liv, int((t, tag, t0) not in senza_k)) for (t, tag, t0), liv in esploso.items()])

        # scelte
        self._carica_csv(c, "RARITA_POTS_SETTINGS", "rarita_pots_settings.csv", ("classe", "ordine", "crescita", "resa"))
        self._carica_csv(c, "TERRENO_RARITA", "terreno_rarita.csv", ("terreno_id", "classe", "motivo"))
        self._carica_csv(c, "TERRENO_TAG_CUSTOM", "terreno_tag_custom.csv", ("terreno_id", "ambito", "tag"))
        self._carica_csv(c, "COLTURA_CUSTOM", "coltura_custom.csv", ("coltura_id", "mod", "seme", "tempo", "richiesti", "display_blocco", "display_offset", "rotazione", "da_provare", "nota"))
        self._carica_csv(c, "COLTURA_TAG_CUSTOM", "coltura_tag_custom.csv", ("coltura_id", "ordine", "ambito", "tag"))
        self._carica_csv(c, "COLTURA_RACCOLTO_CUSTOM", "coltura_raccolto_custom.csv", ("coltura_id", "gruppo", "tipo", "id", "count", "chance"))

        # conteggio diretto delle coppie, indipendente dalla vista: per ogni coltura vincente, gli oggetti dei suoi tag
        membri = defaultdict(set)
        for (t, tag, _t0) in esploso:
            membri[tag].add(t)
        coppie = set()
        for r in colture_r:
            if (r["id"], r["_fonte"]) in vinc_c:
                for tag in self._tag_di_soil(r.get("soil"), r["id"]):
                    coppie |= {(t, r["_coltura"]) for t in membri[tag]}
        self._coppie_attese = len(coppie)

    def _carica_csv(self, c: sqlite3.Connection, tabella: str, nome: str, colonne: tuple) -> None:
        p = self.vasi / nome
        if not p.exists():
            return
        with p.open(encoding="utf-8", newline="") as f:
            righe = list(csv.DictReader(f))
        for r in righe:
            mancanti = [k for k in colonne if k not in r]
            if mancanti:
                raise ErroreDati(f"{nome}: colonne mancanti {mancanti}")
        c.executemany(f"INSERT INTO {tabella} ({','.join(colonne)}) VALUES ({','.join('?' * len(colonne))})",
                      [tuple(r[k] if r[k] != "" else None for k in colonne) for r in righe])


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    db, cmd = BotanyPotsDB(argv[0]), argv[1]
    if cmd == "refresh":
        for nome, ok, det in db.refresh():
            print(("✅" if ok else "❌"), nome, det)
        print("scritto", db.db_path)
    elif cmd in ("query", "analisi"):
        righe = db.query(argv[2]) if cmd == "query" else db.analisi(argv[2])
        if righe:
            print("\t".join(righe[0].keys()))
            for r in righe:
                print("\t".join("" if v is None else str(v) for v in r))
        print(f"({len(righe)} righe)")
    elif cmd == "tabelle":
        for nome, tipo, n in db.tabelle():
            print(f"{tipo:8s} {nome:24s} {n:6d}")
    elif cmd == "controlli":
        for nome, ok, det in db.controlli():
            print(("✅" if ok else "❌"), nome, det)
    else:
        print("comando sconosciuto:", cmd)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:  # output troncato da `head` e simili
        sys.exit(0)
