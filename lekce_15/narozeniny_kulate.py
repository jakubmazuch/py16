from datetime import date, datetime, timedelta

vstup = "jmena.csv"
vystup = "narozeniny_kulate.csv"


# Načtení kladného čísla n
def nacti_n():
    while True:
        n = input("Zadej počet dnů: ").strip()
        try:
            n = int(n)
            if n <= 0:
                print("Chyba vstupu: číslo musí být kladné.")
                continue
            return n
        except ValueError:
            print("Chyba vstupu: zadej kladné číslo.")


# Načtení narozenin v intervalu
def nacti_narozeniny(n):
    dnes = date.today()
    konec = dnes + timedelta(days=n)

    nalezy = []

    with open(vstup, "r", encoding="utf-8") as f:
        for radek in f:
            radek = radek.strip()

            if radek == "":
                continue

            casti = radek.split(";")
            if len(casti) != 2:
                continue

            jmeno = casti[0].strip()
            datumText = casti[1].strip()

            try:
                narozen = datetime.strptime(datumText, "%d.%m.%Y").date()
            except ValueError:
                continue

            try:
                narozky = date(dnes.year, narozen.month, narozen.day)
            except ValueError:
                continue

            if narozky < dnes:
                try:
                    narozky = date(dnes.year + 1, narozen.month, narozen.day)
                except ValueError:
                    continue

            if dnes <= narozky <= konec:
                vek = narozky.year - narozen.year

                if vek % 10 != 0:
                    continue

                nalezy.append({
                    "datum": narozky,
                    "jmeno": jmeno,
                    "vek": vek
                })
    return nalezy


# Řazení
def serad_podle_data(seznam):
    for i in range(len(seznam)):
        for j in range(i+1, len(seznam)):
            if seznam[j]["datum"] < seznam[i]["datum"]:
                seznam[i], seznam[j] = seznam[j], seznam[i]


# Výpis a ložení do CSV
def uloz(seznam, n):
    with open(vystup, "w", encoding="utf-8") as f:
        f.write("datum;jmeno;vek\n")

        if len(seznam) == 0:
            print(
                f"V následujících {n} dnech, vč. dneška nemá nikdo narozeniny."
                )
            return

        for z in seznam:
            datum_text = z["datum"].strftime("%d.%m.%Y")
            print(f"{datum_text} bude mít narozeniny {z['jmeno']} (věk: {z['vek']})")
            f.write(datum_text + ";" + z["jmeno"] + ";" + str(z["vek"]) + "\n")


# Hlavní část
def main():
    n = nacti_n()
    nalezy = nacti_narozeniny(n)
    serad_podle_data(nalezy)
    uloz(nalezy, n)


main()
