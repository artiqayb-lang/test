from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import random
import urllib.parse

# Tokeningizni shu yerga qo'ying
TOKEN = "8387930832:AAF8Slcct6N23AT7JirNAa04lvryapR0fXc"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Ma'lumotlar ---
tips = [
    "🌟 Har kuni yangi narsani o‘rganing!",
    "💪 Sabr va mehnat bilan hamma narsaga erishish mumkin.",
    "📖 Kitob o‘qish aqlni boyitadi.",
    "🧘‍♂️ Dam olish va meditatsiya stressni kamaytiradi.",
    "🎯 Maqsadlaringizni yozing va ularga erishing!"
]

quiz = {
    "Python qaysi yilda yaratilgan?": {"options": ["1991", "1989", "2000", "1995"], "answer": "1991"},
    "Dunyodagi eng katta okean qaysi?": {"options": ["Tinch", "Atlantik", "Hind", "Shimoliy muz okeani"], "answer": "Tinch"}
}

songs = {
    "Shoxrux - Bolaligim": "https://yandex.ru/video/preview/6106334466461291107",
    "Yulduz Usmonova - Vatan": "https://yandex.ru/video/preview/2964766406575938747",
    "chorniy delfin": "https://yandex.ru/video/preview/17675422983046016258",

}

# Namuna kitob sarlavhalari (callback yordamida qidiruvga yo'naltiriladi)
sample_books = [
    "Pride and Prejudice",
    "Alice's Adventures in Wonderland",
    "Don Quixote",
    "War and Peace",
    "The Adventures of Sherlock Holmes",
    "Moby Dick",
    "Crime and Punishment"
]

awaiting_search = {}


def gutenberg_search_url(title: str) -> str:
    q = urllib.parse.quote(title)
    return f"https://www.gutenberg.org/ebooks/search/?query={q}"

def openlibrary_search_url(title: str) -> str:
    q = urllib.parse.quote(title)
    return f"https://openlibrary.org/search?q={q}"

def google_books_search_url(title: str) -> str:
    q = urllib.parse.quote(title)
    return f"https://www.google.com/search?tbm=bks&q={q}"

# --- /start va asosiy menyu ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📚 Kitoblar"), types.KeyboardButton(text="🎵 Musiqa")],
            [types.KeyboardButton(text="🎶 Qo‘shiqlar"), types.KeyboardButton(text="🎮 O'yinlar")],
            [types.KeyboardButton(text="⚙️ Sozlamalar"), types.KeyboardButton(text="📰 Yangiliklar")],
            [types.KeyboardButton(text="📖 O'quv resurslar"), types.KeyboardButton(text="🌐 Internet ilovalar")],
            [types.KeyboardButton(text="💡 Maslahatlar"), types.KeyboardButton(text="❓ Mini-Quiz")],
            [types.KeyboardButton(text="🔍 Google Qidiruv")]
        ],
        resize_keyboard=True
    )
    await message.answer("👋 Salom! Tugmani tanlang:", reply_markup=keyboard)

