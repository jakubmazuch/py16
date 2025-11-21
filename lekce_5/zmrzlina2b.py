penize = int(input("Kolik máš peněz? "))
cena = int(input("Kolik stojí jeden kopeček? "))

koupenychKopecku = 0

for i in range(cena, penize+1, cena):
    koupenychKopecku += 1

print(f"Můžeš si koupit {koupenychKopecku} kopečků.")
