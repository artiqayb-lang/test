"""
Bankomat tiziminig becent qismi
1.Balans ko'rish
2.pul qo'yish
3.pul yechish
"""


class Bankomat:
    def __init__(self, balans=0):
        self.balans = balans

    def balans_korish(self):
        print( f"sizning balansingiz {self.balans} som😁👍")

    def pul_qoyish(self, summ):
        self.balans += summ
        print(f"Qoshilgan summa = {summ}\n"
              f"Hozirgi balansingiz = {self.balans}")

    def pul_yechish(self, summ):
        self.balans -= summ +summ * 0.02
        if summ > self.balans:
            print("Balansingizda kerakli summa yo'q"
                  "Qaytadan urinib korish ")
        else:
            print(f"Yechilgan summ = {summ}/n"
                  f"Hozirgi balanisingiz = {self.balans}")




bankamat = Bankomat(1000000)

while True:
    print("""
    -----M E N Y U-----
    
    1. Balans korish💵
    2. pul qoyish💶
    3. pul yechish💴
    4. Chiqish💸
    """)

    tanlov = input("Tanlang (1-4) = ")
    if tanlov =="1":
        bankamat.balans_korish()
    elif tanlov == "2":
        summ = int(input("Qoyiladian Summani kiriting = "))
        bankamat.pul_qoyish(summ)
    elif tanlov == "3":
        summ = int(input("Yechibolmoqchi bolgan summangiz"))
        bankamat.pul_yechish(summ)
    elif tanlov == "4":
        print("Chiqilmoqda ...........Hayr")
        break
    else:
        print("Bunday buyruq yo'q")