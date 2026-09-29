---
uuid: e0293478-596a-4d8c-aae7-0d2289aca509
name: insolvencni-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Insolvenční právo ČR"
    summary: "Insolvenční řízení z pohledu věřitele, dlužníka i správce - přihlášky, přezkum a popření, incidenční spory, oddlužení, konkurs, moratorium, ISIR."
    examplePrompts:
      - "Klient má pohledávku za firmou, na kterou byl dnes prohlášen úpadek. Co musí udělat a do kdy?"
      - "Správce popřel naši pohledávku co do pravosti. Připrav postup a osnovu incidenční žaloby."
      - "Dlužník v oddlužení přestal platit splátky. Hrozí zrušení oddlužení a jak se bránit?"
  en:
    displayName: "Czech Insolvency Law"
    summary: "Czech insolvency proceedings from the creditor, debtor and trustee perspective - claims, review and denial, incidental disputes, debt relief, bankruptcy, moratorium, ISIR."
    examplePrompts:
      - "My client has a receivable against a company declared insolvent today. What must they do and by when?"
      - "The trustee denied our claim as to its existence. Prepare the procedure and outline of the incidental action."
      - "A debtor in debt relief stopped paying. Is cancellation of debt relief imminent and how to defend?"
  sk:
    displayName: "Insolvenčné právo ČR"
    summary: "České insolvenčné konanie z pohľadu veriteľa, dlžníka aj správcu - prihlášky, prieskum a popretie, incidenčné spory, oddlženie, konkurz, moratórium, ISIR."
    examplePrompts:
      - "Klient má pohľadávku voči firme, na ktorú bol dnes vyhlásený úpadok. Čo musí urobiť a dokedy?"
      - "Správca poprel našu pohľadávku čo do pravosti. Priprav postup a osnovu incidenčnej žaloby."
      - "Dlžník v oddlžení prestal platiť splátky. Hrozí zrušenie oddlženia a ako sa brániť?"
description: 'České insolvenční řízení z pozice věřitele, dlužníka, správce, člena orgánu nebo nabyvatele majetku: návrhy, účinky, přihlášky, přezkum, incidenční spory, zpeněžení, konkurs, reorganizace, oddlužení a preventivní restrukturalizace. Zohledňuje přechodná pravidla, správu majetku, odměnu správce a přeshraniční souvislosti.'
---

