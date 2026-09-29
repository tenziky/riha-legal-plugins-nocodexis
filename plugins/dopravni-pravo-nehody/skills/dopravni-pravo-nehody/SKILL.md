---
uuid: 95b3ce6d-ee08-44bc-82fc-e43edd6308b9
name: dopravni-pravo-nehody
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dopravní právo a nehody ČR"
    summary: "Odpovědnost a náhrada újmy z dopravní nehody, pojistné plnění z povinného ručení, dopravní přestupky a bodový systém, zadržení řidičského průkazu, trestné činy v dopravě, dopravci a cestující."
    examplePrompts:
      - "Klientovi do auta narazil řidič, který od nehody ujel. Kdo zaplatí škodu a jaké nároky uplatnit?"
      - "Řidiči byl zadržen řidičský průkaz po naměření 1,2 promile. Co mu hrozí a jak postupovat v prvních dnech?"
      - "Pojišťovna viníka krátí náhradu za opravu o amortizaci a odmítá náhradní vozidlo. Je to v souladu s judikaturou?"
  en:
    displayName: "Czech Traffic Law and Accidents"
    summary: "Accident liability and compensation, motor insurance claims, traffic offences and the points system, licence suspension, traffic crimes, carriers and passengers."
    examplePrompts:
      - "A hit-and-run driver crashed into my client's car. Who pays the damage and which claims to raise?"
      - "A driver's licence was seized after a reading of 1.2 per mille. What does he face and how to proceed in the first days?"
      - "The at-fault party's insurer deducts depreciation from repair costs and refuses a replacement car. Is that consistent with case law?"
  sk:
    displayName: "Dopravné právo a nehody ČR"
    summary: "Zodpovednosť a náhrada ujmy z dopravnej nehody v ČR, poistné plnenie z povinného zmluvného poistenia, dopravné priestupky a bodový systém, zadržanie vodičského preukazu, trestné činy v doprave, dopravcovia a cestujúci."
    examplePrompts:
      - "Klientovi do auta narazil vodič, ktorý od nehody ušiel. Kto zaplatí škodu a aké nároky uplatniť?"
      - "Vodičovi bol zadržaný vodičský preukaz po nameraní 1,2 promile. Čo mu hrozí a ako postupovať v prvých dňoch?"
      - "Poisťovňa vinníka kráti náhradu za opravu o amortizáciu a odmieta náhradné vozidlo. Je to v súlade s judikatúrou?"
