class Obdelnik:
    def __init__(self, sirka, vyska):
        self.vyska = vyska
        self.sirka = sirka

    @property
    def obsah(self):
        return self.vyska * self.sirka


obd1 = Obdelnik(4, 5)
print(obd1.obsah)
