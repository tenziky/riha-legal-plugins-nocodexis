---
uuid: bbdc0135-4936-43f2-91be-8d0dd8ceefb9
name: opatrovnictvi-svepravnost
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Opatrovnictví a svéprávnost ČR"
    summary: "Omezení svéprávnosti a jeho přezkum, podpůrná opatření (nápomoc při rozhodování, zastoupení členem domácnosti, předběžné prohlášení), opatrovnictví dospělých a dohled, povinnosti opatrovníka a schvalování soudem, veřejný opatrovník, detence ve zdravotnickém zařízení, ochrana zranitelných dospělých, demence a plánování majetku."
    examplePrompts:
      - "Matka klienta má pokročilou demenci a je třeba prodat její byt na úhradu péče. Jaké jsou možnosti - zastoupení členem domácnosti, opatrovník, schválení soudem - a jak dlouho to trvá?"
      - "Soud omezil klienta ve svéprávnosti na 3 roky pro schizofrenii, klient je stabilizovaný a chce omezení zrušit. Jak postupovat a co prokázat?"
      - "Opatrovník sourozence uzavřel za opatrovance darovací smlouvu na chalupu bez souhlasu soudu. Je smlouva platná a jak se bránit?"
  en:
    displayName: "Czech Legal Capacity & Guardianship"
    summary: "Limitation of legal capacity and its review, supportive measures (assisted decision-making, representation by a household member, advance directive), adult guardianship and supervision, guardian's duties and court approvals, public guardians, detention in health-care facilities, protection of vulnerable adults, dementia and estate planning."
    examplePrompts:
      - "My client's mother has advanced dementia and her flat must be sold to pay for care. What are the options - household-member representation, guardian, court approval - and how long does it take?"
      - "The court limited my client's legal capacity for 3 years due to schizophrenia; he is stable and wants the limitation lifted. How to proceed and what to prove?"
      - "A sibling's guardian signed a gift deed for a cottage on behalf of the ward without court approval. Is the deed valid and how to challenge it?"
  sk:
    displayName: "Opatrovníctvo a spôsobilosť ČR"
    summary: "Obmedzenie spôsobilosti na právne úkony a jeho preskúmanie, podporné opatrenia (nápomoc pri rozhodovaní, zastúpenie členom domácnosti, predbežné vyhlásenie), opatrovníctvo dospelých a dohľad, povinnosti opatrovníka a schvaľovanie súdom, verejný opatrovník, detencia v zdravotníckom zariadení, ochrana zraniteľných dospelých, demencia a plánovanie majetku."
    examplePrompts:
      - "Matka klienta má pokročilú demenciu a treba predať jej byt na úhradu starostlivosti. Aké sú možnosti - zastúpenie členom domácnosti, opatrovník, schválenie súdom - a ako dlho to trvá?"
      - "Súd obmedzil klienta v spôsobilosti na 3 roky pre schizofréniu, klient je stabilizovaný a chce obmedzenie zrušiť. Ako postupovať a čo preukázať?"
      - "Opatrovník súrodenca uzavrel za opatrovanca darovaciu zmluvu na chalupu bez súhlasu súdu. Je zmluva platná a ako sa brániť?"
description: Použij pro svéprávnost dospělých, podpůrná opatření, nápomoc, zastoupení domácností, předběžné prohlášení, opatrovnictví, radu a soudní souhlasy, přezkum a navrácení svéprávnosti, nedobrovolnou péči a detenci, ochranu seniorů a napadání jednání při duševní poruše. Právní rešerše přes konektory Salvia a lawgpt.
---

