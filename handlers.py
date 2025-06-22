
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class BotHandlers:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            self.config.FIRST_TIME_MESSAGE,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("View Menu 🍽️", callback_data="menu")],
                [InlineKeyboardButton("Opening Hours 🕘", callback_data="hours")],
                [InlineKeyboardButton("Location 📍", callback_data="location")]
            ])
        )

    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            self.config.get_menu_text(),
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    async def location_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            self.config.get_location_text(),
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    async def hours_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            self.config.get_hours_text(),
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(self.config.WELCOME_MESSAGE)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.message.text.lower()
        if "menu" in message:
            await self.menu_command(update, context)
        elif "location" in message or "where" in message:
            await self.location_command(update, context)
        elif "hours" in message or "open" in message:
            await self.hours_command(update, context)
        else:
            await update.message.reply_text("I'm not sure how to help with that. Type /help to see what I can do!")

    async def callback_query_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        if query.data == "menu":
            await query.edit_message_text(
                self.config.get_menu_text(), parse_mode='Markdown',
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back")]])
            )
        elif query.data == "location":
            await query.edit_message_text(
                self.config.get_location_text(), parse_mode='Markdown',
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back")]])
            )
        elif query.data == "hours":
            await query.edit_message_text(
                self.config.get_hours_text(), parse_mode='Markdown',
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back")]])
            )
        elif query.data == "back":
            await self.start_command(update, context)

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        self.logger.error(msg="Exception while handling an update:", exc_info=context.error)
