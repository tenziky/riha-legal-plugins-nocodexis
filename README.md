# riha-legal-plugins-nocodexis

Automaticky převáděná kopie marketplace [riha-legal-plugins](https://github.com/LexaurinTheDog/riha-legal-plugins) (JUDr. Vojtěch Říha, Ph.D., licence Apache-2.0) pro konektory **Salvia**, **lawgpt**, **Sagasu** a **Ansvar** místo placené databáze CODEXIS.

## Jak to funguje

Workflow `.github/workflows/prevod.yml` každé pondělí (nebo ručně z karty Actions) stáhne aktuální originál, spustí `konverze/konverze.py` a výsledek uloží do tohoto repozitáře. Commit originálu, ze kterého převod vznikl, je v `konverze/original-commit.txt`.

Co převod mění:
- všech 50 oborových skillů: společná metodika (`konverze/puvodni-blok.md`) se nahradí verzí pro konektory (`konverze/novy-blok.md`), zmínky o CODEXIS v oborových částech a popisech se přepíšou,
- `lhutnik`: zápis do iCloud kalendáře „AK - Jirka“ přes konektor Spark (`konverze/lhutnik-novy-SKILL.md`),
- marketplace se jmenuje `riha-legal-plugins-nocodexis`, aby mohl existovat vedle originálu.

## Když převod selže

Skript je záměrně přísný. Pokud autor změní společnou metodiku nebo Lhůtník, nebo po převodu kdekoli zbude CODEXIS, workflow skončí chybou, nic nepřepíše a GitHub pošle e-mail. Opravu udělá Claude Code, stačí mu říct:

> V repozitáři riha-legal-plugins-nocodexis selhal převod. Podle konverze/NAVOD.md zjisti, co autor změnil, a uprav převodní soubory.

## Instalace (Claude Code)

```
/plugin marketplace add tenziky/riha-legal-plugins-nocodexis
/plugin install smluvni-pravo@riha-legal-plugins-nocodexis
```
