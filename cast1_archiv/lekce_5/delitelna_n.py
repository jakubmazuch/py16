cislo = int(input("Zadejte cislo: "))
delenec = int(input("Zadejte dělenec: "))

if cislo % delenec == 0:
    print(f"Číslo {cislo} je dělitelné {delenec}.")
else:
    print(f"Číslo {cislo} není dělitelné {delenec}.")
