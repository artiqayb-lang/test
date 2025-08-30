import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN="8282106892:AAEbAhDzjOSX65QLnLcjIfTUWZcz16O5jtw"

bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_heandlar(massage:types.Message):
    await massage.answer(f"Salom {massage.from_user.first_name} 💵💸")

@dp.message()
async def salom_handler(message: types.Message):
    if message.text.lower() in ['salom','hi','hello']:
        await message.answer("Asalomu aleykum")
    elif message.txt.lower() in ['bye',"i'm off"]:
        await message.answer("hayr korishkuncha")
    else:
        await message.answer("Men faqat salom deyishni bilaman")


async def main():
    print("Bot ishga tushdi...........")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


