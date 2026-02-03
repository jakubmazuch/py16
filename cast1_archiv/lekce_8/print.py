jmeno = input("Zadej jméno: ")

while True:
    try:
        roknarozeni = int(input("Zadej rok narození: "))

        if roknarozeni < 1920:
            print(f"Tento rok narození ({roknarozeni}) není platný.")
            continue

        if roknarozeni > 2025:
            print(f"Tento rok narození ({roknarozeni}) není platný.")
            continue

        break

    except ValueError:
        print("Chyba: rok musí být číslo!")


print(f"Milý {jmeno},\nletos Ti bude {2025-roknarozeni} let.")
