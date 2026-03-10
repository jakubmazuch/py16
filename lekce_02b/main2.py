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
    "cyril@gmail.com",
    "1995-12-24"
)

dasa = Student(
    "Dagmar",
    "Svobodová",
    "dasa@svoboda55.cz",
    "1990-04-05"
)

erik = Student(
    "Erik",
    "Máchal",
    "machalerik@example.com",
    "2020-07-05"
)

python = Kurz("Python - začátečníci", 3)
webdesign = Kurz("Webdesign", 10)

adam.prihlas_se(webdesign)
beata.prihlas_se(webdesign)
cyril.prihlas_se(webdesign)
dasa.prihlas_se(webdesign)
erik.prihlas_se(webdesign)

webdesign.vypis(jen_neplnoleti=True)
