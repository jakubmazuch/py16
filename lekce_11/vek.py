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


with open("jmena.csv", encoding="utf-8") as f, open("vek.csv", "w", encoding="utf-8") as vystup:
    for radek in f:
        jmeno, datum = radek.strip().split(";")

        if vek(datum) is None:
            continue

        vystup.write(f"{jmeno};{vek(datum)}\n")

print("Soubor vek.csv úspěšně vytvořen nebo aktualizován.")
