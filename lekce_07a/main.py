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

        match volba:
            case "0":
                print("Pac a pasu. Program se zavírá.")
                break

            case "1":
                vstup = input("Zadej text k zašifrování: ")
                posun = ziskej_posun()
                sifra = CaesarSifra(posun)
                vysledek = sifra.zasifruj(vstup)
                print("Vstup: ", vstup)
                print("Šifra: ", vysledek)

            case "2":
                vstup = input("Zadej text k dešifrování: ")
                posun = ziskej_posun()
                sifra = CaesarSifra(posun)
                vysledek = sifra.desifruj(vstup)
                print("Šifrovaný text: ", vstup)
                print("Dešifrovaný text: ", vysledek)

            case _:
                print("Neplatná volba")


if __name__ == "__main__":
    main()
