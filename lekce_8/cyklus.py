while True:
    try:
        n = int(input("Zadej číslo n: "))

        if n < 1:
            print("Zadejte prosím kladné číslo: ")
            continue

        x = float(input("Zadej číslo, jehož násobky chceš: "))
        break

    except ValueError:
        print("Chyba: Zadej prosím kladné celé číslo!")


seznam = []

for i in range(1, n+1):
    seznam.append(i*x)

print(seznam)
