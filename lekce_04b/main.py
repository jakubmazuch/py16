from teplomer import Teplomer


def nacti(text: str) -> float:
    while True:
        try:
            return float(input(text).replace(",","."))
        except ValueError:
            print("Zadej prosím platné číslo.")


c = nacti("Zadej teplotu ve °C: ")
t = Teplomer(c)

print(f"Teplota: {t.teplota_c} °C")
print(f"Fahrenheit: {t.fahrenheit():.2f} °F")
print(f"Kelvin: {t.kelvin():.2f} K")
print(f"Komentář: {t.komentar()}")
