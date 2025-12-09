import turtle


def ctverec(velikost):
    for i in range(4):
        turtle.forward(velikost)
        turtle.right(90)


def grid(velikost, pocet):
    for y in range(pocet):
        for x in range(pocet):
            ctverec(velikost)
            turtle.forward(velikost)
        turtle.backward(velikost * pocet)
        turtle.right(90)
        turtle.forward(velikost)
        turtle.left(90)


# nastavení želvy
velikost = int(input("Velikost: "))
pocet = int(input("Počet: "))
rychlost = int(input("Rychlost: "))

turtle.shape("turtle")
turtle.speed(rychlost)
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()

grid(velikost, pocet)

turtle.done()