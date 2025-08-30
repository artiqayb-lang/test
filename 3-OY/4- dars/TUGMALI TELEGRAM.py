import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyexpat.errors import messages

BOT_TOKEN = "8093886216:AAFULEMslAbsTWoOjc-tIWK3cM6nrJ3da3I"

bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()

btn1 = KeyboardButton(text="moshina🚘")
btn2 = KeyboardButton(text="tabiat🌳")
btn3 = KeyboardButton(text="ozim xaqimda‍👤")
btn4 = KeyboardButton(text="yordam👍")
btn5 = KeyboardButton(text="dars👍")

kb = ReplyKeyboardMarkup(
     keyboard=[
        [btn1, btn2],
        [btn3, btn4, btn5]
     ],
     resize_keyboard=True

)


@dp.message(Command("start"))
async def start_heandlar(massage:types.Message):
    await massage.answer("bitta tugmani tanlang",reply_markup=kb)
@dp.message()
async def answer(massage:types.Message):
    if massage.text == "moshina🚘":
        await massage.answer("BMW i — kam yoqilgʻi sarflaydigan yuqori texnologiyali gibrid va elektromobillarni ishlab chiqarish uchun tashkil qilingan BMW boʻlimi. 2010-yil oxirida BMW i1, i2, i3, i4, i5, i6, i7, i8 va i9 avtomobillari nomlarini savdo belgisi sifatida roʻyxatda")


    elif massage.text == "tabiat🌳":
        await massage.answer("Tabiat — odamning paydo boʻlgunicha ham, odam ishtiroki bilan ham mavjud borliq. Umuman — bu dunyo, odam, koinot; mikromakromega dunyolar; Jonsiz. va jonli narsalar bor. Tor maʼnoda — tabiat fanlari oʻrganadigan obyekt. Tabiat odamga, jamiyatga bogʻliq boʻlmagan qonuniyatga boʻysunadi. Odam tabiatning bir qismi. Odam tabiat qonunlarini oʻzgartira olmaydi, faqat qonunlardan foydalanib, tabiat elementlarini, qismlarini oʻzlashtirishi mumkin. Tabiat tushunchasi insoniyat jamiyati yashashi tabiiy sharoitlarining majmui sifatida ham qaraladi. Inson yashashi uchun mehnat qiladi, mehnat (mas., dehqonchilik, qurilish, sanoat), miya faoliyati va boshqa esa tabiatning baʼzi jihatlarini oʻzgartiradi. Odam tomonidan, yaʼni ijtimoiy mehnat jarayonida yaratiladigan moddiy boyliklar shartli ravishda „ikkinchi tabiat“ deyiladi. Masalan, vodoroddan urangacha boʻlgan 92 ta kimyoviy element tabiiydir, undan keyingi kashf etilganlari sunʼiydir. Barcha sunʼiy sintetik kimyoviy birikmalar, odam yaratayotgan atom va yadro energiyalari „ikkinchi tabiat“ga kiradi.")



    elif massage.text == "ozim xaqimda‍👤":
        await massage.answer("meni ismim Nursulton,men hozirda IT darslariga boraman,darslar juda qiziq biz hozirda telegram bot yaratishni organyapman, men va akam intelekt edu oquv markazida oqiymiz!")


    elif massage.text == "yordam👍":
        await massage.answer("siz darsga xar-xil molumotlar kerak bolsa sizga wikipediya yordam beradi uyerdan xar-xil turdagi savolarga ham javob topasiz ")


    elif massage.text == "dars👍":
        await massage.answer(" darsda eng qiziq voqiyalar boladigan paytlar kop boladi masalan sozni xato yozib qoyish,xarflarni almashtirib qoyishingiz mumkun  xato qilmaslik uchun koproq oqing! ")






async def main():
    print("bugungi sana bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())






































