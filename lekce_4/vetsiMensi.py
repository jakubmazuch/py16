a = int(input("Zadej číslo a: "))
b = int(input("Zadej číslo b: "))

if a > b:
    print(f"{a}>{b}")
    print(f"Diferenciace: {a-b}")
elif a == b:
    print(f"{a}={b}")
else:
    print(f"{a}<{b}")
    print(f"Diferenciace: {b-a}")
