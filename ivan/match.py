volba = int(input("Zadej číslo 1, 2, 3"))

match volba:
    case 1:
        print("Uživatel zadal jedničku.")
    case 2:
        print("Uživatel zadal dvojku.")
    case 3:
        print("Uživatel zadal trojku.")
    case _:
        print("Uživatel nezadal jedničku, dvojku ani trojku.")
