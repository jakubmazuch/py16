pocet = int(input("Počet čísel: "))

cisla = []
soucet = 0
for _ in range(pocet):
    x = int(input("Zadej číslo: "))
    cisla.append(x)
    if x > 0:
        soucet += x

print("Součet kladných čísel: ", soucet)
