class Auto:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def __eq__(self, other) -> bool:
        if not isinstance(other, Auto):
            return False
        return (self.znacka == other.znacka) and (self.model == other.model)


a1 = Auto("Audi", "Q7")
a2 = Auto("Audi", "Q7")

print(a1 == a2)
