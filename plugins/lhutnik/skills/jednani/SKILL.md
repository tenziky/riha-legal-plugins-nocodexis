---
name: jednani
description: 'Záznam z jednání soudu → hlídané lhůty v kalendáři „AK - Jirka“. Z volných poznámek po jednání vytáhne lhůty všech stran a termín dalšího jednání, spočítá konce lhůt dle § 57 o. s. ř. skriptem a po schválení založí události s upomínkami. Triggers: /lhutnik, /jednani, záznam z jednání, byl jsem u soudu, po jednání, zapiš lhůtu, odročeno, lhůtník, procesní lhůta.'
---

<!-- Upraveno z pluginu lhutnik (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zápis do kalendáře přes Spark místo gog CLI, kalendář „AK - Jirka“, metadata v popisu události. -->

# Záznam z jednání → hlídané lhůty

Účel: aby se poznámka z jednací síně **ve stejném úkonu** změnila na termín s budíkem. Dva oddělené kroky („zapsat“ a „zanést do lhůtníku“) selhávají na tom druhém — proto se tady dělají naráz.

Kalkulátor lhůt leží vedle tohoto souboru (`lhuta.py`).

## Konfigurace

| Klíč | Hodnota |
|---|---|
| Kalendář (zdroj pravdy pro lhůty) | iCloud kalendář **„AK - Jirka“**, zápis nástrojem Spark `event` (`mode: create`, `calendar: <účet>:AK - Jirka`). Název účtu zjisti nástrojem Spark `accounts`. |
| Časové pásmo | `Europe/Prague` |
| Kam ukládat záznam | do složky kauzy; neznáš-li ji, zeptej se |
| Upomínky u lhůty | 7 dní, 3 dny, 1 den předem (`alerts: 604800s,259200s,86400s`) |
| Upomínky u jednání | 7 dní, 1 den předem (`alerts: 604800s,86400s`) |

Kalendář „AK - Jirka“ vidí i školitel. Každý zápis do něj musí uživatel předem výslovně potvrdit. Není-li Spark dostupný, zeptej se, kam termíny zapsat — **nikdy je nezakládej „naslepo“ jinam**.

## ŽELEZNÁ PRAVIDLA

1. **Nikdy nehádat lhůtu.** Nevíš-li jistě rozhodnou skutečnost (od čeho lhůta běží) nebo její délku, ZEPTEJ SE. Chybný termín v kalendáři je horší než žádný — vypadá jako ohlídaný.
2. **Zachytit lhůty VŠECH stran**, ne jen klientovy: moje / protistrany / soudu. Zmeškaná lhůta protistrany je procesní příležitost, ne cizí starost.
3. **Konce lhůt počítat výhradně skriptem**, nikdy zpaměti ani odhadem.
4. **Rozhodná skutečnost není vždy den jednání.** Bývá i doručení, zveřejnění v rejstříku, právní moc. Rozliš to a v pochybnosti se ptej.
5. Před založením událostí předlož **souhrn ke schválení**. Teprve po potvrzení zakládej.

## Postup

### 1. Získej vstup

Poznámky jsou ve zprávě nebo v přiloženém souboru; jinak o ně požádej.

### 2. Vytěž fakta

Sestav tabulku z toho, co v poznámkách je. Co chybí, **vypiš jako otázky** — nedomýšlej:

| Pole | Pozn. |
|---|---|
| Klient / spis | |
| Sp. zn. / č. j. | přesně dle záhlaví |
| Soud, senát/samosoudce | |
| Datum jednání | |
| Co se stalo | přednesy, dokazování, uznané/sporné skutečnosti |
| **Lhůty** | pro každou: *kdo*, *co má udělat*, *délka*, *od jaké skutečnosti* |
| **Další jednání** | datum, čas, síň, adresa |
| Poučení | zejm. § 118a, § 118b odst. 1 (koncentrace) |
| Úkoly pro mě | co sepsat, co doložit, koho oslovit |

Stav řízení lze doplnit ze skillu ak-infosoud (InfoSoud), pokud je sp. zn. známa.

### 3. Spočítej lhůty

Pro každou lhůtu zavolej kalkulátor a použij `posledni_den`:

```bash
python3 lhuta.py 2026-02-02 30d --json
```

Podporuje `Nd` / `Nt` / `Nm` / `Nr` (dny, týdny, měsíce, roky). Implementuje § 57 o. s. ř.: běh od následujícího dne po rozhodné skutečnosti; u týdnů/měsíců/let shoda označení dne (není-li takový den, poslední den měsíce); posun z víkendu a svátku na nejblíže následující pracovní den. Svátky včetně pohyblivých Velikonoc.

### 4. Předlož souhrn ke schválení

Vypiš, co se založí — každou lhůtu s posledním dnem a upomínkami, jednání s časem a síní, kontrolní události. Vyžádej výslovné potvrzení.

### 5. Založ události (Spark `event`, `mode: create`)

Metadata pro pozdější kontrolní přejezd ulož na konec popisu události v jednom řádku:
`[lhutnik] typ=lhuta|jednani|kontrola; kdo=my|protistrana|soud; spis=<sp. zn.>`

**Lhůta** — celodenní událost na poslední den:
- `title`: `LHŮTA (protistrana): <co> — <sp. zn.>`
- `start`: `2026-03-04`, `all_day: true`
- `description`: od čeho běží, co se stane při nesplnění, kde ověřit + řádek metadat
- `alerts`: `604800s,259200s,86400s`

**Jednání** — časovaná událost:
- `title`: `Jednání: <klient> — <sp. zn.>`
- `start`: `2026-06-15T15:00:00+02:00`, `end`: `2026-06-15T16:30:00+02:00`
- `location`: soud, adresa, jednací síň
- `alerts`: `604800s,86400s`

U lhůty protistrany založ **navíc kontrolní událost** den po jejím uplynutí: „ověřit ve spisu/rejstříku, zda protistrana doplnila“ (`typ=kontrola`).

Neznáš-li délku jednání, počítej 90 minut a řekni to uživateli. Pozvánky (`add`) nikomu neposílej.

### 6. Ulož strukturovaný záznam

`Zaznam_z_jednani_YYYY-MM-DD.md` do složky kauzy, s frontmatter `spis`, `sp_zn`, `soud`, `datum`, `lhuty`, `dalsi_jednani`, `zalozeno_v_kalendari: true`.

### 7. Uzavři

Shrň, co bylo založeno, a **výslovně vyjmenuj, co jsi nezaložil a proč** (chybějící údaj, nejasná rozhodná skutečnost). Nedopověděné údaje musí zůstat viditelné, ne zmizet.

## Časté pasti

- **§ 118b odst. 1 poslední věta**: byla-li dána výzva dle § 118a, smí soud přihlédnout i k později uvedeným skutečnostem. Zmeškání takové lhůty protistranou tedy *není* prekluze — argumentovat neunesením břemene tvrzení, ne prekluzí.
- Lhůta „ode dne zveřejnění v rejstříku“ běží od zveřejnění, ne od jednání ani od doručení.
- Odročeno „na neurčito“ = žádná událost jednání, ale **založ kontrolu za 3 měsíce**, ať věc nezapadne.
- Vyhlásí-li soud rozhodnutí při jednání, běží lhůta k opravnému prostředku typicky od **doručení písemného vyhotovení** — v den jednání ji tedy ještě nelze uzavřít; založ kontrolu na očekávané doručení.
- Doručení do datové schránky: fikce doručení 10. dnem od dodání (§ 17 odst. 4 z. č. 300/2008 Sb.); rozhodnou skutečností je pak den přihlášení, nebo den fikce — ověř, co nastalo dřív.
- Lhůty hmotněprávní (promlčecí, prekluzivní dle o. z.) se počítají jinak než procesní a **musí dojít včas**, ne jen být odeslány. Kalkulátor je stavěný na procesní lhůty dle § 57 o. s. ř. — u hmotněprávních jeho výsledek nepoužívej bez kontroly.
