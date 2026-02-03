def nactiCislo(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Chyba. Zadejte prosím číslo")


def vypocet(a, b, c):
    # Lineární rovnice
    if a == 0:
        if b == 0:
            if c == 0:
                return "Rovnice má nekonečně mnoho řešení."
            else:
                return "Rovnice nemá řešení v reálném oboru."
        else:
            x = -c/b
            return f"Lineární rovnice má řešení: x={x}"

    # Kvadratická rovnice
    D = b**2 - 4*a*c

    if D < 0:
        return "Rovnice nemá řešení v reálném oboru."
    elif D == 0:
        x = -b / (2*a)
        return f"Rovnice má jeden dvojnásobný kořen: x₁,₂ = {x}"
    else:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D**(1/2))/(2*a)
        return f"Rovnice má dva kořeny: x₁ = {x1}, x₂ = {x2}"



print("Řešení kvadratické rovnice ax²+bx+c=0")
print("-------------------------------------")
# Hlavní program
while True:
    a = nactiCislo("Zadej kvadratický člen: ")
    b = nactiCislo("Zadej lineární člen: ")
    c = nactiCislo("Zadej absolutní člen: ")

    print(vypocet(a, b, c))

    while True:
        odpoved = input("Chcete řešit další rovnici? (a/n): ").strip().lower()
        if odpoved in ("a", "n"):
            break
        else:
            print("Zadej prosím 'a' nebo 'n'.")

    if odpoved == "n":
        print("Konec programu. Děkuji a pac a pusu!")
        break
