n = int(input("Zadej číslo n: "))
hodnota = 1


for _ in range(n):
    print(hodnota, end=", ")
    hodnota *= 2
