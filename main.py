from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "Here is the token for bot cleannest_uz_bot @cleannestuzbot:

8967778406:AAFEscinvyQikkchuTGSQuwWZe1jxcTYqY4"

keyboard = [
    ["🧼 Gilam yuvish"],
    ["🚘 Moshina yuvish"],
    ["📞 Aloqa"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "CleanUZ botiga xush kelibsiz!",
        reply_markup=reply_markup
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🧼 Gilam yuvish":
        await update.message.reply_text(
            "Gilam yuvish narxi: 25 000 so'm"
        )

    elif text == "🚘 Moshina yuvish":
        await update.message.reply_text(
            "Moshina yuvish narxi: 80 000 so'm"
        )

    elif text == "📞 Aloqa":
        await update.message.reply_text(
            "Telefon: +998 77 455 28 29"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(filters.TEXT, message_handler)
    )

    print("Bot ishladi...")
    app.run_polling()

if __name__ == "__main__":
    main()