class ATM:
    def __init__(self):
        self.balans = 0
        self.parol = self._parol_ol()
        self.bloklanan = False

    def _parol_ol(self):
        try:
            with open("password.txt", 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print("parol topilmadi")
            return None

    def parol_tekshirish(self):
        urinishlar = 3
        while urinishlar > 0:
            kiritilgan_parol = input("parolni kiriting")
            if kiritilgan_parol == self.parol:
                print("Muofiqiyali kirdiniz👍")
                return True
            else:
               urinishlar -=1
               print("Paroliniz xato")
        print("Kartaniz bloklandi sababi 3 martadan kop xato parol kiritdiniz")
        self.bloklanan = True
        return False

    def balans_korish(self):
        print(f"sizi balansiniz{self.balans}som")


    def pull_qoshish(self):
        miqdor = int(input("summa kiriting : "))
        self.balans +=miqdor
        if miqdor <=self.balans:
            self.balans -= miqdor
            print(f"Yechilan summa = {miqdor}\n"
            f"Balans ={self.balans}")
    def pull_yechish(self):
                 f"Balans ={self.balans}"

        else:
            print("hisoinizda yealicha malag yoq")
    def menu(self):
        with True
            print("..................ATM..................")
            print("1. Balans korish")
            print("2. pul qoyish")
            print("3 pul yechsh")
            print("4. chiqish")
            tanlov = input("")
        if tanlov == "1":
            self.balans_korish()
        elif tanlov == "2":
            self.pull_qoshish()
        elif tanlov == "3":
            self.pull_yechish()
        elif tanlov == "4":
            print("Tzimdan chiqildi")
            break
        else:
            print("Bunday buyruq mavjud emas")

atm = ATM()
if atm.parol_tekshirish():
    atm.menu
else:


