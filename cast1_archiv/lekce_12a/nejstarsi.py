nejstarsi = ""
maxVek = (-1)*float("inf")

with open("vek.csv", "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if radek == "":
            continue

        casti = radek.split(";")
        jmeno = casti[0]
        vek = int(casti[1])

        if vek > maxVek:
            nejstarsi = jmeno
            maxVek = vek

print(f"Nejstarší účastník: {nejstarsi} (věk: {maxVek})")
