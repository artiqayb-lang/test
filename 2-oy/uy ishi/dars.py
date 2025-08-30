class Transport:
    def __init__(self, nomi):
        self.nomi = nomi

    def harakatlan(self):
        return f"{self.nomi} harakatlanmoqda"


class Avtomabil(Transport):
    def harakatlan(self):
        return f"{self.nomi} BMWdan otib ketmoqda"


class Vertalyot(Transport):
    def harakatlan(self):
        return f"{self.nomi} hovoda uchadi"

avto = Avtomabil('mersades')
vertalyot = Vertalyot('qiruvchi')
print(avto.harakatlan())
print(vertalyot.harakatlan())
