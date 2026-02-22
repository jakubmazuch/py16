import turtle


class Grid:
    def __init__(self, velikost, pocet, rychlost, x=150, y=150):
        self.velikost = velikost
        self.pocet = pocet
        self.rychlost = rychlost
        self.x = x
        self.y = y

    def nastav_zelvu(self):
        turtle.shape("turtle")
        turtle.speed(self.rychlost)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

    def ctverec(self):
        for _ in range(4):
            turtle.forward(self.velikost)
            turtle.right(90)

    def grid(self):
        for _ in range(self.pocet):
            for _ in range(self.pocet):
                self.ctverec()
                turtle.forward(self.velikost)
            turtle.backward(self.velikost * self.pocet)
            turtle.right(90)
            turtle.forward(self.velikost)
            turtle.left(90)

    def kresli(self):
        self.nastav_zelvu()
        self.grid()
        turtle.done()
