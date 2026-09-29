#!/usr/bin/env python3
"""Převod marketplace riha-legal-plugins z CODEXIS na konektory Salvia, lawgpt, Sagasu a Ansvar.

Použití:
    python3 konverze/konverze.py <slozka-originalu> <cilova-slozka>

Skript je záměrně přísný: pokud autor originálu změní společnou metodiku nebo Lhůtník
tak, že je skript nepozná, nebo pokud po převodu kdekoli zbude CODEXIS, skončí chybou
a nic nezapíše. Opravu pak udělá člověk (aktualizací souborů v této složce), ne náhoda.
"""
import glob
import json
import os
import re
import shutil
import sys

import yaml

TU = os.path.dirname(os.path.abspath(__file__))
MARKETPLACE_NAME = "riha-legal-plugins-nocodexis"
LOC = "připojených pramenech (Salvia, lawgpt)"
BODY_SUBS = [
    (r"\bV nativním CODEXIS\b", "V " + LOC),
    (r"\bv nativním CODEXIS\b", "v " + LOC),
    (r"\bV CODEXIS\b", "V " + LOC),
    (r"\bv CODEXIS\b", "v " + LOC),
    (r"\bNativním CODEXIS\b", "Připojenými prameny (Salvia, lawgpt)"),
    (r"\bnativním CODEXIS\b", "připojenými prameny (Salvia, lawgpt)"),
    (r"\bze? CODEXIS\b", "z připojených pramenů (Salvia, lawgpt)"),
    (r"\bnativní CODEXIS\b", "připojené prameny"),
]
EN_OLD = re.compile(r",? on top of the CODEXIS legal database")
EN_NEW = " - research via the Salvia and lawgpt connectors"
FM_DESC_EN = ("Research legal sources only through native CODEXIS in the application.",
              "Research legal sources through the Salvia and lawgpt connectors (registries via Sagasu, EU law via Ansvar).")
FM_DESC_CZ = (re.compile(r"(Právní|Veškeré)?[^.'\n]*CODEXIS[^.'\n]*\."),
              "Právní rešerše přes konektory Salvia a lawgpt.")
POZNAMKA = ("\n<!-- Upraveno z pluginu {name} (JUDr. Vojtěch Říha, Ph.D., "
            "github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS "
            "nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->\n")

chyby = []


def cti(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def zapis(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


def spolecny_blok(t):
    if "## Výhradní zdrojový režim" not in t or "## Oborové otázky" not in t:
        return None
    return t[t.index("## Výhradní zdrojový režim"):t.index("## Oborové otázky")]


def prevod_skillu(f, puvodni, novy):
    t = cti(f)
    blok = spolecny_blok(t)
    if blok is None:
        chyby.append(f"{f}: nenalezen společný blok (struktura skillu se změnila)")
        return
    if blok != puvodni:
        chyby.append(f"{f}: autor změnil společnou metodiku — zkontrolujte rozdíl proti konverze/puvodni-blok.md "
                     "a aktualizujte puvodni-blok.md i novy-blok.md")
        return
    t = t.replace(puvodni, novy)
    head, sep, rest = t.partition("\n---\n")
    head = head.replace(*FM_DESC_EN)
    head = FM_DESC_CZ[0].sub(FM_DESC_CZ[1], head)
    for a, b in BODY_SUBS:
        rest = re.sub(a, b, rest)
    name = f.split(os.sep)[-4]
    zapis(f, head + sep + POZNAMKA.format(name=name) + rest)


def main(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", ".github", "promo"))

    puvodni, novy = cti(os.path.join(TU, "puvodni-blok.md")), cti(os.path.join(TU, "novy-blok.md"))

    # 1) oborové skilly (všechny kromě Lhůtníku)
    skilly = sorted(glob.glob(os.path.join(dst, "plugins", "*", "skills", "*", "SKILL.md")))
    for f in skilly:
        if os.sep + "lhutnik" + os.sep in f:
            continue
        prevod_skillu(f, puvodni, novy)

    # 2) Lhůtník ponecháváme beze změny (zápis do kalendáře dle originálu)

    # 3) metadata pluginů a marketplace
    for f in glob.glob(os.path.join(dst, "plugins", "*", ".claude-plugin", "plugin.json")):
        zapis(f, EN_OLD.sub(EN_NEW, cti(f)).replace("CODEXIS", "Salvia/lawgpt"))
    mp = os.path.join(dst, ".claude-plugin", "marketplace.json")
    m = json.loads(EN_OLD.sub(EN_NEW, cti(mp)).replace("CODEXIS", "Salvia/lawgpt"))
    m["name"] = MARKETPLACE_NAME
    m.setdefault("metadata", {})["description"] = (
        "Automaticky převedená kopie riha-legal-plugins (JUDr. Vojtěch Říha, Ph.D., Apache-2.0) "
        "pro konektory Salvia, lawgpt, Sagasu a Ansvar.")
    zapis(mp, json.dumps(m, ensure_ascii=False, indent=2) + "\n")

    # 4) sdílené texty
    shared = os.path.join(dst, "shared")
    if os.path.isdir(shared):
        a, b = novy.index("### 2a."), novy.index("### 3. Předpis")
        hl = POZNAMKA.format(name="shared").lstrip()
        zapis(os.path.join(shared, "rozhodna-uprava-a-judikatura.md"), hl + novy[a:b].rstrip() + "\n")
        zapis(os.path.join(shared, "native-contract-r4.md"), hl + (novy[:a] + novy[b:]).rstrip() + "\n")

    # 4b) přehled změn (Apache-2.0, čl. 4 písm. b)
    shutil.copy(os.path.join(TU, "ZMENY.md"), os.path.join(dst, "ZMENY.md"))

    # 5) README původního autora ponecháme pod jiným názvem
    if os.path.exists(os.path.join(dst, "README.md")):
        os.rename(os.path.join(dst, "README.md"), os.path.join(dst, "README-original.md"))

    # 6) kontroly
    for f in glob.glob(os.path.join(dst, "**", "*"), recursive=True):
        if not os.path.isfile(f) or not f.endswith((".md", ".json", ".py")) or f.endswith(("README-original.md", "ZMENY.md")):
            continue
        for i, radek in enumerate(cti(f).splitlines(), 1):
            if "CODEXIS" in radek and "Upraveno z pluginu" not in radek and "CODEXIS nahrazen" not in radek:
                chyby.append(f"{f}:{i}: po převodu zůstal CODEXIS: {radek.strip()[:120]}")
    for f in skilly:
        if os.sep + "lhutnik" + os.sep in f:
            continue  # ponechán beze změny podle originálu
        try:
            d = yaml.safe_load(cti(f).split("---")[1])
            assert d.get("name") and d.get("description")
        except Exception as e:  # noqa: BLE001
            chyby.append(f"{f}: neplatná hlavička skillu ({e})")
    for f in glob.glob(os.path.join(dst, "**", "*.json"), recursive=True):
        try:
            json.loads(cti(f))
        except Exception as e:  # noqa: BLE001
            chyby.append(f"{f}: neplatný JSON ({e})")

    if chyby:
        shutil.rmtree(dst)
        print("PŘEVOD SELHAL — nic nebylo zapsáno:\n" + "\n".join(" - " + c for c in chyby), file=sys.stderr)
        sys.exit(1)
    print(f"Převedeno {len(skilly)} skillů do {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
