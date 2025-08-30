# """
# Inkapsiulyatsiya
# """
#
#
# class Biznes:
#     def __init__(self, nomi, login, password):
#         self.nomi = nomi
#         self.login = login
#         self.__password = password
#         def malumot(self):
#             return (f"Kampaniyaning nomi {self.nomi},"
#                     f"login {self._login}, {self.__password}")
# class Filial(Biznes):
#     def malumot(self):
#         return (f"Kampaniyaning nomi {self.nomi}"
#                 f"Login {self.login},")
# b = Biznes('acer','acer','acer')
# f = Filial('Viktus','acer','acer')
# print(b.malumot())
# print(f.malumot())

# class BankHisobi:
#     def __init__(self, ism, balans):
#         self.ism = ism
#         self.balans = balans
#
#     def balans(self):
#         return f"{self.ism}ning balansi {self.__balans}"
#
# b = BankHisobi('Diyor','10 mln')
# print(b.balans())
