def pocetSamohlasek(text):
    samohlasky = "aeiouyAEIOUYáéíóúůýÁÉÍÓÚŮÝĚě"
    pocet = 0

    for znak in text:
        if znak in samohlasky:
            pocet += 1

    return pocet


veta = input("Zadej text: ")
print(pocetSamohlasek(veta))
