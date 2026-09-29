# Návod na opravu převodu (pro Claude Code)

Převod selhal, protože se originál změnil způsobem, který skript nepozná. Postup:

1. Stáhni originál: `git clone --depth 1 https://github.com/LexaurinTheDog/riha-legal-plugins.git /tmp/original`
2. Spusť `python3 konverze/konverze.py /tmp/original /tmp/prevedeno` a přečti chybové hlášky.
3. Podle typu chyby:
   - **„autor změnil společnou metodiku“**: vezmi společný blok z libovolného oborového SKILL.md v originálu (od `## Výhradní zdrojový režim` do `## Oborové otázky`) a porovnej ho s `konverze/puvodni-blok.md`. Věcné změny autora (nové kroky, upřesnění) promítni do `konverze/novy-blok.md`, ale vždy ve verzi pro konektory Salvia a lawgpt, nikdy s CODEXIS. Pak nový blok z originálu ulož jako `konverze/puvodni-blok.md`.
   - **„po převodu zůstal CODEXIS“**: autor použil novou formulaci. Doplň pravidlo do `BODY_SUBS` nebo `FM_DESC_CZ` v `konverze.py` tak, aby věta zůstala gramaticky správná.
   - **„nenalezen společný blok“**: struktura skillu se změnila zásadněji — nic neopravuj naslepo, popiš uživateli, co se změnilo, a navrhni řešení.
4. Spusť převod znovu, dokud neprojde, a namátkou zkontroluj 2–3 převedené skilly, že dávají smysl.
5. Commitni změny ve složce `konverze/` a ručně spusť workflow (`gh workflow run prevod.yml`).

Pravidla: zdroje v převedených skillech jsou vždy Salvia a lawgpt (doplňkově Sagasu, Ansvar). Poznámku o úpravě a licenci Apache-2.0 zachovej.
