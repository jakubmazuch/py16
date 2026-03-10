from kalkulacka import Kalkulacka


def nacti(text):
    while True:
        try:
            return float(input(text).replace(",","."))
        except ValueError:
            print("Chyba. Zadej platné číslo.")


a = nacti("Zadej první číslo: ")
b = nacti("Zadej druhé číslo: ")

k = Kalkulacka(a, b)

print("Sčítání: ", k.scitani())
print("Odčítání: ", k.odcitani())
print("Násobení: ", k.nasobeni())

try:
    print("Dělení: ", k.deleni())
except ZeroDivisionError as e:
    print(e)
