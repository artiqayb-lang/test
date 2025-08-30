import telebot
import random

TOKEN = "8413025019:AAGDICIXm_jpmTJ7tUuhoIRFnnq3okwiqfA"
bot = telebot.TeleBot(TOKEN)

qahramonlar = ["Ali", "Laylo", "Rustam", "Gulchehra", "Bahrom", "Malika", "Shahzoda", "Temur", "Oydin", "Kamron"]
joylar = ["sehrli o‘rmon", "oltin shahar", "sirli g‘or", "moviy dengiz bo‘yi", "tog‘ etagi", "keng dashtlar", "qorli cho‘qqilar", "cho‘l o‘rtasi"]
voqealar = [
    "yovuz ajdarhoga duch kelibdi",
    "yashirin xazinani topibdi",
    "qanotli otga minib osmonga uchibdi",
    "g‘ayritabiiy qudratga ega bo‘libdi",
    "do‘stlarini yovdan qutqaribdi",
    "sirli odam bilan uchrashibdi",
    "qudratli sehrgar bilan do‘stlashibdi",
    "oltin kalitni topibdi",
    "ko‘hna qal’aga kiribdi",
    "yulduzlar bilan suhbatlashibdi"
]
yakunlar = [
    "Shundan keyin mamlakat tinchlikka erishibdi.",
    "Yurtida qahramon sifatida tanilibdi.",
    "Hayoti abadiy baxtli kechibdi.",
    "Xalq uni doimo eslab yuribdi.",
    "Hamma unga minnatdor bo‘libdi."
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 👋 Men 400 qatorlik ertak yozuvchi botman.\n/ertak yozing va men sizga juda uzun ertak yozaman.")

@bot.message_handler(commands=['ertak'])
def ertak(message):
    ertak_qatorlari = []

    # Birinchi qator
    qahramon = random.choice(qahramonlar)
    joy = random.choice(joylar)
    ertak_qatorlari.append(f"Bir bor ekan, bir yo‘q ekan, {joy}da {qahramon} ismli qahramon yashagan ekan.")

    # 398 ta o‘rta qator
    for i in range(398):
        voqea = random.choice(voqealar)
        joy_vaqt = random.choice(joylar)
        qahramon_ism = random.choice(qahramonlar)
        ertak_qatorlari.append(f"{qahramon_ism} {joy_vaqt}da {voqea}.")

    # Yakun qatori
    ertak_qatorlari.append(random.choice(yakunlar))

    # Har 20 qatorni alohida yuborish
    for i in range(0, len(ertak_qatorlari), 20):
        bolak = "\n".join(ertak_qatorlari[i:i+20])
        bot.send_message(message.chat.id, bolak)

print("Bot ishga tushdi...")
bot.polling()


