class Student:
    def __init__(self, jmeno): # konstruktor
        self.jmeno = jmeno
        self.znamky = []

    def pridej_znamku(self, znamka):
        if not (1 <= znamka <= 5):
            print("Chyba: známka musí být mezi 1 a 5.")
            return
        self.znamky.append(znamka)

    def prumer(self):
        if len(self.znamky) == 0:
            return 0
        return sum(self.znamky) / len(self.znamky)

    def prospel(self):
        if 5 in self.znamky:
            return False
        if self.prumer() > 4.5:
            return False
        return True

    def vypis(self):
        print("Student: ", self.jmeno)
        print("Známky: ", self.znamky)
        print("Průměr: ", round(self.prumer(), 2))
        if self.prospel:
            print("Prospěl")
        else:
            print("Neprospěl")
        print()
