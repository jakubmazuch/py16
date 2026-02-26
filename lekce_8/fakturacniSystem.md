# 🧾 Samostatná práce – Fakturační systém (OOP v praxi)

## Kontext

Jste součástí týmu, který vyvíjí jednoduchý interní fakturační systém pro menší firmu.  
Systém musí podporovat různé typy dokladů a umožnit jejich jednotné zpracování.

Cílem je navrhnout objektový model tak, aby byl:

- rozšiřitelný,
- přehledný,
- založený na abstrakci,
- bez použití zbytečných podmínek typu `if isinstance(...)`.

---

## Požadavky

### 1️⃣ Abstraktní třída

Vytvořte abstraktní třídu `Doklad`.

Musí obsahovat:

- číslo dokladu  
- zákazníka  
- seznam položek  
- datum vystavení  

Metody:

- `soucet_bez_dph()` – spočítá součet všech položek  
- **abstraktní metoda** `celkova_castka()`  
- metoda `typ()` – vrací textový název dokladu  

Použijte `abc.ABC` a `@abstractmethod`.

---

### 2️⃣ Položka dokladu

Vytvořte třídu `Polozka`, která obsahuje:

- název
- množství
- cenu za kus

Musí umět spočítat svou celkovou cenu.

---

### 3️⃣ Konkrétní typy dokladů (dědičnost)

Implementujte minimálně tři potomky třídy `Doklad`:

- `Faktura`
- `Zaloha`
- `Dobropis`

Každý typ musí:

- implementovat metodu `celkova_castka()`
- případně upravit chování metody `typ()`

Pravidla výpočtu si navrhněte realisticky (např. práce s DPH, záporné částky, procentuální záloha apod.).

---

### 4️⃣ Polymorfismus v praxi

Vytvořte třídu `Uctarna`, která:

- přijme seznam různých dokladů,
- vypíše jejich přehled,
- spočítá celkový obrat.

Důležité:

- Nesmí se používat podmínky podle typu objektu.
- Musí fungovat čistě polymorfně.

---

## Technické požadavky

- použití abstraktní třídy
- dědičnost
- polymorfismus
- rozdělení do více souborů
- čistý, čitelný návrh

---

## Odevzdání

Projekt musí obsahovat:

- funkční hlavní soubor `main.py`
- alespoň 3 různé doklady v ukázce
- komentovaný kód

---

## Cíl

Ukázat, že rozumíte:

- rozdílu mezi abstrakcí a implementací
- principu dědičnosti
- polymorfismu v praxi
- návrhu rozšiřitelného systému
