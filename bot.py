import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import Config
from handlers import BotHandlers

class BrowniesCafeBot:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = Config()

        if not self.config.BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is required")

        self.application = Application.builder().token(self.config.BOT_TOKEN).build()
        self.handlers = BotHandlers(self.config)
        self._setup_handlers()

    def _setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.handlers.start_command))
        self.application.add_handler(CommandHandler("menu", self.handlers.menu_command))
        self.application.add_handler(CommandHandler("location", self.handlers.location_command))
        self.application.add_handler(CommandHandler("hours", self.handlers.hours_command))
        self.application.add_handler(CommandHandler("help", self.handlers.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handlers.handle_message))
        self.application.add_handler(CallbackQueryHandler(self.handlers.callback_query_handler))
        self.application.add_error_handler(self.handlers.error_handler)

    def start(self):
        self.logger.info("Bot is running...")
        self.application.run_polling()

    async def stop(self):
        await self.application.stop()
