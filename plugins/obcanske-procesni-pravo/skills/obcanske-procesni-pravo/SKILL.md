---
uuid: 66f31eeb-2f0d-4023-bde4-6c9f8d3eb0f6
name: obcanske-procesni-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Občanské procesní právo ČR"
    summary: "Pravomoc a příslušnost, sepis žaloby a petitu, soudní poplatky, doručování a lhůty, dokazování a důkazní břemeno, rozsudek pro zmeškání a platební rozkaz, předběžná opatření, odvolání a mimořádné opravné prostředky včetně přípustnosti dovolání, náklady řízení a advokátní tarif, nesporná řízení."
    examplePrompts:
      - "Rozsudek odvolacího soudu byl doručen do datové schránky 3. 6. a klient ho otevřel 15. 6. Do kdy běží lhůta pro dovolání a jak správně vymezit přípustnost podle § 237?"
      - "Žalovaný se nedostavil k prvnímu jednání a soud vydal rozsudek pro zmeškání. Jaké jsou možnosti obrany a lhůty?"
      - "Připrav petit a strukturu žaloby na zaplacení 480 000 Kč s příslušenstvím z nezaplacené faktury, včetně výpočtu soudního poplatku a nákladů."
  en:
    displayName: "Czech Civil Procedure"
    summary: "Jurisdiction and venue, drafting claims and petitions, court fees, service and deadlines, evidence and burden of proof, default judgments and payment orders, interim measures, appeals and extraordinary remedies including admissibility of dovolání, costs and attorney tariff, non-contentious proceedings."
    examplePrompts:
      - "The appellate judgment was delivered to the data box on 3 June and opened on 15 June. When does the deadline for an appeal on points of law expire and how to frame admissibility under § 237?"
      - "The defendant did not attend the first hearing and the court issued a default judgment. What are the remedies and deadlines?"
      - "Draft the relief sought and structure of a claim for CZK 480,000 with accessories from an unpaid invoice, including the court fee and costs calculation."
  sk:
    displayName: "Občianske procesné právo ČR"
    summary: "Právomoc a príslušnosť, spísanie žaloby a petitu, súdne poplatky, doručovanie a lehoty, dokazovanie a dôkazné bremeno, rozsudok pre zmeškanie a platobný rozkaz, predbežné opatrenia, odvolanie a mimoriadne opravné prostriedky vrátane prípustnosti dovolania, trovy konania a advokátska tarifa, nesporové konania."
    examplePrompts:
      - "Rozsudok odvolacieho súdu bol doručený do dátovej schránky 3. 6. a klient ho otvoril 15. 6. Dokedy plynie lehota na dovolanie a ako správne vymedziť prípustnosť podľa § 237?"
      - "Žalovaný sa nedostavil na prvé pojednávanie a súd vydal rozsudok pre zmeškanie. Aké sú možnosti obrany a lehoty?"
      - "Priprav petit a štruktúru žaloby na zaplatenie 480 000 Kč s príslušenstvom z nezaplatenej faktúry, vrátane výpočtu súdneho poplatku a trov."
description: 'Použij pro civilní sporné, zvláštní a hromadné řízení: pravomoc, příslušnost, žalobu a petit, doručování, lhůty, dokazování a koncentraci, platební rozkazy, uznání a zmeškání, předběžná opatření, odvolání a dovolání, obnovu a zmatečnost, soudní poplatky, tarifní náklady, průtahy a spravedlivý proces. Právní rešerše přes konektory Salvia a lawgpt.'
---

