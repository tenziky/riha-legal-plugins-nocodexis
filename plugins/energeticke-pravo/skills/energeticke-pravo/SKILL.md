---
uuid: 4e1b642c-1332-469b-8d06-72075b71159d
name: energeticke-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Energetické právo ČR"
    summary: "Licence a regulace ERÚ, smlouvy o dodávce elektřiny a plynu a změna dodavatele, podpora a povolování OZE, komunitní energetika a sdílení, připojení k síti, cenová regulace a spory, teplárenství, energetická náročnost budov."
    examplePrompts:
      - "Dodavatel elektřiny jednostranně zvýšil cenu a klient chce odejít bez sankce. Jaké jsou lhůty a jak správně vypovědět smlouvu?"
      - "Obec chce postavit FVE na střechách škol a sdílet elektřinu mezi budovami. Jaký režim (energetické společenství, sdílení) a jaká povolení?"
      - "Distributor odmítl připojit výrobnu 500 kW pro nedostatek kapacity. Lze se bránit a u koho?"
  en:
    displayName: "Czech Energy Law"
    summary: "Energy Act licences and ERÚ regulation, electricity and gas supply contracts and switching, renewable support and permitting, community energy and self-consumption, grid connection, price regulation and disputes, heat supply, energy performance of buildings."
    examplePrompts:
      - "An electricity supplier unilaterally raised the price and my client wants to leave without penalty. What are the deadlines and how to terminate properly?"
      - "A municipality wants rooftop PV on schools and to share electricity between buildings. Which regime (energy community, sharing) and which permits?"
      - "The distributor refused to connect a 500 kW plant for lack of capacity. Can we challenge it and where?"
  sk:
    displayName: "Energetické právo ČR"
    summary: "Licencie a regulácia ERÚ, zmluvy o dodávke elektriny a plynu a zmena dodávateľa, podpora a povoľovanie OZE, komunitná energetika a zdieľanie, pripojenie do siete, cenová regulácia a spory, teplárenstvo, energetická náročnosť budov."
    examplePrompts:
      - "Dodávateľ elektriny jednostranne zvýšil cenu a klient chce odísť bez sankcie. Aké sú lehoty a ako správne vypovedať zmluvu?"
      - "Obec chce postaviť FVE na strechách škôl a zdieľať elektrinu medzi budovami. Aký režim (energetické spoločenstvo, zdieľanie) a aké povolenia?"
      - "Distribútor odmietol pripojiť výrobňu 500 kW pre nedostatok kapacity. Možno sa brániť a u koho?"
