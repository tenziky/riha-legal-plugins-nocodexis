---
uuid: 87ba06bb-dbca-425b-a949-e59074af597d
name: pojistne-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Pojistné právo ČR"
    summary: "Pojistná smlouva podle OZ, předsmluvní povinnosti a pravdivé odpovědi, lhůty likvidace, odmítnutí a snížení plnění, povinné ručení a garanční fond, majetkové, odpovědnostní, životní a cestovní pojištění, distribuce pojištění, ombudsman a finanční arbitr, promlčení."
    examplePrompts:
      - "Pojišťovna odmítla plnění z pojištění domácnosti, protože klient při sjednání neuvedl dřívější škodu. Je odmítnutí oprávněné a co lze namítat?"
      - "Po dopravní nehodě pojišťovna viníka krátí náhradu za totální škodu o amortizaci a neplatí náhradní vozidlo. Jaké nároky má poškozený a v jakých lhůtách?"
      - "Klient dostal výzvu ČKP k úhradě příspěvku za nepojištěné vozidlo, které měl v depozitu. Jak se bránit?"
  en:
    displayName: "Czech Insurance Law"
    summary: "Insurance contract under the Civil Code, pre-contractual duties and disclosure, claims handling deadlines, refusal and reduction of indemnity, motor third-party liability and the guarantee fund, property, liability, life and travel insurance, distribution rules, ombudsman and financial arbiter, limitation."
    examplePrompts:
      - "The insurer refused a household claim because my client failed to disclose an earlier loss when contracting. Is the refusal justified and what can we argue?"
      - "After a car accident the liable driver's insurer reduces the total-loss indemnity for depreciation and refuses a replacement car. What can the victim claim and within what deadlines?"
      - "My client received a demand from the Czech Insurers' Bureau for a contribution for an uninsured vehicle that was deregistered. How to defend?"
  sk:
    displayName: "Poistné právo ČR"
    summary: "Poistná zmluva podľa OZ, predzmluvné povinnosti a pravdivé odpovede, lehoty likvidácie, odmietnutie a zníženie plnenia, povinné zmluvné poistenie a garančný fond, majetkové, zodpovednostné, životné a cestovné poistenie, distribúcia poistenia, ombudsman a finančný arbiter, premlčanie."
    examplePrompts:
      - "Poisťovňa odmietla plnenie z poistenia domácnosti, lebo klient pri dojednaní neuviedol skoršiu škodu. Je odmietnutie oprávnené a čo možno namietať?"
      - "Po dopravnej nehode poisťovňa vinníka kráti náhradu za totálnu škodu o amortizáciu a neplatí náhradné vozidlo. Aké nároky má poškodený a v akých lehotách?"
      - "Klient dostal výzvu ČKP na úhradu príspevku za nepoistené vozidlo, ktoré mal v depozite. Ako sa brániť?"
