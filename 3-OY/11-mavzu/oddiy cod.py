from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio


TOKEN = "8387930832:AAF8Slcct6N23AT7JirNAa04lvryapR0fXc"

bot = Bot(token=TOKEN)
dp = Dispatcher()


trucks = {
    "daf_xf105": "🚛 DAF XF 105 — Uzoq masofaga mo‘ljallangan yuk mashinasi. Quvvatli va qulay kabinaga ega.",
    "volvo_fh16": "🚚 Volvo FH16 — 16 litrli kuchli motor, og‘ir yuklarni tashishga mo‘ljallangan.",
    "scania_r500": "🚛 Scania R500 — Yoqilg‘i tejamkorligi va chidamliligi bilan mashhur.",
    "man_tgx": "🚚 MAN TGX — Evropa bozorida mashhur, qulay kabina va kuchli motor.",
    "mercedes_actros": "🚛 Mercedes-Benz Actros — Zamonaviy texnologiyalar bilan jihozlangan yuk mashinasi.",
    "iveco_stralis": "🚚 Iveco Stralis — Og‘ir transport uchun ishlab chiqarilgan, mustahkamligi bilan mashhur.",
    "renault_t": "🚛 Renault T — Qulaylik va samaradorlik uchun yaratilgan, uzoq safarlar uchun mos.",
    "kamaz_5490": "🚚 KAMAZ 5490 — Rossiyada ishlab chiqarilgan, iqtisodiy va ishonchli yuk mashinasi.",
    "maz_5440": "🚛 MAZ 5440 — Belarusda ishlab chiqarilgan, og‘ir yuk tashishga mos.",
    "hino_700": "🚚 Hino 700 — Yaponiya yuk mashinasi, sifatli va uzoq muddatli xizmat uchun."
}



@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    # Inline keyboard
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="👋 Salom ayt", callback_data="say_hello")],
        [types.InlineKeyboardButton(text="ℹ️ Ismimni ayt", callback_data="say_name")],
        [types.InlineKeyboardButton(text="🚛 Yuk mashinalari", callback_data="show_trucks")]
    ])

    await message.answer("Salom! Quyidagi tugmalardan birini tanlang 👇", reply_markup=keyboard)



@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "say_hello":
        await callback.message.answer("Assalomu alaykum! 😊")

    elif callback.data == "say_name":
        await callback.message.answer(f"Sizning ismingiz: {callback.from_user.full_name}")

    elif callback.data == "show_trucks":

        truck_keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text=name.replace("_", " ").upper(), callback_data=key)]
                for key, name in zip(trucks.keys(), trucks.keys())
            ]
        )
        await callback.message.answer("🚛 Yuk mashinasini tanlang:", reply_markup=truck_keyboard)

    elif callback.data in trucks:

        await callback.message.answer(trucks[callback.data])

    await callback.answer()


async def main():
    print("bot ishlaydi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
