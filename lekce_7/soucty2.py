pocet = int(input("Počet čísel: "))

cisla = []
sudy = 0
lichy = 0

for _ in range(pocet):
    x = int(input("Zadej číslo: "))
    cisla.append(x)
    if x % 2 == 0:
        sudy += x
    else:
        lichy += x

print("Součet sudých čísel: ", sudy)
print("Součet lichých čísel: ", lichy)
