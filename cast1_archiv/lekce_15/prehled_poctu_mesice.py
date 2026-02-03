from datetime import datetime
import turtle

VSTUP = "jmena.csv"


# Načtení počtu narozenin podle měsíce
def nacti_pocty():
    pocty = {}
    for m in range(1, 13):
        pocty[m] = 0

    with open(VSTUP, "r", encoding="utf-8") as f:
        for radek in f:
            radek = radek.strip()

            if radek == "":
                continue

            casti = radek.split(";")
            if len(casti) != 2:
                continue

            datum = casti[1].strip()
            try:
                narozen = datetime.strptime(datum, "%d.%m.%Y").date()
            except ValueError:
                continue

            mesic = narozen.month
            pocty[mesic] += 1

    return pocty


def vypis_prehled(pocty):
    nazvy = ["",
             "leden",
             "únor",
             "březen",
             "duben",
             "květen",
             "červen",
             "červenec",
             "srpen",
             "září",
             "říjen",
             "listopad",
             "prosinec",
             ]

    print("Přehled narozenin podle měsíce:")
    for m in range(1, 13):
        print(nazvy[m] + ": ", pocty[m])


# kleslení sloupce
def nakresli_sloupec(t, vyska, sirka):
    t.left(90)
    t.forward(vyska)
    t.right(90)
    t.forward(sirka)
    t.right(90)
    t.forward(vyska)
    t.left(90)


# Kreslení grafu
def graf(pocty):
    screen = turtle.Screen()
    screen.title("Narozeniny podle měsíce - sloupcový graf")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)

    mesice = ["", "I", "II", "III", "IV", "V", "VI", "VII",
              "VIII", "IX", "X", "XI", "XII"]

    sirka = 30
    mezera = 10
    meritko = 5

    # pevná startovní pozice
    t.penup()
    t.goto(-250, -200)
    t.pendown()

    # osa x
    t.forward(12 * (sirka + mezera) + 10)

    # zpět na startovní pozici
    t.penup()
    t.goto(-250, -200)
    t.pendown()

    for m in range(1, 13):
        vyska = pocty[m] * meritko
        nakresli_sloupec(t, vyska, sirka)
        t.penup()
        t.backward(sirka / 2)
        t.right(90)
        t.forward(20)
        t.write(mesice[m], align="center", font=("Arial", 10, "normal"))
        t.backward(20)
        t.left(90)
        t.forward(sirka / 2)
        t.pendown()

        # mezera mezi sloupci
        t.penup()
        t.forward(mezera)
        t.pendown()

    t.hideturtle()
    screen.mainloop()


# Hlavní program
def main():
    pocty = nacti_pocty()
    vypis_prehled(pocty)
    graf(pocty)


main()
