# 🧾 Fakturační systém – Teoretický podklad a komentáře kódu

## 📚 Teoretický background

### Smysl OOP?

OOP je paradigma, které organizuje kód do **objektů** – instancí tříd. Objekt kombinuje **data** (= atributy) a **chování** (= metody) do jednoho celku. 
Oproti předchozímu přístupu (procedurální programování) je OOP přehlednější, lépe rozšiřitelné a umožňuje znovupoužití kódu.

Čtyři základní principy OOP:

| Princip | Popis |
|---|---|
| **Zapouzdření** | Skrytí vnitřní implementace, přístup přes metody |
| **Dědičnost** | Třída přebírá vlastnosti jiné třídy |
| **Polymorfismus** | Stejné rozhraní, různé chování podle typu |
| **Abstrakce** | Definice „co", bez „jak" – odkládáme implementaci na potomky |

---

### Abstraktní třída a `abc` modul

**Abstraktní třída** je třída, ze které nelze přímo vytvořit instanci. Slouží jako „šablona" pro potomky – definuje rozhraní, které musí potomci implementovat.

V Pythonu se abstraktní třídy tvoří pomocí modulu `abc`:

```python
from abc import ABC, abstractmethod

class Tvar(ABC):
    @abstractmethod
    def obsah(self) -> float:
        pass  # Žádná implementace – potomek ji MUSÍ dodat
```

Pokud potomek neimplementuje všechny abstraktní metody, Python při pokusu o vytvoření instance vyhodí `TypeError`.

```python
class Ctverec(Tvar):
    def __init__(self, strana: float):
        self.strana = strana

    def obsah(self) -> float:
        return self.strana ** 2

# Tvar() → TypeError: Can't instantiate abstract class
# Ctverec(5) → funguje ✓
```

---

### Dědičnost

Dědičnost umožňuje jedné třídě (**potomek**) přebírat atributy a metody jiné třídy (**rodič**). Potomek může:

- **zdědit** metody rodiče beze změny,
- **přepsat (override)** metodu vlastní implementací,
- **rozšířit** rodiče o nové atributy a metody.

```python
class Zvire:
    def zvuk(self) -> str:
        return "..."

class Pes(Zvire):
    def zvuk(self) -> str:  # přepíše metodu rodiče
        return "Haf!"
```

Volání konstruktoru rodiče se provádí přes `super().__init__(...)`.

---

### Polymorfismus

