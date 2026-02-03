def soucet(a, b):
    if a > b:
        raise ValueError("Dolní hranice nesmí být větší než horní")
    soucet = 0
    for i in range(a, b+1):
        if i >= 1:
            soucet += i
    return soucet


try:
    a = int(input("Zadej dolní hranici: "))
    b = int(input("Zadej horní hranici: "))

    vysledek = soucet(a, b)
    print(f"Součet všech přirozených čísel v int. <{a}, {b}> je {vysledek}.")

except ValueError as e:
    print("Chyba: ", e)

except Exception:
    print("Neočekávaná chyba.")