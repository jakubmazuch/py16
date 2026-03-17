# 🚗 Samostatná práce – Parkoviště (OOP + soubor)

# Zadání

Navrhni a implementuj jednoduchý systém parkoviště v Pythonu.

Systém eviduje auta podle SPZ, ukládá čas vjezdu a umožňuje:
- výpočet ceny parkovného,
- evidenci zaplacení,
- kontrolu, zda auto může odjet.

Data o zaparkovaných autech se ukládají do souboru.

---

# Kontext

Na parkoviště přijíždí auta.

Při vjezdu:
- zaznamená se SPZ,
- uloží se datum a čas vjezdu.

Při výjezdu:
- zadá se SPZ a čas,
- spočítá se cena parkování,
- pokud není zaplaceno → auto neodjede,
- pokud je zaplaceno → auto odjede a záznam se odstraní.

---

# Požadavky

# 1️⃣ Parkovací záznam

Navrhni třídu reprezentující jedno parkování.

Obsahuje:
- SPZ
- čas vjezdu
- informaci o zaplacení

Umí:
- uložit čas výjezdu
- spočítat délku parkování
- označit parkování jako zaplacené

---

# 2️⃣ Ceník

Navrhni třídu pro výpočet ceny.

Obsahuje:
- cenu za hodinu

Umí:
- spočítat cenu podle délky parkování

---

# 3️⃣ Parkoviště

Navrhni hlavní třídu, která spravuje parkování.

Umí:
- zapsat vjezd auta
- najít záznam podle SPZ
- spočítat cenu parkování
- označit parkování jako zaplacené
- rozhodnout, zda auto může odjet

---

# 4️⃣ Ukládání do souboru

Data se ukládají do souboru(např. `parkovani.csv`).

Požadavky:
- při vjezdu se záznam uloží do souboru
- při načtení programu se data načtou ze souboru
- při výjezdu(pokud je zaplaceno) se záznam ze souboru odstraní

---

# 5️⃣ Práce s časem

Použij modul `datetime`.

- ukládej čas jako text(string)
- při výpočtech převáděj na `datetime`

---

# 6️⃣ Návratové hodnoty

Navrhni rozhraní metod tak, aby:

- výpočet ceny vracel číslo
- kontrola výjezdu vracela `True` / `False`

---

# Doporučená struktura souborů


parkovaci_zaznam.py
cenik.py
parkoviste.py
main.py
parkovani.json


---

# Poznámky

- Program nemusí mít grafické rozhraní.
- Stačí jednoduché testování v `main.py`.
- Dbej na přehlednost kódu a rozdělení odpovědností mezi třídy.
- Nepoužívej globální proměnné.

---

# Rozšíření (volitelné)

- kontrola duplicitní SPZ při vjezdu
- minimální účtovaná doba(např. 1 hodina)
- zaokrouhlování ceny
- historie parkování

---
