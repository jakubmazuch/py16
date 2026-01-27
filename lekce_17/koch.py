import turtle


def nacti_rad():
    while True:
        text = input("Zadej řád Kochovy křivky: ")

        try:
            rad = int(text)
            if rad < 0 or rad > 8:
                print("Řád musí být mezi 1 a 9.")
            else:
                return rad

        except ValueError:
            print("Chyba vstupu. Vstupem musí být kladné celé číslo.")


def koch(delka, rad):
    if rad == 0:
        turtle.forward(delka)
        return

    tretina = delka / 3

    koch(tretina, rad-1)
    turtle.left(60)
    koch(tretina, rad-1)
    turtle.right(120)
    koch(tretina, rad-1)
    turtle.left(60)
    koch(tretina, rad-1)


rad = nacti_rad()
turtle.speed(0)
turtle.pensize(3)

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

koch(600, rad)
turtle.done()
