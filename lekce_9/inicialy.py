def inicialy(jmeno, prijmeni):
    prvni = jmeno[0].upper()
    druha = prijmeni[0].upper()
    return prvni + "." + druha + "."


jmeno = input("Zadejte křestní jméno: ")
prijmeni = input("Zadejte prijmeni: ")
print(inicialy(jmeno, prijmeni))
