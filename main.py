import telebot
from telebot import types
import random

# Naya token revoke karke yahan dalein
API_TOKEN = '8273081654:AAFyU56FG3PV5ohPMVk5EOqQuCKjnUO-DWc'
bot = telebot.TeleBot(API_TOKEN)

chatbot_active = {}

# 1. Start Command with English Interface
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_help = types.InlineKeyboardButton("Explore Commands 📜", callback_data="help")
    btn_support = types.InlineKeyboardButton("Support / Owner 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(btn_help, btn_support)
    
    welcome_text = (
        "✨ *WELCOME TO THE PREMIUM GROUP ASSISTANT* ✨\n\n"
        "Greetings! I am your advanced group companion. 🚀\n\n"
        "Please use the buttons below to explore my commands!"
    )
    # bot.reply_to keyboard ke upar tag (reply) karta hai
    bot.reply_to(message, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. Couple Command (Group Only)
@bot.message_handler(commands=['couple'])
def find_couple(message):
    if message.chat.type == "private":
        bot.reply_to(message, "❌ This command is only for Groups!")
        return
    
    bot.reply_to(message, "🔍 *Searching for today's perfect match...*")
    # Yahan logic add hoga, filhaal testing ke liye:
    bot.send_message(message.chat.id, "🎉 *Today's Couple:* \n\n👤 Member A + 👤 Member B \n\n❤️ *Match made in heaven!*")

# 3. Chatbot Toggle
@bot.message_handler(commands=['chatbot'])
def toggle_chat(message):
    chat_id = message.chat.id
    if "on" in message.text.lower():
        chatbot_active[chat_id] = True
        bot.reply_to(message, "✅ AI Chatbot is now ENABLED.")
    elif "off" in message.text.lower():
        chatbot_active[chat_id] = False
        bot.reply_to(message, "❌ AI Chatbot is now DISABLED.")

# 4. Handle Help Button
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_info(call):
    help_text = (
        "📖 *COMMAND DIRECTORY*\n\n"
        "👉 /couple - Pick a random couple.\n"
        "👉 /chatbot on/off - Toggle AI chat.\n"
        "👉 /id - Get your ID."
    )
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                          text=help_text, parse_mode='Markdown')

bot.infinity_polling()
