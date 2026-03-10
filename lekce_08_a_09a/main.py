from polozka import Polozka
from typy_dokladu import Faktura, Zaloha, Dobropis
from uctarna import Uctarna


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

    doklady = [
        Faktura("2026-01", "Abeceda s.r.o.", polozky1, sazba_dph=-0.2),
        Zaloha("2026-Z01", "OMEGA s.r.o.", polozky2, procento=0.5),
        Dobropis("2026-D01", "Mr. Q", polozky3, procento_vraceni=1.0)
    ]

    uctarna = Uctarna(doklady)
    uctarna.vypis_prehled()

    print(f"Celkový obrat: {uctarna.obrat():.2f}")
    print(f"Celkové DPH (jen fa): {uctarna.celkove_dph():.2f}")
    print(f"Počet dokladů podle typu: {uctarna.souhrn_podle_typu()}")


if __name__ == "__main__":
    main()
