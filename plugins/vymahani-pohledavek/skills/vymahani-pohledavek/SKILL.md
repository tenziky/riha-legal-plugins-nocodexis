---
uuid: b8def4ff-b6cd-4650-8e27-5baeb96c8a6e
name: vymahani-pohledavek
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Vymáhání pohledávek ČR"
    summary: "Od promlčení a předžalobní výzvy přes platební rozkaz a žalobu po exekuci - příslušenství, náklady, poplatky, insolvenční křižovatka."
    examplePrompts:
      - "Dlužník nezaplatil tři faktury po 80 000 Kč z roku 2024. Navrhni postup vymáhání a spočítej, co lze požadovat."
      - "Přišel odpor proti elektronickému platebnímu rozkazu. Co teď a jaké lhůty běží?"
      - "Máme pravomocný rozsudek, dlužník neplatí. Jak podat exekuční návrh a co když je v insolvenci?"
  en:
    displayName: "Czech Debt Recovery"
    summary: "From limitation and pre-action notice through payment orders and litigation to enforcement - interest, costs, fees, insolvency crossover."
    examplePrompts:
      - "A debtor has not paid three invoices of CZK 80,000 from 2024. Propose the recovery path and calculate what can be claimed."
      - "An objection against the electronic payment order arrived. What now and which deadlines run?"
      - "We have a final judgment and the debtor does not pay. How to file for enforcement, and what if they are insolvent?"
  sk:
    displayName: "Vymáhanie pohľadávok ČR"
    summary: "Od premlčania a predžalobnej výzvy cez platobný rozkaz a žalobu po exekúciu v ČR - príslušenstvo, trovy, poplatky, insolvenčná križovatka."
    examplePrompts:
      - "Dlžník nezaplatil tri faktúry po 80 000 Kč z roku 2024. Navrhni postup vymáhania a vypočítaj, čo možno požadovať."
      - "Prišiel odpor proti elektronickému platobnému rozkazu. Čo teraz a aké lehoty bežia?"
      - "Máme právoplatný rozsudok, dlžník neplatí. Ako podať exekučný návrh a čo ak je v insolvencii?"
description: 'Use for Czech debt recovery and debtor defence: claim verification, interest and limitation, demands, payment orders, litigation, security and settlements, enforcement, insolvency intersections and economic recovery assessment.Právní rešerše přes konektory Salvia a lawgpt.'
---

