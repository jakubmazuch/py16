from abc import ABC, abstractmethod


class Vozidlo(ABC):
    def __init__(self, znacka, kapacita, spotreba):
        self.znacka = znacka
        self.kapacita = kapacita
        self.spotreba = spotreba
        self.ujeto_km = 0

    @abstractmethod
    def typ_paliva(self):
        pass

    def vypocet_spotreba(self, vzdalenost):
        return (self.spotreba / 100) * vzdalenost

    @abstractmethod
    def jed(self, vzdalenost):
        pass

    def info(self):
        return f"{self.znacka} ({self.__class__.__name__}) - kapacita: {self.kapacita} míst, spotřeba: {self.spotreba} {self.typ_paliva()}/100km"


class Auto(Vozidlo):
    def typ_paliva(self):
        return "l benzínu"

    def jed(self, vzdalenost):
        spotreba = self.vypocet_spotreba(vzdalenost)
        self.ujeto_km += vzdalenost
        print(f"{self.znacka} ujel {vzdalenost} km, spotřeba: {spotreba:.2f} l benzínu.")


class Motocykl(Vozidlo):
    def typ_paliva(self):
        return "l benzínu"

    def jed(self, vzdalenost):
        spotreba = self.vypocet_spotreba(vzdalenost)
        self.ujeto_km += vzdalenost
        print(f"{self.znacka} ujel {vzdalenost} km, spotřeba: {spotreba:.2f} l benzínu.")


class Autobus(Vozidlo):
    def typ_paliva(self):
        return "l naftu"

    def jed(self, vzdalenost):
        spotreba = self.vypocet_spotreba(vzdalenost)
        self.ujeto_km += vzdalenost
        print(f"{self.znacka} ujel {vzdalenost} km, spotřeba: {spotreba:.2f} l nafty.")


class Elektroauto(Vozidlo):
    def typ_paliva(self):
        return "kWh eletkřiny"

    def jed(self, vzdalenost):
        spotreba = self.vypocet_spotreba(vzdalenost)
        self.ujeto_km += vzdalenost
        print(f"{self.znacka} ujel {vzdalenost} km, spotřeba: {spotreba:.2f} kWh elektřiny.")


class VozovyPark:
    def __init__(self):
        self.vozidla = []

    def pridej_vozidlo(self, vozdilo):
        self.vozidla.append(vozdilo)

    def odeber_vozidlo(self, znacka):
        self.vozidla = [v for v in self.vozidla if v.znacka != znacka]

    def vypis(self):
        print("=== Vozový park ===")
        print(f"Počet vozidel: {len(self.vozidla)}\n")
        for v in self.vozidla:
            print(v.info())

    def vysli_vsechna(self, vzdalenost):
        print(f"\n=== Všechna vozdila jedou {vzdalenost} km ===")
        for v in self.vozidla:
            v.jed(vzdalenost)

    def pocet(self):
        return len(self.vozdila)

    def nejuspornejsi_vozidlo(self):
        if not self.vozidla:
            return None
        return min(self.vozidla, key=lambda v: v.spotreba)
