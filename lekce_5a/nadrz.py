class Nadrz:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self.stav = 0

    def natankuj(self, litry):
        if self.stav + litry <= self.kapacita:
            self.stav += litry
            return f"Natankováno {litry} l."
        else:
            return "Překročena kapacita nádrže. Nelze natankovat"

    def ujed(self, litry):
        if self.stav >= litry:
            self.stav -= litry
            return f"Ujeto {litry} l."
        else:
            return "Nedostatek paliva. Nelze ujet."

    def vypis(self):
        return f"V nádrži zbývá {self.stav} litrů"
