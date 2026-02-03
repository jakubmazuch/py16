rozpocet = int(input("Kolik máš peněz? "))
cenaZmrzliny = int(input("Kolik stojí zmrzlina? "))

if cenaZmrzliny <= rozpocet:
    print("Kup si zmzlinu.")
else:
    print(f"Chybí ti {cenaZmrzliny-rozpocet} Kč.")
