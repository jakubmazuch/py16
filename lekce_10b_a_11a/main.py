from polozka import Polozka
from typy_dokladu import Faktura, Zaloha, Dobropis, SlevaDoklad
from uctarna import Uctarna
from platba import Platba


def main() -> None:
    polozky1 = [
        Polozka("Vývoj webu", 15, 1200),
        Polozka("Školení", 3, 1500),
    ]
    polozky2 = [
        Polozka("Výuka matematiky", 16, 600),
        Polozka("Tvorba programu na míru", 20, 1500),
    ]
    polozky3 = [
        Polozka("Reklamace", 1, 3000),
    ]

    faktura = Faktura("2026-01", "Abeceda s.r.o.", polozky1, sazba_dph=0.2)
    zaloha = Zaloha("2026-Z01", "OMEGA s.r.o.", polozky2, procento=0.5)
    dobropis = Dobropis("2026-D01", "Mr. Q", polozky3, procento_vraceni=1.0)
    sleva = SlevaDoklad("2026-S01", "Nováková Pavlína, s.r.o.", polozky2, sleva=0.2, sazba_dph=0.21)

    faktura.pridej_platbu(Platba(10000, "bankovni převod"))
    faktura.pridej_platbu(Platba(5000, "hotově"))

    zaloha.pridej_platbu(Platba(15000, "bankovní převod"))

    doklady = [faktura, zaloha, dobropis, sleva]

    uctarna = Uctarna(doklady)
    uctarna.vypis_prehled()
    uctarna.vypis_stav_plateb()

    print(f"Celkový obrat: {uctarna.obrat():.2f}")
    print(f"Celkové DPH (jen fa): {uctarna.celkove_dph():.2f}")
    print(f"Počet dokladů podle typu: {uctarna.souhrn_podle_typu()}")


if __name__ == "__main__":
    main()
