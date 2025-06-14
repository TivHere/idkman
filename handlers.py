from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [[InlineKeyboardButton("📋 Menu", callback_data='menu'),
                     InlineKeyboardButton("📍 Location", callback_data='location'),
                     InlineKeyboardButton("🕘 Hours", callback_data='hours')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Welcome to Brownies Café!", reply_markup=reply_markup)

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_menu_text())

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_location_text())

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_hours_text())

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Please use the buttons or type /start")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        data = query.data

        keyboard_back = [[InlineKeyboardButton("⬅ Back", callback_data="start")]]
        reply_markup = InlineKeyboardMarkup(keyboard_back)

        if data == "menu":
            await query.edit_message_text(self.config.get_menu_text(), reply_markup=reply_markup)
        elif data == "location":
            await query.edit_message_text(self.config.get_location_text(), reply_markup=reply_markup)
        elif data == "hours":
            await query.edit_message_text(self.config.get_hours_text(), reply_markup=reply_markup)
        elif data == "start":
            keyboard = [[InlineKeyboardButton("📋 Menu", callback_data='menu'),
                         InlineKeyboardButton("📍 Location", callback_data='location'),
                         InlineKeyboardButton("🕘 Hours", callback_data='hours')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text("Welcome to Brownies Café!", reply_markup=reply_markup)

    async def error_handler(self, update, context):
        print(f"Update {update} caused error {context.error}")