from random import randint

a = int(input("Zadej dolní mez: "))
b = int(input("Zadej horní mez: "))
if a > b:
    a, b = b, a

nahodneCislo = randint(a, b)
tahy = 0

print(f"------------------------------------\nAhoj! \nMyslím si číslo od {a} do {b}. Zkus to uhodnout!\n---------------------------------")

while True:
    tip = int(input(f"Jaký je tvůj tip?\n"))
    tahy += 1
    if tip > nahodneCislo:
        print(f"\nMoje číslo je menší, než tvůj tip ({tip}).\nZkus to znovu.\n\n")
    elif tip < nahodneCislo:
        print(f"\nMoje číslo je větší, než tvůj tip ({tip}).\nZkus to znovu.\n\n")        
    else:
        print(f"BINGO! Našel jsi číslo {nahodneCislo} na {tahy} tahů.")
        break
