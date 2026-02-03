while True:
    try:
        n = int(input("Zadej počet prvočísel: "))
        if n < 1:
            print("Počet prvočísel musí být kladný.")
            continue
        break
    except ValueError:
        print("Očekáváme zadání celého kladného čísla:")

prvocisla = []
cislo = 2

while len(prvocisla) < n:
    je_prvo = True

    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            je_prvo = False
            break

    if je_prvo:
        prvocisla.append(cislo)

    cislo += 1

print(prvocisla)
