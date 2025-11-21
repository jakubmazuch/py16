penize = int(input("Kolik máš peněz? "))
cena = int(input("Kolik stojí jeden kopeček? "))
pocetKopecku = int(input("Kolik chceš kopečků? "))

celkovaCena = 0

for i in range(pocetKopecku):
    celkovaCena += cena

if penize >= celkovaCena:
    print("Ano, můžeš si koupit zmrzlinu, ", end="")
    print(f"a zbyde Ti {penize-celkovaCena} Kč.")
else:
    print("Bohužel si zmrlinu nemůžeš koupit, ", end="")
    print(f"chybí ti {celkovaCena-penize} Kč.")
