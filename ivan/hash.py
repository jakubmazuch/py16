class Auto:
    def __init__(self, znacka, model, spz):
        self.znacka = znacka
        self.model = model
        self.spz = spz

    def __eq__(self, other) -> bool:
        if not isinstance(other, Auto):
            return False
        return self.spz == other.spz

    def __hash__(self):
        return hash(self.znacka)


a1 = Auto("Audi", "Q7", "1A8 5566")
a2 = Auto("Audi", "Q7", "7A5 4411")

auta = {a1, a2}
print(len(auta))