<!-- Upraveno z pluginu insolvencni-pravo (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Insolvenční právo

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

## Role, stav řízení a zdroj faktů

Urči roli klienta, ekonomický cíl a fázi věci: před návrhem, po zahájení, po rozhodnutí o úpadku, při přezkumu, při řešení úpadku nebo po skončení. Rozliš nezajištěného a zajištěného věřitele, dlužníka, insolvenčního správce, člena orgánu, zaměstnance a zájemce o majetek. Podklady o spisu čerpej z poskytnutých dokumentů a dostupných nativních záznamů; nepředstírej provedení kontroly rejstříku, která neproběhla.

U každého rozhodnutí zaznamenej výrok, datum, zveřejnění, zvláštní doručení, právní moc a případné napadení, změnu či zrušení. Starší zrušené usnesení není aktuálním stavem. Sestav časovou osu a odliš procesní účinek zveřejnění od běhu lhůty závislé na zvláštním doručení. V připojených pramenech (Salvia, lawgpt) vyhledej rozhodná znění a přechodná ustanovení podle jednotlivých událostí; nepoužij jediné dnešní znění pro celé starší řízení.

## Zahájení a účinky

Jaké jsou konkrétní znaky úpadku nebo hrozícího úpadku a kdo je oprávněn podat návrh? U věřitelského návrhu ověř splatnou pohledávku, další věřitele a důkazní požadavky; u dlužníka povinné seznamy, prohlášení, odpovědnost za včasnost a možné konflikty orgánů. Insolvenční návrh nesmí být neodůvodněným prostředkem nátlaku.

Zjisti účinky zahájení a rozhodnutí o úpadku na dispozice s majetkem, splatnost, individuální výkon, probíhající spory, započtení, smlouvy a oprávnění jednat za dlužníka. Rozliš omezení dlužníka, rozsah oprávnění správce a změny podle způsobu řešení úpadku. U zahraničního prvku vyhledej pravomoc, centrum hlavních zájmů, hlavní a vedlejší řízení, uznání a rozhodné právo; sídlo samo nezaměňuj za prokázaný celý test.

## Pohledávky a přezkum

Každý nárok zařaď jako přihlašovaný, za majetkovou podstatou, postavený na roveň, vyloučený či jiný podle ověřených podmínek. Rozliš jistinu a příslušenství, vykonatelnost, podmínku, cizí měnu, dílčí plnění, pořadí a zajištění. Hodnota ocenění zástavy není bez dalšího výší zajištěné pohledávky ani částkou očekávaného výtěžku.

Ověř obsah a formu přihlášky, skutečný důvod a výši, označení zajištění, přílohy, lhůtu a místo doručení. Co lze doplnit nebo změnit, jak se odstraňují vady a kdy hrozí sankce za nadhodnocení? Chybějící důkaz nenahrazuj smyšleným titulem. U dílčích plateb kontroluj zůstatek a vyloučení dvojího uspokojení.

Při přezkumu odděl popření pravosti, výše a pořadí a každého popírajícího: správce, věřitele a dlužníka. Jak se liší jejich oprávnění a účinky v jednotlivých způsobech řešení úpadku, včetně zvláštního přezkumu v oddlužení? Rozhodující je obsah úkonu a jeho včasnost, nikoli jen označení.

## Incidenční spory a majetková podstata

Před každou incidenční žalobou vytvoř matici druhu pohledávky, vykonatelnosti, popírající osoby, směru popření, žalobce a žalovaného. Kdo musí žalovat koho a o čem má znít výrok? Vyhledej samostatně lhůtu, její počátek, návaznost na doručení vyrozumění, případnou ochrannou minimální dobu a požadavky na včasné podání či dojití. Nepřevracej procesní role podle obecné šablony.

U vykonatelné pohledávky rozliš skutkové důvody skutečně uplatněné v předchozím řízení, skutečnosti pouze dříve uplatnitelné a jiné právní posouzení. Jaké omezení platí pro právě tohoto popírajícího a co lze ještě tvrdit či změnit? U věřitelského popření ověř zvláštní obsah, formu, jistotu, účinky a pokračování sporu. Náklady incidenčního řízení neposuzuj paušálně jako nenahraditelné; zjisti zvláštní pravidlo a jeho výjimky.

U vyloučení věci z podstaty dolož vlastnictví, soupis, skutečné doručení vyrozumění a legitimaci proti správci. Ověř lhůtu, ochranu před zpeněžením a výjimky. U odpůrčí žaloby odděl nedostatečné protiplnění, zvýhodnění a úmyslné zkrácení: každý důvod má vlastní skutkové znaky, rozhodné období, vztah osob, břemena a čas pro žalobu. Prověř oprávnění správce, správného odpůrce, předmět vydání a konkrétní hodnotu plnění.

## Způsoby řešení a správa

U konkursu a zajištěného majetku zmapuj pokyny ke správě a zpeněžení, souhlasy, způsob prodeje, střet zájmů a rozvrh. Odděl hrubý výtěžek, náklady správy a zpeněžení, odměnu správce, DPH a čisté uspokojení; limity a základ každé položky ověř pro daný režim, nikoli z uložené tabulky.

U oddlužení zjisti osobní a věcné podmínky, poctivost, příjmový potenciál, vyživovací povinnosti, majetek, obydlí, společný návrh manželů a povinnosti v průběhu. Samotné uplatnění procesního práva nepovažuj za nepoctivost bez konkrétního podkladu. Ověř oprávnění sepisovatele, formuláře, odměnu, rozhodnou dobu a přechodná pravidla, důvody neschválení, zrušení a osvobození i jeho rozsah.

U reorganizace prověř přípustnost, plán, skupiny věřitelů, hlasování, financování, kontroly a ochranu nesouhlasících. Moratorium a preventivní restrukturalizaci odliš od insolvenční reorganizace: vyhledej vlastní podmínky, seznamy, souhlasy, doručování a účinky. Nepředpokládej automatické prodloužení splatnosti nebo zablokování zesplatnění.

U správce řeš oprávnění, ustanovení, nepodjatost, změnu či odvolání, odbornou péči, součinnost, zprávy, odpovědnost, odměnu a výdaje. Zohledni věřitelský orgán, dohled soudu a ekonomickou výhodnost úkonu pro podstatu.

## Povinný výstup

Dodej aktuální stav doložený konkrétními rozhodnutími, nejbližší ověřenou lhůtu, klasifikaci nároků, mapu důkazů a procesních rolí, úplné požadované podání či návrh a přesný petit. Vyčíslení uspokojení, nákladů a rizik musí mít kontrolovatelné vstupy a citované normy. Zachovej protinámitky, alternativní postup a neověřené otázky. Připravený formulář, nahrání dokumentu, podpis, podání a soudní rozhodnutí označuj odděleně.
