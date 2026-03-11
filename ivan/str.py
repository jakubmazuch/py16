class Auto:
    def __init__(self, znacka):
        self.znacka = znacka

    def __str__(self):
        return f"Text {self.znacka}"


a1 = Auto("BMW")
a2 = Auto("acsnijadc")
print(a1, a2)