<!-- Upraveno z pluginu obcanske-procesni-pravo (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Občanské procesní právo ČR

## Zdrojový režim: Salvia, lawgpt a oficiální prameny

Právní předpisy a judikaturu získávej z připojených konektorů:
- **Salvia** – předpisy (`search_regulations`, `fetch_regulation_text`, `fetch_regulation_info`) a judikatura NS, NSS, ÚS, obecných soudů a ISIR (`search_decisions`, `fetch_decision`, `search_by_case_number`);
- **lawgpt** – znění předpisů a paragrafů (`get_law`, `get_paragraph`, `get_law_text`), judikatura k ustanovení (`find_judgments_by_provision`), vyhledávání (`search_judgments`) a kontrola tvrzení (`fact_check_czech_law_claim`);
- **Ansvar** (je-li připojen) – předpisy EU a jejich ustanovení; **Sagasu** – rejstříky (identita stran, zastoupení, insolvence) a kalkulačky (úrok z prodlení, soudní poplatek, odměna advokáta);
- oficiální weby (e-Sbírka, EUR-Lex, psp.cz – důvodové zprávy, nalus.usoud.cz, nsoud.cz, nssoud.cz) jen k doplnění, pokud konektor pramen nevrátí.

Komentářovou literaturu tyto zdroje neobsahují. Komentář dodaný uživatelem (PDF, výňatek) použij jako navigaci a odkazy v něm ověř načtením pramene. Otevřené komentáře sestavené s pomocí AI (např. Open Commentary) smějí sloužit jen k orientaci, nikdy jako citovaná opora.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán; existence konektoru sama nedokládá funkční rešerši. Rozliš prázdné výsledky, odmítnutý přístup, nedostupný nástroj a neúplný obsah. Identický neúspěšný požadavek neopakuj bez změny; zkus věcně odůvodněnou alternativu (jiný konektor, jiný index, jiná formulace), pak přesně označ mezeru. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením. Identifikátory, spisové značky a ECLI přebírej jen z odpovědí nástrojů.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a příloh zpřístupněných uživatelem v aplikaci; právní tvrzení v nich nejsou nezávisle ověřeným právem. Identitu stran a zastoupení ověř v rejstříku (Sagasu). Chybějící skutkový doklad si vyžádej jako podklad do aplikace a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v prameni. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v Salvii a lawgpt. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. Používej dostupné oborové, soudní a časové filtry podle jejich skutečného významu. V Salvii volí index soudu parametr `idx` (`ns`, `nss`, `us`, `justice`, `isir`); u obecných otázek prohledej více indexů. Komentář, literatura či vzor dodaný uživatelem slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením pramene.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Projdi pokračování cílených výsledků, pokud je nativní nástroj zpřístupňuje, a prověř relevantní související i navazující dokumenty. Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf obě cesty:

1. **Salvia s filtrem na ustanovení:** `search_decisions` s `reg_num`/`reg_year`/`reg_par` přes indexy `ns`, `us` a podle povahy věci `justice` (správní věci `nss`). Jednou bez dotazu (seznam rozhodnutí citujících ustanovení, nejnovější první), jednou s krátkým dotazem (2–5 slov, právní pojem + klíčový skutkový znak) v režimu hybrid či knn. Pro novou úpravu přidej `date_from`.
2. **lawgpt:** `find_judgments_by_provision` k témuž paragrafu; výsledky porovnej se Salvií a sjednoť podle ECLI.
3. **Citační graf:** u nosného rozhodnutí načti `fetch_decision` a projdi `citedBy` o 1–2 kroky k nejnovějšímu zopakování právní věty; `regulations[]` použij jako další filtr.
4. **Třídění kandidátů:**
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (bm25 dotaz „velký senát <právní pojem>“ a řazení podle data). Starší rozhodnutí použij jen, když ho sjednocující rozhodnutí přejímá; jinak ho označ jako překonané a uveď data obou. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované ve Sbírce soudních rozhodnutí a stanovisek má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí k jinému znění paragrafu použij jen po ověření, že se pravidlo věcně nezměnilo.
5. Ve zdrojovém přehledu u každého judikátu uveď, zda pochází z vazby na paragraf, z citačního grafu, nebo z fulltextu. Vrací-li vazba nulu, uveď to a pokračuj fulltextem.
6. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Takovou dílčí otázku odpověz samostatně podle zákona a další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti (Salvia `fetch_regulation_text`, lawgpt `get_paragraph`/`get_law_text`) úplný text použitého ustanovení v dané verzi, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v Salvii a lawgpt relevantní pozdější, překonávající a nepříznivou judikaturu. Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástroje, nikoli o tvrzení, že aplikace provedla neexistující automatickou certifikaci. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení pramene.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí (Salvia, index `ns`/`nss`); obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej z odpovědí nástrojů nebo oficiálních webů; nesestavuj neověřené URL a neuváděj odkaz, který jsi neotevřel. Ve výstupu použij nástrojem vrácený uživatelský odkaz a přesnou právní citaci, nikoli interní ID či technickou adresu. Pokud uživatelský odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revize či kontrolu, pokud neproběhly dostupnými nástroji aplikace.

Zkontroluj všechny požadované artefakty. Označ pracovní, neúplný či k revizi určený výstup pravdivě. Uložení, odeslání, doručení, podpis a podání jsou odlišné stavy; žádný nepředstírej. Bez výslovného pokynu nic neposílej ani nepodávej. Nedodané části a neověřené rozhodné zdroje nesmějí být skryty prohlášením „hotovo“ nebo „vše ověřeno“.

## Oborové otázky a požadované výstupy

## Fáze, rozhodnutí a nejbližší úkon

Nejprve zjisti klienta, účastníky, zastoupení, soud, typ a fázi řízení, požadovanou ochranu a všechny napadené výroky. Z podkladů odděl datum vyhotovení, vyhlášení, dodání do schránky, právně účinného doručení, právní moci a vykonatelnosti. Komu a jak bylo doručováno, byl ustanoven zástupce, je k dispozici úplná doručenka a poučení? Lhůtu nepočítej automaticky od data dokumentu ani vždy od doručení: nejprve vyhledej skutečný zákonný spouštěč.

V připojených pramenech (Salvia, lawgpt) vyhledej občanský soudní řád, zvláštní soudní řízení, soudní poplatky včetně sazebníku, advokátní tarif, elektronické úkony, hromadné řízení, soudy a soudce, mediaci, výkon a odpovědnost veřejné moci. Podle povahy sporu přidej hmotný zákon a přeshraniční instrument. Prověř přechodná pravidla podle zahájení řízení i konkrétního úkonu, nikoli jen dnešní verzi.

## Podmínky řízení a volba prostředku

Odděl pravomoc, věcnou a místní příslušnost, procesní způsobilost, zastoupení, legitimaci a důvodnost. U místní příslušnosti projdi výlučný režim před obecným, případnou volbu a prorogaci. U rozhodčí smlouvy ověř rozsah a okamžik námitky. U cizího prvku nepřejdi přímo k tuzemskému obecnému soudu. Prověř litispendenci, rozhodnutou věc, podjatost a zákonné obsazení soudu.

Porovnej žalobu na plnění, určení nebo jiný druh ochrany, platební rozkaz, elektronický platební rozkaz a hromadné řízení. Výši nároku nepovažuj bez načteného pravidla za limit formulářového řízení. U určovací žaloby konkrétně vysvětli právní zájem a vztah k žalobě na plnění. U předžalobní výzvy ověř obsah, adresu, odeslání, interval a možné výjimky nákladového následku. Samostatně posuď promlčení, zajištění důkazu, předběžné opatření, jeho jistotu a odpovědnost za újmu.

## Podání, doručování a dokazování

Žaloba musí spojit rozhodující skutky, jednotlivé nároky a důkazy s určitým vykonatelným petitem. Rozliš hlavní, eventuální a alternativní návrh. U platební povinnosti uveď konkrétní příslušenství a počátek i délku plnění odpovídající požadovanému rozhodnutí; neurčité jak stanoví soud není hotový petit. U nepeněžité povinnosti přesně urč adresáta, předmět, rozsah a čas. Kontroluj změnu, zpětvzetí, vzájemný návrh, započtení a procesní nástupnictví podle jejich vlastních pravidel.

Pro každý způsob podání vyhledej formu, podpis, doplnění, příslušného příjemce a okamžik zachování lhůty. Pro fikci doručení a konec lhůty samostatně prověř pracovní dny, svátky, vyloučení fikce, neúčinnost a případnou nápravu. Předlož řetězec právní událost–počátek–běh–konec–způsob včasného úkonu. Neznámé doručení nevyřeš vymyšleným datem.

Zmapuj povinnost tvrzení a důkazní břemeno podle konkrétního titulu, domněnek a ochranných pravidel, nikoli sloganem kdo tvrdí, prokazuje. Prověř koncentraci, poučení, přípravné a první jednání, výjimky novot a návrhy na doplnění. Rozliš soukromou a veřejnou listinu, výslech svědka a účastníka, odborné vyjádření a znalecký posudek, soukromý posudek s potřebnou doložkou, ohledání a nahrávku s testem přípustnosti. Opomenutý důkaz nebo překvapivý závěr konkrétně spoj s dopadem na obranu.

## Rozhodnutí a opravné prostředky

Platební rozkaz, rozsudek pro uznání a pro zmeškání kontroluj odděleně. U kvalifikované výzvy prověř doručení, poučení, obsah reakce a překážky. U zmeškání odděl odvolání proti vadným předpokladům od návrhu na zrušení pro omluvitelný důvod; jejich lhůty a účinky neslučuj. Prověř smír, přerušení, zastavení, opravu a doplnění rozhodnutí.

U odvolání zjisti subjektivní i objektivní přípustnost, rozsah, důvody, novoty, vázanost, odkladný účinek a návrh na změnu či zrušení. Bagatelní výluku, poučení a zvláštní režim vždy načti. U dovolání odděl právní otázku, závislost napadeného rozhodnutí na jejím řešení, konkrétní variantu přípustnosti a dovolací důvod. Připoj skutečně ověřené srovnání s rozhodovací praxí; skutkový nesouhlas nevydávej za právní otázku. Prověř výluky, povinné zastoupení, lhůtu, doplnění a odklad.

U obnovy, zmatečnosti, ústavní ochrany a průtahů ověř samostatné důvody, legitimaci, lhůty a vyčerpání prostředků. Zvaž návrh na určení lhůty a odpovědnost státu odděleně. U nesporného, rodinného, pracovního, spotřebitelského a insolvenčního sporu nepřenášej obecná pravidla bez zvláštní kontroly.

## Náklady a hotový dokument

Nejprve rozhodni nákladový základ: úspěch, procesní zavinění, výzva, úvaha soudu, moderace, náklady státu a nezastoupeného účastníka. Pak spočti každý úkon podle jeho data, tarifní hodnoty, sazby, rozsahu, paušálu, cestovného, času a podmínek DPH. Pro každý samostatný návrh ověř poplatek, osvobození, splatnost, následky neplacení a vrácení; jistotu veď zvlášť. Historické příklady částek nejsou aktuální sazebník.

Dodej požadované podání, přílohový seznam, výpočet a strategii s protiargumenty, nikoli pouze osnovu. U přípravy jednání připoj pořadí důkazů, reakce na námitky a praxi skutečně identifikovaného senátu, je-li zadána. Při převodu dokumentu ověř skutečnou funkčnost odkazů v souboru; vzhled citace nenahrazuje hyperlink. Připravený dokument, odeslání a podání soudu označ jako rozdílné stavy.
