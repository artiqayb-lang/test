import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from deep_translator import GoogleTranslator

BOT_TOKEN="8093886216:AAFULEMslAbsTWoOjc-tIWK3cM6nrJ3da3I"

bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_heandlar(massage:types.Message):
    return massage.answer("bu telegram bot translate qilib beradi\n"
                          "Ingiliz tilida biror soz yozish\n"
                          "O'zbek tiliga tarjimasini korish mumkun😁")





dp.message()
async def translate(message: types.Message):
    text = message.text
    try:
        translator = GoogleTranslator(sourse='en',
                                      target='uz').translate(text)
        await message.answer(f"Translated: {translator}")
    except Exception as e:
        await message.answer("Tarjima qilib bolmadi")


async def main():
    print("tarjima bot ishlayabti")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())











