from kresleni import Grid


def nacti_int(popisek):
    while True:
        try:
            return int(input(popisek))
        except ValueError:
            print("Zadej prosím celé číslo: ")


def main():
    velikost = nacti_int("Velikost: ")
    pocet = nacti_int("Počet: ")
    rychlost = nacti_int("Rychlost: ")

    mrizka = Grid(velikost, pocet, rychlost)
    mrizka.kresli()


if __name__ == "__main__":
    main()
