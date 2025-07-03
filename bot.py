# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import config, replies, ai_reply, utils

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 I'm an auto-reply bot. Send me a message!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message
    text = message.text.strip()

    # Log the message
    utils.log_message(user.id, user.username or user.full_name, text)

    # Try smart reply first
    reply = replies.get_smart_reply(text)
    
    if not reply and config.USE_GPT:
        # Fallback to AI
        reply = ai_reply.get_ai_reply(text)

    # Simulate typing + reply
    utils.simulate_typing_and_reply(message, reply)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Unknown command. Try sending a message instead!")

def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
