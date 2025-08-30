class Transport:
    def __init__(self, nomi):
        self.nomi = nomi

    def harakatlan(self):
        return f"{self.nomi} harakatlanmoqda"


class Qayiq(Transport):
    def harakatlan(self):
        return f"{self.nomi} suvda suzadi"


class Vertalyot(Transport):
    def harakatlan(self):
        return f"{self.nomi} hovoda uchadi"

qayiq = Qayiq('yamaha')
vertalyot = Vertalyot('bell 205')
print(qayiq.harakatlan())
print(vertalyot.harakatlan())
