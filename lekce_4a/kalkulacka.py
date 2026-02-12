class Kalkulacka:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def scitani(self):
        return self.a + self.b

    def odcitani(self):
        return self.a - self.b

    def nasobeni(self):
        return self.a * self.b

    def deleni(self):
        if self.b == 0:
            raise ZeroDivisionError("Nelze dělit nulou")
        return self.a / self.b
