---
uuid: 05998376-b1d7-40bb-9db3-a4ecf194a7b6
name: franchising-distribuce-obchodni-zastoupeni
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Franchising, distribuce a obchodní zastoupení ČR"
    summary: "Franšízové smlouvy a předsmluvní informace, licence know-how a značky, výhradní a selektivní distribuce, vertikální omezení a bloková výjimka, určování cen pro další prodej a zákazy online prodeje, provize obchodního zástupce, ukončení a zvláštní odměna, konkurenční doložky, riziko zastřeného zaměstnání, přeshraniční rozhodné právo a příslušnost, DPH a srážková daň z licenčních poplatků."
    examplePrompts:
      - "Klient (výrobce kosmetiky) vypověděl po 8 letech smlouvu o obchodním zastoupení. Zástupce požaduje zvláštní odměnu ve výši roční provize a provize z objednávek po skončení. Na co má nárok a jak to spočítat?"
      - "Klient staví franšízový koncept kaváren. Navrhni strukturu franšízové smlouvy, předsmluvní informace, ochranu know-how, cenová doporučení bez porušení soutěžního práva a konkurenční doložku po skončení."
      - "Dodavatel zakázal našemu klientovi (distributorovi) prodej přes vlastní e-shop a Alza.cz a určuje minimální ceny. Je to platné a lze se bránit u ÚOHS?"
  en:
    displayName: "Czech Franchising, Distribution & Agency"
    summary: "Franchise agreements and pre-contractual disclosure, know-how and brand licensing, exclusive and selective distribution, vertical restraints and the block exemption, resale price maintenance and online sales bans, commercial agents' commission, termination and goodwill indemnity, non-compete clauses, disguised employment risks, cross-border governing law and jurisdiction, VAT and withholding on royalties."
    examplePrompts:
      - "My client (a cosmetics manufacturer) terminated an 8-year commercial agency contract. The agent claims a goodwill indemnity equal to one year's commission plus commission on post-termination orders. What is he entitled to and how is it calculated?"
      - "My client is building a coffee-shop franchise. Propose the franchise agreement structure, pre-contractual disclosure, know-how protection, price recommendations compliant with competition law and a post-term non-compete."
      - "A supplier banned our client (a distributor) from selling via its own e-shop and Alza.cz and dictates minimum prices. Is this valid and can we complain to the competition office?"
  sk:
    displayName: "Franchising, distribúcia a obchodné zastúpenie ČR"
    summary: "Franšízové zmluvy a predzmluvné informácie, licencie know-how a značky, výhradná a selektívna distribúcia, vertikálne obmedzenia a bloková výnimka, určovanie cien pre ďalší predaj a zákazy online predaja, provízia obchodného zástupcu, ukončenie a osobitná odmena, konkurenčné doložky, riziko zastretého zamestnania, cezhraničné rozhodné právo a príslušnosť, DPH a zrážková daň z licenčných poplatkov."
    examplePrompts:
      - "Klient (výrobca kozmetiky) vypovedal po 8 rokoch zmluvu o obchodnom zastúpení. Zástupca požaduje osobitnú odmenu vo výške ročnej provízie a provízie z objednávok po skončení. Na čo má nárok a ako to spočítať?"
      - "Klient stavia franšízový koncept kaviarní. Navrhni štruktúru franšízovej zmluvy, predzmluvné informácie, ochranu know-how, cenové odporúčania bez porušenia súťažného práva a konkurenčnú doložku po skončení."
      - "Dodávateľ zakázal nášmu klientovi (distribútorovi) predaj cez vlastný e-shop a Alza.cz a určuje minimálne ceny. Je to platné a možno sa brániť na ÚOHS?"
description: Kvalifikace, tvorba, revize a ukončení franchisingových, distribučních a agentských vztahů včetně provizí, zvláštní odměny, území, online prodeje, soutěžních omezení, know-how, přeshraničních a daňových aspektů. Zohledňuje postavení zastoupeného, zástupce, dodavatele, distributora, franchisora i franchisanta.
---

<!-- Upraveno z pluginu franchising-distribuce-obchodni-zastoupeni (JUDr. Vojtěch Říha, Ph.D., github.com/LexaurinTheDog/riha-legal-plugins, Apache-2.0): zdroj CODEXIS nahrazen konektory Salvia, lawgpt, Ansvar a Sagasu. -->

# Franchising, distribuce a obchodní zastoupení

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

## Kvalifikace a zájem klienta

Urči zastupovanou stranu, obchodní model, země působení, zákazníky, peněžní toky a požadovaný výsledek. Kdo uzavírá obchody vlastním jménem a na čí účet, kdo nese zásobní, úvěrové, marketingové a investiční riziko? Rozliš dlouhodobé obchodní zastoupení, jednotlivé zprostředkování, komisi, distribuci na vlastní riziko, franchising a platformu. Název smlouvy ani fakturace nerozhodují samy; ověř také možné znaky závislé práce a soutěžněprávní skutečné zastoupení.

U každé varianty odděl občanskoprávní kvalifikaci, soutěžní pravidla, rozhodné právo, daňové zacházení a praktickou ekonomiku. Sestav mapu existujících smluv, dodatků, obchodních podmínek, manuálů, e-mailových pokynů, skutečného plnění, investic a ukončovacích jednání. Chybějící obrat, provizi nebo získané zákazníky nepředpokládej.

## Obchodní zastoupení a vypořádání