<!-- Upraveno z pluginu vymahani-pohledavek (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Vymáhání pohledávek

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

## Oborový postup: vymáhání pohledávek

### Nárok, klient a naléhavost

Urči, zda klient pohledávku uplatňuje, brání se jí nebo přebírá portfolio. Zjisti skutečného věřitele a dlužníka, právní důvod, splatnost, zajištění a nejbližší riziko promlčení či procesní lhůty. Předžalobní postup nesmí mechanicky odsunout nezbytný urgentní ochranný krok.

Z dodaných smluv, objednávek, předání, komunikace a plateb sestav položkový přehled. Faktura sama nemusí prokazovat vznik a splnění smlouvy. Rozliš jistinu, úrok, úrok z prodlení, smluvní pokutu, paušální náklady a škodu. U každé položky dolož titul, částku, splatnost a důkaz. Zkontroluj postoupení, oznámení, částečné úhrady, jejich započtení, uznání, zápočet a protinároky; nevytvářej nulový zůstatek z chybějících údajů.

### Rozhodné právo a výpočty

V připojených pramenech (Salvia, lawgpt) ověř právní režim závazku, časovou verzi, ochranu spotřebitele, případné zahraniční právo a omezení příslušenství. U promlčení rozliš splatnost a okamžik možné první žaloby, subjektivní a objektivní běh, uznání, rozhodnutí, smluvní ujednání, stavění a obnovení běhu. Námitka promlčení, prekluze a zánik pohledávky nejsou zaměnitelné.

Úrok vypočti z doložené jistiny, skutečného počátku prodlení a ověřeného pravidla sazby. Pokud se sazba odvíjí od referenční hodnoty k určitému okamžiku, určuj právě tento okamžik a ověř, zda se při trvajícím prodlení mění. Nepřeceňuj automaticky sazbu v každém dalším období. Zvláštní režim například výživného posuď samostatně.

Uveď intervaly, počet dnů, zahrnutí nebo nezahrnutí hraničního dne, rozhodný dělitel a mezikroky. Odděl částku vyčíslenou k datu od pokračujícího příslušenství požadovaného do zaplacení. Ověř přípustnost úročení příslušenství a souběhu sankcí. Částka ve výpočtu, skutkovém tvrzení a petitu musí souhlasit.

### Volba postupu

Porovnej předžalobní výzvu, dohodu, uznání a splátky, běžný platební rozkaz, elektronický platební rozkaz, standardní žalobu a případně směnečný, evropský nebo přímo vykonatelný titul. Zvol postup podle doložených předpokladů, očekávané obrany, rychlosti, nákladů a vymahatelnosti. Očekávaný odpor nemusí být právní překážkou rozkazního řízení; ekonomicky však může změnit vhodnost cesty.

U elektronického návrhu ověř aktuální podmínky, formulář, identifikátory, podpis a zvláštní režim vad. Nepřebírej historický hodnotový limit ani předpoklad běžného odstraňování všech vad. Při chybějícím nástroji či formuláři v povoleném prostředí dodej použitelný obsah a konkrétně označ technicky nedokončenou část.

U výzvy zkontroluj adresáta, místo odeslání, obsah a doklad skutečného odeslání či doručení. Podmínky náhrady nákladů rozliš od přípustnosti samotné žaloby. Nákladovou kvalifikaci jednoduché výzvy a plnohodnotného právního úkonu ověř podle skutečného obsahu, nikoli názvu dokumentu.

### Obrana a proces

Podle postoje dlužníka zvaž neexistenci dluhu, vadné plnění, nesplatnost, zaplacení, zápočet, neplatnost, promlčení nebo nepřiměřenou sankci. Každou obranu spoj s důkazem a odpovědí na nejsilnější protiargument. Procesní obrana nesmí být založena na vědomě nepravdivých tvrzeních nebo obstrukci bez právního základu.

U odporu, vyjádření, kvalifikované výzvy, uznání, zmeškání a odvolání ověř konkrétní předpoklady a skutečné doručení. Z pasivity nevyvozuj automaticky jakýkoli požadovaný typ rozsudku. U změny návrhu a přechodu mezi procesními režimy přepočti poplatek a dopad případného nezaplacení.

### Insolvence, výkon a zajištění

Doložený insolvenční stav vyhodnoť podle fáze, typu nároku a relevantních výjimek. Zahájení insolvenčního řízení, rozhodnutí o úpadku a jiná rozhodnutí mohou mít různé účinky. Nesmí vzniknout univerzální tvrzení, že jakákoli insolvenční zmínka zakazuje všechny žaloby. Ověř přihlášku, jiné uplatnění pohledávky, zajištění, pořadí a rozhodnou lhůtu.

Před výkonem ověř existenci titulu, jeho obsah, doručení, právní moc, vykonatelnost a splnění podmínek plnění. Samotný návrh nebo nepravomocná listina není vykonatelným titulem. Odděl oprávněnost výkonu, možný majetek podle dodaných podkladů, zálohy a skutečnou dobytnost; náklady nelze automaticky slíbit v plné výši zpět.

U dohody nebo zajištění formuluj splátky, případné zesplatnění, uznání, ručení, zástavu, notářský souhlas s vykonatelností či směnečné řešení jen po ověření podmínek. Respektuj postavení slabší strany a související kogentní omezení. Zajištění nesmí bez kontroly změnit klientův nárok nebo se stát nechtěným prominutím.

### Výstup

Dodej skutečnou výzvu, žalobu, odpor, návrh nebo dohodu, včetně přesného petitu a soupisu důkazů. Připoj úplný rozpočet všech navržených nároků, poplatků, zastoupení a výkonu, hlavní rizika a variantu čistého ekonomického výnosu. Technické vytvoření formuláře, odeslání a podání uváděj jen jako skutečně provedené stavy.
