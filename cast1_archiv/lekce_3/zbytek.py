x = int(input("Zadejte číslo x="))
y = int(input("Zadejte číslo y="))

celeCislo = (x//y)
zbytek = x-(celeCislo*y)

print(f"{x}÷{y}={celeCislo}, zb. {zbytek}")
