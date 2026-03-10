from evidenceStudentu_OOP import Student


def nacti_znamku():
    while True:
        text = input("Zadej znamku: ")
        try:
            z = int(text)
            if 1 <= z <= 5:
                return z
            else:
                print("Chyba.")
        except ValueError:
            print("Chyba.")


studenti = []
studenti.append(Student("Jana"))
studenti.append(Student("Pavel"))

for student in studenti:
    print("\nZadávání známek pro ", student.jmeno)
    for i in range(3):
        znamka = nacti_znamku()
        student.pridej_znamku(znamka)

print("=== VÝPIS ===")
for student in studenti:
    student.vypis()