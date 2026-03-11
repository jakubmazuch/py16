class Auto:
    def __init__(self, znacka):
        self.znacka = znacka

    def __repr__(self):
        return f"Auto {self.znacka}"


a1 = Auto("BMW")
print(repr(a1))
print([a1])
