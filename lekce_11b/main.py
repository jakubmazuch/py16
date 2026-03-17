from auto import Auto
from pujcovna import Pujcovna


def main() -> None:
    auto1 = Auto("Škoda", "Octavia", "2AB 8855", 950)
    auto2 = Auto("Hyundai", "i30", "9AX 1245", 850)
    auto3 = Auto("Toyota", "Corolla", "8AC", 990)
    auto4 = Auto("Tatra", "603", "02V 1233", 2750)

    pujcovna = Pujcovna("Kolínská půjčovna")

    pujcovna.pridej_auto(auto1)
    pujcovna.pridej_auto(auto3)
    pujcovna.pridej_auto(auto2)
    pujcovna.pridej_auto(auto4)

    pujcovna.rezervuj_auto(4, 5)
    auto4.zrus_rezervaci()
    pujcovna.rezervuj_auto(4, 1)

    pujcovna.vypis_vsechna_auta()


if __name__ == "__main__":
    main()
