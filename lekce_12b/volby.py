predmety = {}

with open("volby.csv", "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if radek == "":
            continue

        casti = radek.split(";")
        jmeno = casti[0]
        prijmeni = casti[1]
        trida = casti[2]
        predmet1 = casti[3]
        predmet2 = casti[4]

        student = f"{prijmeni} {jmeno} ({trida})"

        if predmet1 not in predmety:
            predmety[predmet1] = []
        predmety[predmet1].append(student)
        if predmet2 not in predmety:
            predmety[predmet2] = []
        predmety[predmet2].append(student)


for predmet, studenti in predmety.items():
    nazev_souboru = predmet.replace(" ", "_") + ".txt"

    with open(nazev_souboru, "w", encoding="utf-8") as f:
        for s in studenti:
            f.write(s + "\n")

    print(f"Vytvořen soubor: {nazev_souboru}")
