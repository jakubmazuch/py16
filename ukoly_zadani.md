# Úloha: Vigenèrova šifra v OOP (Python)

## Cíl
Naprogramujte konzolovou aplikaci, která umí **šifrovat i dešifrovat** text pomocí **Vigenèrovy šifry**. Řešení musí být **objektové (OOP)** – hlavní logika bude zapouzdřena ve třídě.

> Vigenèrova šifra je „poskládaná Caesarova šifra“: pro každý znak textu se použije jiný posun podle znaku v klíči.

---

## Požadavky na program
### 1) OOP návrh
Vytvořte třídu `VigenereSifra`, která bude mít:

- `__init__(self, klic: str)`
- `odstran_diakritiku(self, text: str) -> str` *(volitelné, ale doporučené – viz níže)*
- `zasifruj(self, text: str) -> str`
- `desifruj(self, text: str) -> str`

> Inspirujte se strukturou třídy `CaesarSifra`, kterou jste dostali.

---

### 2) Abeceda a chování programu
- Používejte **anglickou abecedu**: `abcdefghijklmnopqrstuvwxyz`
- Program musí:
  - zachovat **velká/malá písmena** původního textu,
  - **nešifrovat** znaky mimo abecedu (mezery, tečky, čárky, čísla… se jen přepíšou),
  - pracovat pouze s písmeny `a–z` (proto doporučujeme odstranit diakritiku).

---

### 3) Klíč (klic)
- Klíč je řetězec (např. `"heslo"`).
- Klíč se používá cyklicky: pokud je text delší než klíč, pokračuje se znovu od začátku.
- Klíč **ovlivňuje jen písmena**, takže:
  - pokud v textu narazíte na znak mimo abecedu, klíč se **neposouvá** (klíč se posune až při šifrování písmena).

#### Validace klíče
- Klíč musí obsahovat alespoň jedno písmeno.
- Doporučení: odstraňte z klíče diakritiku a jiné znaky, případně je ignorujte.

---

## Jak funguje šifrování (specifikace)
Pro každý znak `text[i]`, který je písmeno:

1. Vezměte odpovídající znak klíče `k` (používaný cyklicky).
2. Posun je:  
   `posun = index(k)`, kde `index('a') = 0`, `index('b') = 1`, …, `index('z') = 25`
3. Šifrování:
   - `novyIndex = (index(znak) + posun) % 26`
4. Dešifrování:
   - `novyIndex = (index(znak) - posun) % 26`

---

## Konzolové rozhraní (main)
V souboru `main.py` vytvořte program, který:

1. Zeptá se uživatele:
   - zda chce **šifrovat** nebo **dešifrovat** (např. volba `1/2` nebo `s/d`)
   - na **klíč**
   - na **text**
2. Vytvoří objekt `VigenereSifra(klic)`
3. Vypíše výsledek

---

## Doporučené rozdělení do souborů
- `vigenere.py` – třída `VigenereSifra`
- `main.py` – komunikace s uživatelem, volání metod třídy

---

## Příklad chování programu (orientačně)
Zvol akci (s = šifrovat, d = dešifrovat): s
Zadej klíč: heslo
Zadej text: Ahoj světe!
Výsledek: ...
---

## Testovací případy (které musí projít)
Zkuste si sami ověřit, že platí:

- `desifruj(zasifruj(text)) == text` *(alespoň pro text bez diakritiky)*
- Text s mezerami a interpunkcí zachová stejné znaky na stejných místech.
- Velká písmena zůstanou velká.

---

## Bonus (volitelné rozšíření)
- Přidejte možnost zadat posun/volbu abecedy.
- Přidejte opakované menu (program běží, dokud uživatel neukončí).
- Ošetřete vstupy pomocí `try/except` a validace (prázdný klíč, špatná volba akce).
- Umožněte „čistý klíč“: odstranění diakritiky + ponechání jen písmen.

---

## Hodnocení
- **Správnost algoritmu** (šifrování i dešifrování)
- **OOP struktura** (třída, metody, zapouzdření)
- **Čitelnost kódu** (názvy proměnných, komentáře, struktura)
- **Zpracování okrajových případů** (mezery, interpunkce, klíč, velká písmena)