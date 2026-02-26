from abc import ABC, abstractmethod
from datetime import date
from typing import List
from polozka import Polozka


class Doklad(ABC):
    def __init__(self, cislo: str, zakaznik: str, polozky: List[Polozka], datum: date | None = None):
        if not cislo or not cislo.strip():
            raise ValueError("Číslo dokladu nesmí být prázdné")
        if not zakaznik or not zakaznik.strip():
            raise ValueError("Zákazník nesmí být prázdné")
        if polozky is None or len(polozky) == 0:
            raise ValueError("Doklad musí mít aspoň jednu položku")

        self.cislo = cislo
        self.zakaznik = zakaznik
        self.polozky = list(polozky)
        self.datum = datum if datum is not None else date.today()

    def soucet_bez_dph(self) -> float:
        return sum(p.cena_celkem() for p in self.polozky)

    @abstractmethod
    def celkova_castka(self) ->float:
        raise NotImplementedError

    def typ(self) -> str:
        return self.__class__.__name__
