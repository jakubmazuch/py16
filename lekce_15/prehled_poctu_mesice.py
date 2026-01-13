from datetime import datetime

VSTUP = "jmena.csv"


# Načtení počtu narozenin podle měsíce
def nacti_pocty():
    pocty = {}
    for m in range(1, 13):
        pocty[m] = 0

    with open(VSTUP, "r", encoding="utf-8") as f:
        for radek in f:
            radek = radek.strip()

            if radek == "":
                continue

            casti = radek.split(";")
            if len(casti) != 2:
                continue

            datum = casti[1].strip()
            try:
                narozen = datetime.strptime(datum, "%d.%m.%Y").date()
            except ValueError:
                continue

            mesic = narozen.month
            pocty[mesic] += 1

    return pocty


def vypis_prehled(pocty):
    nazvy = ["",
             "leden",
             "únor",
             "březen",
             "duben",
             "květen",
             "červen",
             "červenec",
             "srpen",
             "září",
             "říjen",
             "listopad",
             "prosinec",
             ]

    print("Přehled narozenin podle měsíce:")
    for m in range(1, 13):
        print(nazvy[m] + ": ", pocty[m])


# Hlavní program
def main():
    pocty = nacti_pocty()
    vypis_prehled(pocty)


main()
