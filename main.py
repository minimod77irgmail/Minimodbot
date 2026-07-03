from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "توکن_ربات_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌷 سلام، به MiniMod خوش آمدید.\n\n"
        "ربات در حال راه‌اندازی است و به‌زودی امکانات کامل فعال می‌شود."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
