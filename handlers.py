from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import ContextTypes
from config import Config

class BotHandlers:
    def __init__(self, config: Config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        image_url = "https://i.ibb.co/Jrc9G7y/cafe-banner.jpg"  # Replace with your actual hosted image URL
        keyboard = [
            [InlineKeyboardButton("📋 Menu", callback_data="menu")],
            [InlineKeyboardButton("📍 Location", callback_data="location")],
            [InlineKeyboardButton("🕘 Hours", callback_data="hours")]
        ]

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_url,
            caption=self.config.FIRST_TIME_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Type /menu, /location, or /hours to get information.")

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_menu_text(), parse_mode="Markdown")

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_location_text(), parse_mode="Markdown")

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_hours_text(), parse_mode="Markdown")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.message.text.lower()
        if "menu" in message:
            await update.message.reply_text(self.config.get_menu_text(), parse_mode="Markdown")
        elif "location" in message:
            await update.message.reply_text(self.config.get_location_text(), parse_mode="Markdown")
        elif "hour" in message or "time" in message:
            await update.message.reply_text(self.config.get_hours_text(), parse_mode="Markdown")
        else:
            await update.message.reply_text("Sorry, I didn't understand that. Try /menu or /help.")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "menu":
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
            await query.edit_message_text(
                text=self.config.get_menu_text(),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        elif query.data == "location":
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
            await query.edit_message_text(
                text=self.config.get_location_text(),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        elif query.data == "hours":
            keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
            await query.edit_message_text(
                text=self.config.get_hours_text(),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        elif query.data == "back":
            keyboard = [
                [InlineKeyboardButton("📋 Menu", callback_data="menu")],
                [InlineKeyboardButton("📍 Location", callback_data="location")],
                [InlineKeyboardButton("🕘 Hours", callback_data="hours")]
            ]
            await query.edit_message_text(
                text=self.config.FIRST_TIME_MESSAGE,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        print(f"Error: {context.error}")
