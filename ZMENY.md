# Změny oproti originálu

Tento repozitář obsahuje upravené dílo odvozené z [riha-legal-plugins](https://github.com/LexaurinTheDog/riha-legal-plugins),
jehož autorem je JUDr. Vojtěch Říha, Ph.D. Originál i tato úprava jsou šířeny pod licencí Apache License 2.0 (soubor `LICENSE`).
Původní README autora je zachováno jako `README-original.md`. Úprava není autorem originálu schválena ani s ním spojena.

Upravené soubory (upravuje je automaticky skript `konverze/konverze.py`):

- `plugins/*/skills/*/SKILL.md` — společná metodika a všechny zmínky o databázi CODEXIS nahrazeny postupem pro konektory Salvia, lawgpt, Sagasu a Ansvar; popisy skillů upraveny; každý soubor nese poznámku o úpravě.
- `plugins/*/.claude-plugin/plugin.json` a `.claude-plugin/marketplace.json` — v popisech nahrazen odkaz na CODEXIS; marketplace přejmenován.
- `shared/native-contract-r4.md`, `shared/rozhodna-uprava-a-judikatura.md` — nahrazeny verzí pro konektory.
- Vynechána složka `promo/`.

Soubory ve složce `konverze/` (`novy-blok.md`, `puvodni-blok.md`) obsahují převzaté, případně upravené části originálu.
Ostatní soubory (např. celý plugin `lhutnik`, ikony) jsou převzaty beze změny.

CODEXIS® je ochranná známka svého vlastníka; je zde uvedena jen k popisu provedené změny.
