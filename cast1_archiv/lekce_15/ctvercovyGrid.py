import turtle


def nacti_kladne_cislo(text):
    while True:
        try:
            n = int(input(text))
            if n <= 0:
                print("Zadej kladné číslo.")
            else:
                return n
        except ValueError:
            print("Chyba vstupu. Zadej kladné celé číslo.")


def nakresli_ctverec(t, a):
    for _ in range(4):
        t.forward(a)
        t.left(90)


def nakresli_grid(sirka, vyska, a):
    t = turtle.Turtle()
    t.speed(0)

    for i in range(vyska):
        for j in range(sirka):
            nakresli_ctverec(t, a)
            t.forward(a)

        # návrat na začátek řádku
        t.backward(sirka * a)
        t.left(90)
        t.forward(a)
        t.right(90)


def main():
    sirka = nacti_kladne_cislo("Počet čtverců do řady: ")
    vyska = nacti_kladne_cislo("Počet čtverců do výšky: ")
    # velikost strany čtverce
    a = 30

    nakresli_grid(sirka, vyska, a)
    turtle.done()


main()
