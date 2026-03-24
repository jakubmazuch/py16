from datetime import datetime


class ParkovaciZaznam:
    def __init__(self, spz: str, cas_vjezdu: str, zaplaceno: bool = False) -> None:
        self.spz = spz
        self.cas_vjezdu = cas_vjezdu
        self.zaplaceno = zaplaceno
        self.cas_vyjezdu = None

    def uloz_cas_vyjezdu(self, cas_vyjezdu: str) -> None:
        self.cas_vyjezdu = cas_vyjezdu

    def delka_parkovani(self) -> float:
        if self.cas_vyjezdu is None:
            raise ValueError("Čas výjezdu není nastaven")

        vjezd = datetime.fromisoformat(self.cas_vjezdu)
        vyjezd = datetime.fromisoformat(self.cas_vyjezdu)

        rozdil = vyjezd - vjezd
        hodiny = rozdil.total_seconds() / 3600
        return hodiny

    def oznac_jako_zaplacene(self) -> None:
        self.zaplaceno = True

    def na_slovnik(self) -> dict:
        return {
            "spz": self.spz,
            "cas_vjezdu": self.cas_vjezdu,
            "zaplaceno": self.zaplaceno
        }

    @classmethod
    def ze_slovniku(cls, data: dict) -> "ParkovaciZaznam":
        return cls(
            spz=data["spz"],
            cas_vjezdu=data["cas_vjezdu"],
            zaplaceno=data["zaplaceno"]
        )

    def __str__(self) -> str:
        stav = "zaplaceno" if self.zaplaceno else "nezaplaceno"
        return f"{self.spz} | vjezd: {self.cas_vjezdu} | {stav}"