V připojených pramenech (Salvia, lawgpt) ověř požadavky na formu, vymezení činnosti, území, výhradnost, součinnost, informování, výkazy, kontrolu podkladů a případné ručení za zákazníka. Kdy vzniká provize, jak se počítá, kdy je splatná a kdy může zaniknout? Odděl provizi za konkrétní obchod, provizi po skončení zastoupení, náhradu škody a zvláštní odměnu. Jaký význam mají rozpracované obchody a následný zástupce?

Při ukončení vyhledej vztah sjednané doby, pokračování plnění a započtení předchozího trvání do výpovědní doby. Jaké jsou zákonné minimální a přípustně sjednané delší výpovědní doby a poměr dob pro jednotlivé strany? Nepředepisuj jejich shodnost bez ověření. Která ustanovení jsou kogentní a která dovolují smluvní úpravu?

Zvláštní odměnu řeš po jednotlivých podmínkách: nové či rozvinuté zákaznické vztahy, přetrvávající podstatné výhody, ztracené provize a spravedlnost výsledku. Teprve poté zjisti způsob výpočtu a strop, včetně krátce trvajícího vztahu; strop není automatickou výší nároku. Odliš lhůtu pro uplatnění od promlčení. Může později zjištěné porušení povinnosti nárok vyloučit a jaká kauzální vazba k ukončení je třeba? Každý závěr podlož okolnostmi a přesným zdrojem, nikoli obecnou formulí.

## Distribuce a soutěžní kontrola

U rámcových dodávek uprav objednávky, přijetí, dodání, přechod rizika a vlastnictví, cenu, její změny, měnu, daně, úvěrový limit, vady, servis, bezpečnost výrobků a svolání výrobku. Jak mají fungovat minimální odběry, reporting, audit, ochranné známky a výměna zákaznických údajů? Zjisti účinky doložek Incoterms a jejich skutečně sjednané verze.

U každého omezení proveď celý soutěžní test: dohoda a její skutečný obsah, relevantní trh, cíl či účinky, obchod mezi členskými státy, podmínky blokové výjimky, případné individuální ospravedlnění a právní následek. Ztráta blokové výjimky sama nedokazuje protiprávnost ani neplatnost celé smlouvy. Posuď oddělitelnost konkrétní klauzule.

Ověř určování cen dalšího prodeje podle faktického nátlaku, pobídek, monitoringu a korespondence; označení ceny za doporučenou či maximální nestačí. U výhradní a selektivní distribuce prověř aktivní a pasivní prodej, zákazníky, území, tržiště, účinné využívání internetu, dvojí ceny a paritní doložky. V duální distribuci vyhodnoť sdílení citlivých informací. U zákazu konkurence rozliš trvání smlouvy a dobu po skončení, předmět, území, zákazníky, know-how a reálnou možnost změny dodavatele včetně obnovování a nákladů odchodu. Vyhledej relevantní podmínky bez předem stanovených dob nebo tržních podílů. U agentské konkurenční doložky samostatně prověř možnost soudního omezení a účinky nepřiměřeného rozsahu. V potravinových vztazích prověř zvláštní pravidla významné tržní síly a nekalých obchodních praktik.

## Franchising a provozní kontinuita

Prověř předsmluvní informace, zdroj ekonomických projekcí, NDA, nezávaznost či závaznost LOI a vstupní investice. Identifikuj vlastníka známek, skutečně vymezené důvěrné know-how, obsah a změny manuálu, licenci, sublicence a master-franchise oprávnění. Jak se počítá vstupní poplatek, obratová odměna, marketingový fond a IT poplatek? Definuj základ, výjimky, kontrolu a použití fondu tak, aby byly ověřitelné.

Vyvaž provozní standardy, školení a kvalitu se samostatností franchisanta. Řeš územní ochranu, nové pobočky, centrální internetový prodej, přidělování objednávek a zákaznická data. Prověř obnovu, převod provozu, změnu kontroly, podnájem či návaznost nájmu, pojištění a odpovědnost vůči konečným zákazníkům. Smluvní omezení odpovědnosti navrhni ve prospěch klienta jen v ověřených mezích, s konkrétními výjimkami a návazností na pojistné krytí.

## Ukončení, mezinárodní a daňová vrstva

Při odchodu uprav výzvu k nápravě, výpověď či odstoupení, rozpracované objednávky, zásoby, odkup nebo doprodej, odznačení provozovny, vrácení manuálů, ochranu tajemství, migraci dat, vybavení, nájem a případný vstup jiné osoby do provozu. Nepředpokládej automaticky existenci ani vyloučení nároku distributora obdobného agentské odměně; vyhledej podmínky a protiargumenty pro konkrétní rozhodné právo.

Odděl volbu práva od volby soudu, rozhodného práva bez volby a případných imperativních pravidel agentské a soutěžní ochrany. Prověř mezinárodní kupní režim, sankce a exportní omezení podle zboží a zemí. U daní rozliš úplatu za zboží, službu a licenci, bonusy, DPH, přenesení povinnosti, srážku z licenčních plateb, rezidenci, skutečného vlastníka příjmu, smluvní a skupinové podmínky a převodní ceny. Daňovou výhodnost odvoď z doložených toků a variant, ne z názvu smlouvy.

## Povinný výstup

Dodej kvalifikační závěr s alternativou, tabulku klauzulí a rizik, úplnou požadovanou smlouvu nebo revizi každé dotčené klauzule, nikoli několik ukázek. Ke každé změně připoj zájem klienta, ověřené právní omezení, náhradní formulaci a zbytkové riziko. Zvlášť vyhodnoť cenu, území a online prodej. Připoj vypořádání provizí a zvláštní odměny s kontrolovatelným výpočtem, ukončovací kalendář, důkazy, protistraniny námitky a případný přesný petit a náklady.
