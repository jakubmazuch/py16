class Automobil:
    def vypis_typ(self):
        print(self.__class__.__name__)


a = Automobil()
a.vypis_typ()