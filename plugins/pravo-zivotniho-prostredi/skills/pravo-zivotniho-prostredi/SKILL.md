---
uuid: f5a03fe0-0212-4d96-9350-debb036e07eb
name: pravo-zivotniho-prostredi
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Právo životního prostředí ČR"
    summary: "EIA a integrované povolování, vodní právo a povolení k vypouštění, ochrana ovzduší, odpady a obaly, ochrana přírody a krajiny, lesy a zemědělská půda, hluk, ekologická újma a sanace, kontroly a pokuty ČIŽP, účast veřejnosti a spolků."
    examplePrompts:
      - "ČIŽP uložila klientovi pokutu 800 000 Kč za nakládání s odpady bez povolení. Jaké jsou lhůty a důvody pro odvolání a lze pokutu snížit?"
      - "Spolek chce napadnout záměr skladové haly u obce. V jaké fázi (EIA, územní řízení, povolení) se může účastnit a jak založit aktivní legitimaci?"
      - "Klient koupil pozemek se starou ekologickou zátěží. Kdo odpovídá za sanaci a jak se bránit uložení nápravných opatření?"
  en:
    displayName: "Czech Environmental Law"
    summary: "EIA and integrated permitting, water law and discharge permits, air protection, waste and packaging, nature and landscape protection, forests and agricultural land, noise, environmental liability and remediation, inspections and penalties by ČIŽP, public participation and NGO standing."
    examplePrompts:
      - "The Environmental Inspectorate fined my client CZK 800,000 for handling waste without a permit. What are the deadlines and grounds for appeal and can the fine be reduced?"
      - "An association wants to challenge a warehouse project near the village. At which stage (EIA, zoning, permit) can it participate and how to establish standing?"
      - "My client bought land with historical contamination. Who is liable for remediation and how to defend against remedial orders?"
  sk:
    displayName: "Právo životného prostredia ČR"
    summary: "EIA a integrované povoľovanie, vodné právo a povolenie na vypúšťanie, ochrana ovzdušia, odpady a obaly, ochrana prírody a krajiny, lesy a poľnohospodárska pôda, hluk, ekologická ujma a sanácia, kontroly a pokuty ČIŽP, účasť verejnosti a spolkov."
    examplePrompts:
      - "ČIŽP uložila klientovi pokutu 800 000 Kč za nakladanie s odpadmi bez povolenia. Aké sú lehoty a dôvody na odvolanie a možno pokutu znížiť?"
      - "Spolok chce napadnúť zámer skladovej haly pri obci. V akej fáze (EIA, územné konanie, povolenie) sa môže zúčastniť a ako založiť aktívnu legitimáciu?"
      - "Klient kúpil pozemok so starou ekologickou záťažou. Kto zodpovedá za sanáciu a ako sa brániť uloženiu nápravných opatrení?"
