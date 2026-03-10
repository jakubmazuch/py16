from datetime import date


class Platba:
    def __init__(
        self,
        castka: float,
        poznamka: str = "",
        datum: date | None = None
    ):
        if castka <= 0:
            raise ValueError("Částka platby musí být kladná.")

        self.castka = float(castka)
        self.poznamka = poznamka
        self.datum = datum if datum else date.today()

    def __repr__(self) -> str:
        return f"Platba({self.castka}, {self.poznamka}, {self.datum})"
