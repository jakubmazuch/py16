from nakladni_auto import NakladniAuto


def vypis(popis: str, povedlo_se: bool, auto: NakladniAuto):
    stav = auto.stav()
    vysledek = "OK" if povedlo_se else "Neprovedeno."
    print(f"{popis:<15} -> {vysledek:>11} | naklad: {stav} kg")


auto = NakladniAuto(nosnost_kg=3000)

ok = auto.naloz(10000)
vypis("Nalož 10 tun", ok, auto)

ok = auto.naloz(500)
vypis("Nalož 0,5 tun", ok, auto)

ok = auto.vyloz(300)
vypis("Vylož 300 kg", ok, auto)

ok = auto.vyloz(1000)
vypis("Vylož 1 tunu", ok, auto)

print("\n\nKonečný stav auta: ", auto.stav(), " kg")