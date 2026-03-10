from Kurz import Kurz
from Student import Student

adam = Student(
    "Adam",
    "Švihlý",
    "adam.svihly@centrum.cz",
    "2005-05-14"
)

beata = Student(
    "Beáta",
    "Kolínská",
    "kocicka25@gmail.com",
    "1977-12-24"
)

cyril = Student(
    "Cyril",
    "Novák",
    "kocicka25@gmail.com",
    "1995-12-24"
)

python = Kurz("Python - začátečníci", 3)

ok, zprava = python.pridej_studenta(adam)
print(zprava)

ok, zprava = python.pridej_studenta(beata)
print(zprava)

ok, zprava = python.pridej_studenta(cyril)
print(zprava)


python.vypis()
