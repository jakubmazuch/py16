VSTUP = "zamestnanci1.csv"


def nacti_zamestnance(soubor):
    oddeleni = {}

    try:
        with open(soubor, "r", encoding="utf-8") as f:
            for radek in f:
                radek = radek.strip()

                if radek == "":
                    continue

                casti = radek.split(";")
                if len(casti) != 4:
                    continue

                jmeno = casti[0].strip()
                prijmeni = casti[1].strip()
                o = casti[3].strip()
                if o not in oddeleni:
                    oddeleni[o] = []

                oddeleni[o].append((prijmeni, jmeno))

    except FileNotFoundError:
        print("Chyba: vstupni soubor nebyl nalezen.")
    except Exception as e:
        print("Neočekávaná chyba: ", e)

    return oddeleni


def uloz_soubory(oddeleni):
    for o in oddeleni:
        nazev_souboru = o + ".txt"

        try:
            with open(nazev_souboru, "w", encoding="utf-8") as f:
                seznam = sorted(oddeleni[o])

                for prijmeni, jmeno in seznam:
                    f.write(prijmeni + " " + jmeno + "\n")

            print("Vytvořen nebo upraven soubor: ", nazev_souboru)

        except Exception as e:
            print("Chyba při zápisu souboru ", nazev_souboru, e)


def main():
    data = nacti_zamestnance(VSTUP)

    if data:
        uloz_soubory(data)
    else:
        print("Nejsou data, nevím, co po mě chceš.")


main()
