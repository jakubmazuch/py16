from datetime import datetime, date


def nacti_datum():
    while True:
        text = input("Zadej datum narození ve tvaru 'dd.mm.rrrr': ").strip()
        try:
            d = datetime.strptime(text, "%d.%m.%Y").date()
            return d
        except ValueError:
            print("Chyba: Neplaný formát data. Zadejte např. 04.08.1999")


def nacti_pohlavi():
    while True:
        p = input("Zadejte pohlaví (m/ž): ").strip().lower()
        if p == "ž":
            p = "z"
        if p in ("m", "z"):
            return p
        else:
            print("Chyba: Neplatný symbol pro pohlaví.")


def generuj_prefix(datum, pohlavi):
    r = datum.year % 100
    m = datum.month
    d = datum.day

    if pohlavi == "z":
        m += 50

    return f"{r:02d}{m:02d}{d:02d}"


def generuj_rc(prefix):
    vysledky = []

    for p in range(10):
        for q in range(10):
            for r in range(10):
                prvnich_devet = prefix + f"{p}{q}{r}"
                zbytek = int(prvnich_devet) % 11

                if zbytek == 10:
                    zbytek = 0

                suffix = f"{p}{q}{r}{zbytek}"
                rc = f"{prefix}/{suffix}"
                vysledky.append(rc)
    return vysledky


print("Generátor rodných čísel") # prefix rrmmdd / suffix abcd
print("-------------------------------")

datum = nacti_datum()
pohlavi = nacti_pohlavi()

hranice = date(1954, 1, 1)
if datum < hranice:
    print("Pozor: pro datum před 1.1.1954 se v praxi používala 9místná ročná čísla. Program přesto generuje 4místné koncovky podle kontrolní číslice.")

prefix = generuj_prefix(datum, pohlavi)
rocne_cislo = generuj_rc(prefix)

with open("rodna_cisla.txt", "w", encoding="utf-8") as f:
    for rc in rocne_cislo:
        f.write(rc + "\n")

print(f"Počet přípustných rodných čísel: {len(rocne_cislo)}")
print("Výsledek uložen do soubory 'rodna_cisla.txt'")
