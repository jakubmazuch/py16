a = int(input("Zadej vstup: "))
b = int(input("Zadej vstup: "))
zaver = ""

if a % b == 0:
    zaver = "je dělitelné"
else:
    zaver = "není dělitelné"

print(f"Číslo {a} je {zaver} číslem {b} beze zbytku.")