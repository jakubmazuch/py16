from datetime import date, datetime


class Student:
    def __init__(self, jmeno, prijmeni, email, datum_narozeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.email = email
        self.datum_narozeni = datetime.strptime(datum_narozeni, "%Y-%m-%d").date()

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni

    def vek(self):
        dnes = date.today()
        vek = dnes.year - self.datum_narozeni.year
        if (dnes.month, dnes.day) < (self.datum_narozeni.month, self.datum_narozeni.day):
            vek -= 1
        return vek

    def __str__(self):
        return f"{self.cele_jmeno()} ({self.email}), věk: {self.vek()}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)
