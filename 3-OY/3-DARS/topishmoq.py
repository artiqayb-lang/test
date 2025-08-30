import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random

TOKEN = "8093886216:AAFULEMslAbsTWoOjc-tIWK3cM6nrJ3da3I"  # BotFather'dan olgan tokeningiz

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Topishmoqlar (savol, javob)
topishmoqlar = [
    ("O‘zi qora, suvi oq, nima bu?", "Choy"),
    ("Oyoqlari bor, lekin yura olmaydi, nima bu?", "Stul"),
    ("Uchadi, ammo qanoti yo‘q, nima bu?", "Vaqt"),
    ("O‘zi kichkina, lekin ovozi katta, nima bu?", "Chumchuq"),
    ("Ko‘p teshigi bor, ammo suvni ushlay olmaydi, nima bu?", "G‘ovak (shimgich)")
]

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! Men Topishmoq botiman.\n/topishmoq buyrug‘ini yuboring.")

@dp.message(Command("topishmoq"))
async def topishmoq_handler(message: types.Message):
    savol, javob = random.choice(topishmoqlar)
    await message.answer(f"Topishmoq: {savol}")
    await asyncio.sleep(10)  # 10 soniyadan keyin javobni aytadi
    await message.answer(f"Javobi: {javob}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())