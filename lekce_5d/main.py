from ctenar import Ctenar


anna = Ctenar("Anna Dvořáková", 21, "1984")
tomas = Ctenar("Tomáš Vlček", 19, "Harry Potter")

anna.predstav_se()
tomas.predstav_se()

anna.ohodnot(4)
tomas.ohodnot(5)

anna.zobraz_hodnoceni()
tomas.zobraz_hodnoceni()

tomas.vymen_knihy(anna)