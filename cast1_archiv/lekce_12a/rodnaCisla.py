from datetime import datetime, date


def nacti_datum():
    while True:
        text = input("Zadej datum narození ve tvaru 'dd.mm.rrrr': ").strip()
        try:
            d = datetime.strptime(text, "%d.%m.%Y").date()
            return d
        except ValueError:
            print("Chyba: Neplatný formát data. Zadejte např. 04.08.1999")


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


def generuj_suffix(prefix):
    vysledky = []

    for p in range(10):
        for q in range(10):
            for r in range(10):
                prvnich_devet = prefix + f"{p}{q}{r}"
                zbytek = int(prvnich_devet) % 11

                if zbytek == 10:
                    zbytek = 0

                suffix = f"{p}{q}{r}{zbytek}"
                vysledky.append(suffix)
    return vysledky


print("Generátor suffixů rodného čísla") # prefix rrmmdd / suffix abcd
print("-------------------------------")

datum = nacti_datum()
pohlavi = nacti_pohlavi()

hranice = date(1954, 1, 1)
if datum < hranice:
    print("Pozor: pro datum před 1.1.1954 se v praxi používala 9místná ročná čísla. Program přesto generuje 4místné koncovky podle kontrolní číslice.")

prefix = generuj_prefix(datum, pohlavi)
suffix = generuj_suffix(prefix)

print(f"Prefix rodného čísla: {prefix}")
print(f"Počet přípustných suffixů: {len(suffix)}")
print("Seznam všech přípustných suffixů pro dané datum narození a pohlaví: ")

for i, suffix in enumerate(suffix, start=1):
    print(suffix, end=" ")
    if i % 10 == 0:
        print()
print()
