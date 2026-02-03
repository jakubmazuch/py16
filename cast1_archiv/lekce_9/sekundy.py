def prevod(sekundy):
    h = sekundy // 3600
    m = (sekundy % 3600) // 60
    s = sekundy % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


sekundy = int(input("Zadej vteřiny: "))
print(f"{sekundy} s. = {prevod(sekundy)}")