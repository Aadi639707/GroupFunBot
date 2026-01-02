import telebot
from telebot import types
import random

# Aapka sahi wala token yahan hai
API_TOKEN = '8273081654:AAFyU5699_7S-LzSRE4pI6kYI9F6Y96G8U' 
bot = telebot.TeleBot(API_TOKEN)

# Chatbot status control
chatbot_active = {}

# 1. Start Command & Welcome Message
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    help_btn = types.InlineKeyboardButton("Help ❓", callback_data="help")
    support_btn = types.InlineKeyboardButton("Support 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(help_btn, support_btn)
    
    welcome_text = "👋 *Swagat hai!* \n\nMain aapke group ko active rakhne wala bot hoon.\n\nNiche diye buttons use karein 👇"
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. Couple Generator (/couple)
@bot.message_handler(commands=['couple'])
def couple(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Ye command sirf group mein chalti hai! 😅")
        return
    
    bot.send_message(message.chat.id, "🔍 *Searching for today's perfect match...*")
    # Yahan random jodi ka msg jayega
    bot.send_message(message.chat.id, "🎉 Aaj ki special jodi:\n\n👤 Member 1 + 👤 Member 2\n\n❤️ *Rab ne bana di jodi!*")

# 3. Chatbot Toggle (/chatbot on/off)
@bot.message_handler(commands=['chatbot'])
def toggle_chat(message):
    chat_id = message.chat.id
    if "on" in message.text.lower():
        chatbot_active[chat_id] = True
        bot.reply_to(message, "✅ Chatbot ON! Ab main baatein karunga.")
    elif "off" in message.text.lower():
        chatbot_active[chat_id] = False
        bot.reply_to(message, "❌ Chatbot OFF ho gaya.")
    else:
        bot.reply_to(message, "Sahi tarika: /chatbot on ya /chatbot off", parse_mode='Markdown')

# 4. Help Button Action
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_callback(call):
    help_text = "📜 *Bot Commands:*\n\n/couple - Perfect match dhunde\n/chatbot - AI chat on/off karein\n/start - Menu ke liye"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, help_text, parse_mode='Markdown')

# AI Chat Response (Jab ON ho)
@bot.message_handler(func=lambda m: True)
def chat_reply(message):
    if chatbot_active.get(message.chat.id, False) and not message.text.startswith('/'):
        replies = ["Hnji, kaise ho?", "Aur batao kya chal raha hai?", "Main toh bot hoon, par maze poore leta hoon!"]
        bot.reply_to(message, random.choice(replies))

bot.infinity_polling()
