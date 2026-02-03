n = int(input("Zadej číslo n: "))

vysledek = 1
i = 1

while i <= n:
    vysledek *= i
    i += 1
    
print(f"{n}! = {vysledek}")
