import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def main_menu(self):
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("📋 View Menu", callback_data="menu")],
            [InlineKeyboardButton("📍 Location", callback_data="location")],
            [InlineKeyboardButton("🕘 Hours", callback_data="hours")]
        ])

    def back_button(self):
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="start")]
        ])

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=self.config.MAIN_PHOTO_URL,
            caption="🍫 Welcome to Brownies Café!\nTap a button below:",
            reply_markup=self.main_menu()
        )

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_menu_text(), parse_mode='Markdown')

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_location_text(), parse_mode='Markdown')

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_hours_text(), parse_mode='Markdown')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.WELCOME_MESSAGE)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.start_command(update, context)

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "menu":
            await query.edit_message_text(self.config.get_menu_text(), parse_mode='Markdown', reply_markup=self.back_button())
        elif query.data == "location":
            await query.edit_message_text(self.config.get_location_text(), parse_mode='Markdown', reply_markup=self.back_button())
        elif query.data == "hours":
            await query.edit_message_text(self.config.get_hours_text(), parse_mode='Markdown', reply_markup=self.back_button())
        elif query.data == "start":
            await self.start_command(update, context)

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        self.logger.error(msg="Exception while handling an update:", exc_info=context.error)
