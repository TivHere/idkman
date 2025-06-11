from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=self.config.START_IMAGE_URL,
            caption=self.config.WELCOME_MESSAGE
        )

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [[InlineKeyboardButton("⬅ Back to Start", callback_data="start")]]
        await update.message.reply_text(
            self.config.get_menu_text(),
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [[InlineKeyboardButton("⬅ Back to Start", callback_data="start")]]
        await update.message.reply_text(
            self.config.get_location_text(),
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [[InlineKeyboardButton("⬅ Back to Start", callback_data="start")]]
        await update.message.reply_text(
            self.config.get_hours_text(),
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Type /menu, /location, or /hours to get started!")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("I'm not sure what you meant. Try /menu or /help!")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "start":
            await self.start_command(update, context)

    async def error_handler(self, update, context):
        print(f"Error: {context.error}")
