import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = ("8766754955:AAE5TsP7tYzM68kfpJYBkuGhnYoeZH0ET64")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "درود":
        await update.message.reply_text("درود👋")

    elif text == "خوبی":
        await update.message.reply_text("مرسی، خوبم 🙏")

    elif text == "مارال":
        await update.message.reply_text("بهترینه💖")

    elif text == "زیبا ترین دختر جهان کیه؟":
        await update.message.reply_text("ماراله😍")

    elif text == "مارال چقدر قشنگه؟":
        await update.message.reply_text("اندازه تمام ستاره های جهان✨")

    else:
        await update.message.reply_text("میخواستی بگی مارال چقدر قشنگه؟")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot Started...")

app.run_polling()
