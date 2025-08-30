fayl = open("example1.txt", "w")
with fayl as f:
    f.write("Salom, bu with misolidir.")

fayl = open("example1.txt", "r")
with fayl as f:
    print(f.read())

fayl = open("example1.txt", "a")
with fayl as f:
    f.write("\nYana bir qator")

fayl = open("example1.txt", "r")
with fayl as f:
    for qator in f:
        print(qator.strip())

raqamlar = open("raqamlar.txt", "w")
with raqamlar as f:
    for i in range(5):
        f.write(f"{i}\n")

b_fayl = open("binfile1.dat", "wb")
with b_fayl as f:
    f.write(b"binary data")

b_fayl = open("binfile1.dat", "rb")
with b_fayl as f:
    print(f.read())

import json

data = {"name": "Ali", "age": 25}
jsonfile = open("data1.json", "w")
with jsonfile as f:
    json.dump(data, f)

jsonfile = open("data1.json", "r")
with jsonfile as f:
    info = json.load(f)
    print(info)

try:
    fayl = open("yoqfayl.txt", "r")
    with fayl as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi.")  # 1. Faylga yozish
fayl = open("example1.txt", "w")
with fayl as f:
    f.write("Salom, bu with misolidir.")

    data = {"ism": "Ali", "yosh": 25}
    f = open("data.json", "w")
    json.dump(data, f)
    f.close()
f = open("file1.txt", "w")
f.write("Salom, dunyo!")
f.close()

f = open("file1.txt", "r")
print(f.read())
f.close()

f = open("file1.txt", "a")
f.write("\nYangi qator")
f.close()

try:
    f = open("file2.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Fayl topilmadi!")

f = open("list.txt", "w")
for i in range(5):
    f.write(f"{i}\n")
f.close()

f = open("list.txt", "r")
for line in f:
    print(line.strip())
f.close()

f = open("binary.dat", "wb")
f.write(b"12345")
f.close()

f = open("binary.dat", "rb")
data = f.read()
print(data)
f.close()

f = open("rewrite.txt", "w")
f.write("Bu yangi matn.")
f.close()

import json

data = {"ism": "Ali", "yosh": 25}
f = open("data.json", "w")
json.dump(data, f)
f.close()