description: Použij pro pojistné smlouvy a distribuci, podmínky a dotazníky, likvidaci, zálohy, snížení či odmítnutí plnění, výluky, promlčení, zánik, majetek, odpovědnost, povinné ručení, ČKP a regres, životní, úrazové, cestovní a podnikatelské pojištění, finančního arbitra a ADR.Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu pojistne-pravo (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Pojistné právo ČR

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

## Role a úplný smluvní základ

Urči, zda klientem je pojistník, pojištěný, oprávněná osoba, poškozený, pojistitel nebo zprostředkovatel. Rozliš škodové a obnosové pojištění, spotřebitele a podnikatele a konkrétní riziko. Zjisti datum smlouvy, počátek krytí, změny, událost, oznámení, šetření a doručení rozhodných sdělení. Vyžádej úplnou smlouvu, skutečně sjednanou verzi podmínek, dotazník, záznam z jednání, upomínky a likvidační podklady. Dnešní podmínky jiného produktu nenahrazují rozhodnou smlouvu. Neznámou výluku nebo lhůtu veď jako variantu, nikoli smyšlenou klauzuli.

## Nativní zdroje a časový režim

V připojených pramenech (Salvia, lawgpt) vyhledej občanskoprávní pojištění a podle času dřívější zákon o pojistné smlouvě, pojištění odpovědnosti z provozu vozidla, pojišťovnictví, distribuci, ochranu spotřebitele a finančního arbitra. Pro náhradu přidej odpovědnostní úpravu, dopravu a vozidla, zdraví a daňové předpisy; pro spor proces a náklady. Unijní rámec pojišťovnictví, distribuce a ochrany údajů používej podle skutečné působnosti. Rozhodné právo smlouvy, události, porušení povinnosti a procesního kroku určuj samostatně s přechodnými ustanoveními.

Přímý nárok vůči pojistiteli nejprve ověř ze zákona či relevantního smluvního základu; nepředpokládej jej pro každé pojištění odpovědnosti ani jej paušálně nevylučuj mimo motorovou oblast. Údaje o licenci, vozidle nebo pojištění čerpej z dodaných podkladů a označ jejich aktuálnost. Nedostupný právní nebo statistický údaj nehledej externě.

## Vznik, informace a rozsah krytí

Prověř formu, pojistný zájem, předsmluvní informace, skutečné seznámení s podmínkami, překvapivá ujednání a výklad nejasností. Které písemné otázky byly položeny, komu a co bylo odpovězeno? Nepředpokládej zatajení otázky, která nezazněla. U distribuce zkoumej analýzu potřeb, doporučení, střet zájmů, informační dokument a příčinnou souvislost případného chybně nastaveného krytí.

Rozliš pojistnou událost od škodní události a ověř limity, spoluúčast, čekací dobu, časový a územní rozsah. U každé výluky zjisti její začlenění do smlouvy, určitost, přípustnost a důkazní podmínky. Snížení, odmítnutí, odstoupení, neplatnost a zánik mají odlišné předpoklady; neměň právní důvod pojistitelova sdělení bez vysvětlení. Podezření pojistného podvodu odděl od pouhé nepřesnosti údajů.

## Šetření, splatnost a krácení

Sestav časovou osu oznámení, zahájení šetření, sdělení jeho výsledku oprávněné osobě, smluvní či zákonné splatnosti a prodlení. Interní uzavření likvidačního spisu není samo doloženým sdělením výsledku. Z nativního znění vyhledej podmínky vysvětlení prodlouženého šetření, žádosti o přiměřenou zálohu, rozumného důvodu jejího odepření a samostatného prodlení při porušení povinností. Zjisti rozsah součinnosti, přístupu k podkladům a zachraňovacích nákladů.

Odděl neoznámené zvýšení rizika, nesprávně sjednané pojistné a kauzální vliv porušení na vznik, průběh, rozsah či zjištění události. Pro každý mechanismus načti jeho předpoklady a výpočet; paušální procento není odůvodnění. U podpojištění ověř hodnotu, částku, smluvní úpravu a případnou indexaci. Hrubou nedbalost nebo alkohol nelze mechanicky přenést mezi výlukou, krácením a regresem.

Promlčení vlastního plnění, přímého nároku a regresu počítej samostatně, včetně zvláštních počátků a návaznosti na nárok proti škůdci. Reklamaci nepovažuj bez pramene za stavení. U úroků dolož první den prodlení, pravidlo konce lhůty, rozhodné pololetí či jiný zákonný parametr a sazbu získanou nativní cestou. Chybí-li vstup, předej ověřený vzorec s označenou mezerou místo vymyšlené částky.

## Jednotlivé produkty a nároky

U provozu vozidla prověř osobu povinnou pojistit, definici provozu, výjimky, vyřazení vozidla, územní krytí, přímý nárok, limity a likvidačního zástupce. U ČKP rozliš plnění z garančního fondu, příspěvek za nepojištění a regres, jejich podmínky, adresáta a promlčení. Nepoužívání vozidla není samo úplným právním testem. Změnu zákona nepřenášej pouze podle názvu novějšího předpisu.

U vozidla a majetku prověř opravu, totální škodu, obvyklou či novou hodnotu, zbytky, zhodnocení, pokles hodnoty, DPH podle odpočtu, náhradní užívání, odtah a ušlý zisk. Rozliš škodní nárok od rozsahu pojistného krytí. U zdraví přidej bolest, společenské uplatnění, péči, výdělek a pozůstalé podle ověřené metody bez pevného ceníku.

U podnikatele zkoumej all-risk či vyjmenovaná rizika, přerušení provozu, profesní a výrobkovou odpovědnost, claims-made a occurrence, retroaktivitu, dodatečnou lhůtu, D&O, stavebně-montážní, přepravní, kybernetické a právní ochrany. Prověř svobodnou volbu zástupce, soupojištění, vedoucího pojistitele, zajištění a odpovědnost makléře. U životního, úrazového, schopnosti splácet a cestovního pojištění odděl obmyšleného od dědice, odkupné od pojistné částky, tabulku následků, asistenci, výluky, investiční poplatky a daňové dopady ukončení.

## Ukončení a výstup

Při nezaplacení, výpovědi, odstoupení, změně vlastníka nebo zájmu ověř formu, upomínku, doručení a následky pro pokračující krytí. U claims-made neukončuj smlouvu bez analýzy budoucích nároků. Porovnej reklamaci, příslušné ADR, finančního arbitra a žalobu podle skutečné působnosti, nikoli obecné představy o pojištění.

Dodej tabulku nárok–zákon–smluvní článek–důkaz–lhůta–výpočet, konkrétní výzvu či podání a rozpočet. Při sjednávání napiš požadované klauzule krytí, oznamování, odpovědnosti a ukončení s přípustnými výjimkami. Ekonomickou a daňovou výhodnost odvoď od klientových dat. Nativní judikaturu k výlukám, krácení, regresu a promlčení porovnej včetně opačných výsledků; příslib plnění ani odeslaný návrh nejsou skutečně přijaté peníze.
