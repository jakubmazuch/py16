n = int(input("Zadej číslo n: "))

vysledek = 1

for i in range(1, n+1):
    vysledek *= i
    
print(f"{n}! = {vysledek}")