<!-- Upraveno z pluginu opatrovnictvi-svepravnost (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Opatrovnictví a svéprávnost dospělých

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

## Osoba a skutečné potřeby

Urči klienta: dotčeného dospělého, rodinu, opatrovníka, obec, poskytovatele péče, banku nebo smluvního partnera. Zájem rodiny neztotožňuj se zájmem a vůlí člověka. Popiš konkrétní obtíže při smlouvách, financích, bydlení, léčbě či jednání s úřady; diagnóza sama nevysvětluje schopnost každého právního jednání. Z doložených zpráv odděl průběh, prognózu a přechodnost potíží od pouhých obav. Respektuj důstojnost a preference, používej jazyk osoby s omezenou svéprávností, nikoli nálepku.

Vyžádej existující rozhodnutí včetně právní moci a doby, návrhy přezkumu, plnou moc, předběžné prohlášení, smlouvy o podpoře, zprávy, majetkové podklady a konflikty. Zjisti naléhavost: hospitalizace, hrozící převod, podvod, exekuce či ztráta bydlení. Chybějící lékařské nebo rejstříkové údaje ponech jako mezeru; žádný externí průzkum nenahrazuje podklady dodané do aplikace.

## Prameny a škála podpory

V připojených pramenech (Salvia, lawgpt) vyhledej občanský zákoník, zvláštní soudní řízení, zdravotní a specifické zdravotní služby, sociální služby, notářství, veřejné opatrovnictví a úpravu obcí. Podle otázky připoj ochranné léčení a detenci v trestním právu, banky a platební styk, antidiskriminační úpravu, mezinárodní ochranu dospělých, Úmluvu o právech osob se zdravotním postižením a lidskoprávní prameny. Zjisti znění k jednání, rozhodnutí, přezkumu a pokračující detenci včetně přechodu historického zbavení způsobilosti.

Porovnej plnou moc, předběžné prohlášení, nápomoc, zastoupení členem domácnosti, opatrovnictví bez omezení a omezení svéprávnosti. U každého nástroje ověř vznik, souhlas či odmítnutí, formu, schválení, oprávněné osoby, rozsah, dobu, zánik a důsledky konfliktu. Neoznačuj podporu za zastoupení. U více členů domácnosti prověř samostatné a rozporné projevy vůle; příjmy a prostředky na účtu mají vlastní pravidla. U plné moci prověř schopnost při udělení a účinky následných změn, neslibuj automaticky univerzální trvalé zastoupení.

## Omezení, návrat a proces

Před návrhem na omezení zjisti konkrétní hrozící újmu a proč nestačí méně omezující řešení. Každou navrženou oblast spoj s doloženou schopností a rizikem; neurčitý zákaz všech jednání ani paušální částka nenahrazuje odůvodnění. Samostatně posuď běžné každodenní záležitosti, osobní a volební práva, pořizovací způsobilost a správu majetku. Navrácení svéprávnosti nepodmiňuj přijetím podpůrce bez konkrétního právního základu.

Ověř zahájení, příslušnost, účastníky, možnost vlastního zástupce, procesního opatrovníka, výslech, zhlédnutí a dokazování. Nevyvozuj automaticky povinného advokáta ani potřebu vždy nového psychiatrického posudku; načti celý rozhodný důkazní režim a výjimky. Znalci polož otázky ke konkrétním schopnostem a možnostem podpory, ne jen k diagnóze. U omezení vypočti dobu a účinky včas zahájeného přezkumu včetně zákonného maxima pokračování. Odděl změnu rozsahu, zánik omezení a odvolání opatrovníka.

## Opatrovník, rada a soud

Při výběru opatrovníka ověř zákonné pořadí, přání člověka, vhodnost, kontakt, střet zájmů a rozsah rozhodnutí. U veřejného opatrovníka zjisti kompetenci obce a kontrolu; kapacitu či poskytování služby posuzuj v konkrétním konfliktu. Prověř péči, respektování vůle, správu oddělených peněz, soupis, vyúčtování, zprávy a dohled. Rodinný souhlas není automaticky právně potřebným schválením.

U každé dispozice odděl vlastní jednání opatrovance, zastupování opatrovníkem, souhlas rady, nahrazení její působnosti a souhlas soudu. Nemovitosti, bydlení, úvěr, dary a jiné významné úkony prověř podle konkrétního ustanovení; obecné pravidlo rady nenahrazuje soudní souhlas. Neodvozuj jeden univerzální následek chybějícího schválení. U prodeje na úhradu péče porovnej potřebu, alternativy, cenu, použití výtěžku a pořadí podpisu, schválení a vkladu. Návrh smlouvy musí chránit člověka i při odmítnutí schválení.

## Svoboda, péče a zdravotní souhlasy

Rozliš převzetí do nemocnice bez souhlasu, další držení, omezení pohybu v sociální službě, ochranné léčení a zabezpečovací detenci. Pro každou větev ověř důvod, oznámení soudu, lhůtu přezkumu, zastoupení, výslech, znalce, trvání, odvolání a možnost propuštění. Souhlas opatrovníka automaticky neodstraňuje nesouhlas člověka a soudní kontrolu. U sociální smlouvy prověř oprávnění zastupující obce a význam nesouhlasu vyjádřeného chováním.

U zdravotní péče ověř informovaný a zástupný souhlas, pořadí oprávněných osob, dokumentaci, stížnost a omezovací prostředky. Předběžné prohlášení neztotožňuj s dříve vysloveným přáním; u přání zjisti formu, poučení, platnost a meze použitelnosti. Zvláštní zákroky a výzkum mají vlastní ochranné podmínky. Náhradu za nezákonné omezení svobody vyhodnoť odděleně od samotného propuštění.

## Majetková ochrana a předání

Při napadání jednání zkoumej schopnost právě v době úkonu, důkazní břemeno, druh vady, případné schválení a újmu; samotný pozdější rozsudek není důkazem dřívější neschopnosti. Prověř lichvu, tíseň, spotřebitelská ujednání, zneužitou plnou moc, darování, výměnek, závěť a bankovní dispozice. Ověření podpisu neslibuje úplné potvrzení způsobilosti. U plánování budoucnosti slaď prohlášení, plnou moc, zdravotní přání, dědické řešení a případné majetkové zajištění podle klientových potřeb.

Dodej srovnání nejmírnějších variant, konkrétní návrh nebo smlouvu, důkazní plán, časovou osu přezkumu, potřebné souhlasy a náklady. Procesní kolizi zástupce nepřenášej automaticky na omezení všech práv člověka. Judikaturu k subsidiaritě, výslechu, souhlasům, duševní poruše a detenci vyhledej v připojených pramenech (Salvia, lawgpt) včetně opačných výsledků; neoznačuj právní ani zdravotní výsledek za předem jistý.
