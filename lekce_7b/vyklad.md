# Objektově orientované programování v Pythonu
### Výukový materiál ke kódu s želvou (turtle)

---

## Obsah

1. [Co je OOP a proč ho používáme?](#1-co-je-oop-a-proč-ho-používáme)
2. [Třídy a objekty](#2-třídy-a-objekty)
3. [Atributy a metody](#3-atributy-a-metody)
4. [Konstruktor `__init__`](#4-konstruktor-__init__)
5. [Dědičnost](#5-dědičnost)
6. [`super()` – volání rodiče](#6-super--volání-rodiče)
7. [Abstraktní třídy a abstraktní metody](#7-abstraktní-třídy-a-abstraktní-metody)
8. [Polymorfismus](#8-polymorfismus)
9. [Kompozice](#9-kompozice)
10. [Kompletní přehled kódu s komentáři](#10-kompletní-přehled-kódu-s-komentáři)
11. [Shrnutí pojmů](#11-shrnutí-pojmů)

---

## 1. Co je OOP a proč ho používáme?

Programování lze přistupovat různými způsoby – tzv. **paradigmaty**. Dva nejrozšířenější jsou:

- **Procedurální programování** – píšeme příkazy jeden za druhým, funkce pracují s daty, která jim předáváme jako argumenty.
- **Objektově orientované programování (OOP)** – data a funkce, které s nimi pracují, **svazujeme dohromady** do celků zvaných **objekty**.

### Proč OOP?

Představ si, že píšeš program pro zoo. Procedurálně bys měl třeba proměnné `lev_jmeno`, `lev_vek`, `tygr_jmeno`, `tygr_vek` a funkce `nakrm_lva()`, `nakrm_tygra()`. Při stovce zvířat se kód stane nepřehledným.

V OOP místo toho vytvoříš **třídu** `Zvire`, která v sobě nese jak data (jméno, věk), tak chování (nakrmení). Každé konkrétní zvíře je pak **objekt** (instance) této třídy.

**Výhody OOP:**
- **Přehlednost** – kód je organizovaný do logických celků
- **Znovupoužitelnost** – jednou napsanou třídu použijeme mnohokrát
- **Rozšiřitelnost** – přidáme nové typy bez přepisování starého kódu
- **Údržba** – oprava chyby na jednom místě se projeví všude

---

## 2. Třídy a objekty

### Třída (class)

**Třída** je **šablona** (předpis, plán) pro vytváření objektů. Sama o sobě nic nedělá – je to jen popis toho, jak budou objekty vypadat a co budou umět.

```python
class Pes:
    pass  # prázdná třída
```

### Objekt (instance)

**Objekt** je **konkrétní výskyt** třídy – skutečná věc vytvořená podle šablony.

```python
rex = Pes()   # rex je objekt (instance) třídy Pes
brok = Pes()  # brok je jiný objekt téže třídy
```

`rex` a `brok` jsou oba psi, ale jsou to dva různé objekty. Každý si nese vlastní data.

### Analogie

| Pojem | Analogie |
|-------|----------|
| Třída | Architektonický výkres domu |
| Objekt | Konkrétní postavený dům podle výkresu |
| Atribut | Barva domu, počet oken |
| Metoda | Co se v domě děje (vaření, spaní) |

---

## 3. Atributy a metody

### Atributy

**Atributy** jsou proměnné patřící objektu. Ukládají jeho **stav** (data).

```python
class Pes:
    def __init__(self):
        self.jmeno = "Rex"   # atribut
        self.vek = 3          # atribut
```

Klíčové slovo `self` odkazuje na **konkrétní objekt**, se kterým právě pracujeme. Díky `self` si každý objekt nese svá vlastní data.

```python
rex = Pes()
brok = Pes()
brok.jmeno = "Brok"

print(rex.jmeno)   # Rex
print(brok.jmeno)  # Brok
```

### Metody

**Metody** jsou funkce patřící třídě. Definují **chování** objektu.

```python
class Pes:
    def __init__(self):
        self.jmeno = "Rex"

    def stekej(self):           # metoda
        print(f"{self.jmeno}: Haf!")
```

Volání metody:
```python
rex = Pes()
rex.stekej()  # Rex: Haf!
```

> **Důležité:** Každá metoda třídy přijímá jako **první parametr `self`**. Python ho doplní automaticky při volání – ty ho nepíšeš při volání, jen při definici.

---

## 4. Konstruktor `__init__`

**Konstruktor** je speciální metoda `__init__`, která se zavolá **automaticky při vytvoření objektu**. Slouží k **inicializaci atributů** – nastavení počátečního stavu objektu.

```python
class Tvar:
    def __init__(self, velikost, rychlost=6):
        self.velikost = velikost   # uložíme parametr jako atribut
        self.rychlost = rychlost
```

Při vytvoření objektu předáváme argumenty konstruktoru:
```python
ctverec = Tvar(100)        # velikost=100, rychlost=6 (výchozí hodnota)
trojuhelnik = Tvar(50, 3)  # velikost=50, rychlost=3
```

### Výchozí hodnoty parametrů

Parametr `rychlost=6` má **výchozí hodnotu** – pokud ho při vytváření objektu nevyplníme, automaticky se použije hodnota `6`. Toto platí pro obyčejné funkce i pro konstruktory.

---

## 5. Dědičnost

**Dědičnost** (inheritance) je mechanismus, kdy nová třída **přebírá** vlastnosti a metody jiné třídy.

- Třída, ze které se dědí = **rodič** (parent, nadtřída, superclass)
- Třída, která dědí = **potomek** (child, podtřída, subclass)

### Proč dědičnost?

Chceme vytvořit třídy `Trojuhelnik`, `Ctverec`, `Sestiuhlenik`. Všechny mají společné vlastnosti (`velikost`, `rychlost`) a společnou metodu (`nastav_zelvu`). Místo abychom tyto věci psali třikrát, vytvoříme společného rodiče.

```python
class PravidelnyMnohouhelnik(Tvar):  # dědíme z třídy Tvar
    def __init__(self, n, velikost, rychlost=6):
        super().__init__(velikost, rychlost)  # zavoláme konstruktor rodiče
        self.n = n
```

Zápis `class PravidelnyMnohouhelnik(Tvar):` říká: „Tato třída dědí z třídy `Tvar`."

Potomek **zdědí** všechny metody rodiče, takže například `nastav_zelvu()` nemusí psát znovu.

### Hierarchie dědičnosti v našem kódu

```
Tvar  (abstraktní)
  └── PravidelnyMnohouhelnik
        ├── Trojuhelnik
        ├── Ctverec
        └── Sestiuhlenik
```

Každá třída v hierarchii rozšiřuje nebo upřesňuje svého rodiče.

### Příklad dědičnosti v praxi

```python
class Trojuhelnik(PravidelnyMnohouhelnik):
    def __init__(self, velikost, rychlost=6):
        super().__init__(3, velikost, rychlost)  # n=3, zbytek předá rodiči
```

Třída `Trojuhelnik` nepotřebuje vlastní metodu `kresli()` – zdědí ji od `PravidelnyMnohouhelnik`. Jedinou věcí, která ji odlišuje, je že `n` je vždy `3`.

---

## 6. `super()` – volání rodiče

`super()` vrací **odkaz na nadřazenou třídu**. Nejčastěji ho používáme v konstruktoru potomka, abychom zavolali konstruktor rodiče.

```python
class Ctverec(PravidelnyMnohouhelnik):
    def __init__(self, velikost, rychlost=6):
        super().__init__(4, velikost, rychlost)
        #     ↑ voláme PravidelnyMnohouhelnik.__init__(4, velikost, rychlost)
```

Bez `super().__init__(...)` by se atributy rodiče (`self.velikost`, `self.rychlost`, `self.n`) **nenastavily** a kód by selhal.

Řetěz volání při vytvoření `Ctverec(100)`:

```
Ctverec.__init__(100)
  → PravidelnyMnohouhelnik.__init__(4, 100, 6)
      → Tvar.__init__(100, 6)
          → self.velikost = 100
          → self.rychlost = 6
      → self.n = 4
```

---

## 7. Abstraktní třídy a abstraktní metody

### Problém bez abstraktních tříd

Představ si, že někdo omylem vytvoří objekt přímo z třídy `Tvar`:
```python
tvar = Tvar(100)
tvar.kresli()  # Co by se mělo stát? Tvar neví, jak se kreslit!
```

Třída `Tvar` je záměrně **obecná** – nemá žádný konkrétní tvar. Nechceme, aby z ní šlo vytvářet objekty.

### Řešení: Abstraktní třída (ABC)

**Abstraktní třída** je třída, ze které **nemůžeme přímo vytvořit objekt**. Slouží pouze jako základ pro dědičnost.

V Pythonu ji vytvoříme pomocí modulu `abc`:

```python
from abc import ABC, abstractmethod

class Tvar(ABC):   # ABC = Abstract Base Class
    ...
```

Pokud se nyní někdo pokusí vytvořit objekt přímo:
```python
tvar = Tvar(100)  # ❌ TypeError: Can't instantiate abstract class Tvar
```

Python vyhodí chybu. To je **záměrné** – abstraktní třída říká: „Jsem jen šablona, použij mé potomky."

### Abstraktní metoda

**Abstraktní metoda** je metoda, která je v rodičovské třídě **deklarována, ale neimplementována**. Každý potomek ji **musí implementovat**, jinak nemůže ani on vytvářet objekty.

```python
class Tvar(ABC):
    @abstractmethod
    def kresli(self):
        pass  # žádná implementace!
```

Dekorátor `@abstractmethod` říká Pythonu: „Tato metoda musí být přepsána v potomkovi."

```python
class Trojuhelnik(PravidelnyMnohouhelnik):
    # kresli() zdědí od PravidelnyMnohouhelnik – OK

class MujTvar(Tvar):
    # nepřepíše kresli()
    pass

obj = MujTvar(100)  # ❌ Chyba! kresli() není implementována.
```

### Proč to je užitečné?

Abstraktní třídy a metody jsou **smlouvou**: garantují, že každý potomek bude mít určité metody. Díky tomu můžeme psát kód, který pracuje s obecným rozhraním, aniž bychom znali konkrétní typ.

```python
# Toto bude fungovat pro JAKÝKOLIV potomek třídy Tvar
def nakresli_tvar(tvar: Tvar):
    tvar.nastav_zelvu()
    tvar.kresli()  # víme, že tato metoda existuje díky abstraktní třídě
```

---

## 8. Polymorfismus

**Polymorfismus** (z řečtiny: „mnoho forem") znamená, že **různé objekty reagují na stejnou zprávu různým způsobem**.

V praxi: voláme stejnou metodu (`kresli()`), ale výsledek je pokaždé jiný, podle toho, jakého typu je objekt.

```python
tvary = [
    Trojuhelnik(80),
    Ctverec(80),
    Sestiuhlenik(80),
]

for tvar in tvary:
    tvar.nastav_zelvu()
    tvar.kresli()  # pokaždé jiný výsledek!
```

Nemusíme psát:
```python
if type(tvar) == Trojuhelnik:
    kresli_trojuhelnik()
elif type(tvar) == Ctverec:
    kresli_ctverec()
# ...
```

Kód je díky polymorfismu **čistší, kratší a snáze rozšiřitelný**.

### Polymorfismus v třídě Mrizka

```python
class Mrizka:
    def __init__(self, tvar: Tvar, pocet, x=150, y=150):
        self.tvar = tvar   # může být Trojuhelnik, Ctverec, nebo cokoliv jiného
        ...

    def kresli(self):
        ...
        self.tvar.kresli()  # polymorfismus! Mrizka neví, co za tvar dostala
```

Třída `Mrizka` ví jen to, že dostane **nějaký** objekt, který umí `kresli()`. Nezajímá ji typ – to je podstata polymorfismu.

### Přetížení metod (Override)

Potomek může **přepsat** (override) metodu rodiče – dát jí novou implementaci:

```python
class PravidelnyMnohouhelnik(Tvar):
    def kresli(self):
        uhel = 360 / self.n
        for _ in range(self.n):
            turtle.forward(self.velikost)
            turtle.right(uhel)
```

Třída `PravidelnyMnohouhelnik` implementuje abstraktní metodu `kresli()` ze třídy `Tvar`. Tím „splňuje smlouvu" abstraktní třídy.

---

## 9. Kompozice

**Kompozice** (composition) je alternativní způsob sdílení funkcionality oproti dědičnosti. Místo aby třída **dědila** z jiné třídy, **obsahuje** objekt jiné třídy.

> **Dědičnost:** „Je to" (Čtverec **je** Tvar)
> **Kompozice:** „Má" nebo „používá" (Mřížka **má** Tvar)

### Příklad v kódu

Třída `Mrizka` nedědí z `Tvar`. Místo toho dostane objekt typu `Tvar` jako parametr:

```python
class Mrizka:
    def __init__(self, tvar: Tvar, pocet, x=150, y=150):
        self.tvar = tvar   # Mrizka "obsahuje" objekt Tvar
        self.pocet = pocet
        self.x = x
        self.y = y
```

Při vytváření:
```python
ctverec = Ctverec(50)
mrizka = Mrizka(ctverec, 4)   # předáme objekt
mrizka.kresli()
```

### Výhody kompozice oproti dědičnosti

Dědičnost vytváří **pevné vazby** mezi třídami – pokud změníme rodiče, ovlivníme všechny potomky. Kompozice je **flexibilnější**: `Mrizka` může pracovat s jakýmkoliv tvarem, dokonce i s tvary, které ještě nebyly napsány.

```python
# Funguje s čtvercem
mrizka1 = Mrizka(Ctverec(50), 3)

# Funguje s trojúhelníkem
mrizka2 = Mrizka(Trojuhelnik(50), 3)

# Funguje s osmiúhelníkem (i kdyby byl napsán až za rokem)
mrizka3 = Mrizka(PravidelnyMnohouhelnik(8, 50), 3)
```

---

## 10. Kompletní přehled kódu s komentáři

Nyní si projdeme celý kód krok po kroku s detailními vysvětlivkami.

### Import a základní nastavení

```python
import turtle
from abc import ABC, abstractmethod
```

- `turtle` – modul pro kreslení pomocí „želvy" (grafické pero)
- `ABC`, `abstractmethod` – nástroje pro vytváření abstraktních tříd

---

### Třída `Tvar` – abstraktní základ

```python
class Tvar(ABC):
    def __init__(self, velikost, rychlost=6):
        self.velikost = velikost   # délka strany / velikost tvaru
        self.rychlost = rychlost   # rychlost kreslení (1–10)
```

- Dědí z `ABC` → je abstraktní, nelze z ní přímo vytvářet objekty
- Konstruktor uloží společné atributy všech tvarů

```python
    def nastav_zelvu(self, x=0, y=0):
        turtle.shape("turtle")
        turtle.speed(self.rychlost)
        turtle.penup()        # zvedne pero (nekreslí při pohybu)
        turtle.goto(x, y)     # přesune na počáteční pozici
        turtle.pendown()      # spustí pero (začne kreslit)
```

- Konkrétní metoda (ne abstraktní) – dědí ji všichni potomci bez nutnosti přepsat

```python
    @abstractmethod
    def kresli(self):
        pass
```

- Abstraktní metoda – každý potomek **musí** tuto metodu implementovat

---

### Třída `PravidelnyMnohouhelnik`

```python
class PravidelnyMnohouhelnik(Tvar):
    def __init__(self, n, velikost, rychlost=6):
        super().__init__(velikost, rychlost)   # inicializace rodiče
        if n < 3:
            raise ValueError("n musí být alespoň 3.")
        self.n = n   # počet stran
```

- `raise ValueError(...)` – pokud zadáme nesmyslné `n`, Python vyhodí chybu s vysvětlením
- Toto se nazývá **validace vstupů** – bráníme vytvoření neplatného objektu

```python
    def kresli(self):
        uhel = 360 / self.n   # vnější úhel pravidelného n-úhelníku
        for _ in range(self.n):
            turtle.forward(self.velikost)   # krok vpřed
            turtle.right(uhel)              # otočení
```

**Geometrické vysvětlení:** Součet všech vnějších úhlů pravidelného mnohoúhelníku je vždy 360°. Pro čtverec (n=4) je to 90°, pro trojúhelník (n=3) je to 120°, pro šestiúhelník (n=6) je to 60°.

---

### Specializované třídy

```python
class Trojuhelnik(PravidelnyMnohouhelnik):
    def __init__(self, velikost, rychlost=6):
        super().__init__(3, velikost, rychlost)   # n je vždy 3
```

Tyto třídy jsou minimalistické – pouze nastavují `n` na správnou hodnotu. Metodu `kresli()` dědí od `PravidelnyMnohouhelnik` beze změny.

Proč je to dobré? Pokud bychom někdy opravili chybu v `kresli()`, oprava se automaticky projeví i v `Trojuhelnik`, `Ctverec` i `Sestiuhlenik`.

---

### Třída `Mrizka`

```python
class Mrizka:
    def __init__(self, tvar: Tvar, pocet, x=150, y=150):
        self.tvar = tvar     # objekt tvaru (kompozice!)
        self.pocet = pocet   # počet tvarů v řadě/sloupci
        self.x = x           # počáteční x souřadnice
        self.y = y           # počáteční y souřadnice
```

Anotace `tvar: Tvar` říká: „Očekáváme objekt typu `Tvar`." Jde o tzv. **type hint** – Python ji nevynutí, ale je to dokumentace pro programátora.

```python
    def kresli(self):
        self.tvar.nastav_zelvu(self.x, self.y)

        for _ in range(self.pocet):           # pro každý řádek
            for _ in range(self.pocet):       # pro každý sloupec
                self.tvar.kresli()            # nakresli tvar (polymorfismus)
                turtle.forward(self.tvar.velikost)   # posuň se doprava

            # Návrat na začátek řádku
            turtle.backward(self.tvar.velikost * self.pocet)

            # Posunutí o řádek dolů
            turtle.right(90)
            turtle.forward(self.tvar.velikost)
            turtle.left(90)

        turtle.done()   # ukončení animace
```

---

## 11. Shrnutí pojmů

| Pojem | Definice | Příklad v kódu |
|-------|----------|----------------|
| **Třída** | Šablona pro vytváření objektů | `class Tvar`, `class Ctverec` |
| **Objekt** | Konkrétní instance třídy | `ctverec = Ctverec(100)` |
| **Atribut** | Proměnná patřící objektu | `self.velikost`, `self.n` |
| **Metoda** | Funkce patřící třídě | `nastav_zelvu()`, `kresli()` |
| **Konstruktor** | Speciální metoda `__init__` | `def __init__(self, velikost, ...)` |
| **Abstraktní třída** | Třída, ze které nelze vytvořit objekt | `class Tvar(ABC)` |
| **Abstraktní metoda** | Metoda bez implementace, musí ji přepsat potomek | `@abstractmethod def kresli(self)` |
| **Dědičnost** | Potomek přebírá vlastnosti rodiče | `class Ctverec(PravidelnyMnohouhelnik)` |
| **`super()`** | Odkaz na nadřazenou třídu | `super().__init__(...)` |
| **Override** | Přepsání metody rodiče v potomkovi | `kresli()` v `PravidelnyMnohouhelnik` přepisuje abstraktní `kresli()` z `Tvar` |
| **Polymorfismus** | Stejná metoda, různé chování podle typu | `self.tvar.kresli()` v `Mrizka` |
| **Kompozice** | Třída obsahuje objekt jiné třídy | `Mrizka` obsahuje `Tvar` |

---

## Bonusové příklady – jak kód použít

```python
# Vytvoření a nakreslení čtverce
c = Ctverec(100)
c.nastav_zelvu()
c.kresli()
turtle.done()

# Mřížka 3x3 trojúhelníků
t = Trojuhelnik(60)
mrizka = Mrizka(t, 3)
mrizka.kresli()

# Mřížka 4x4 šestiúhelníků
s = Sestiuhlenik(40)
mrizka = Mrizka(s, 4, x=-200, y=200)
mrizka.kresli()

# Libovolný n-úhelník – např. dvanáctistěn
dvanactistran = PravidelnyMnohouhelnik(12, 80)
mrizka = Mrizka(dvanactistran, 2)
mrizka.kresli()
```

---

## Časté chyby a jak se jim vyhnout

**Zapomenutí `self` v parametrech metody:**
```python
# ❌ Špatně
def kresli():
    pass

# ✅ Správně
def kresli(self):
    pass
```

**Nezavolání `super().__init__()`:**
```python
# ❌ Špatně – atributy rodiče se nenastaví
class Ctverec(PravidelnyMnohouhelnik):
    def __init__(self, velikost):
        self.n = 4  # chybí super().__init__()!

# ✅ Správně
class Ctverec(PravidelnyMnohouhelnik):
    def __init__(self, velikost):
        super().__init__(4, velikost)
```

**Přímé vytvoření abstraktní třídy:**
```python
# ❌ Způsobí TypeError
tvar = Tvar(100)

# ✅ Správně – vytvoříme konkrétního potomka
tvar = Ctverec(100)
```

**Neimplementování abstraktní metody v potomkovi:**
```python
# ❌ Způsobí TypeError při vytváření objektu
class MujTvar(Tvar):
    pass  # kresli() není implementována

obj = MujTvar(100)  # TypeError!

# ✅ Správně
class MujTvar(Tvar):
    def kresli(self):
        # vlastní implementace
        pass
```