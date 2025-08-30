import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import datetime
BOT_TOKEN="8282106892:AAEbAhDzjOSX65QLnLcjIfTUWZcz16O5jtw"

bot =Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_heandlar(massage:types.Message):
    await massage.answer(f"Salom {massage.from_user.first_name} 💵💸")

@dp. message()
async  def data(message: types.Message):
    now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    await message.answer(f"Bugungi sana va vaqt {now}")




async def main():
    print("Bot ishga tushdi...........")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


