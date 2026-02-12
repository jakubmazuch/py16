class Teplomer:
    def __init__(self, teplota_c: float):
        self.teplota_c = teplota_c

    def fahrenheit(self) -> float:
        return self.teplota_c * 9/5 + 32

    def kelvin(self) -> float:
        return self.teplota_c + 273.15

    def komentar(self) -> str:
        t = self.teplota_c

        if t < -12:
            return "Nikam nechoď, nebo zmrzne nos."
        elif t < 0:
            return "Mrzne"
        elif t < 13:
            return "Chladno"
        elif t < 25:
            return "Příjmeně"
        elif t < 33:
            return "Teplo"
        else:
            return "Vedro"
