---
uuid: 4161bc8f-7865-4571-86c7-2d805a98a43e
name: korporatni-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Korporátní právo ČR"
    summary: "Založení a fungování s.r.o. a a.s. - valná hromada, převod podílu, odpovědnost jednatelů, akcionářské dohody, rozdělení zisku, obchodní rejstřík, skuteční majitelé, přeměny, likvidace."
    examplePrompts:
      - "Investor vstupuje do s.r.o. se třetinovým podílem a chce ochranu proti přehlasování. Jak nastavit společenskou smlouvu a dohodu společníků?"
      - "Jednatel uzavřel smlouvu bez souhlasu valné hromady, který vyžaduje společenská smlouva. Je smlouva platná a kdo odpovídá?"
      - "Připrav postup převodu obchodního podílu na třetí osobu včetně zápisu do rejstříku."
  en:
    displayName: "Czech Corporate Law"
    summary: "Formation and operation of s.r.o. and a.s. - general meetings, share transfers, directors' liability, shareholder agreements, profit distribution, commercial register, beneficial owners, transformations, liquidation."
    examplePrompts:
      - "An investor joins an s.r.o. with a one-third share and wants protection against being outvoted. How to set up the articles and the shareholders' agreement?"
      - "A director signed a contract without the general meeting's consent required by the articles. Is the contract valid and who is liable?"
      - "Prepare the procedure for transferring a share to a third party including the register filing."
  sk:
    displayName: "Korporátne právo ČR"
    summary: "Založenie a fungovanie českej s.r.o. a a.s. - valné zhromaždenie, prevod podielu, zodpovednosť konateľov, akcionárske dohody, rozdelenie zisku, obchodný register, koneční užívatelia výhod, premeny, likvidácia."
    examplePrompts:
      - "Investor vstupuje do s.r.o. s tretinovým podielom a chce ochranu proti prehlasovaniu. Ako nastaviť spoločenskú zmluvu a dohodu spoločníkov?"
      - "Konateľ uzavrel zmluvu bez súhlasu valného zhromaždenia, ktorý vyžaduje spoločenská zmluva. Je zmluva platná a kto zodpovedá?"
      - "Priprav postup prevodu obchodného podielu na tretiu osobu vrátane zápisu do registra."
description: 'Použij pro obchodní korporace: s.r.o., a.s., družstva, založení, společenské smlouvy a stanovy, kapitál, podíly a akcie, převody a zástavy, valné hromady a per rollam, orgány, péči řádného hospodáře, střet zájmů, odměňování, odpovědnost při úpadku, zisk, dohody společníků, koncerny, přeměny, likvidaci, veřejný rejstřík a skutečné majitele.Právní rešerše přes konektory Salvia a lawgpt.'
---

