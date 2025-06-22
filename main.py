import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import Config
from handlers import BotHandlers

logging.basicConfig(level=logging.INFO)
config = Config()
bot_app = Application.builder().token(config.BOT_TOKEN).build()
handlers = BotHandlers(config)

bot_app.add_handler(CommandHandler("start", handlers.start_command))
bot_app.add_handler(CallbackQueryHandler(handlers.callback_query_handler))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))
bot_app.add_error_handler(handlers.error_handler)

if __name__ == "__main__":
    logging.info("✅ Bot is starting...")
    bot_app.run_polling()
