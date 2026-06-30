import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "سلام":
        await update.message.reply_text("سلام 😊")

    elif text == "خوبی":
        await update.message.reply_text("مرسی، خوبم ❤️")

    else:
        await update.message.reply_text("متوجه نشدم.")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot Started...")

app.run_polling()