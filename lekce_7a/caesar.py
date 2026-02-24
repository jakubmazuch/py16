class CaesarSifra:
    def __init__(self, posun):
        self.diakritika = "ěščřžýáíéóöďťňúůľĺåäĚŠČŘŽÝÁÍÉÓĎŤŇÚŮĽĹÅ"
        self.bezd = "escrzyaieoodtnuullaaESCRZYAIEODTNUULLA"
        self.abeceda = "abcdefghijklmnopqrstuvwxyz"
        self.posun = posun

    def odstran_diakritiku(self, text):
        vysledek = ""

        for z in text:
            if z in self.diakritika:
                i = self.diakritika.index(z)
                vysledek += self.bezd[i]
            else:
                vysledek += z

        return vysledek

    def zasifruj(self, text):
        text = self.odstran_diakritiku(text)
        vysledek = ""

        for znak in text:
            z = znak.lower()
            if z in self.abeceda:
                index = self.abeceda.index(z)
                novyIndex = (index + self.posun) % 26
                novyZnak = self.abeceda[novyIndex]

                if znak.isupper():
                    vysledek += novyZnak.upper()
                else:
                    vysledek += novyZnak
            else:
                vysledek += znak

        return vysledek

    def desifruj(self, text):
        opacna_sifra = CaesarSifra(-self.posun)
        return opacna_sifra.zasifruj(text)