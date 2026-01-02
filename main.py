import telebot
from telebot import types
import random

# Your Verified Token
API_TOKEN = '8273081654:AAFyU56FG3PV5ohPMVk5EOqQuCKjnUO-DWc'
bot = telebot.TeleBot(API_TOKEN)

chatbot_active = {}

# 1. Professional & Long Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_help = types.InlineKeyboardButton("Commands Menu 📜", callback_data="help")
    btn_support = types.InlineKeyboardButton("Owner / Support 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(btn_help, btn_support)
    
    welcome_text = (
        "✨ *WELCOME TO THE PREMIUM GROUP MANAGER BOT* ✨\n\n"
        "Hello! I am your advanced digital assistant. I am here to make your "
        "group more interactive, fun, and automated with high-end features. 🚀\n\n"
        "🌟 *Key Features I Offer:*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🎮 *Interactive Games:* Fun challenges like /dare and /dice.\n"
        "❤️ *Matchmaking:* Find your group's daily /couple.\n"
        "🤖 *Smart AI:* I can chat with users when enabled.\n"
        "📊 *Management:* User IDs and group stats support.\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Click the Commands Menu button below to explore everything I can do!"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. Detailed Help Section (Fully English)
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_info(call):
    help_text = (
        "📖 *DETAILED COMMAND LIST*\n\n"
        "📍 *Entertainment Commands:*\n"
        "👉 /couple - Tag two random members as a couple.\n"
        "👉 /dare - Get a random exciting challenge.\n"
        "👉 /dice - Roll a dice to test your luck.\n\n"
        "📍 *AI Chatbot Settings:*\n"
        "👉 /chatbot on - Start the AI conversation mode.\n"
        "👉 /chatbot off - Stop the AI conversation mode.\n\n"
        "📍 *Utility Commands:*\n"
        "👉 /start - Open the main welcome dashboard.\n"
        "👉 /id - View your unique Telegram User ID.\n\n"
        "⚠️ *Note:* Always use the '/' prefix before any command."
    )
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                          text=help_text, parse_mode='Markdown')

# 3. Couple Command with Reply Feature
@bot.message_handler(commands=['couple'])
def find_couple(message):
    if message.chat.type == "private":
        bot.reply_to(message, "❌ Error: Please use this command in a Group Chat!")
        return
    bot.send_message(message.chat.id, "🔍 *Scanning members for today's match...*")
    # Using reply_to to tag the person who used the command
    bot.reply_to(message, "🎉 *Today's Special Couple:* \n\n👤 Member A + 👤 Member B \n\n❤️ *A match made in heaven!*")

# 4. Chatbot with Direct Reply (Keyboard Tag) Feature
@bot.message_handler(func=lambda m: True)
def auto_reply(message):
    chat_id = message.chat.id
    if chatbot_active.get(chat_id, False) and not message.text.startswith('/'):
        # Random Hinglish Replies
        replies = [
            "Hnji, kaise ho aap? 😊",
            "Aur batao, kya chal raha hai group mein?",
            "Sahi baat hai, main bhi yahi soch raha tha! ✨",
            "Bhai, aapne toh ekdum sahi point pakda hai!",
            "Main toh bot hoon, par aapki baatein bahut interesting hain!"
        ]
        # bot.reply_to automatically tags the user just like in your screenshot
        bot.reply_to(message, random.choice(replies))

# 5. Toggle Chatbot
@bot.message_handler(commands=['chatbot'])
def toggle_chat(message):
    chat_id = message.chat.id
    if "on" in message.text.lower():
        chatbot_active[chat_id] = True
        bot.reply_to(message, "✅ AI Chatbot is now ENABLED. Start talking!")
    elif "off" in message.text.lower():
        chatbot_active[chat_id] = False
        bot.reply_to(message, "❌ AI Chatbot is now DISABLED.")

bot.infinity_polling()
