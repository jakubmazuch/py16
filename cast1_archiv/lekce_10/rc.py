def zkontroluj_format(rc):
    """ Funkce boolean True/False """
    if rc.count("/") != 1:
        print("Chyba formátu: rodné číslo musí obsahovat jeden znak '/'")
        return False

    leva, prava = rc.split("/")

    if len(leva) != 6 or len(prava) != 4:
        print("Chyba formátu: očekáváme tvar '######/####'")
        return False

    if not (leva.isdigit() and prava.isdigit()):
        print("Chyba formátu: rodné číslo může obsahovat jet číslice a znak '/'")
        return False

    return True


def kontrolni_cislice(rc_bez):
    prvnich_devet = rc_bez[:9]
    kontrolni = int(rc_bez[9])

    try:
        cislo = int(prvnich_devet)
    except ValueError:
        return False

    zbytek = cislo % 11
    return kontrolni == zbytek


def je_platne(rc):
    """ Funkce boolean True/False """
    if not zkontroluj_format(rc):
        return False

    rc_bez = rc.replace("/", "")

    if not kontrolni_cislice(rc_bez):
        print("Rodné číslo má neplatnou kontrolní číslici.")
        return False

    print("Rodné číslo má správný formát.")
    return True


print("Kontrola validity rodného čísla:")
print("--------------------------------")

rc = input("Zadejte ročné číslo: ").strip()
je_platne(rc)
