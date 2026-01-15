from datetime import datetime, date
import calendar

soubor = "zamestanci.csv"


def delka_praxe(od: date, do: date) -> tuple[int, int, int]:
    if od > do:
        return (0, 0, 0)

    roky = do.year - od.year
    mesice = do.month - od.month
    dny = do.day - od.day

    if dny < 0:
        mesice -= 1
        predchozi_mesic = do.month - 1
        predchozi_rok = do.year
        if predchozi_mesic == 0:
            predchozi_mesic = 12
            predchozi_rok -= 1
        dny += calendar.monthrange(predchozi_rok, predchozi_mesic)[1]

    if mesice < 0:
        roky -= 1
        mesice += 12

    return (roky, mesice, dny)


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

dnes = date.today()

# vypisovat služebně nejstarší
roky, mesice, dny = delka_praxe(nejstarsi[2], dnes)
print("Služebně nejstarší zaměstanec:")
print(f"{nejstarsi[1]} {nejstarsi[0]}")
print(f"nástup: {nejstarsi[2].strftime('%d.%m.%Y')}")
print(f"délka praxe: {roky} let, {mesice} mesíců, {dny} dnů\n\n")

# vypisovat služebně nejmladší
roky, mesice, dny = delka_praxe(nejmladsi[2], dnes)
print("Služebně nejmladší zaměstanec:")
print(f"{nejmladsi[1]} {nejmladsi[0]}")
print(f"nástup: {nejmladsi[2].strftime('%d.%m.%Y')}")
print(f"délka praxe: {roky} let, {mesice} mesíců, {dny} dnů\n")
