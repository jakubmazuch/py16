vstupni_soubor = "vek.csv"
vystupni_soubor = "vek_output.csv"

osoby = []

# Načítám soubor - read
with open(vstupni_soubor, "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()

        if radek == "":
            continue

        casti = radek.split(";")
        if len(casti) != 2:
            continue

        jmeno = casti[0].strip()
        try:
            vek = int(casti[1])
        except ValueError:
            continue

        osoba = {
            "jmeno": jmeno,
            "vek": vek
        }
        osoby.append(osoba)

# řadíme seznam podle věku (Bubble sort)
for i in range(len(osoby)):
    for j in range(i+1, len(osoby)):
        if osoby[j]["vek"] > osoby[i]["vek"]:
            osoby[i], osoby[j] = osoby[j], osoby[i]

# zápis do nového souboru
with open(vystupni_soubor, "w", encoding="utf-8") as f:
    for osoba in osoby:
        f.write(osoba["jmeno"] + ";" + str(osoba["vek"]) + "\n")

print("Hotovo :-) Soubor 'vek_output.csv' byl vytvořen nebo byl aktualizován.")
