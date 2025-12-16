import datetime


def vek(datum):
    d, m, r = map(int, datum.split("."))
    narozeni = datetime.date(r, m, d)
    dnes = datetime.date.today()

    if narozeni > dnes:
        return None

    vek = dnes.year - narozeni.year
    if (dnes.month, dnes.day) < (m, d):
        vek -= 1

    return vek


with open("jmena.csv", "r", encoding="utf-8") as vstup:
    radky = vstup.readlines()

nove_radky = []

for radek in radky:
    jmeno, datum = radek.strip().split(";")
    v = vek(datum)
    nove_radky.append(f"{jmeno};{datum};{v}\n")

with open("jmena.csv", "w", encoding="utf-8") as vystup:
    vystup.writelines(nove_radky)

print("Soubor vek.csv úspěšně vytvořen nebo aktualizován.")
