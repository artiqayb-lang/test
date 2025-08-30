# def calculator(a, b, ishora):
#     if ishora == '+':
#         return f"natija = {a+b}"
#     elif ishora == '-':
#         return f"Natija={a-b}"
#     elif ishora=='*':
#         return f"Natija = {a/b}"
#     elif ishora=='/':
#         return f"Natija={a*b}"
#     elif ishora=='/':
#         if b == 0:
#             return "0 ga bo'lish munkun emas"
#         else:
#             return f"Natija= {a/b}"
#     else:
#         return 'bunday amal mavjud emas'
#
# a=int(input("1-sonni kiriting=")
# b=int(input("2-sonni kiriting=")
# ishora=input("ishorani kiriting=")
# print( canculator (a,b, ishora)
#
#
# def musbat_manfiy(a):
#     if a > 0:
#         return f"{a} - bu son musbat"
#     elif a == 0:
#         return f"{a} - bu son 0 ga teng"
#     else:
#         return f"{a} - bu son manfiy"
#
# a = int(input('son kiriting'))
# print(musbat_maniy(a))
#
#
# def teskari(a):
#      return str(a)[::-1]
#
# print(teskari(nurli))


def yosh_chegara(yosh):
    if yosh < 8 and yosh >=0:
        return "8 yoshdan kichik yoshlar toifasiga kiradi"
    elif 7 < yosh < 19:
        return" 7 dan katta va 19 dan kichik yoshlar osmir yoshda boladi"
    elif yosh > 18:
        return