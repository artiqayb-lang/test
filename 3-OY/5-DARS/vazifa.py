from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = "8413025019:AAGDICIXm_jpmTJ7tUuhoIRFn nq3okwiqfA"

bot = Bot(token=TOKEN)
dp = Dispatcher()


reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" yangi xabarlar📣"), KeyboardButton(text="malumot📪")],
        [KeyboardButton(text="📞 qong'iroq"), KeyboardButton(text="🎯 savol")]
    ],
    resize_keyboard=True
)


inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Google", url="https://google.com")],
        [InlineKeyboardButton(text="google meet", callback_data="https://meet.google.com/landing")],
        [InlineKeyboardButton(text="git hub", url="https://github.com/")],
        [InlineKeyboardButton(text="zo'r tv futbol", url="https://t.me/zor_tv_jonli_efir_zortv0")],

    ]
)

@dp.message()
async def main_handler(message: types.Message):
    if message.text == "/start":
        await message.answer("Assalomu alaykum! Tugmalardan birini tanlang iltimos 👇", reply_markup=reply_kb)

    elif message.text == "yangi xabarlar📣":
        await message.answer("siz uchun yangiliklar:", reply_markup=inline_kb)

    elif message.text == "malumot📪":
        await message.answer("bu bot maxsus tugmalarni ishlati")

    elif message.text == "📞 qong'iroq":
        await message.answer("bizga qong'iroq qiling: @yourusername")

    elif message.text == "🎯 savol":
        await message.answer("Test uchun  maxsus tugmalar 👇", reply_markup=inline_kb)


@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "about":
        await callback.message.answer("Bu bot aiogram 3 yordamida tuzilgan.")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())