from dopravni_system import *


if __name__ == "__main__":
    auto = Auto("Toyota Corolla", 5, 6.5)
    moto = Motocykl("Harley-Davidson", 2, 4.0)
    autobus = Autobus("Mercedes Sprinter", 30, 18.0)
    elekto = Elektroauto("Tesla Model 3", 5, 15.0)

    park = VozovyPark()

    park.pridej_vozidlo(auto)
    park.pridej_vozidlo(moto)
    park.pridej_vozidlo(autobus)
    park.pridej_vozidlo(elekto)

    park.vypis()
    park.vysli_vsechna(150)

    nejuspornejsi = park.nejuspornejsi_vozidlo()
    if nejuspornejsi:
        print(nejuspornejsi.znacka)
