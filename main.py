import telebot
from telebot import types
import random

# Your Verified Token
API_TOKEN = '8273081654:AAFyU56FG3PV5ohPMVk5EOqQuCKjnUO-DWc'
bot = telebot.TeleBot(API_TOKEN)

chatbot_active = {}

# 1. Premium English Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_help = types.InlineKeyboardButton("Command Directory 📜", callback_data="help")
    btn_support = types.InlineKeyboardButton("Support / Owner 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(btn_help, btn_support)
    
    welcome_text = (
        "✨ *WELCOME TO THE ULTIMATE GROUP COMPANION* ✨\n\n"
        "Greetings! I am your premium-tier group assistant. I am here to make your "
        "community active, engaged, and highly entertained. 🚀\n\n"
        "🌟 *What I Can Do For You:*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "❤️ *Social:* Find your daily match with /couple.\n"
        "🎮 *Fun:* Get exciting tasks with /dare and /dice.\n"
        "🤖 *Smart AI:* I can chat with users when enabled.\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Click the Command Directory button below to explore all features!"
    )
    # Tags the user's message as a reply (Just like your screenshot)
    bot.reply_to(message, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. Advanced Help Menu
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_info(call):
    help_text = (
        "📖 *OFFICIAL COMMAND DIRECTORY*\n\n"
        "👉 /couple - Tag a random couple in the group.\n"
        "👉 /dare - Receive a random fun challenge.\n"
        "👉 /dice - Roll a dice and test your luck.\n"
        "👉 /chatbot on/off - Toggle the smart reply module.\n"
        "👉 /id - View your unique Telegram User ID.\n\n"
        "💡 *Note:* I will reply directly to your messages to keep the chat organized!"
    )
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                          text=help_text, parse_mode='Markdown')

# 3. Smart Chatbot with Tag (Reply)
@bot.message_handler(func=lambda m: True)
def auto_reply(message):
    chat_id = message.chat.id
    if chatbot_active.get(chat_id, False) and not message.text.startswith('/'):
        replies = [
            "Hnji, kaise ho aap? 😊",
            "Aur batao, kya chal raha hai group mein? ✨",
            "Sahi baat hai, main bhi yahi soch raha tha!",
            "Bhai, aapne toh dil jeet liya ye baat bol kar! ❤️"
        ]
        # This will tag the user on their keyboard
        bot.reply_to(message, random.choice(replies))

# 4. Toggle Command
@bot.message_handler(commands=['chatbot'])
def toggle_chat(message):
    chat_id = message.chat.id
    if "on" in message.text.lower():
        chatbot_active[chat_id] = True
        bot.reply_to(message, "✅ AI Chatbot is now ENABLED.")
    elif "off" in message.text.lower():
        chatbot_active[chat_id] = False
        bot.reply_to(message, "❌ AI Chatbot is now DISABLED.")

bot.infinity_polling()
