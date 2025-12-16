def odstranDiakritiku(text):
    diakritika  = "ěščřžýáíéóďťňúůľĺåĚŠČŘŽÝÁÍÉÓĎŤŇÚŮĽĹÅ"
    bezd        = "escrzyaieodtnuullaescrzyaieodtnuulla"

    vysledek = ""

    for z in text:
        if z in diakritika:
            i = diakritika.index(z)
            vysledek += bezd[i]
        else:
            vysledek += z

    return vysledek


pouzite = {}

with open("vek.csv", "r", encoding="utf-8") as f:
    for radek in f:
        radek = radek.strip()
        if radek == "":
            continue

        jmeno_prijmeni = radek.split(";")[0]
        jmena_seznam = jmeno_prijmeni.split()

        if len(jmena_seznam) < 2:
            continue

        jmeno = odstranDiakritiku(jmena_seznam[0]).lower()
        prijmeni = odstranDiakritiku(jmena_seznam[-1]).lower()

        prefix = f"{prijmeni}.{jmeno[0]}"
        if prefix not in pouzite:
            pouzite[prefix] = 1
            email = f"{prefix}@example.com"
        else:
            pouzite[prefix] += 1
            email = f"{prefix}{pouzite[prefix]}@example.com"

        print(email)
