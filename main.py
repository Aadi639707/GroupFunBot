import telebot
from telebot import types

# Apna Bot Token yahan dalein
API_TOKEN = 'YAHAN_APNA_TOKEN_DALEIN'
bot = telebot.TeleBot(API_TOKEN)

# Welcome Message with Support & Help Button
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    help_btn = types.InlineKeyboardButton("Help ❓", callback_data="help")
    support_btn = types.InlineKeyboardButton("Support 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(help_btn, support_btn)
    
    bot.send_message(message.chat.id, "Welcome! Group me mja krne ke liye me taiyar hu.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_msg(call):
    bot.send_message(call.message.chat.id, "Commands:\n/couple - Random Couple\n/chatbot on/off - AI Chat")

bot.infinity_polling()
