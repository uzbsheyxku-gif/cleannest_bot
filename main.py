from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

TOKEN = "8967778406:AAFEscinvyQikkchuTGSQuwWZe1jxcTYqY4"

keyboard = [
    ["🧼 Gilam yuvish"],
    ["🚘 Moshina yuvish"],
    ["📞 Aloqa"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "CleanUZ botiga xush kelibsiz!",
        reply_markup=reply_markup
    )

def message_handler(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "🧼 Gilam yuvish":
        update.message.reply_text(
            "Gilam yuvish narxi: 25 000 so'm"
        )

    elif text == "🚘 Moshina yuvish":
        update.message.reply_text(
            "Moshina yuvish narxi: 80 000 so'm"
        )

    elif text == "📞 Aloqa":
        update.message.reply_text(
            "Telefon: +998 77 455 28 29"
        )

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()