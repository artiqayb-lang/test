import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyexpat.errors import messages

BOT_TOKEN = "8413025019:AAGDICIXm_jpmTJ7tUuhoIRFnnq3okwiqfA"

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
        await massage.answer("Avtomobil (lotincha: mobilis – harakatchan) – dvigatel yordamida harakatga keltiriladigan relssiz transport vositasi. Yoʻlovchilar va yuk tashishga moʻljallangan.1751-1752-yillarda Nijniy Novgorod gubernyasi (Rossiya) dehqoni Leontiy Shamshurenkov ikki kishi oyogʻi bilan yurgiziladigan „oʻziyurar aravacha“ qurdi. I. P. Kulibin bir qancha muhim mexanizmlarni, uzatmalar qutisini taklif qildi. Bugʻ mashinasi paydo boʻlgandan keyin ixtirochilar undan mexanik aravada foydalanishga harakat qildilar. 1769-1770 yillarda fransuz harbiy muhandisi N. J. Kyuno artilleriya toʻplari uchun 3 gʻildiraklibugʻ aravasi qurdi. Angliyada 1802-yilda Trevitnik bugʻ mashinasi oʻrnatilgan A. qurdi. 1830-yilda rus ustasi K. Yankevich bugʻ avtomobillariga temirdan yasalgan 100 dan ortiq gaz quvurli bugʻ qozoni oʻrnatishni taklif etdi. Akkumulyatordan tok olib ishlay-digan elektr dvigatelli avtomobillar bilan ham koʻpgina tajribalar oʻtkazildi. Ichki yonuv dvigateli ixtiro qilingandan keyin avtomobillar muntazam rivojlantirila boshlandi. Avtomobillarga benzin va kerosin bilan ishlaydigan dvigatellar oʻrnatish borasida turli mamlakatlarning koʻpgina ixtirochilari ish olib bordilar. 1885-1886-yillarda Germaniyada Daymler benzin bilan ishlaydigan dvigatelni mototsiklga, Bens esa uch gʻildirakli avtomobillarga oʻrnatdi. Temir gʻildiraklar oʻrniga yaxlit rezina shinalar, 1890-yildan esa pnevmatik rezina shinalar ishlatila boshladi. Avtomobilsozlik dastlab Fransiyada, soʻngra AQSH, Germaniya va Yaponiyada rivojlandi. Oʻzbekiston mustaqillikka erishganidan soʻng avtomobil sanoati rivojlangan mamlakatlar qatoriga qoʻshildi. Asaka shahri (Andijon viloyati)da Janubiy Koreyaning DAEWOO korporatsiyasi bilan hamkorlikda barpo etilgan „OʻzDAEWOO Avto“ qoʻshma korxonasida 1996-yildan boshlab „Neksiya“, „Damas“ va „Tiko“ yengil avtomobillari ishlab chiqara boshlandi. 1999-yilda Samarqandda ishga tushgan „SamKochAvto“ oʻzbek-turk qoʻshma korxonasi M23.9, M24.9, M29 rusumli avtobuslar va 35.9, 65.9, 80.12, 85.12, 85.14 rusumli har xil yuk avtomobillari ishlab chiqaradi (qarang Avtomobil sanoati). Avtomobil turlarining transport, maxsus va poygaga muljallangan xillari bor. Transport avtomobillari yengil avtomobillar, avtobus va yuk avtomobillarga boʻlinadi. Maxsus avtomobillar maʼlum ishlar uchun moʻljallanadi va tegishli uskunalar bilan jihozlanadi. Oʻt oʻchirish, un tashish, sement tashish, sanitariya avtomobillari, axlat tashiydigan avtomobillar, avtokranlar, avtoyuklagichlar va boshqa maxsus avtomobillar shular jumlasidan. Poyga avtomobillari sportda ishla-tiladi. Yengil avtomobillar 2 dan 8 tagacha oʻrinli boʻladi. Ular berk kuzovli (sedan va limuzin), ochiq kuzovli (faeton) va ochiladigan kuzovli (kabriolet) boʻlishi mumkin. Yuk avtomobillari 0,25 tonnadan 100 tonnagacha va undan ortiq yuklarni tashiydigan kuzovli, tirkamalar, yarim tirkamalarni tortish uchun muljallangan kuzovsiz boʻladi. Oʻtuvchanligi boʻyicha tekis va qiyin yoʻllarda yuradigan, harakatlanuvchi qismning tuzilishi boʻyicha gʻildirakli, gʻildirak-gusenitsali, yarim gusenitsali, pnevmatik galtakli va boshqa xillarga boʻlinadi.")


    elif massage.text == "tabiat🌳":
        await massage.answer("Tabiat — odamning paydo boʻlgunicha ham, odam ishtiroki bilan ham mavjud borliq. Umuman — bu dunyo, odam, koinot; mikromakromega dunyolar; Jonsiz. va jonli narsalar bor. Tor maʼnoda — tabiat fanlari oʻrganadigan obyekt. Tabiat odamga, jamiyatga bogʻliq boʻlmagan qonuniyatga boʻysunadi. Odam tabiatning bir qismi. Odam tabiat qonunlarini oʻzgartira olmaydi, faqat qonunlardan foydalanib, tabiat elementlarini, qismlarini oʻzlashtirishi mumkin. Tabiat tushunchasi insoniyat jamiyati yashashi tabiiy sharoitlarining majmui sifatida ham qaraladi. Inson yashashi uchun mehnat qiladi, mehnat (mas., dehqonchilik, qurilish, sanoat), miya faoliyati va boshqa esa tabiatning baʼzi jihatlarini oʻzgartiradi. Odam tomonidan, yaʼni ijtimoiy mehnat jarayonida yaratiladigan moddiy boyliklar shartli ravishda „ikkinchi tabiat“ deyiladi. Masalan, vodoroddan urangacha boʻlgan 92 ta kimyoviy element tabiiydir, undan keyingi kashf etilganlari sunʼiydir. Barcha sunʼiy sintetik kimyoviy birikmalar, odam yaratayotgan atom va yadro energiyalari „ikkinchi tabiat“ga kiradi.")



    elif massage.text == "ozim xaqimda‍👤":
        await massage.answer("meni ismim Nursulton,men hozirda IT darslariga boraman,darslar juda qiziq biz hozirda telegram bot yaratishni organyapman, men va akam intelekt edu oquv markazida oqiymiz!")


    elif massage.text == "yordam👍":
        await massage.answer("siz darsga xar-xil molumotlar kerak bolsa sizga wikipediya yordam beradi uyerdan xar-xil turdagi savolarga ham javob topasiz ")


    elif massage.text == "dars👍":
        await massage.answer(" darsda eng qiziq voqiyalar boladigan paytlar kop boladi masalan sozni xato yozib qoyish,xarflarni almashtirib qoyishingiz mumkun  xato qilmaslik uchun koproq oqing! ")






async def main():
    print("bugungi  nursulton bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


