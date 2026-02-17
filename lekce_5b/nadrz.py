class Nadrz:
    def __init__(self, kapacita, spotreba):
        self.kapacita = kapacita
        self.spotreba = spotreba
        self.stav = 0

    def natankuj(self, litry):
        if self.stav + litry <= self.kapacita:
            self.stav += litry
            return True
        return False

    def ujed_litry(self, litry):
        if self.stav >= litry:
            self.stav -= litry
            return True
        return False

    def ujed_km(self, km):
        potrebne_litry = (self.spotreba/100)*km
        return self.ujed_litry(potrebne_litry)

    def dojezd(self):
        if self.spotreba == 0:
            return 0
        return (self.stav / self.spotreba) * 100

    def vypis(self):
        return f"V nádrži zbývá {self.stav:.2f} litrů. Dojezd: {self.dojezd():.2f} km"
