class Kurz:
    def __init__(self, nazev, kapacita):
        self.nazev = nazev
        self.kapacita = kapacita
        self.studenti = []

    def je_plny(self):
        return len(self.studenti) >= self.kapacita

    def volna_mista(self):
        return self.kapacita - len(self.studenti)

    def pridej_studenta(self, student):
        if self.je_plny():
            return False, "Kurz je plný."
        if student in self.studenti:
            return False, "Duplicita Studenta."

        self.studenti.append(student)
        return True, "Student byl přidán."

    def odeber_studenta(self, student):
        if student not in self.studenti:
            return False, "Student v kurzu není."

        self.studenti.remove(student)
        return True, "Student byl odebrán."

    def vypis(self):
        print("Název kurzu", self.nazev)
        print("Kapacita", len(self.studenti), "/", self.kapacita)

        if len(self.studenti) == 0:
            print("Žádní žáci v kurzu.")
            return

        print("Studenti:")
        for s in self.studenti:
            print("-", s)
