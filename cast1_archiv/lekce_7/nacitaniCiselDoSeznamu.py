pocet = int(input("Počet čísel: "))

cisla = []
for _ in range(pocet):
    x = int(input("Zadej číslo: "))
    cisla.append(x)

print("Zadal jsi: ", cisla)

print("Minimum: ", min(cisla))
print("Maximum: ", max(cisla))
print("Průměr: ", sum(cisla)/len(cisla))
