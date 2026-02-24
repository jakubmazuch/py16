from kresleni import (
    Mrizka,
    Ctverec,
    Trojuhelnik,
    Sestiuhelnik,
    PravidelnyMnohouhlenik
)


def nacti(popisek, min=None):
    while True:
        try:
            x = int(input(popisek))
            if min is not None and x < min:
                print(f"Zadej alespoň číslo {min}")
                continue
            return x
        except ValueError:
            print("Neplatná hodnota")


def vyber_tvar(velikost, rychlost):
    print("\n === VÝBĚR TVARU ===")
    print("1: Čtverec")
    print("2: Trojúhleník")
    print("3: Šestiúhleník")
    print("4: n-úhleník")

    volba = nacti("Volba", 1)

    match volba:
        case 1:
            return Ctverec(velikost, rychlost)
        case 2:
            return Trojuhelnik(velikost, rychlost)
        case 3:
            return Sestiuhelnik(velikost, rychlost)
        case 4:
            n = nacti("Zadej počet stran: ", 3)
            return PravidelnyMnohouhlenik(n, velikost, rychlost)
        case _:
            print("Neplatná volba.")
            return Ctverec(velikost, rychlost)


def main():
    velikost = nacti("Velikost strany: ", 1)
    pocet = nacti("Počet tvarů v řádku: ", 1)
    rychlost = nacti("Rychlost (1-10): ")

    tvar = vyber_tvar(velikost, rychlost)

    mrizka = Mrizka(tvar, pocet)
    mrizka.kresli()


if __name__ == "__main__":
    main()
