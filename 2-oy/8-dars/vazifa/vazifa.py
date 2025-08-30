#
#  1. Faylni o‘qish uchun ochish
# file = open('file.txt', 'r')
#
#  2. Faylni yozish uchun ochish
# file = open('file.txt', 'w')
#
#  3. Faylni qo‘shish (append) rejimida ochish
# file = open('file.txt', 'a')
#
# # 4. Faylga yozish
# file = open('file.txt', 'w')
# file.write('Salom')
# file.close()
#
#  5. Faylni o‘qib chiqarish
# file = open('file.txt', 'r')
# print(file.read())
# file.close()
#
#  6. Faylni mavjud bo‘lmasa yaratib yozish
# file = open('file.txt', 'x')
#
#  7. Faylni ochib, qatorma-qator o‘qish
# file = open('file.txt', 'r')
# for line in file:
#     print(line)
# file.close()
#
#  8. Faylga bir nechta qatordan yozish
# file = open('file.txt', 'w')
# file.writelines(['salom\n', 'dunyo\n'])
# file.close()
#
#  9. Faylga yangi qator qo‘shish
# file = open('file.txt', 'a')
# file.write('\nYangi qator')
# file.close()
#
#  10. Faylni binar holatda ochish
# file = open('file.txt', 'rb')
#
# 11. Faylni binar yozish uchun ochish
# file = open('file.txt', 'wb')
#
#  12. Faylni yangilash
# file = open('file.txt', 'r+')
# file.write('Yangilandi')
# file.close()
#
#  13. Faylni mavjudligini tekshirish
# try:
#     file = open('file.txt', 'r')
# except FileNotFoundError:
#     print("Fayl topilmadi")
#
#  14. Faylni ochib, birinchi qatordan faqat o‘qish
# file = open('file.txt', 'r')
# print(file.readline())
# file.close()
#
#  15. Fayl ochish va darhol yopish
# file = open('file.txt', 'w'); file.close()

# # 1. Fayl ochish va o‘qish
# with open('file.txt', 'r') as file:
#     data = file.read()
#     print("1. Fayl mazmuni:", data)
#
# # 2. Faylga yozish
# with open('output.txt', 'w') as file:
#     file.write("Hello, world!")
#
# # 3. Bir nechta fayllarni birgalikda ochish
# with open('file1.txt', 'w') as f1:
#     f1.write("File 1")
# with open('file2.txt', 'w') as f2:
#     f2.write("File 2")
# with open('file1.txt') as f1, open('file2.txt') as f2:
#     print("3. File1:", f1.read())
#     print("3. File2:", f2.read())
#
# # 4. Faylni satrma-satr o‘qish
# with open('file.txt', 'r') as file:
#     print("4. Fayl satrlari:")
#     for line in file:
#         print(line.strip())
#
# # 5. ZIP faylni ochish
# import zipfile
# with zipfile.ZipFile('example.zip', 'w') as zipf:
#     zipf.writestr('test.txt', 'Zip ichidagi fayl')
#
# with zipfile.ZipFile('example.zip', 'r') as zip_ref:
#     zip_ref.extractall('extracted_folder')
#
# # 6. JSON faylni o‘qish
# import json
# with open('data.json', 'w') as f:
#     json.dump({"name": "Ali", "age": 25}, f)
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print("6. JSONdan o'qildi:", data)
#
# # 7. threading.Lock() bilan ishlash
# import threading
# lock = threading.Lock()
# with lock:
#     print("7. Thread-safe hudud")
#
# # 8. decimal.localcontext() bilan hisoblash
# from decimal import Decimal, localcontext
# with localcontext() as ctx:
#     ctx.prec = 4
#     result = Decimal('1') / Decimal('7')
#     print("8. Decimal natija:", result)
#
# # 9. sqlite3 bilan ishlash
# import sqlite3
# with sqlite3.connect('example.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
#     cursor.execute("SELECT sqlite_version();")
#     print("9. SQLite versiya:", cursor.fetchone())
#
# # 10. Faylni ochishda xatolikni ushlash
# try:
#     with open('file.txt', 'r') as file:
#         print("10. Fayl o‘qildi:", file.read())
# except FileNotFoundError:
#     print("10. Fayl topilmadi.")
#
# # 11. Faylni binary rejimda o‘qish
# with open('output.txt', 'rb') as f:
#     content = f.read()
#     print("11. Binary mazmuni:", content)
#
# # 12. CSV faylni o‘qish
# import csv
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name', 'Age'])
#     writer.writerow(['Ali', 25])
# with open('data.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     print("12. CSV fayl mazmuni:")
#     for row in reader:
#         print(row)
#
# # 13. Faylga qo‘shimcha yozish
# with open('test.txt', 'a') as f:
#     f.write("13. Yangi satr\n")
#
# # 14. Maxsus kontekst menejeri
# class MyContext:
#     def __enter__(self):
#         print("14. Enter blok")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("14. Exit blok")
#
# with MyContext():
#     print("14. Ichki blok")
#
# # 15. Vaqtinchalik fayl yaratish
# import tempfile
# with tempfile.TemporaryFile() as temp:
#     temp.write(b'15. Hello!')
#     temp.seek(0)
#     print("15. Temp fayldan o‘qish:", temp.read())







