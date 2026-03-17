class Auto:
    def __init__(
            self,
            znacka: str,
            model: str,
            spz: str,
            cena_za_den: float
    ) -> None:
        if cena_za_den < 0:
            raise ValueError("Cena za den nesmí být záporná.")

        self.znacka = znacka
        self.model = model
        self.spz = spz
        self.cena_za_den = cena_za_den
        self.rezervovano = False

    def nazev(self) -> str:
        return f"{self.znacka} {self.model} (SPZ: {self.spz})"

    def je_volne(self) -> bool:
        return not self.rezervovano

    def spocitej_cenu(self, pocet_dni: int) -> float:
        if pocet_dni <= 0:
            raise ValueError("Počet dní musí být kladné číslo.")

        return self.cena_za_den * pocet_dni

    def rezervuj(self) -> bool:
        if self.rezervovano:
            return False

        self.rezervovano = True
        return True

    def zrus_rezervaci(self) -> None:
        self.rezervovano = False

    def __str__(self) -> str:
        stav = "volné" if self.je_volne() else "rezervované"
        return f"{self.nazev()} | {self.cena_za_den:.0f} Kč/den | {stav}"