# --- Asosiy xabarlarni qayta ishlovchi handler ---
@dp.message()
async def handle_reply_buttons(message: types.Message):
    user_id = message.from_user.id
    text = (message.text or "").strip()

    # Agar foydalanuvchi kitob nomi yozish uchun chaqirilgan bo'lsa:
    if awaiting_search.get(user_id):
        title = text
        if not title:
            await message.answer("❌ Iltimos, kitob nomini yuboring (masalan: Pride and Prejudice).")
            return
        g_url = gutenberg_search_url(title)
        o_url = openlibrary_search_url(title)
        gb_url = google_books_search_url(title)
        kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="📚 Gutenberg'da qidirish", url=g_url)],
            [types.InlineKeyboardButton(text="📘 OpenLibrary'da qidirish", url=o_url)],
            [types.InlineKeyboardButton(text="🔎 Google Books qidiruvi", url=gb_url)]
        ])
        await message.answer(f"🔎 \"{title}\" uchun qidiruv natijalari:", reply_markup=kb)
        awaiting_search[user_id] = False
        return


    if text == "📚 Kitoblar":

        book_kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="📘 Project Gutenberg (public-domain)", url="https://www.gutenberg.org/")],
            [types.InlineKeyboardButton(text="📗 Open Library (Internet Archive)", url="https://openlibrary.org/")],
            [types.InlineKeyboardButton(text="📙 Google Books", url="https://books.google.com/")],
            [types.InlineKeyboardButton(text="📕 RoyalLib (online reader)", url="https://royallib.com/")],
            [types.InlineKeyboardButton(text="📒 LitRes (commercial)", url="https://www.litres.ru/")],
            # Pastga sample kitoblarni qidirish uchun tugma (callback)
            [types.InlineKeyboardButton(text="🔎 Kitob nomi bo'yicha qidirish", callback_data="book_search")],
            [types.InlineKeyboardButton(text="📚 Mashhur sarlavhalar (sample)", callback_data="book_samples")]
        ])
        await message.answer("📚 Onlayn kitoblar va qidiruv manbalari — birini tanlang:", reply_markup=book_kb)

    elif text == "🎵 Musiqa":
        await message.answer("🎵 Tavsiya: Imagine Dragons - Believer"
                             "tavsiya Tokyo Drift - Six Days lyrics Edit\n")
    elif text == "🎶 Qo‘shiqlar":
        song_kb = types.InlineKeyboardMarkup(
            inline_keyboard=[[types.InlineKeyboardButton(text=title, url=link)] for title, link in songs.items()]
        )
        await message.answer("🎶 Qo‘shiqlardan birini tanlang va tinglang:", reply_markup=song_kb)
    elif text == "🎮 O'yinlar":
        game_kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="🎲 Domino", url="https://yandex.ru/games/app/239966")],
            [types.InlineKeyboardButton(text="🧩 Puzzle", url="https://yandex.ru/games/app/336968")],
            [types.InlineKeyboardButton(text="⚔️ Duel", url="https://yandex.ru/games/app/192940")],
            [types.InlineKeyboardButton(text="🎮 Sunday", url="https://yandex.ru/games/app/123456")]
        ])
        await message.answer("🎮 O‘yinlardan birini tanlang:", reply_markup=game_kb)
    elif text == "⚙️ Sozlamalar":
        await message.answer("⚙️ Bu yerda bot sozlamalari (hozircha test).")
    elif text == "📰 Yangiliklar":
        await message.answer("📰 Bugungi yangilik: AI texnologiyalari tez rivojlanmoqda!")
    elif text == "📖 O'quv resurslar":
        await message.answer("📖 Tavsiya: Python darslari, Data Science kurslari (Coursera, Udemy).")
    elif text == "🌐 Internet ilovalar":
        web_kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="🔍 Google", url="https://www.google.com")],
            [types.InlineKeyboardButton(text="📺 YouTube", url="https://www.youtube.com")],
            [types.InlineKeyboardButton(text="📘 Wikipedia", url="https://www.wikipedia.org")],
            [types.InlineKeyboardButton(text="🛒 Amazon", url="https://www.amazon.com")]
        ])
        await message.answer("🌐 Internet ilovalar:", reply_markup=web_kb)
    elif text == "💡 Maslahatlar":
        tip = random.choice(tips)
        await message.answer(f"💡 Maslahat: {tip}")
    elif text == "❓ Mini-Quiz":
        question = random.choice(list(quiz.keys()))
        options = quiz[question]["options"]
        quiz_kb = types.InlineKeyboardMarkup(
            inline_keyboard=[[types.InlineKeyboardButton(text=opt, callback_data=f"quiz_{urllib.parse.quote(question)}_{opt}")]
                             for opt in options]
        )
        await message.answer(f"❓ Savol: {question}", reply_markup=quiz_kb)
    elif text == "🔍 Google Qidiruv":
        await message.answer("🔍 Qidiruv uchun matn yuboring. Masalan: Python darslari")
    elif text.startswith("🔍"):
        query = text.replace("🔍", "").strip()
        if query:
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            await message.answer(f"🔗 Google natijasi: {url}")
        else:
            await message.answer("❌ Qidiruv matni topilmadi!")
    else:
        await message.answer("Iltimos, menyudan birini tanlang!")


@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    data = callback_query.data or ""


    if data.startswith("quiz_"):

        parts = data.split("_", 2)
        if len(parts) == 3:
            question = urllib.parse.unquote(parts[1])
            option = parts[2]
            correct = quiz.get(question, {}).get("answer")
            if correct and option == correct:
                await callback_query.message.answer(f"✅ To‘g‘ri javob! {option}")
            else:
                await callback_query.message.answer(f"❌ Noto‘g‘ri. To‘g‘ri javob: {correct or 'N/A'}")
        return


    if data == "book_search":
        awaiting_search[callback_query.from_user.id] = True
        await callback_query.message.answer("🔎 Iltimos, qidiriladigan kitob nomini yozing (masalan: Pride and Prejudice).")
        return


    if data == "book_samples":
        ikb = []

        for title in sample_books:
            ikb.append([types.InlineKeyboardButton(text=title, callback_data=f"book_pick:{urllib.parse.quote(title)}")])
        kb = types.InlineKeyboardMarkup(inline_keyboard=ikb)
        await callback_query.message.answer("📚 Tanlang: (sample sarlavhalar)", reply_markup=kb)
        return


    if data.startswith("book_pick:"):
        title = urllib.parse.unquote(data.split(":", 1)[1])
        g_url = gutenberg_search_url(title)
        o_url = openlibrary_search_url(title)
        gb_url = google_books_search_url(title)
        kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="📚 Gutenberg'da qidirish", url=g_url),
             types.InlineKeyboardButton(text="📘 OpenLibrary'da qidirish", url=o_url)],
            [types.InlineKeyboardButton(text="🔎 Google Books qidiruvi", url=gb_url)]
        ])
        await callback_query.message.answer(f"\"{title}\" uchun havolalar:", reply_markup=kb)
        return

# --- Botni ishga tushirish ---
if __name__ == "__main__":
    print("mukammal")
    asyncio.run(dp.start_polling(bot))