description: Použij pro dopravní nehody, náhradu újmy, povinné ručení a regres, dopravní přestupky a trestné činy, řidičská oprávnění a body, provoz vozidel, komunikace, taxislužbu a nákladní dopravu, CMR a práva cestujících.Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu dopravni-pravo-nehody (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Dopravní právo a nehody ČR

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

## Oborový postup: dopravní události a přeprava

### Role a paralelní větve
Nejprve odděl řidiče, provozovatele, vlastníka, poškozeného, chodce, cyklistu, cestujícího, dopravce a pojistitele. Zjisti klientův cíl a skutečný stav přestupkového, trestního, pojistného a civilního řízení. Jedna událost není jeden nárok s jedinou lhůtou. V připojených pramenech (Salvia, lawgpt) ověř rozhodné znění silničních, přestupkových, občanských, trestních a pojistných pravidel včetně nástupnické úpravy povinného ručení. U trestání prověř časové použití a případnou příznivější úpravu; sazby, body a limity nedoplňuj z paměti.

### Událost a důkazy
Z podkladů sestav přesný průběh nehody, datum a místo, vozidla, pojištění, zranění, okolnosti komunikace a stav zahájených řízení. Odděl měřenou rychlost či hladinu látky, odborný závěr a pouhé tvrzení. Vyžádej záznam o nehodě, policejní listiny, fotografie, svědky, dostupné záznamy, lékařské podklady a oznámení pojistiteli. U technických měření prověř potřebné ověření přístroje, obsluhu, odchylky a návaznost znaleckého posouzení.

V nativních pramenech zjisti povinnosti účastníka na místě, přivolání policie, poskytnutí pomoci, výměnu údajů, zachování důkazů a podrobení se zákonnému vyšetření. Nevyvozuj automaticky trestný čin z každého porušení. Nenavrhuj únik před kontrolou, nepravdivou identifikaci řidiče ani dodatečné zkreslení děje. Uznání viny v listině a právní odpovědnost zkoumej samostatně.

### Odpovědnost a peněžní nároky
Pro každého potenciálně odpovědného ověř vlastní titul: zvláštní povahu provozu, zaviněné jednání, užití bez souhlasu, střet provozů, závadu ve sjízdnosti nebo přepravní vztah. Zjisti liberační důvody, míru účasti, příčinnou souvislost a spoluúčast poškozeného; porušení povinnosti nepřepočítej bez odůvodnění na mechanické procento krácení.

Ke každé újmě přiřaď vlastní právní základ, období a důkaz. Rozliš opravu, obvyklou cenu, totální škodu, hodnotu zbytku, znehodnocení, odtah, náhradní vozidlo, znalecké náklady a ušlý zisk. Amortizaci a délku náhradního vozidla zkoumej podle konkrétního případu a ověřené judikatury. U zdraví odděl bolest, ztížení uplatnění, péči a léčbu, pracovní neschopnost, následnou ztrátu výdělku a důchodu, duševní útrapy, pohřeb a výživu pozůstalých. Metodiku soudu dostupnou v připojených pramenech (Salvia, lawgpt) nepředstavuj jako závazný sazebník.

Při dílčím plnění ukaž základ nároku, právně odůvodněné krácení a až potom odečet skutečně přijatých peněz. Platbu jednoho subjektu nezapočítej duplicitně. Úroky, promlčení a oznámení vůči škůdci, pojistiteli a případnému garančnímu subjektu posuzuj odděleně.

### Pojištění a regres
Prověř přímý nárok, pojistnou událost, rozsah a limit krytí, výluky, šetření, splatnost, úrok a potřebnou součinnost. U nezjištěného či nepojištěného vozidla ověř podmínky garančního plnění a spoluúčasti. Odděl povinné ručení a havarijní pojištění. Regres zkoumej podle konkrétního důvodu, příčinné souvislosti, osoby a případných mezí; alkohol, nehlášení či technickou vadu nepovažuj bez načtení pravidla za univerzální regres. Zahrň nepojištěný provoz a příspěvky do garančního systému.

### Přestupky, trestní řízení a oprávnění
U přestupku určuj skutkovou podstatu, sankci, bodový následek, důkazní břemeno a promlčení. Rozliš příkaz na místě, písemný příkaz, odpor, řádné řízení, odvolání a soudní přezkum; jejich následky a rizika změny sankce ověř samostatně. U odpovědnosti provozovatele zjisti podmínky subsidiárního postupu, výzvu a skutečný pokus zjistit řidiče.

U řidičského oprávnění odliš zadržení dokladu, zákaz činnosti, záznam bodů, pozbytí a vrácení oprávnění. Prověř započtení doby, námitky proti bodům, odečty, školení, přezkoušení a zdravotní či psychologické požadavky. Profesní dopad na zaměstnání nebo živnost vycházej z klientových podkladů.

Trestně zkoumej nedbalostní újmu a usmrcení, důležitou povinnost, stav vylučující způsobilost, neposkytnutí pomoci, maření a obecné ohrožení. Odděl obhajobu od procesních práv poškozeného, adhezního nároku a zajištění. Prověř odklony a dohodu, náhradu újmy, souběh a zákaz dvojího postihu bez automatické analogie mezi větvemi.

### Doprava, vozidla a výstup
U dopravce prověř oprávnění, taxislužbu, mezinárodní dopravu, doby řízení a odpočinku, tachografy a odpovědnost řidiče i dopravce. U nákladní přepravy zjisti působnost CMR, limity, reklamace, promlčení, výluky a rozhodné právo. U letecké dopravy odliš zpoždění, zrušení, odepření nástupu, péči a mimořádné okolnosti. U vozidla zahrň převod, registraci, technickou způsobilost, leasing a ukončení provozu.

Dodej mapu řízení a nároků s adresátem, ověřenou lhůtou a důkazy. Požadovanou výzvu, obranu či petit skutečně sepiš; připoj výpočet náhrady a zvlášť náklady řízení, alternativu dohody a seznam chybějících podkladů.
