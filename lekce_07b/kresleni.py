import turtle
from abc import ABC, abstractmethod


class Tvar(ABC):
    def __init__(self, velikost, rychlost=8):
        self.velikost = velikost
        self.rychlost = rychlost

    def nastav_zelvu(self, x=0, y=0):
        turtle.shape("turtle")
        turtle.speed(self.rychlost)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    @abstractmethod
    def kresli(self):
        pass


class PravidelnyMnohouhlenik(Tvar):
    def __init__(self, n, velikost, rychlost=8):
        super().__init__(velikost, rychlost)

        if n < 3:
            raise ValueError("n musí být alespoň 3.")

        self.n = n

    def kresli(self):
        uhel = 360/self.n

        for _ in range(self.n):
            turtle.forward(self.velikost)
            turtle.right(uhel)


class Trojuhelnik(PravidelnyMnohouhlenik):
    def __init__(self, velikost, rychlost=8):
        super().__init__(3, velikost, rychlost)


class Ctverec(PravidelnyMnohouhlenik):
    def __init__(self, velikost, rychlost=8):
        super().__init__(4, velikost, rychlost)


class Sestiuhelnik(PravidelnyMnohouhlenik):
    def __init__(self, velikost, rychlost=8):
        super().__init__(6, velikost, rychlost)


class Mrizka:
    def __init__(self, tvar: Tvar, pocet, x=0, y=0):
        self.tvar = tvar
        self.pocet = pocet
        self.x = x
        self.y = y

    def kresli(self):
        self.tvar.nastav_zelvu(self.x, self.y)

        for _ in range(self.pocet):
            for _ in range(self.pocet):
                self.tvar.kresli()
                turtle.forward(self.tvar.velikost)

            turtle.backward(self.tvar.velikost * self.pocet)

            turtle.right(90)
            turtle.forward(self.tvar.velikost)
            turtle.left(90)

        turtle.done()
