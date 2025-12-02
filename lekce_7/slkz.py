pocet = int(input("Počet čísel: "))

cisla = []
for _ in range(pocet):
    x = int(input("Zadej číslo: "))
    cisla.append(x)


sk = []
sz = []
lk = []
lz = []

for i in cisla:
    if i % 2 == 0 and i > 0:
        sk.append(i)
        continue
    if i % 2 == 0 and i < 0:
        sz.append(i)
        continue
    if i % 2 != 0 and i > 0:
        lk.append(i)
        continue
    if i % 2 != 0 and i < 0:
        lz.append(i)
        continue

print(f"Sudá kladná čísla: {sk}")
print(f"Sudá záporná čísla: {sz}")
print(f"Lichá kladná čísla: {lk}")
print(f"Lichá záporná čísla: {lz}")