<!-- Upraveno z pluginu korporatni-pravo (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Korporátní právo ČR

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

## Klient, společnost a podklady

Urči, zda klientem je společnost, většinový nebo menšinový společník, investor, člen orgánu, věřitel či nabyvatel podílu. Nezaměňuj jejich zájmy. Z dodaných listin zjisti právní formu, časovou osu a skutečný stav společnosti ke každému úkonu. Vyžádej potřebný výpis, úplné zakladatelské dokumenty, seznam společníků, dohody, zápisy orgánů, smlouvy o výkonu funkce a účetní podklady. Výpis nenahrazuje obsah stanov; stará smlouva nedokládá nynější jednající osobu. Chybějící rejstříkové či insolvenční podklady označ, neprováděj externí průzkum a nepředstírej jejich obsah v právní databázi.

## Mapa nativní rešerše

V připojených pramenech (Salvia, lawgpt) vyhledej podle otázky zákon o obchodních korporacích, občanský zákoník, úpravu veřejných rejstříků, evidence skutečných majitelů, přeměn, notářství, zvláštních soudních řízení, insolvence a živností. Názvy jsou vyhledávací vodítka, nikoli předem potvrzená působnost. Odděl znění rozhodné pro vznik vztahu, rozhodnutí orgánu, právní jednání, výplatu a soudní či rejstříkový úkon. U historické judikatury prověř, zda její závěr přežil změnu úpravy.

## Kompetence, hlasování a jednání

Kdo má o zamýšleném kroku rozhodnout a na jakém právním či smluvním základě? Jaké jsou podmínky svolání, pořadu jednání, zastoupení, usnášeníschopnosti a hlasování? Z jaké množiny hlasů se počítá většina, kdo nesmí hlasovat a lze pravidlo změnit stanovami? Vyhledej formu usnesení, nutnost notářského osvědčení, souhlasy dotčených osob a pravidla per rollam. Vyhodnoť protest, neplatnost, legitimaci, lhůty a ochranu třetích osob podle konkrétního rozhodnutí.

U jednání za společnost odděl způsob zastupování, prokuru, překročení oprávnění, střet zájmů a dodatečné schválení. Je souhlas vyžadován zákonem, nebo jde o vnitřní omezení? Ověř odlišné následky absence; nezaměňuj oba režimy. Prověř zvláštní formu jednání jednočlenné společnosti se společníkem. Menšinovou ochranu posuzuj podle hlasovacích práv, druhů podílů a konkrétních vet, nikoli jen poměru kapitálu.

## Podíly, orgány a odpovědnost

U převodu nebo přechodu podílu ověř omezení, souhlasy, předkupní práva, formu a okamžiky účinků mezi stranami, vůči společnosti a třetím osobám. Rozliš převod na společníka a jinou osobu, dědění, zastavení, kmenový list, akcie, uvolněný a vypořádací podíl, zánik účasti i vyloučení. U dohody společníků zkoumej, koho konkrétně zavazuje, co musí navazovat ve stanovách a jak zajistit drag along, tag along, předkupní mechanismus či řešení patu.

U členů orgánů prověř informovanost, loajalitu, podnikatelský úsudek, důkazní břemeno, střet zájmů, zákaz konkurence a podmínky výkonu funkce. Jak vzniká nárok na odměnu a jaký následek má chybějící schválení? Odděl odpovědnost, ručení, vyloučení z funkce, insolvenční povinnosti, doplnění majetku a pojistné krytí D&O. Obranu nepodkládej dodatečně vymyšleným rozhodovacím procesem; určuj, které informace měl člen skutečně k dispozici.

## Kapitál, zisk a životní cyklus

Prověř vklady, jejich správu, nepeněžité ocenění, příplatky, vracení prostředků a změny kapitálu. U zisku odděl rozhodnutí o rozdělení, rozhodnutí o výplatě a skutečnou platbu. Pro každou fázi zjisti účetní základ, bilanční a likviditní podmínky, příslušný orgán a potřebnou aktualizaci podkladů. Kladné vlastní zdroje nenahrazují schopnost hradit splatné dluhy. Trvání či zánik nároku odvozuj od skutečné překážky výplaty; administrativní prodlevu nezaměňuj s insolvenční překážkou. Dopad evidence skutečných majitelů posuď samostatně.

U založení ověř název, předmět činnosti, oprávnění, formu a rejstříkové přílohy. U změn, koncernu, squeeze-out, fúze, rozdělení, převodu jmění, změny právní formy a přeshraniční přeměny zjisti projekt, ocenění, informační povinnosti a ochranu společníků či věřitelů. U zrušení a likvidace prověř likvidátora, výzvy, vypořádání, konečnou zprávu a výmaz. Nezaměňuj založení, vznik, zápis změny a její hmotněprávní účinky.

## Použitelný výstup

Dodej závěr pro klientovu stranu, matici kdo rozhoduje–jakou většinou–v jaké formě–co se zapisuje, harmonogram a seznam nezbytných listin. Pokud jsou požadovány smlouvy, stanovy či usnesení, napiš konkrétní úplné znění včetně návazných mechanismů, nikoli jen doporučení. Prověř přípustné omezení odpovědnosti, ekonomické a daňové varianty z doložených vstupů. U sporu připoj vykonatelný návrh, důkazní plán, náklady a nejsilnější protiargument. Nativní judikaturu hledej zejména k neplatnosti usnesení, dispozitivnosti, péči orgánů, převodům, zisku a rejstříkovým požadavkům; výběr senátu ověř podle skutečných rozhodnutí, nikoli podle přednastavené značky.
