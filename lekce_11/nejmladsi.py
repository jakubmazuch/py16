nejmladsi = ""
minVek = float("inf")

with open("vek.csv", "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if radek == "":
            continue

        casti = radek.split(";")
        jmeno = casti[0]
        vek = int(casti[1])

        if vek < minVek:
            nejmladsi = jmeno
            minVek = vek

print(f"Nejmladší účastník: {nejmladsi} (věk: {minVek})")
