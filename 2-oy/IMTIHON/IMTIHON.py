# 11
# f = open("hello.txt",'w')
# f.write("salom dunyo\n")
# f.close()





# 12
# f = open("data.txt",'r')
# print(f.read())
# f.close()

# 13
# ism = input("Iltimos, ismingizni kiriting: ")
#
# with open("ism_fayli.txt", "w") as fayl:
#     fayl.write(ism)
#
# print("Ismingiz faylga saqlandi: ism_fayli.txt")


# 14
# f = open("open.txt", "r")
# print(f.readline())
# f.close()

# 15
# with open("ism_fayli.txt", 'r', ) as fayl:
#     satrlar = fayl.readlines()
#
# print("Fayldagi satrlar ro'yxati:")
# print(satrlar)

"""
16
"""

# with open("raqamlar.txt", "w") as fayl:
#     for raqam in range(1, 6):
#         fayl.write(f"{raqam}\n")


"""
17
"""
# with open("input.txt", "r", ) as fayl:
#     matn = fayl.read()
#
# sozlar = matn.split()
# sozlar_soni = len(sozlar)
#
# print("So‘zlar soni:", sozlar_soni)


"""
18
"""

# with open("with.txt", "r") as f:
#     matn = f.read()
#     print(matn)

# """
# 19
# """

# with open("python.txt", "w") as fayl:
#     for i in range(5):
#         fayl.write("Python\n")






"""
20
"""
# try:
#     with open("malumot.txt", "r") as fayl:
#         mazmun = fayl.read()
#         print(mazmun)
# except FileNotFoundError:
#     print("Fayl topilmadi")










