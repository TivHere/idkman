from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        buttons = [
            [InlineKeyboardButton("📋 Menu", callback_data="menu")],
            [InlineKeyboardButton("📍 Location", callback_data="location")],
            [InlineKeyboardButton("🕘 Hours", callback_data="hours")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        chat_id = update.effective_chat.id
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=self.config.MAIN_PHOTO_URL,
            caption="🍫 Welcome to Brownies Café!
Tap below to begin:",
            reply_markup=reply_markup
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.start_command(update, context)

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        data = query.data
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅ Back", callback_data="start")]]
        )

        if data == "menu":
            await query.edit_message_text(
                text=self.config.get_menu_text(),
                reply_markup=back_button,
                parse_mode="Markdown"
            )
        elif data == "location":
            await query.edit_message_text(
                text=self.config.get_location_text(),
                reply_markup=back_button,
                parse_mode="Markdown"
            )
        elif data == "hours":
            await query.edit_message_text(
                text=self.config.get_hours_text(),
                reply_markup=back_button,
                parse_mode="Markdown"
            )
        elif data == "start":
            await self.start_command(update, context)

    async def error_handler(self, update, context):
        print(f"Error: {context.error}")