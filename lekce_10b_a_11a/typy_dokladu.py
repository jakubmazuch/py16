from typing import List
from datetime import date

from polozka import Polozka
from doklad import Doklad


class Faktura(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        sazba_dph: float = 0.21,
        datum: date | None = None
    ):
        super().__init__(cislo, zakaznik, polozky, datum)
        self.sazba_dph = float(sazba_dph)

    @property
    def sazba_dph(self):
        return self._sazba_dph

    @sazba_dph.setter
    def sazba_dph(self, value):
        if value < 0:
            raise ValueError("DPH nesmí být záporné.")
        self._sazba_dph = float(value)

    @property
    def dph(self) -> float:
        return self.soucet_bez_dph() * self.sazba_dph

    @property
    def celkova_castka(self) -> float:
        return self.dph + self.soucet_bez_dph()

    def typ(self) -> str:
        return "Faktura"


class Zaloha(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        procento: float = 0.5,
        datum: date | None = None
    ):
        if not (0 < procento <= 1):
            raise ValueError("Procento musí být v intervalu (0, 1>.")
        super().__init__(cislo, zakaznik, polozky, datum)
        self.procento = float(procento)

    @property
    def celkova_castka(self):
        return self.soucet_bez_dph() * self.procento

    def typ(self):
        return "Záloha"


class Dobropis(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        procento_vraceni: float = 1.0,
        datum: date | None = None
    ):
        if not (0 < procento_vraceni <= 1):
            raise ValueError("Procento vrácení musí být v intervalu (0, 1>.")
        super().__init__(cislo, zakaznik, polozky, datum)
        self.procento_vraceni = float(procento_vraceni)

    @property
    def celkova_castka(self) -> float:
        return -(self.soucet_bez_dph() * self.procento_vraceni)

    def typ(self) -> str:
        return "Dobropis"


class SlevaDoklad(Doklad):
    def __init__(
        self,
        cislo: str,
        zakaznik: str,
        polozky: List[Polozka],
        sleva: float = 0.1,
        sazba_dph: float = 0.21,
        datum: date | None = None
    ):
        super().__init__(cislo, zakaznik, polozky, datum)

        if not (0 <= sleva <= 1):
            raise ValueError("Sleva musí být v int. <0; 1>.")

        if sazba_dph < 0:
            raise ValueError("DPH nesmí být záporné.")

        self.sleva = float(sleva)
        self.sazba_dph = float(sazba_dph)

    def zaklad_po_sleve(self) -> float:
        return super().soucet_bez_dph() * (1 - self.sleva)

    @property
    def dph(self) -> float:
        return self.soucet_bez_dph() * self.sazba_dph

    @property
    def celkova_castka(self) -> float:
        return -(self.zaklad_po_sleve() + self.dph)

    def typ(self) -> str:
        return "Sleva Doklad"
