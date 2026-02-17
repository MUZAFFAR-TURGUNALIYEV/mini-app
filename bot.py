from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = "8348433221:AAFrQnL4E-WPs994pQe58VO7SoQ1QskJudY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            KeyboardButton(
                "🚀 Mini App ochish",
                web_app=WebAppInfo(
                    url="https://yourproject.vercel.app"
                )
            )
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Mini App ni ochish:",
        reply_markup=reply_markup
    )


async def handle_webapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.web_app_data:
        data = update.message.web_app_data.data
        await update.message.reply_text(f"Kelgan data:\n{data}")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
