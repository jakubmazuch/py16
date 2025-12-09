import turtle


def sestiuhlenik(strana):
    for _ in range(6):
        turtle.forward(strana)
        turtle.right(60)


def posun(strana, radek, sloupec):
    x = strana * 1.5 * sloupec
    y = (-1) * strana * 1.73 * (radek - sloupec / 2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def grid_sestihelnik(strana, radky, sloupce):
    for r in range(radky):
        for s in range(sloupce - (r // 2)):
            posun(strana, r, s)
            sestiuhlenik(strana)


# nastavení želvy
turtle.shape("turtle")
turtle.speed(2)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

grid_sestihelnik(50, 5, 4)

turtle.done()