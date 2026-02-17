class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.kamos = None

    def skamarad_se(self, druhy):
        self.kamos = druhy
        druhy.kamos = self

    def zrus_kamaradstvi(self):
        if self.kamos is not None:
            druhy = self.kamos
            self.kamos = None
            druhy.kamos = None

    def predstav_se(self):
        if self.kamos is None:
            kamarad = "nemám"
        else:
            kamarad = self.kamos.jmeno

        print("Ahoj, jmenuji se", self.jmeno,
              "a mám", self.vek, " let a můj kámoš je", kamarad, ".")
