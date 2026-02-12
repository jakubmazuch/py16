class NakladniAuto:
    def __init__(self, nosnost_kg: int = 3000):
        self.nosnost_kg = nosnost_kg
        self.naklad_kg = 0

    def naloz(self, kolik_kg: int) -> bool:
        if kolik_kg <= 0:
            False

        if self.naklad_kg + kolik_kg > self.nosnost_kg:
            return False

        self.naklad_kg += kolik_kg
        return True

    def vyloz(self, kolik_kg: int) -> bool:
        if kolik_kg <= 0:
            return False

        if kolik_kg > self.naklad_kg:
            return False

        self.naklad_kg -= kolik_kg
        return True

    def stav(self) -> int:
        return self.naklad_kg
