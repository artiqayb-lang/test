# class Hayvon:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
#
# class Ot(Hayvon):
#     def __str__(self):
#         return f"Bu ot nomli class"
#
#     def tezlik(self):
#         return f"{self.nomi} --- bu hayvon tez yuguradi"
#
#
# class SHer(Hayvon):
#     def qirol(self):
#         return f"{self.nomi} O'rmon va hayvonlar qiroli"
#
#
# b = SHer('Sher')
# a = Ot('Mustang')
# print(a.tezlik())
# print(b.qirol())
#
#
# class Moshina:
#     def __init__(self, brend, rangi, narxi):
#         self.brend = brend
#         self.rangi = rangi
#         self.narxi = narxi
#
#     def __str__(self):
#         return "Bu class ota class"
#
#     def malumot(self):
#
#         return "Malumot"
#
# class BMW(Moshina):
#     def __init__(self, brend, rangi, narxi, max_tezligi, ot_kuchi):
#         super().__init__(brend, rangi, narxi)
#         self.max_tezligi = max_tezligi
#         self.ot_kuchi = ot_kuchi
#
#     def umumiy(self):
#         return (f"brend = {self.brend}\n"
#                 f"Nomi = {self.rangi}")
#
# bmw = BMW('Bmw','qora','55567','400km/h','15000')
# print(bmw. umumiy())
# print(bmw.malumot())