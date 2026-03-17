from auto import Auto


class Pujcovna:
    def __init__(self, nazev: str) -> None:
        self.nazev = nazev
        self.auta = []

    def pridej_auto(self, auto: Auto) -> None:
        self.auta.append(auto)

    def vypis_vsechna_auta(self) -> None:
        print(f"=== Nabídka půjčovny ({self.nazev}) ===")
        for poradi, auto in enumerate(self.auta, start=1):
            print(f"{poradi}. {auto}")

    def vypis_volna_auta(self) -> None:
        print("= Volná auta =")
        naslo_se_volne = False

        for poradi, auto in enumerate(self.auta, start=1):
            if auto.je_volne():
                print(f"{poradi}. {auto}")
                naslo_se_volne = True

        if not naslo_se_volne:
            print("Žádné auto není volné.")

    def rezervuj_auto(self, poradi_auta: int, pocet_dni: int) -> bool:
        if poradi_auta < 1 or poradi_auta > len(self.auta):
            print("Neplatné číslo auta.")
            return False

        auto = self.auta[poradi_auta - 1]

        if not auto.je_volne():
            print(f"Auto {auto.nazev()} je již zarezervované.")
            return False

        cena = auto.spocitej_cenu(pocet_dni)
        auto.rezervuj()

        print(
            f"Auto {auto.nazev()} bylo úspěšně zar. na {pocet_dni} dní."
            f"Cena: {cena:.0f} Kč."
        )
        return True
