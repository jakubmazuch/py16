import json
import os

from parkovaci_zaznam import ParkovaciZaznam
from cenik import Cenik


class Parkoviste:
    def __init__(self, cenik: Cenik, soubor: str = "parkovani.json") -> None:
        self.cenik = cenik
        self.soubor = soubor
        self.zaznamy = []

        self.nacti_ze_souboru()

    def nacti_ze_souboru(self) -> None:
        if not os.path.exists(self.soubor):
            self.zaznamy = []
            return

        with open(self.soubor, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.zaznamy = [ParkovaciZaznam.ze_slovniku(polozka) for polozka in data]

    def uloz_do_souboru(self) -> None:
        data = [zaznam.na_slovnik() for zaznam in self.zaznamy]

        with open(self.soubor, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def zapis_vjezd(self, spz: str, cas_vjezdu: str) -> bool:
        if self.najdi_zaznam(spz) is not None:
            return False

        novy_zaznam = ParkovaciZaznam(spz, cas_vjezdu)
        self.zaznamy.append(novy_zaznam)
        self.uloz_do_souboru()
        return True

    def najdi_zaznam(self, spz: str) -> ParkovaciZaznam | None:
        for zaznam in self.zaznamy:
            if zaznam.spz == spz:
                return zaznam
        return None

    def spocitej_cenu_parkovani(self, spz: str, cas_vyjezdu: str) -> float | None:
        zaznam = self.najdi_zaznam(spz)
        if zaznam is None:
            return None

        zaznam.uloz_cas_vyjezdu(cas_vyjezdu)
        delka = zaznam.delka_parkovani()
        cena = self.cenik.spocitej_cenu(delka)
        return cena

    def oznac_jako_zaplacene(self, spz: str) -> bool:
        zaznam = self.najdi_zaznam(spz)
        if zaznam is None:
            return False

        zaznam.oznac_jako_zaplacene()
        self.uloz_do_souboru()
        return True

    def muze_odjet(self, spz: str) -> bool:
        zaznam = self.najdi_zaznam(spz)
        if zaznam is None:
            return False

        return zaznam.zaplaceno

    def proved_vyjezd(self, spz: str) -> bool:
        zaznam = self.najdi_zaznam(spz)
        if zaznam is None:
            return False

        if not zaznam.zaplaceno:
            return False

        self.zaznamy.remove(zaznam)
        self.uloz_do_souboru()
        return True

    def vypis_vsechna_auta(self) -> None:
        if not self.zaznamy:
            print("Parkoviště je prázdné-")
            return

        print("=== Auta na parkovišti ===")
        for zaznam in self.zaznamy:
            print(zaznam)
