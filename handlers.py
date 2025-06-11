from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes
from config import Config

class BotHandlers:
    def __init__(self, config: Config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message with buttons and image"""
        chat_id = update.effective_chat.id

        buttons = [
            [InlineKeyboardButton("📋 Menu", callback_data='menu')],
            [InlineKeyboardButton("📍 Location", callback_data='location')],
            [InlineKeyboardButton("🕘 Hours", callback_data='hours')],
            [InlineKeyboardButton("❓ Help", callback_data='help')]
        ]

        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://i.imgur.com/y2jVZB3.jpeg",  # Replace with your own café image URL
            caption=self.config.FIRST_TIME_MESSAGE,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.WELCOME_MESSAGE)

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_menu_text())

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_location_text())

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_hours_text())

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text.lower()
        if "menu" in user_message:
            await self.menu_command(update, context)
        elif "location" in user_message:
            await self.location_command(update, context)
        elif "hours" in user_message or "time" in user_message:
            await self.hours_command(update, context)
        elif "help" in user_message:
            await self.help_command(update, context)
        else:
            await update.message.reply_text("I'm not sure how to respond to that. Try using the buttons or type /help.")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        data = query.data
        await query.answer()

        if data == "menu":
            text = self.config.get_menu_text()
        elif data == "location":
            text = self.config.get_location_text()
        elif data == "hours":
            text = self.config.get_hours_text()
        elif data == "help":
            text = self.config.WELCOME_MESSAGE
        elif data == "main":
            return await self.start_command(update, context)
        else:
            text = "Unknown selection"

        buttons = [
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='main')]
        ]

        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        print(f"Error occurred: {context.error}")
