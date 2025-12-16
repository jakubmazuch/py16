soucet = 0
pocet = 0

with open("vek.csv", "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if radek == "":
            continue

        casti = radek.split(";")
        vek = int(casti[1])

        soucet += vek
        pocet += 1

if pocet > 0:
    prumer = soucet / pocet
    print(f"Průměrný věk: {prumer:.2f}")
else:
    print("Soubor neobsahuje žádná data.")
