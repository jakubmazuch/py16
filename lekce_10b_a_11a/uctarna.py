from typing import Iterable, Dict
from doklad import Doklad


class Uctarna:
    def __init__(self, doklady: Iterable[Doklad]):
        self.doklady = list(doklady)

    def vypis_prehled(self) -> None:
        print("=== Přehled dokladů ===")
        print("-" * 80)
        print(f"{'Číslo':<12} {'Typ':<10} {'Zákazník':<20} {'Datum':<12} {'Částka':>14}")
        print("-" * 80)
        for w in self.doklady:
            castka = w.celkova_castka
            print(f"{w.cislo:<12} {w.typ():<10} {w.zakaznik:<20} {str(w.datum):<12} {castka:>14}")
        print("-" * 80)

    def vypis_stav_plateb(self):
        print("=== Stav plateb ===")
        print("-" * 70)
        print(f"{'Číslo':<12} {'Typ':<10} {'Celkem':<10} {'Zaplaceno':<12} {'Zbývá':<12}")
        print("-" * 70)
        for q in self.doklady:
            print(
                f"{q.cislo:<12} "
                f"{q.typ():<10} "
                f"{q.celkova_castka:<10.2f} "
                f"{q.zaplaceno:<12} "
                f"{q.zbyva_zaplatit:<12}"
            )

    def obrat(self) -> float:
        return sum(w.celkova_castka for w in self.doklady)

    def souhrn_podle_typu(self) -> Dict[str, float]:
        vysledek: Dict[str, float] = {}
        for w in self.doklady:
            vysledek[w.typ()] = vysledek.get(w.typ(), 0) + 1
        return vysledek

    def celkove_dph(self) -> float:
        return sum(w.dph for w in self.doklady)
