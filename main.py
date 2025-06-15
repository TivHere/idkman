import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
APP_URL = os.environ.get("APP_URL")

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📋 Menu", "📍 Location", "🕒 Hours")
    bot.send_photo(
        message.chat.id,
        photo="https://i.imgur.com/MpPC69Z.jpeg",  # Replace with your image
        caption="Welcome to Brownies Café! 🍫\nWhat would you like to check?",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📋 Menu":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Back")
        bot.send_message(message.chat.id, "Here's our menu:\n- Brownie RM4\n- Ice Latte RM6", reply_markup=markup)
    elif message.text == "📍 Location":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Back")
        bot.send_message(message.chat.id, "We are located at: 123 Brownie Street 🍫", reply_markup=markup)
    elif message.text == "🕒 Hours":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("⬅️ Back")
        bot.send_message(message.chat.id, "Open daily: 10am - 8pm 🕗", reply_markup=markup)
    elif message.text == "⬅️ Back":
        send_welcome(message)
    else:
        bot.send_message(message.chat.id, "Please use the menu buttons 😊")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"{APP_URL}/{TOKEN}")
    return 'Webhook set ✅', 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
