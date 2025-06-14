import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [
                InlineKeyboardButton("📋 Menu", callback_data="menu"),
                InlineKeyboardButton("📍 Location", callback_data="location")
            ],
            [
                InlineKeyboardButton("🕘 Hours", callback_data="hours"),
                InlineKeyboardButton("❓ Help", callback_data="help")
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(
            photo="https://i.ibb.co/1McM6hZ/brownies-cafe.jpg",
            caption=self.config.FIRST_TIME_MESSAGE,
            reply_markup=reply_markup
        )

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_menu_text(), parse_mode="Markdown")

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_location_text(), parse_mode="Markdown")

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.get_hours_text(), parse_mode="Markdown")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.WELCOME_MESSAGE, parse_mode="Markdown")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.lower()

        if "menu" in text:
            await self.menu_command(update, context)
        elif "location" in text or "where" in text:
            await self.location_command(update, context)
        elif "hour" in text or "time" in text:
            await self.hours_command(update, context)
        else:
            await update.message.reply_text(self.config.WELCOME_MESSAGE, parse_mode="Markdown")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "menu":
            await query.edit_message_text(self.config.get_menu_text(), parse_mode="Markdown",
                                           reply_markup=self.get_back_button())
        elif query.data == "location":
            await query.edit_message_text(self.config.get_location_text(), parse_mode="Markdown",
                                           reply_markup=self.get_back_button())
        elif query.data == "hours":
            await query.edit_message_text(self.config.get_hours_text(), parse_mode="Markdown",
                                           reply_markup=self.get_back_button())
        elif query.data == "help":
            await query.edit_message_text(self.config.WELCOME_MESSAGE, parse_mode="Markdown",
                                           reply_markup=self.get_back_button())
        elif query.data == "back_to_main":
            await query.edit_message_caption(
                caption=self.config.FIRST_TIME_MESSAGE,
                reply_markup=self.get_main_menu_buttons()
            )

    def get_main_menu_buttons(self):
        keyboard = [
            [
                InlineKeyboardButton("📋 Menu", callback_data="menu"),
                InlineKeyboardButton("📍 Location", callback_data="location")
            ],
            [
                InlineKeyboardButton("🕘 Hours", callback_data="hours"),
                InlineKeyboardButton("❓ Help", callback_data="help")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    def get_back_button(self):
        keyboard = [[InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")]]
        return InlineKeyboardMarkup(keyboard)

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logging.error(msg="Exception while handling an update:", exc_info=context.error)
