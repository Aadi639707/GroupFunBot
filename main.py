import telebot
from telebot import types
import random

# Your Verified Token
API_TOKEN = '8273081654:AAFyU56FG3PV5ohPMVk5EOqQuCKjnUO-DWc'
bot = telebot.TeleBot(API_TOKEN)

chatbot_active = {}

# 1. High-End Professional Welcome Message (English)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_help = types.InlineKeyboardButton("Explore Commands 📜", callback_data="help")
    btn_support = types.InlineKeyboardButton("Support/Owner 👤", url="https://t.me/SANATANI_GOJO")
    markup.add(btn_help, btn_support)
    
    welcome_text = (
        "✨ *WELCOME TO THE ULTIMATE GROUP ASSISTANT* ✨\n\n"
        "Greetings! I am a premium-tier Telegram bot designed to elevate your group's "
        "engagement and entertainment. I am packed with interactive features and smart automation. 🚀\n\n"
        "🌟 *What I Bring to Your Group:*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "❤️ *Social:* Weekly/Daily match with /couple command.\n"
        "🎮 *Games:* Fun challenges including /dare and /dice.\n"
        "🤖 *AI Module:* Integrated smart chatbot for active conversations.\n"
        "⚙️ *Utilities:* Fast responses and easy management.\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Click the Explore Commands button below to get started!"
    )
    # Using reply_to to tag user on start
    bot.reply_to(message, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. Detailed Commands Menu (English)
@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_info(call):
    help_text = (
        "📖 *DETAILED COMMAND DIRECTORY*\n\n"
        "📍 *Entertainment & Fun:*\n"
        "👉 /couple - Tag random members as today's match.\n"
        "👉 /dare - Receive a random fun challenge.\n"
        "👉 /dice - Roll a virtual dice for luck.\n\n"
        "📍 *AI Chatbot Settings:*\n"
        "👉 /chatbot on - Enable the smart reply module.\n"
        "👉 /chatbot off - Disable the smart reply module.\n\n"
        "📍 *General Information:*\n"
        "👉 /start - Access the main dashboard.\n"
        "👉 /id - View your Telegram User Account ID.\n\n"
        "💡 *Tip:* Reply to any of my messages to keep the conversation going!"
    )
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                          text=help_text, parse_mode='Markdown')

# 3. Couple Command with Reply/Tag Feature
@bot.message_handler(commands=['couple'])
def find_couple(message):
    if message.chat.type == "private":
        bot.reply_to(message, "❌ This feature is exclusively for Group Chats!")
        return
    bot.send_message(message.chat.id, "🔍 *Analyzing group activity to find the perfect match...*")
    # Tags the user who used the command
    bot.reply_to(message, "🎉 *Today's Featured Couple:* \n\n👤 Member 1 + 👤 Member 2 \n\n❤️ *A perfect match made in this group!*")

# 4. Smart Chatbot with "Reply-to-User" Feature
@bot.message_handler(func=lambda m: True)
def auto_reply(message):
    chat_id = message.chat.id
    if chatbot_active.get(chat_id, False) and not message.text.startswith('/'):
        # Friendly Hinglish replies
        replies = [
            "Hnji, kaise ho aap? 😊",
            "Aur batao, kya chal raha hai aaj kal?",
            "Sahi baat hai, main bhi yahi soch raha tha! ✨",
            "Bhai, aapne toh dil jeet liya ye baat bol kar!",
            "Main bot hoon par feeling puri hai meri! 😂"
        ]
        # reply_to tags the user's message exactly like in your screenshot
        bot.reply_to(message, random.choice(replies))

# 5. Toggle Command
@bot.message_handler(commands=['chatbot'])
def toggle_chat(message):
    chat_id = message.chat.id
    if "on" in message.text.lower():
        chatbot_active[chat_id] = True
        bot.reply_to(message, "✅ AI Chatbot has been ENABLED.")
    elif "off" in message.text.lower():
        chatbot_active[chat_id] = False
        bot.reply_to(message, "❌ AI Chatbot has been DISABLED.")

bot.infinity_polling()
