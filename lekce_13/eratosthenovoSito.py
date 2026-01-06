def eratosthenovoSito(n):
    if n < 2:
        return []

    sito = [True] * (n+1)
    sito[0] = sito[1] = False

    for i in range(2, int(n**0.5)+1):
        if sito[i]:
            for j in range(i*i, n+1, i):
                sito[j] = False

    prvocisla = []
    for i in range(2, n+1):
        if sito[i]:
            prvocisla.append(i)

    return prvocisla


try:
    n = int(input("Zadej číslo N: "))
    vysledek = eratosthenovoSito(n)
    print("Prvočísla: ", vysledek)

except ValueError:
    print("Chyba: Zadej celé číslo")

except Exception:
    print("Neočekávaná chyba.")