description: Použij pro dodávky elektřiny, plynu a tepla, zákazníky a dodavatele, ukončení a změny smluv, připojení, licence a výrobny, FVE a OZE, podporu, komunitní energetiku a sdílení, akumulaci, teplárenství, PENB, cenovou regulaci, ERÚ a SEI, energetické transakce a spory. Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu energeticke-pravo (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Energetické právo ČR

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

## Oborový postup: energetika

### Komodita, role a časové vrstvy
Urči zákazníka domácnost, podnikatele či obec, výrobce, obchodníka, distributora, provozovatele lokální soustavy, společenství, developera nebo dodavatele tepla. Odděl elektřinu, plyn a teplo, vlastní spotřebu, přetok, akumulaci a agregaci. Ze smluv zjisti sdruženou službu nebo oddělenou dodávku a distribuci, typ produktu, rozhodná oznámení a regulační rok. V připojených pramenech (Salvia, lawgpt) prověř energetický zákon, občanské a spotřebitelské právo, prováděcí předpisy, cenová rozhodnutí a unijní vrstvu. Nenačtené roční ceny nedoplňuj z jiné sezony ani externě.

### Dodávka, cena a ukončení
Zkoumej smluvní náležitosti, fixní a dynamickou cenu, změnu podmínek, povinnost oznámení, předání ceníku, zálohy, měření a vyúčtování. U zprostředkovatele ověř oprávnění, rozsah plné moci a smluvní ochranu. Prověř distanční a mimo provozovnu uzavřený vztah, obecní omezení, předčasné ukončení, dobu neurčitou, prolongaci a dodavatele poslední instance. U reklamace a přerušení či obnovení dodávky zjisti vlastní podmínky a termíny.

Nejprve odděl zákonné bezsankční ukončení od porušení smlouvy. Teprve v druhé větvi zkoumej platnost pokuty, zákonný strop a případnou moderaci. Ověř konkrétní spouštěč a délku práva ukončit při změně ceny; historické lhůty nejsou instrukcí pro nový případ. Prokázanou nulovou škodu, neznámou škodu a doloženou škodu drž jako rozdílné kategorie také v závěru a klientské výzvě. Neznámou škodu nepřepisuj na absenci škody. Před navržením ukončení popiš kontinuitu nové dodávky a možné riziko přerušení.

### Připojení a majetkový rámec
Prověř žádost, potřebné podklady, posouzení kapacity, smlouvu, rezervovaný příkon či výkon, podíl na nákladech, měření a termíny. U odmítnutí zjisti povinnost odůvodnění, dostupné alternativy omezení výkonu, akumulace či provozu bez přetoků a příslušný prostředek ochrany. Odděl mikrozdroj, změnu parametrů a novou výrobnu; limity výkonu nikdy nepředpokládej. Zahrň přeložky, vstup na pozemek, ochranná pásma, věcná práva, náhrady a spory o uzavření smlouvy.

### Výroba, podpora a povolování
Ověř potřebu licence a výjimky, odbornou způsobilost, vztah k výrobně, změnu držitele, registraci, revize, bezpečnost a pojištění. Soukromou FVE nepovažuj automaticky za osvobozenou od všech povolení. Prověř stavební, územní a environmentální vrstvu, EIA, zemědělskou půdu a agrivoltaiku, památky, hluk, požární podmínky, přístup k pozemku a zrychlené povolovací mechanismy.

U podpory zjisti formu, vznik nároku, rok uvedení do provozu, délku, měření, výkazy, cenové rozhodnutí, změnu vlastníka, modernizaci a záruky původu. Odděl provozní podporu, investiční dotaci a překompenzaci. Zkoumej odnětí, snížení, kontrolu přiměřenosti, solární odvod, veřejnou podporu a legitimní očekávání podle konkrétního zdroje a období. Dotaci nepovažuj za přislíbenou nebo vyplacenou bez podkladu. Historické krizové stropy, odvody či tarif posuzuj jen v jejich časové působnosti.

### Sdílení, teplo a budovy
U energetického společenství ověř přípustnou formu, členy, účel, kontrolu, registraci a pravidla výstupu. U sdílení prověř datové centrum, skupinu, alokaci, odběrná místa, územní omezení, měření, poplatky a smlouvy. U SVJ nebo obce navazuj na souhlasy, rozúčtování, veřejné zakázky, koncesi a veřejnou podporu. Právní přípustnost sdílení není důkaz jeho technického spuštění.

U tepla zkoumej smlouvu, měření, kalkulaci a věcné usměrňování ceny. Odpojení od centrálního zásobování posuzuj podle konkrétních zákonných podmínek, potřebných souhlasů a nákladů. Zahrň rozúčtování v domě, PENB, audit a posudek, energetického specialistu, energetickou koncepci, ESCO/EPC, tepelná čerpadla a související hluk či dotace.

### Pravomoc a nároky
Každý požadavek kvalifikuj samostatně: splnění smluvní povinnosti, existence, trvání či zánik vztahu, negativní určení jednotlivého dluhu, připojení, škoda nebo veřejnoprávní licence a sankce. Z úplného textu ověř rozsah pravomoci ERÚ; negativní určení pokuty nezaměňuj s určením zániku smluvního vztahu. Soudní přezkum a procesní předpis odvoď od povahy rozhodnutí, nikoli názvu orgánu.

U dohledu ERÚ a SEI prověř kontrolu, povinnosti, skutkovou podstatu, sankci, nápravu, opravný prostředek a lhůty. Podle věci zahrň ÚOHS, REMIT, manipulaci s trhem, OTE a odpovědnost za odchylku. U neoprávněného odběru ověř skutečný základ a způsob výpočtu náhrady, ne pouze paušální tvrzení dodavatele.

### Transakce a výstupy
U koupě výrobny, PPA, výkupu přetoků, údržby, EPC, pachtu a financování vytvoř mapu licence, podpory, pozemků, připojení, dotací a převoditelnosti smluv. Vymez cenu, profil dodávky, regulační změnu, záruky původu, odpovědnost, step-in, zástavy a obnovu pozemku. Ekonomické a daňové varianty opři o uvedené vstupy.

Dodej konkrétní návrh nebo smluvní znění, tabulku nárok–pramen–adresát–lhůta–důkaz, náklady řízení odděleně od energetického vyúčtování a plán nepřerušeného provozu. Všechny právní a judikatorní opory získávej výhradně připojenými prameny (Salvia, lawgpt).
