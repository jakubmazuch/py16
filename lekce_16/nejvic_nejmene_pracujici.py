from datetime import datetime

soubor = "zamestanci.csv"

nejstarsi = None
nejmladsi = None

with open(soubor, "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if not radek:
            continue

        jmeno, prijmeni, datum = radek.split(";")
        try:
            datum = datetime.strptime(datum, "%d.%m.%Y").date()
        except ValueError:
            continue

        if nejstarsi is None or datum < nejstarsi[2]:
            nejstarsi = (jmeno, prijmeni, datum)

        if nejmladsi is None or datum > nejmladsi[2]:
            nejmladsi = (jmeno, prijmeni, datum)

print("Služebně nejstarší zaměstanec:")
print(f"{nejstarsi[1]} {nejstarsi[0]} - nástup: {nejstarsi[2].strftime('%d.%m.%Y')}")
print("Služebně nejmladší zaměstanec:")
print(f"{nejmladsi[1]} {nejmladsi[0]} - nástup: {nejmladsi[2].strftime('%d.%m.%Y')}")