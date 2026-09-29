---
uuid: 640c522f-ca14-4392-aa25-a1f5526e2127
name: nahrada-ujmy-odpovednost
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Náhrada újmy a odpovědnost ČR"
    summary: "Obecná a objektivní odpovědnost podle OZ, škoda na věci a čistě ekonomická újma, újma na zdraví a Metodika NS k nemajetkové újmě, usmrcení a sekundární oběti, odpovědnost za výrobek, odpovědnost zaměstnavatelů, profesionálů a státu, příčinná souvislost a spoluzavinění, promlčení, vazba na pojištění a vyčíslení."
    examplePrompts:
      - "Klient utrpěl při pádu na neuklizeném chodníku zlomeninu s trvalými následky. Kdo odpovídá, jak vyčíslit bolestné a ztížení společenského uplatnění podle Metodiky NS a jaké jsou lhůty?"
      - "Manžel klientky zemřel po chybě lékaře. Jaké nároky mají manželka a děti, v jaké výši se přiznávají a jak prokázat příčinnou souvislost?"
      - "Dodavatel software chybou zničil klientovi data a firma přišla o zakázky. Lze žádat ušlý zisk a jak ho prokázat, když smlouva limituje náhradu?"
  en:
    displayName: "Czech Tort & Liability Law"
    summary: "General and strict liability under the Civil Code, property damage and pure economic loss, personal injury and the Supreme Court methodology for non-pecuniary harm, wrongful death and secondary victims, product liability, liability of employers, professionals and public bodies, causation and contributory fault, limitation, insurance and quantification."
    examplePrompts:
      - "My client fractured a bone with permanent consequences after falling on an uncleared pavement. Who is liable, how to quantify pain and loss of amenity under the Supreme Court methodology, and what are the deadlines?"
      - "A client's husband died after a doctor's error. What claims do the wife and children have, in what amounts, and how to prove causation?"
      - "A software vendor's error destroyed a client's data and the company lost contracts. Can lost profit be claimed and proven when the contract caps liability?"
  sk:
    displayName: "Náhrada ujmy a zodpovednosť ČR"
    summary: "Všeobecná a objektívna zodpovednosť podľa OZ, škoda na veci a čisto ekonomická ujma, ujma na zdraví a Metodika NS k nemajetkovej ujme, usmrtenie a sekundárne obete, zodpovednosť za výrobok, zodpovednosť zamestnávateľov, profesionálov a štátu, príčinná súvislosť a spoluzavinenie, premlčanie, väzba na poistenie a vyčíslenie."
    examplePrompts:
      - "Klient utrpel pri páde na neupratanom chodníku zlomeninu s trvalými následkami. Kto zodpovedá, ako vyčísliť bolestné a sťaženie spoločenského uplatnenia podľa Metodiky NS a aké sú lehoty?"
      - "Manžel klientky zomrel po chybe lekára. Aké nároky majú manželka a deti, v akej výške sa priznávajú a ako preukázať príčinnú súvislosť?"
      - "Dodávateľ softvéru chybou zničil klientovi dáta a firma prišla o zákazky. Možno žiadať ušlý zisk a ako ho preukázať, keď zmluva limituje náhradu?"
