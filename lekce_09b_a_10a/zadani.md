# 🧾 Zadání – Refaktorizace systému pomocí abstraktních vlastností

---

## Kontext

Ve stávajícím fakturačním systému:

- `Doklad` je abstraktní třída
- `Faktura`, `Zaloha`, `Dobropis` ji dědí
- některé hodnoty jsou počítané (`dph`, `celkova_castka`)
- používáš `@property` pro zapouzdření

Cílem je systém dále **zpřesnit architektonicky** a odstranit zbytečné rozdíly v rozhraní tříd.

---

# 🎯 Cíl úlohy

1. Zavést **abstraktní property** do rodičovské třídy.
2. U všech dokladů sjednotit rozhraní.
3. Upravit `Uctarna`, aby nikdy nepoužívala závorky.
4. Odstranit jakékoliv `isinstance()`.

---

# 🔷 ČÁST 1 – Abstraktní property

V třídě `Doklad`:

- změň metodu `celkova_castka()` na **abstraktní property**.

Tedy místo:

```python
@abstractmethod
def celkova_castka(self) -> float:
    ...
```

musí vzniknout abstraktní property.

💡 Nápověda: kombinace `@property` + `@abstractmethod`.

---

# 🔷 ČÁST 2 – Refaktor potomků

Ve všech potomcích:

- `celkova_castka` musí být `@property`
- nesmí se používat závorky

Například:

```python
@property
def celkova_castka(self) -> float:
    ...
```

---

# 🔷 ČÁST 3 – DPH jako univerzální property

Momentálně má `dph` jen `Faktura`.

Uprav systém tak, aby:

- každý doklad měl property `dph`
- u `Zaloha` a `Dobropis` vracela `0.0`
- `Uctarna` už nemusela řešit typ dokladu

Tím odstraníš:

```python
isinstance(...)
```

To je důležité z hlediska polymorfismu.

---

# 🔷 ČÁST 4 – Refaktor Učtárny

V `Uctarna`:

- používej jen vlastnosti
- žádné závorky
- žádné podmínky podle typu

Například:

```python
w.celkova_castka
w.dph
```

---

# 🔷 ČÁST 5 – Nový typ dokladu

Přidej nový typ:

## `SlevaDoklad`

### Chování:

- počítá celkovou částku jako běžná faktura
- ale aplikuje slevu v procentech
- DPH se počítá až po slevě

Třída musí fungovat bez úprav v `Uctarna`.

---

# 🧠 Architektonický cíl

Výsledný systém musí splňovat:

- žádné `isinstance()`
- žádné `if typ ==`
- jednotné rozhraní tříd
- čistý polymorfismus
- všechny výpočty přes `@property`

---

# 🔥 Extra výzva

Do rodičovské třídy přidej:

```python
@property
def pocet_polozek(self) -> int:
```

která bude fungovat pro všechny typy dokladů.

---

# 📌 Kritéria hotového řešení

- Kód je čitelný a konzistentní
- Všechny doklady mají stejné veřejné rozhraní
- Učtárna pracuje pouze přes polymorfismus
- Systém je otevřený pro další rozšíření bez úprav stávající logiky
