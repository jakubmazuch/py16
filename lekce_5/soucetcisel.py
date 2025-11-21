dolniH = int(input("Zadej dolní hranici: "))
horniH = int(input("Zadej horní hranici: "))

i = dolniH
soucet = 0

while i <= horniH:
    soucet += i
    i += 1


print(f"Součet čísel od {dolniH} do {horniH} je {soucet}.")