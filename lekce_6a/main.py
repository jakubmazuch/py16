from caesar import CaesarSifra


def ziskej_posun():
    while True:
        try:
            posun = int(input("Zadej číselné heslo: "))
            return posun
        except ValueError:
            print("Chyba! Musíš zadat celé číslo: ")


def menu():
    print("\n=== Caesarova šifra ===")
    print("1 - Šifrovat")
    print("2 - Dešifrovat")
    print("0 - Ukončit program")


def main():
    while True:
        menu()
        volba = input("Vyber možnost: ")

        if volba == "0":
            print("Pac a pusu, zase někdy příště. Ukončuji program!")
            break

        elif volba == "1":
            vstup = input("Zadej text k zašifrování: ")
            posun = ziskej_posun()

            sifra = CaesarSifra(posun)
            vysledek = sifra.zasifruj(vstup)

            print("Vstup: ", vstup)
            print("Šifra: ", vysledek)

        elif volba == "2":
            vstup = input("Zadej text k dešifrování: ")
            posun = ziskej_posun()

            sifra = CaesarSifra(posun)
            vysledek = sifra.desifruj(vstup)

            print("Šifra: ", vstup)
            print("Dešifrovaný text: ", vysledek)

        else:
            print("Neplatná volba.")


if __name__ == "__main__":
    main()
