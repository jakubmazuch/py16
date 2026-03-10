# Samostatná práce -- Evidence plateb k dokladům

## Kontext

V předchozí úloze jste vytvořili jednoduchý fakturační systém. Ten umí
pracovat s různými typy dokladů (např. faktura, záloha, dobropis) a
spočítat jejich celkovou hodnotu.

V reálném účetním systému však doklad obvykle nezůstává jen jako číslo
-- postupně se k němu přiřazují **platby**, které jej mohou částečně
nebo úplně uhradit.

Vaším úkolem je stávající model rozšířit tak, aby systém dokázal
evidovat platby a určit, zda je doklad zaplacen.

------------------------------------------------------------------------

## Cíl úlohy

Rozšiřte stávající program tak, aby:

-   doklad mohl evidovat více plateb,
-   bylo možné zjistit, kolik již bylo zaplaceno,
-   bylo možné zjistit, kolik zbývá zaplatit,
-   účetní systém dokázal zobrazit přehled dokladů včetně jejich stavu.

------------------------------------------------------------------------

## ČÁST 1 -- Třída Platba

Vytvořte novou třídu:

    Platba

Třída bude reprezentovat jednu přijatou nebo odeslanou platbu.

Měla by obsahovat alespoň tyto informace:

-   datum platby
-   částku
-   krátkou poznámku (např. „bankovní převod", „hotově", apod.)

Dbejte na základní kontrolu vstupních hodnot (např. částka nesmí být
záporná).

------------------------------------------------------------------------

## ČÁST 2 -- Evidence plateb u dokladu

Rozšiřte třídu `Doklad`.

Každý doklad bude nově obsahovat seznam plateb.

Například:

    self.platby

Do třídy přidejte metodu:

    pridej_platbu(platba)

která přidá novou platbu do seznamu plateb daného dokladu.

------------------------------------------------------------------------

## ČÁST 3 -- Kolik je zaplaceno

Do třídy `Doklad` přidejte vlastnost:

    zaplaceno

která vrací součet všech plateb evidovaných u dokladu.

Použijte `@property`.

------------------------------------------------------------------------

## ČÁST 4 -- Kolik zbývá zaplatit

Přidejte další vlastnost:

    zbyva_zaplatit

Ta by měla vracet rozdíl mezi:

-   celkovou částkou dokladu
-   již zaplacenou částkou

Jinými slovy:

    celkova_castka - zaplaceno

------------------------------------------------------------------------

## ČÁST 5 -- Stav dokladu

Do třídy `Doklad` přidejte ještě vlastnost:

    je_zaplaceno

Doklad je považován za zaplacený, pokud už není co doplácet.

Tedy například:

    zbyva_zaplatit <= 0

------------------------------------------------------------------------

## ČÁST 6 -- Rozšíření třídy Uctarna

Rozšiřte třídu `Uctarna` o metodu, která zobrazí přehled dokladů včetně
jejich stavu.

Výstup může vypadat například takto:

    Číslo        Typ        Celkem     Zaplaceno     Zbývá
    ------------------------------------------------------
    2026-01      Faktura     35000        20000      15000
    2026-Z01     Záloha      18000        18000          0
    2026-D01     Dobropis    -3000            0      -3000

Formát není předepsaný, důležité je, aby byl přehledný.

------------------------------------------------------------------------

## ČÁST 7 -- Ověření v main.py

V hlavním programu vytvořte několik dokladů a přidejte k nim různé
platby.

Například:

    faktura.pridej_platbu(...)
    faktura.pridej_platbu(...)

Poté vypište přehled dokladů pomocí nové metody v `Uctarna`.

------------------------------------------------------------------------

## Poznámka

Snažte se zachovat stejný styl návrhu jako v předchozí úloze:

-   používejte vlastnosti (`@property`),
-   vyhněte se podmínkám typu `isinstance`,
-   pracujte s objekty a jejich odpovědnostmi.

Cílem není napsat co nejkratší kód, ale rozšířit stávající návrh tak,
aby zůstal přehledný a dobře rozšiřitelný.
