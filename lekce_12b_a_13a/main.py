from cenik import Cenik
from parkoviste import Parkoviste


def main() -> None:
    cenik = Cenik(48)

    parkoviste = Parkoviste(cenik)

    print("Vjezdy:")
    print(parkoviste.zapis_vjezd("1AC5547", "2026-03-19 08:15:25"))
    print(parkoviste.zapis_vjezd("3T42055", "2026-03-19 09:48:42"))
    print(parkoviste.zapis_vjezd("7SA0144", "2026-03-19 10:10:10"))

    print(parkoviste.spocitej_cenu_parkovani("1AC5547", "2026-03-19 20:31:59"))
    print(parkoviste.oznac_jako_zaplacene("1AC5547"))
    print(parkoviste.muze_odjet("1AC5547"))


if __name__ == "__main__":
    main()
