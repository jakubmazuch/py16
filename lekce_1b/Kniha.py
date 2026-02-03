class Kniha:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.pujcena = False

    def pujcit(self):
        if self.pujcena:
            print("Kniha není k dispozici, je ve výpůjčce. (", self.nazev, ")")
            return
        self.pujcena = True

    def vratit(self):
        if not self.pujcena:
            print("Kniha je dostupná. Nelze ji vrátit (", self.nazev, ")")
            return
        self.pujcena = False

    def stav_text(self):
        if self.pujcena:
            return "půjčená"
        return "dostupná"

    def vypis(self):
        print("Kniha: ", self.nazev)
        print("Autor: ", self.autor)
        print("Stav: ", self.stav_text())
        print()
