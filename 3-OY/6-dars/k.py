import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 🔑 BotFather bergan tokenni shu yerga yozing
TOKEN = "8429957777:AAHgCi8bvjLTNRCktdYXrIz8sd9YKTZwVCw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Bankomat ma'lumotlari ---
PIN = "9999"
user_data = {}  # foydalanuvchilar ma'lumotlari

# /start komandasi
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"balans": 1_000_000_000_000_000_000_000_000, "auth": False}
    await message.answer("🏧 Bankomat botiga xush kelibsiz!\n\nIltimos, PIN kodni kiriting :")

# PIN tekshirish
@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    # Agar foydalanuvchi hali PIN kiritmagan bo‘lsa
    if user_id not in user_data:
        await message.answer("⚠️ Avval /start buyrug‘ini yuboring.")
        return

    # Avval PIN tekshirish
    if not user_data[user_id]["auth"]:
        if text == PIN:
            user_data[user_id]["auth"] = True
            await message.answer(
                "✅ PIN to‘g‘ri!\n\nMenyu:\n1️⃣ Balansni ko‘rish\n2️⃣ Pul yechish\n3️⃣ Pul qo‘yish\n4️⃣ Chiqish"
            )
        else:
            await message.answer("❌ Noto‘g‘ri PIN. Qaytadan urinib ko‘ring.")
        return

    # Agar foydalanuvchi avtorizatsiya qilingan bo‘lsa
    balans = user_data[user_id]["balans"]

    if text == "1":
        await message.answer(f"💰 Sizning balansingiz: {balans} mlrd")

    elif text == "2":
        await message.answer("❓ Qancha summa yechmoqchisiz?")
        user_data[user_id]["state"] = "withdraw"

    elif text == "3":
        await message.answer("❓ Qancha summa qo‘ymoqchisiz?")
        user_data[user_id]["state"] = "deposit"

    elif text == "4":
        user_data[user_id]["auth"] = False
        await message.answer("✅ Chiqdingiz. Xizmatimizdan foydalanganingiz uchun rahmat!")

    else:
        # Agar foydalanuvchi summani kiritayotgan bo‘lsa
        if "state" in user_data[user_id] and user_data[user_id]["state"] is not None:
            state = user_data[user_id]["state"]
            try:
                summa = int(text)
            except:
                await message.answer("❌ Iltimos, faqat raqam kiriting.")
                return

            if state == "withdraw":
                if summa <= balans:
                    user_data[user_id]["balans"] -= summa
                    await message.answer(f"✅ {summa} so‘m yechildi.\nQolgan balans: {user_data[user_id]['balans']} so‘m")
                else:
                    await message.answer("❌ Balansingiz yetarli emas.")

            elif state == "deposit":
                user_data[user_id]["balans"] += summa
                await message.answer(f"✅ {summa} so‘m qo‘shildi.\nYangi balans: {user_data[user_id]['balans']} so‘m")

            user_data[user_id]["state"] = None
        else:
            await message.answer("⚠️ Menyudan 1-4 orasidagi tanlovni kiriting.")

# --- Botni ishga tushirish ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
