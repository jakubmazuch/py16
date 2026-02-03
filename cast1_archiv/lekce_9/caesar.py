def odstranDiakritiku(text):
    diakritika  = "ěščřžýáíéóďťňúůľĺåĚŠČŘŽÝÁÍÉÓĎŤŇÚŮĽĹÅ"
    bezd        = "escrzyaieodtnuullaESCRZYAIEODTNUULLA"

    vysledek = ""

    for z in text:
        if z in diakritika:
            i = diakritika.index(z)
            vysledek += bezd[i]
        else:
            vysledek += z

    return vysledek


def caesar(text, posun):
    text = odstranDiakritiku(text)
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""

    for znak in text:
        z = znak.lower()
        if z in abeceda:
            index = abeceda.index(z)
            novyIndex = (index + posun) % 26
            novyZnak = abeceda[novyIndex]

            if znak.isupper():
                vysledek += novyZnak.upper()
            else:
                vysledek += novyZnak
        else:
            vysledek += znak

    return vysledek


vstup = input("Zadej text: ")
heslo = int(input("Zadej heslo: "))
print(caesar(vstup, heslo))