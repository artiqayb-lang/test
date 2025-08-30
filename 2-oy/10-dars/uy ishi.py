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