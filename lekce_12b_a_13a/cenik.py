import math


class Cenik:
    def __init__(self, cena_za_hodinu: float) -> None:
        self.cena_za_hodinu = cena_za_hodinu

    def spocitej_cenu(self, delka_parkovani: float) -> float:
        if delka_parkovani < 0:
            raise ValueError("Délka parkování nemůže být záporná.")

        pocet_hodin = math.ceil(delka_parkovani)
        return pocet_hodin * self.cena_za_hodinu