description: Použij pro smluvní a deliktní odpovědnost, škodu, ušlý zisk, nemajetkovou újmu, zdraví, pozůstalé, kauzalitu, spoluzavinění, limitaci náhrady, odpovědnost provozovatelů, výrobce, profesionálů, zaměstnavatele či státu, promlčení, pojistné a adhezní souvislosti.Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu nahrada-ujmy-odpovednost (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Náhrada újmy a odpovědnost ČR

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

## Role, událost a samostatné nároky

Urči zastupovanou stranu, primárního poškozeného, případné sekundární oběti a každého možného škůdce. Rozliš fyzickou osobu, společnost, zaměstnavatele, provozovatele, profesionála, stát či územní samosprávu. Zapiš konkrétní jednání, smluvní vztah, škodní událost, vznik jednotlivých následků, vědomost o újmě a odpovědné osobě. Rozděl majetkovou škodu, ušlý zisk, zdraví, osobnostní zásah, náklady péče, výdělek, důchod, pozůstalé a vydání obohacení. Každý nárok má vlastní skutkový základ, výpočet, důkazy a časovou kontrolu.

## Titul a nativní rešerše

V připojených pramenech (Salvia, lawgpt) ověř relevantní občanskoprávní odpovědnostní úpravu a přechodná ustanovení. Podle věci přidej pracovní a služební režim, odpovědnost veřejné moci, zdravotní služby, advokacii, notáře, znalce, výrobky, dopravu, myslivost, školy, GDPR, pojištění, trestní a civilní proces. Výčet názvů je mapa k hledání, nikoli předem určená působnost. Odděl porušení zákona, smlouvy, dobrých mravů, preventivní povinnosti a zvláštní skutkovou podstatu. U čistě ekonomické újmy prověř ochranný účel normy nebo jiný vhodný titul; neodvozuj automaticky nárok z jakéhokoli protiprávního jednání.

Pro každý titul zjisti předpoklady, aktivní a pasivní legitimaci, důkazní břemeno, domněnky, liberační důvody a souběh. U pomocníka odděl zaměstnance a samostatnou osobu; u dopravy vlastníka, řidiče a provozovatele. U zvláštních režimů prověř nezletilého a dohled, závod a zvlášť nebezpečný provoz, stavební činnost a pád stavby, zvíře, věc, výrobek, věci převzaté či odložené, ubytování, informaci a odbornou radu. Nezaměňuj podmínky zproštění různých titulů.

## Kauzalita a obrana

Sestav řetězec příčin a následků podle časových úseků a samostatných škodních bloků. Co by nastalo bez jednání škůdce, které alternativní příčiny dokládají podklady a jaký důkazní standard se podle nativně ověřené judikatury použije? U medicíny odděl chybu, dokumentaci, informovaný souhlas, příčinnou souvislost a argument ztráty šance; jejich právní účinky nepředurčuj. Připrav otázky znalci, ne vlastní medicínský závěr.

Úmysl, hrubou a běžnou nedbalost posuzuj odděleně. Absence úmyslu nedokládá běžnou nedbalost; vypořádej známá varování, odborný standard a vědomé vyřazení ochrany. Souhlas poškozeného, falešné alarmy a možnost škodu odvrátit označ za hypotézu, nejsou-li doloženy. U spolupůsobení, více škůdců, solidarity, regresu, moderace a omezení náhrady ověř vlastní podmínky. Stejný následek neodečti jednou z kauzality a znovu ze spoluúčasti. Smluvní cap aplikuj teprve po ověření přípustnosti včetně slabší strany, zavinění a povahy chráněného práva.

## Vyčíslení bez tabulkových zkratek

U věcné škody porovnej náklady opravy, obvyklou hodnotu, zbytky, zhodnocení, pokles ceny po opravě, cenu zvláštní obliby a účelnou náhradu užívání. DPH posuď podle konkrétní možnosti odpočtu, nikoli jen označení plátce. U ušlého zisku odliš obrat, marži a skutečně ušetřené náklady; podklady tvoří zakázky, historie a doložené možnosti. Interval nejistoty vysvětli spornými vstupy, ne vymyšleným procentem. Prověř započítání prospěchu, sociálních dávek a jednotlivých pojistných plnění, daňové důsledky, splatnost a úroky.

U zdraví rozliš bolest, ztížení společenského uplatnění, další nemajetkové následky, léčení, péči blízkých, pomůcky, úpravy bydlení, výdělek během a po neschopnosti, ztrátu na důchodu, bezplatné práce a rentu. V připojených pramenech (Salvia, lawgpt) vyhledej použitelnou Metodiku NS či zvláštní předpis a skutečný právní význam, aktuálnost a podmínky odchylky. Nepřenášej automaticky civilní metodu do pracovního úrazu. Neznámou hodnotu bodu, statistický vstup, ustálení stavu nebo prognózu nenahrazuj pamětí ani externím zdrojem.

U úmrtí a zvlášť závažného ublížení posuď každou blízkou osobu samostatně, vztah, závislost, okolnosti a vlastní důkazy. Přidej pohřební náklady, výživu a případné jiné sekundární újmy bez dvojí kompenzace. Násobek z judikatury nepoužívej bez ověření kontextu a rozhodného období.

## Zvláštní proces a výstup

U státu rozliš nezákonné rozhodnutí, nesprávný postup a délku řízení, potřebu předchozího zrušení či opravných prostředků, správného adresáta předběžného projednání, lhůty a soudní cestu. U profesionála prověř hypotetický výsledek bez pochybení; obecný neúspěch klienta nedokládá odpovědnost. U pojištění nejprve zjisti, zda existuje přímý nárok, jeho zdroj a rozsah; blanketní výluka všech ostatních než motorových pojištění není přípustnou zkratkou.

Připrav výzvu s rozpisem, případný adhezní návrh, žalobu, návrh na zajištění či mezitímní rozhodnutí a nákladový rozpočet. Zkontroluj promlčení každého nároku, splátek a pouze uplatněné části; řízení či jednání s pojistitelem nepovažuj bez pramene za stavení všeho. Narovnání musí výslovně řešit rozsah vypořádání a budoucí zhoršení. Přiznaný nárok slaď s plněním, exekucí a insolvencí. Odevzdej tabulku titul–předpoklad–důkaz–výše–časové riziko a nejsilnější obranu protistrany. Požadovanou klauzuli nebo petit skutečně formuluj, náhradu ani vymahatelnost neslibuj jako jistou.
