penize = int(input("Kolik máš peněz? "))
cena = int(input("Kolik stojí jeden kopeček? "))

kopecky = 0

for i in range(1000):
    if penize >= cena:
        penize -= cena
        kopecky += 1
    else:
        break


print(f"Můžeš si koupit {kopecky} kopečků.")
print(f"Zbyde Ti {penize} Kč.")
