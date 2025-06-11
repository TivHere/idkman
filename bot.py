import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import Config
from handlers import BotHandlers

class BrowniesCafeBot:
    def __init__(self):
        """Initialize the bot with configuration and handlers"""
        self.logger = logging.getLogger(__name__)
        self.config = Config()
        
        if not self.config.BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is required")
        
        try:
            self.application = Application.builder().token(self.config.BOT_TOKEN).build()
            self.handlers = BotHandlers(self.config)
            self.logger.info("Bot initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize bot: {e}")
            raise

        self._setup_handlers()

    def _setup_handlers(self):
        try:
            self.application.add_handler(CommandHandler("start", self.handlers.start_command))
            self.application.add_handler(CommandHandler("menu", self.handlers.menu_command))
            self.application.add_handler(CommandHandler("location", self.handlers.location_command))
            self.application.add_handler(CommandHandler("hours", self.handlers.hours_command))
            self.application.add_handler(CommandHandler("help", self.handlers.help_command))

            self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handlers.handle_message))
            self.application.add_handler(CallbackQueryHandler(self.handlers.callback_query_handler))
            self.application.add_error_handler(self.handlers.error_handler)

            self.logger.info("All handlers registered successfully")

        except Exception as e:
            self.logger.error(f"Failed to setup handlers: {e}")
            raise

    def start(self):
        try:
            self.logger.info("Starting bot polling...")
            self.application.run_polling(
                poll_interval=1.0,
                timeout=10,
                drop_pending_updates=True
            )
        except Exception as e:
            self.logger.error(f"Error during bot operation: {e}")
            raise
        finally:
            self.logger.info("Bot stopped")

    async def stop(self):
        try:
            self.logger.info("Stopping bot...")
            await self.application.stop()
            self.logger.info("Bot stopped successfully")
        except Exception as e:
            self.logger.error(f"Error stopping bot: {e}")