description: Použij pro EIA, SEA, JES a IPPC, vodu, ovzduší, odpady a obaly, přírodu a krajinu, Natura, les a ZPF, hluk, ekologickou újmu a sanace, ČIŽP a sankce, účast veřejnosti a informace, environmentální transakce, klima, ETS, ESG a CSRD.Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu pravo-zivotniho-prostredi (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Právo životního prostředí ČR

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

## Složka, fáze a role

Urči klienta: investora, provozovatele, vlastníka, obec, souseda, spolek nebo jinou dotčenou veřejnost. Rozliš záměr, územní plán, povolování, provoz, kontrolu, sankci a nápravu. Z dodaných listin identifikuj zařízení, pozemky, činnost, kapacitu, odpady, emise, vodu, hluk a chráněné hodnoty. Povolení, skutečný provoz a technické měření nejsou totéž. U každé chybějící licence, mapy, průzkumu či registru vyžádej podklad do aplikace; nevytvářej vlastní údaje ani externí prohlídku databází.

Vytvoř mapu souběžných složkových a procesních režimů. Jedno povolení nemusí pokrývat všechny činnosti ani soukromoprávní vztahy. Nejbližší lhůtu účasti či obrany zjisti z konkrétního právního nástroje a doloženého oznámení, ne z obecného environmentálního checklistu.

## Nativní prameny a povolování

V připojených pramenech (Salvia, lawgpt) vyhledej úpravu EIA a SEA, integrované prevence, jednotného environmentálního stanoviska, stavebního práva, vod, ovzduší, odpadů, obalů, výrobků s ukončenou životností, přírody, lesa, zemědělské půdy, veřejného zdraví a hluku. Podle věci přidej ekologickou újmu, kontrolu a přestupky, správní soudnictví, environmentální informace, Aarhuskou úmluvu a relevantní unijní akty. Přechod mezi povolovacími režimy vyřeš podle skutečné fáze a úkonů, včetně rozsahu nahrazovaných stanovisek.

U záměru načti příslušnou přílohu a její definice; prověř prahy, podlimitní režim, kumulaci a změny projektu. Rozliš zjišťovací řízení, dokumentaci, posudek, projednání, stanovisko a navazující rozhodnutí. Zjisti platnost, prodloužení a ověření souladu změn, nikoli pevnou dobu ze vzoru. U SEA odliš koncepci od konkrétního záměru. U JES a IPPC přesně urč, co nahrazují, co nikoli a kdo rozhoduje; podstatnou změnu zařízení neodvozuj pouze z obchodního označení.

U Natura a druhové ochrany zkoumej významný vliv, alternativy, veřejný zájem, výjimky a kompenzace. U dřevin prověř povolení, oznámení, havarijní situaci, náhradní výsadbu a další ochranu místa. U ZPF a lesa ověř odnětí či omezení, ochranné režimy, odvody, skrývku a rekultivaci. U vod rozliš nakládání, vodní dílo, odběr, vypouštění, ochranné pásmo a záplavové území; historický vznik zařízení sám nepředurčuje oprávnění.

## Provoz a technické podmínky

U odpadů nejprve kvalifikuj odpad, vedlejší produkt a ukončení odpadového režimu podle úplných kritérií a skutečného použití. Prověř původce, oprávnění příjemce, zařízení a provozní řád, evidenci, hlášení, nebezpečné a stavební odpady, skládku, finanční rezervu a přeshraniční přepravu. U obalů, baterií, elektrozařízení, pneumatik a vozidel zkoumej zpětný odběr a kolektivní systémy. Smlouva s odpadovou firmou sama neprokazuje splnění veřejnoprávních povinností.

U vody ověř podmínky množství, jakosti, měření, havarijního plánu, hlášení a poplatků. U ovzduší urč zařazení zdroje, povolení, limity, BAT/BREF, provozní řád, měření a poplatky. U hluku a vibrací zkoumej chráněný prostor, dobu, korekce, zvláštní režim a průkaznost odborného měření; nevydávej vlastní technickou domněnku za posudek. Podle provozu přidej ETS, F-plyny, REACH, CLP, taxonomii a povinnost ESG/CSRD výkaznictví po ověření osobního a časového rozsahu.

## Kontrola, sankce a nápravná odpovědnost

U ČIŽP nebo jiného orgánu odděl kontrolní protokol, námitky, zahájení přestupku, rozhodnutí, zákaz provozu a nápravné opatření. Ověř kompetenci, vymezení skutku, časové znění včetně případné příznivější úpravy, promlčení, přičitatelnost, liberaci, souběh, důkazní břemeno a majetkové poměry. Výši sankce nenapadej jen přívlastkem vysoká; uveď konkrétní vadu výměry nebo předpokladů. Rozliš odvolání, žalobu, odkladný účinek a soudní moderaci včetně potřeby návrhu.

U ekologické újmy a havárie vyhledej preventivní a nápravná opatření, okruh provozních činností, finanční zajištění, náklady, oznamování a vztah ke složkovým zákonům. Starou zátěž, kontaminaci způsobenou provozem a běžnou civilní škodu neposuzuj stejným titulem. U původce, provozovatele a vlastníka zjisti zvláštní podmínky odpovědnosti; vlastnictví samo nedokládá způsobení, ale ani nevylučuje všechny povinnosti. Trestní přesah posuď odděleně.

## Veřejnost a soukromé nároky

Účast spolku při ochraně přírody, kvalifikované veřejnosti v navazujícím EIA řízení a účast podle vodního či stavebního režimu mají vlastní podmínky. Pro každý nástroj ověř předchozí žádost o informace, kvalifikaci spolku, oznámení, počátek a délku přihlášení, rozsah námitek a opravná práva. Pravidlo jedné větve nepřenášej do jiné. Samostatně prověř odvolací oprávnění kvalifikované veřejnosti bez účasti v první instanci a žalobní legitimaci. Lhůtu pro rozhodnutí soudu nezaměňuj za lhůtu podání žaloby.

U závazných stanovisek a opatření obecné povahy vyhledej konkrétní cestu přezkumu. U environmentálních informací, petic a referenda rozliš dostupný nástroj a jeho účinky. Investorovi navrhni transparentní vypořádání skutečných námitek, nikoli obcházení účasti. U sousedských imisí, kořenů, vody a škody prověř samostatný civilní titul, význam povolení, proporcionalitu a vykonatelný petit; hygienický limit nemusí sám vyčerpat soukromoprávní test.

## Transakce a konečný výstup

Při prověrce koupě či nájmu mapuj převoditelnost povolení, zátěže, odpady, probíhající řízení a náklady nápravy. Připrav konkrétní záruky, indemnity, zádržné, odpovědnostní limit a návratovou variantu v právně přípustném rozsahu; smluvní ochrana neváže automaticky dozor. U sanace a kompenzací uveď nutný odborný podklad a ekonomické či daňové předpoklady. Předej tabulku režim–orgán–úkon–lhůta–důkaz–riziko, požadované podání nebo smlouvu a rozpočet. Judikaturu v připojených pramenech (Salvia, lawgpt) porovnej ke konkrétním podmínkám, nikoli podle pouhé tematické podobnosti.
