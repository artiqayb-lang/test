import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    ReplyKeyboardMarkup, KeyboardButton
)

TOKEN = "8413025019:AAGDICIXm_jpmTJ7tUuhoIRFnnq3okwiqfA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Oddiy reply tugmalar
reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yangiliklar"), KeyboardButton(text="Ma'lumot")],
        [KeyboardButton(text="Aloqa")],
    ],
    resize_keyboard=True
)

# Inline tugmalar
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="GitHub", url="https://github.com/")],
        [InlineKeyboardButton(text="Zo'r TV futbol", url="https://t.me/zor_tv_jonli_efir_zortv0")],
        [InlineKeyboardButton(text="BOT FATHER", url="https://t.me/BotFather")],  # URL bo'lishi kerak!
    ]
)

malumot_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ozim haqimda", url="https://dynamic-crepe-64c2fa.netlify.app/")]
    ]
)

# /start buyrug'i
@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum!\nTugmalardan birini tanlang:", reply_markup=reply_kb)

# Yangiliklar tugmasi
@dp.message(F.text == "Yangiliklar")
async def yangiliklar_handler(message: types.Message):
    await message.answer("Ozim haqimda:", reply_markup=malumot_kb)

# Ma'lumot tugmasi
@dp.message(F.text == "Ma'lumot")
async def malumot_handler(message: types.Message):
    await message.answer("Bu bot oddiy tugmalarni ishlatadi", reply_markup=inline_kb)

# Aloqa tugmasi
@dp.message(F.text == "Aloqa")
async def aloqa_handler(message: types.Message):
    await message.answer("📞 99-896-18-16")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

