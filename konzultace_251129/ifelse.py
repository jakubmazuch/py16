a = float(input("Zadej vstup: "))
zaver = ""

if a > 0:
    zaver = "kladne"
elif a < 0:
    zaver = "zaporne"
else:
    zaver = "nula"


print(f"Číslo {a} je {zaver}.")