import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import datetime

BOT_TOKEN = "8093886216:AAFULEMslAbsTWoOjc-tIWK3cM6nrJ3da3I"

bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()


facts = [
    "Bugun yangi imkonyatlar kuni 💸",
    "Har kuni yangi narsani organishga intiling😊",
    "tabasum qiling - bugun yaxshi kun boladi ",
    "Kichik qadamlar katta natijaga alib keladi ",
    "Bugun biror yaxshi ish qiling"

]


@dp.message(CommandStart())
async def start_heandlar(massage:types.Message):
    await massage.answer("Salom  Men bugungi kun xaqida aytadigan botman")

@dp.message()
async def today_handler(massage: types.Message):
    today = datetime.now()
    sana = today.strftime("%Y-%m-%d")
    hafta_kuni =  today.strftime("%A")

    days_uz = {
        "Monday":     "Dushamba",
        "Tuesday":    "Seshamba",
        "Wednesday":  "chorshamba",
        "Thursday":   "Payshamba",
        "Friday":     "Juma",
        "Saturday":   "SHamba",
        "Sunday" :    "Yakshamba",
    }
    hafta_uz = days_uz.get(hafta_kuni, hafta_kuni)

    import random
    fact = random.choice(facts)

    await massage.answer(
        f"📅 Sana: {sana}\n"
        f"📆 Hafta kuni: {hafta_uz}\n"
        f"💡 Qiziqarli fakt: {fact}"
    )

async def main():
    print("bugungi sana bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


