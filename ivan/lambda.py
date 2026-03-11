class Auto:
    def __init__(self, znacka, spotreba):
        self.znacka = znacka
        self.spotreba = spotreba


auta = [
    Auto("Škoda", 6.5),
    Auto("BMW", 7.9),
    Auto("Toyota", 5.1)
]

auta.sort(key=lambda v: v.spotreba)
for auto in auta:
    print(auto.znacka)
