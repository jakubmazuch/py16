# 🚗 Samostatná práce – Objektový dopravní systém

## Zadání

Navrhni a implementuj jednoduchý objektový model dopravního systému v Pythonu.
Cílem je vytvořit rozšiřitelný systém, který pracuje s různými typy vozidel a umožňuje jejich správu v rámci jednoho vozového parku.

---

## Kontext

Dopravní společnost vlastní různé druhy vozidel:

- Auto
- Motocykl
- Autobus
- Elektroauto

Každé vozidlo:

- má značku,
- má určitou kapacitu cestujících,
- má spotřebu (palivo nebo energie),
- umí jet určitou vzdálenost,
- může se při jízdě chovat odlišně.

---

## Požadavky

### 1️⃣ Základní třída

Vytvoř nadřazenou třídu `Vozidlo`.
Rozmysli a implementuj:

- společné atributy,
- společné metody,
- alespoň jednu metodu, která bude mít u potomků odlišné chování.

Rozhodni, zda bude tato třída abstraktní.

---

### 2️⃣ Potomci

Vytvoř třídy `Auto`, `Motocykl`, `Autobus` a `ElektroAuto`.

Každá třída musí:

- dědit z `Vozidlo`,
- implementovat nebo přepsat metodu jízdy,
- pracovat se svou kapacitou a spotřebou.

Elektroauto může používat jiný typ „spotřeby" než ostatní vozidla.

---

### 3️⃣ Polymorfismus

Vytvoř kolekci různých vozidel a nad všemi zavolej stejnou metodu (např. jízdu na určitou vzdálenost). Každé vozidlo musí reagovat podle svého typu.

Nepoužívej podmínky typu:

```python
if isinstance(vozidlo, Auto):
    ...
```

---

### 4️⃣ Vozový park (kompozice)

Vytvoř třídu `VozovyPark`.

Tato třída **nedědí** z `Vozidlo` – místo toho vozidla **obsahuje** (kompozice).

Třída musí umět:

- přidat vozidlo do parku,
- odebrat vozidlo ze parku (podle značky),
- vypsat přehled všech vozidel,
- vyslat všechna vozidla na zadanou vzdálenost (využij polymorfismus),
- vrátit počet vozidel v parku.

---

### 5️⃣ Rozšíření dle vlastní volby *(bonusové body)*

Vyber a implementuj **alespoň jedno** z následujících rozšíření:

- **A)** Přidej třídu `NakladniAuto` s atributem `nosnost` (v tunách). Přepiš metodu jízdy tak, aby zohledňovala aktuální náklad.
- **B)** Přidej metodu `nejusetrnějsi_vozidlo()` do `VozovyPark`, která vrátí vozidlo s nejnižší spotřebou na 100 km.
- **C)** Přidej do každého vozidla evidenci ujeté vzdálenosti (celkový odometr) a metodu pro jeho výpis.

---

## Nápovědy a tipy

**Tip k abstraktní třídě:**
Zamysli se, zda dává smysl volat `Vozidlo("značka", ...)` přímo. Pokud ne, použij `ABC` a `@abstractmethod` stejně jako u třídy `Tvar` ve cvičení se želvou.

**Tip ke spotřebě:**
Spotřeba se typicky udává v litrech na 100 km (u spalovacích motorů) nebo v kWh na 100 km (u elektroaut). Při jízdě na vzdálenost `d` km spotřebuješ:

```
spotreba_celkem = (spotreba_na_100km / 100) * d
```

**Tip k polymorfismu:**
Místo větvení `if`/`elif` přes typy stačí volat `vozidlo.jed(vzdalenost)` v cyklu. Každý objekt ví, jak se chovat – to je podstata polymorfismu.

**Tip ke kompozici:**
Třída `VozovyPark` by mohla uvnitř uchovávat seznam vozidel, například `self.vozidla = []`. Vozidla do něj přidáváš metodou, ne přímo.

---

## Minimální očekávaný výstup programu

Po spuštění by měl program vypsat něco podobného (přesný formát si zvol sám):

```
=== Vozový park ===
Počet vozidel: 4

Toyota Corolla (Auto) – kapacita: 5 míst, spotřeba: 6.5 l/100km
Harley-Davidson (Motocykl) – kapacita: 2 místa, spotřeba: 4.0 l/100km
Mercedes Sprinter (Autobus) – kapacita: 30 míst, spotřeba: 18.0 l/100km
Tesla Model 3 (ElektroAuto) – kapacita: 5 míst, spotřeba: 15.0 kWh/100km

=== Všechna vozidla jedou 150 km ===
Toyota Corolla ujela 150 km, spotřebovala 9.75 l benzínu.
Harley-Davidson ujel 150 km, spotřeboval 6.0 l benzínu.
Mercedes Sprinter ujel 150 km, spotřeboval 27.0 l nafty.
Tesla Model 3 ujela 150 km, spotřebovala 22.5 kWh elektřiny.
```

---

## Struktura odevzdání

Vytvoř dva soubory `dopravni_system.py` (kde budou třídy) a `main.py`.

Na konci souboru musí být blok s ukázkou použití:

```python
if __name__ == "__main__":
    # vytvoření vozidel
    # vytvoření vozového parku
    # přidání vozidel
    # výpis přehledu
    # vyslání na trasu
```