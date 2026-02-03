def nacti_znamku():
    while True:
        text = input("Zadej známku (1-5): ")
        try:
            z = int(text)
            if 1 <= z <= 5:
                return z
            else:
                print("Neplatná známka.")
        except ValueError:
            print("Zadejte prosím celé číslo.")


def vytvor_studenta(jmeno):
    student = {"jmeno": jmeno, "znamky": []}
    return student


def pridej_znamku(student, znamka):
    student["znamky"].append(znamka)


def prumer(student):
    znamky = student["znamky"]
    if len(znamky) == 0:
        return 0
    return sum(znamky)/len(znamky)


def prospel(student):
    if 5 in student["znamky"]:
        return False
    if prumer(student) >= 4.5:
        return False
    return True


def vypis_studenta(student):
    print("Student: ", student["jmeno"])
    print("Známky: ", student["znamky"])
    print("Průměr: ", round(prumer(student), 2))
    if prospel(student):
        print("Prospěl")
    else:
        print("Neprospěl")
    print()


studenti = []
studenti.append(vytvor_studenta("Jana"))
studenti.append(vytvor_studenta("Jonáš"))
studenti.append(vytvor_studenta("Břetislav"))

for student in studenti:
    print("\nZadáváme známku pro studenta ", student["jmeno"])
    for i in range(3):
        znamka = nacti_znamku()
        pridej_znamku(student, znamka)

print("=== VÝPIS ===")
for student in studenti:
    vypis_studenta(student)
