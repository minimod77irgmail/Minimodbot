from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"   # ← اینجا توکن رباتت رو بذار

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌷 سلام!\n\n"
        "به ربات رسمی مینی مد خوش آمدید.\n\n"
        "ربات با موفقیت راه‌اندازی شد. 🎉"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("MiniModBot is running...")
    app.run_polling()

if name == "main":
    main()
