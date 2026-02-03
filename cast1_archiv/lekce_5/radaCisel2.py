a = int(input("Zadej dolní hranici: "))
b = int(input("Zadej horní hranici: "))
c = int(input("Zadej krok: "))

for i in range(a, b+1, c):
    print(i, end=" ")