Polymorfismus (řecky „mnoho tvarů") znamená, že různé objekty reagují na **stejné volání metody** různým způsobem. Díky tomu lze pracovat s různými typy dokladů jednotně, aniž bychom potřebovali podmínky `if isinstance(...)`.

```python
doklady = [Faktura(...), Zaloha(...), Dobropis(...)]

for d in doklady:
    print(d.celkova_castka())  # Každý typ počítá jinak – polymorfismus
```

---

### Property (vlastnost) v Pythonu

`@property` umožňuje definovat metody, které se tváří jako atributy. Obvykle se používá spolu se setterem pro validaci hodnot při přiřazení.

```python
class Faktura:
    @property
    def sazba_dph(self):
        return self._sazba_dph

    @sazba_dph.setter
    def sazba_dph(self, value):
        if value < 0:
            raise ValueError("DPH nesmí být záporné.")
        self._sazba_dph = float(value)
```

Díky tomu `faktura.sazba_dph = -0.5` automaticky vyhodí chybu.

---

### Type hints (typové anotace)

Python je dynamicky typovaný jazyk, ale od verze 3.5+ podporuje **typové anotace**. Neovlivňují běh programu, ale zlepšují čitelnost a umožňují statickou analýzu nástrojem mypy.

```python
def vypocet(castka: float, sazba: float) -> float:
    return castka * sazba
```

Speciální typy z modulu `typing`:
- `List[Polozka]` – seznam instancí třídy `Polozka`
- `Dict[str, float]` – slovník s klíči `str` a hodnotami `float`
- `Iterable[Doklad]` – cokoli, přes co lze iterovat (seznam, generátor…)

Zápis `date | None` (Python 3.10+) znamená „buď `date`, nebo `None`".

---

## 📁 Struktura projektu

```
projekt/
├── polozka.py        # Datová třída pro jednu položku dokladu
├── doklad.py         # Abstraktní základní třída
├── typy_dokladu.py   # Konkrétní typy: Faktura, Záloha, Dobropis
├── uctarna.py        # Agregační třída pro zpracování dokladů
└── main.py           # Vstupní bod programu s ukázkovými daty
```

---

## 📄 `polozka.py` – Datová třída položky

```python
class Polozka:
    def __init__(self, nazev: str, mnozstvi: int, cena_za_ks: float):
        # Validace vstupů – obranné programování
        if not nazev or not nazev.strip():
            raise ValueError("Název položky nesmí být prázdný.")
        if mnozstvi <= 0:
            raise ValueError("Množství musí být kladné.")
        if cena_za_ks < 0:
            raise ValueError("Cena za ks nesmí být záporná.")

        # .strip() odstraní mezery na začátku a konci řetězce
        self.nazev = nazev.strip()
        # int() a float() zajistí správný typ i při předání "divné" hodnoty
        self.mnozstvi = int(mnozstvi)
        self.cena_za_ks = float(cena_za_ks)

    def cena_clk(self) -> float:
        # Celková cena = množství × cena za kus
        return self.mnozstvi * self.cena_za_ks

    def __repr__(self) -> str:
        # __repr__ se použije při tisku objektu (debug výpis)
        return f"Položka({self.nazev}, {self.mnozstvi}, {self.cena_za_ks})"
```

**Klíčové koncepty:**
- **Validace v konstruktoru** – třída sama hlídá správnost svých dat (zapouzdření)
- **`__repr__`** – speciální metoda pro textovou reprezentaci objektu (užitečné při ladění)
- **Obranné programování** – raději selhat rychle s jasnou chybou než tiše počítat špatně

---

## 📄 `doklad.py` – Abstraktní základní třída

```python
from abc import ABC, abstractmethod
from datetime import date
from typing import List
from polozka import Polozka


class Doklad(ABC):  # ABC = Abstract Base Class
    def __init__(self, cislo: str, zakaznik: str, polozky: List[Polozka], datum: date | None = None):
        # Validace povinných polí
        if not cislo or not cislo.strip():
            raise ValueError("Číslo dokladu nesmí být prázdné")
        if not zakaznik or not zakaznik.strip():
            raise ValueError("Zákazník nesmí být prázdné")
        if polozky is None or len(polozky) == 0:
            raise ValueError("Doklad musí mít aspoň jednu položku")

        self.cislo = cislo
        self.zakaznik = zakaznik
        # list() vytvoří kopii – objekt je pak nezávislý na původním seznamu
        self.polozky = list(polozky)
        # Pokud datum není zadáno, použije se dnešní den
        self.datum = datum if datum is not None else date.today()

    def soucet_bez_dph(self) -> float:
        # Generátorový výraz + sum() – pythonický způsob součtu
        # Volá metodu cena_clk() na každé položce – polymorfismus na úrovni položek
        return sum(p.cena_clk() for p in self.polozky)

    @abstractmethod
    def celkova_castka(self) -> float:
        # Abstraktní metoda – každý potomek MUSÍ implementovat vlastní výpočet
        # raise NotImplementedError je zde jen jako dokumentace záměru
        raise NotImplementedError

    def typ(self) -> str:
        # Výchozí implementace vrací název třídy (např. "Faktura")
        # Potomci ji mohou přepsat pro hezčí výstup (s diakritikou apod.)
        return self.__class__.__name__
```

**Klíčové koncepty:**
- **`ABC`** – značí, že třída je abstraktní; nelze vytvořit `Doklad(...)` přímo
- **`@abstractmethod`** – dekorátor vynutí implementaci v každém potomkovi
- **`date.today()`** – výchozí hodnota při nezadaném datu; trik s `None` jako výchozí parametr (vyhýbá se mutable default argument problému)
- **`list(polozky)`** – obranná kopie vstupu, aby úprava původního seznamu neovlivnila doklad

---

## 📄 `typy_dokladu.py` – Konkrétní typy dokladů

### `Faktura`

```python
class Faktura(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        sazba_dph: float = 0.21,  # Výchozí sazba DPH 21 %
        datum: date | None = None
    ):
        super().__init__(cislo, zakaznik, polozky, datum)  # Volání rodiče
        self.sazba_dph = float(sazba_dph)  # Spustí setter s validací

    @property
    def sazba_dph(self):
        # Getter – čtení hodnoty
        return self._sazba_dph

    @sazba_dph.setter
    def sazba_dph(self, value):
        # Setter – validace při zápisu; interní uložení do _sazba_dph (konvence)
        if value < 0:
            raise ValueError("DPH nesmí být záporné.")
        self._sazba_dph = float(value)

    @property
    def dph(self) -> float:
        # Vypočítaná vlastnost – DPH jako absolutní částka
        return self.soucet_bez_dph() * self.sazba_dph

    def celkova_castka(self) -> float:
        # Implementace abstraktní metody: základ + DPH
        return self.dph + self.soucet_bez_dph()

    def typ(self) -> str:
        return "Faktura"  # Přepsání metody rodiče pro hezčí výstup
```

### `Zaloha`

```python
class Zaloha(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        procento: float = 0.5,  # Výchozí záloha 50 %
        datum: date | None = None
    ):
        # Validace PŘED voláním super() – procento kontrolujeme hned
        if not (0 < procento <= 1):
            raise ValueError("Procento musí být v intervalu (0, 1].")
        super().__init__(cislo, zakaznik, polozky, datum)
        self.procento = float(procento)

    def celkova_castka(self):
        # Záloha = základ bez DPH × procento zálohy
        return self.soucet_bez_dph() * self.procento

    def typ(self):
        return "Záloha"
```

### `Dobropis`

```python
class Dobropis(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        procento_vraceni: float = 1.0,  # Výchozí vrácení 100 %
        datum: date | None = None
    ):
        if not (0 < procento_vraceni <= 1):
            raise ValueError("Procento vrácení musí být v intervalu (0, 1].")
        super().__init__(cislo, zakaznik, polozky, datum)
        self.procento_vraceni = float(procento_vraceni)

    def celkova_castka(self) -> float:
        # Záporná hodnota – dobropis snižuje pohledávku (vrácení peněz)
        return -(self.soucet_bez_dph() * self.procento_vraceni)

    def typ(self) -> str:
        return "Dobropis"
```

**Klíčové koncepty:**
- **`super().__init__(...)`** – povinné volání konstruktoru rodiče; inicializuje společná data
- **`@property` + setter** – u Faktury chrání sazbu DPH před zápornou hodnotou
- **Záporná hodnota u Dobropisu** – elegantní způsob, jak modelovat vrácení peněz; při sečtení s fakturami automaticky snižuje obrat

---

## 📄 `uctarna.py` – Agregační třída

```python
from typing import Iterable, Dict
from doklad import Doklad
from typy_dokladu import Faktura  # Import jen kvůli celkove_dph()


class Uctarna:
    def __init__(self, doklady: Iterable[Doklad]):
        # Iterable přijme jakýkoliv iterovatelný objekt (seznam, tuple, generátor)
        self.doklady = list(doklady)

    def vypis_prehled(self) -> None:
        print("=== Přehled dokladů ===")
        print("-" * 80)
        # f-string s formátovacími specifikátory: <12 = zarovnání vlevo na 12 znaků
        print(f"{'Číslo':<12} {'Typ':<10} {'Zákazník':<20} {'Datum':<12} {'Částka':>14}")
        print("-" * 80)
        for w in self.doklady:
            castka = w.celkova_castka()
            # Každý doklad zavolá SVOU verzi celkova_castka() – polymorfismus
            print(f"{w.cislo:<12} {w.typ():<10} {w.zakaznik:<20} {str(w.datum):<12} {castka:>14}")
        print("-" * 80)

    def obrat(self) -> float:
        # sum() s generátorovým výrazem – čistě polymorfní, bez podmínek
        return sum(w.celkova_castka() for w in self.doklady)

    def souhrn_podle_typu(self) -> Dict[str, float]:
        vysledek: Dict[str, float] = {}
        for w in self.doklady:
            # dict.get(klic, vychozi) vrátí hodnotu nebo výchozí, pokud klíč neexistuje
            vysledek[w.typ()] = vysledek.get(w.typ(), 0) + 1
        return vysledek

    def celkove_dph(self) -> float:
        # isinstance() je zde VÝJIMEČNĚ ospravedlnitelné – DPH existuje jen u Faktury
        # Alternativa by byla přidat metodu dph() do Doklad s výchozí hodnotou 0
        return sum(w.dph for w in self.doklady if isinstance(w, Faktura))
```

**Klíčové koncepty:**
- **`Iterable[Doklad]`** – parametr přijme jakýkoliv iterovatelný zdroj dokladů, nejen seznam
- **Polymorfismus v akci** – `obrat()` a `vypis_prehled()` volají `celkova_castka()` bez znalosti konkrétního typu; každý doklad počítá sám za sebe
- **`isinstance()` jako výjimka** – u `celkove_dph()` je to ospravedlnitelné, protože DPH je specifická vlastnost pouze faktur; ideální řešení by bylo přidat `dph()` do základní třídy s návratovou hodnotou 0

---

## 📄 `main.py` – Vstupní bod programu

```python
from polozka import Polozka
from typy_dokladu import Faktura, Zaloha, Dobropis
from uctarna import Uctarna


def main() -> None:
    # Vytvoření položek pro jednotlivé doklady
    polozky1 = [
        Polozka("Vývoj webu", 15, 1200),   # 15 hodin × 1200 Kč
        Polozka("Školení", 3, 1500),        # 3 dny × 1500 Kč
    ]
    polozky2 = [
        Polozka("Výuka matematiky", 16, 600),
        Polozka("Tvorba programu na míru", 20, 1500),
    ]
    polozky3 = [
        Polozka("Reklamace", 1, 3000),
    ]

    # Vytvoření různých typů dokladů – polymorfní seznam
    doklady = [
        Faktura("2026-01", "Abeceda s.r.o.", polozky1, sazba_dph=-0.2),   # Pozor: záporné DPH → vyhodí chybu!
        Zaloha("2026-Z01", "OMEGA s.r.o.", polozky2, procento=0.5),        # 50% záloha
        Dobropis("2026-D01", "Mr. Q", polozky3, procento_vraceni=1.0)      # 100% vrácení
    ]

    # Předání celého seznamu účtárně – pracuje s nimi polymorfně
    uctarna = Uctarna(doklady)
    uctarna.vypis_prehled()

    # Výpisy využívají metody třídy Uctarna
    print(f"Celkový obrat: {uctarna.obrat():.2f}")
    print(f"Celkové DPH (jen fa): {uctarna.celkove_dph():.2f}")
    print(f"Počet dokladů podle typu: {uctarna.souhrn_podle_typu()}")


# Standardní Python idiom: spustit main() jen při přímém spuštění souboru,
# ne při importu z jiného modulu
if __name__ == "__main__":
    main()
```

> ⚠️ **Pozor na chybu v `main.py`:** `sazba_dph=-0.2` je záporná hodnota – setter v třídě `Faktura` tuto hodnotu odmítne a vyhodí `ValueError`. Pravděpodobně šlo o záměr demonstrovat validaci, nebo je to překlep (správně by bylo `sazba_dph=0.21`).

---

## 🔄 Diagram závislostí tříd

```
         ┌─────────────┐
         │  Polozka    │  ← datová třída, žádná dědičnost
         └──────┬──────┘
                │ používá
         ┌──────▼──────┐
         │  Doklad     │  ← abstraktní třída (ABC)
         │  (abstract) │
         └──────┬──────┘
                │ dědí
    ┌───────────┼───────────┐
    ▼           ▼           ▼
┌────────┐ ┌────────┐ ┌──────────┐
│Faktura │ │Zaloha  │ │Dobropis  │
└────────┘ └────────┘ └──────────┘
    │           │           │
    └───────────┴───────────┘
                │ zpracovává
         ┌──────▼──────┐
         │  Uctarna    │
         └─────────────┘
```

---

## ✅ Shrnutí principů v projektu

| Princip | Kde se projevuje |
|---|---|
| **Abstrakce** | `Doklad` definuje rozhraní, ale ne implementaci `celkova_castka()` |
| **Dědičnost** | `Faktura`, `Zaloha`, `Dobropis` dědí z `Doklad` |
| **Polymorfismus** | `Uctarna.obrat()` volá `celkova_castka()` bez ohledu na konkrétní typ |
| **Zapouzdření** | `Polozka` a `Faktura` hlídají správnost svých dat přes validaci a property |
| **Rozšiřitelnost** | Nový typ dokladu stačí vytvořit jako potomka `Doklad` – `Uctarna` nepotřebuje změnu |
