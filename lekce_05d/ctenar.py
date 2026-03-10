class Ctenar:
    def __init__(self, jmeno, vek, oblibena_kniha):
        self.jmeno = jmeno
        self.vek = vek
        self.oblibena_kniha = oblibena_kniha
        self.hodnoceni = None

    def predstav_se(self):
        print("Čau, já se jmenuji ", self.jmeno, 
              "mám", self.vek,
              "a má oblíbená kniha je",
              self.oblibena_kniha, ".")

    def ohodnot(self, c):
        if 1 <= c <= 5:
            self.hodnoceni = c
            return True
        return False

    def zobraz_hodnoceni(self):
        if self.hodnoceni is None:
            print(self.jmeno, "zatím nemá ohodnocenou knihu", self.oblibena_kniha, ".")
        else:
            print(self.jmeno, "hodnotí knihu", self.oblibena_kniha, "na", self.hodnoceni, "/5")

    def vymen_knihy(self, druhy):
        temp = self.oblibena_kniha
        self.oblibena_kniha = druhy.oblibena_kniha
        druhy.oblibena_kniha = temp
