class Polozka:
    def __init__(self, nazev: str, mnozstvi: int, cena_za_ks: float):
        if not nazev or not nazev.strip():
            raise ValueError("Název položky nesmí být prázdný.")
        if mnozstvi <=0 :
            raise ValueError("Množství musí být kladné.")
        if cena_za_ks < 0:
            raise ValueError("Cena za ks nesmí být záporná.")

        self.nazev = nazev.strip()
        self.mnozstvi = int(mnozstvi)
        self.cena_za_ks = float(cena_za_ks)

    def cena_clk(self) -> float:
        return self.mnozstvi * self.cena_za_ks

    def __repr__(self) -> str:
        return f"Položka({self.nazev}, {self.mnozstvi}, {self.cena_za_ks})"
