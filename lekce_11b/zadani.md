# Samostatná práce – Půjčovna aut

## Kontext

Půjčovna aut eviduje svá vozidla a umožňuje jejich krátkodobé zapůjčení.  
Každé auto má svou cenu za den a může být buď **volné**, nebo **rezervované**.

Pokud je auto volné, zákazník si ho může rezervovat na určitý počet dní.  
V takovém případě je potřeba spočítat cenu půjčení.

Pokud je auto již rezervované, rezervaci nelze provést.

Cílem je navrhnout jednoduchý objektový model této situace.

---

## Zadání

Navrhni a implementuj jednoduchý systém půjčovny aut.

Program bude pracovat s několika auty, která může uživatel rezervovat.

Použij objektový přístup a rozděl program alespoň do dvou tříd.

---

## 1. Třída `Auto`

Vytvoř třídu `Auto`.

Každé auto bude mít například tyto informace:

- značka
- model
- cena za den půjčení
- informace, zda je auto rezervované

Auto by mělo umět:

- vrátit svůj název (např. značka + model)
- zjistit, zda je volné
- spočítat cenu za zadaný počet dní
- provést rezervaci
- zrušit rezervaci

Rozmysli, které informace mají být **atributy** a které operace mají být **metody**.

---

## 2. Třída `Pujcovna`

Vytvoř třídu `Pujcovna`, která bude spravovat více aut.

Třída může obsahovat například:

- seznam aut
- metodu pro přidání auta
- výpis všech aut
- výpis pouze volných aut
- pokus o rezervaci vybraného auta

Rezervace by měla proběhnout pouze v případě, že je auto volné.

---

## 3. Hlavní program

V hlavním programu:

1. vytvoř několik aut,
2. přidej je do půjčovny,
3. vypiš nabídku aut,
4. zkus provést několik rezervací.

Vyzkoušej také situaci, kdy se uživatel pokusí rezervovat auto, které je již obsazené.

---

## Podmínky

- počet dní musí být kladné číslo
- cena za den nesmí být záporná
- auto, které je již rezervované, nelze rezervovat znovu

---

## Doporučená struktura souborů


auto.py
pujcovna.py
main.py


---

## Poznámka

Snaž se, aby logika programu byla umístěna v třídách.  
Hlavní program by měl objekty pouze vytvářet a používat jejich metody.
"""

output_path = "/mnt/data/zadani_pujcovna_aut.md"
pypandoc.convert_text(text, 'md', format='md', outputfile=output_path, extra_args=['--standalone'])

output_path