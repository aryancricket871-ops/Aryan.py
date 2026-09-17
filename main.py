import os
import time
import random
import requests
import telebot
from getuseragent import UserAgent
from flask import Flask
from threading import Thread

# --- वेब सर्वर (बॉट को जगाए रखने के लिए) ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Aryan King Hacker Bot Zinda Hai!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()
# -------------------------------------------

BOT_TOKEN = "8874731134:AAFQMI3WcRUl0mX5Vg1RjAE0qpKvzyQAmso"
MY_CHAT_ID = "8935738319"

bot = telebot.TeleBot(BOT_TOKEN)
user_data = {}

@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.chat.id) != MY_CHAT_ID:
        bot.reply_to(message, "🚫 यह Aryan King Hacker का प्राइवेट बॉट है।")
        return
    msg = bot.reply_to(message, "👋 Aryan King Hacker Free Like Bot चालू है! 🔥\n\nकृपया Instagram Username भेजें:")
    bot.register_next_step_handler(msg, get_username)

def get_username(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'username': message.text}
    msg = bot.reply_to(message, "👍 अब पोस्ट का Link (URL) भेजें:")
    bot.register_next_step_handler(msg, process_smm_request)

def process_smm_request(message):
    chat_id = message.chat.id
    link = message.text
    username = user_data[chat_id]['username']
    bot.send_message(chat_id, "⏳ Aryan King Hacker लाइक्स भेज रहा है...")
    
    try:
        ua = UserAgent('ios').Random()
        email = f"srk{random.randint(100000, 999999)}@gmail.com"
        res = requests.post('https://api.likesjet.com/freeboost/7', json={
            'instagram_username': username, 'link': link, 'email': email
        }, headers={
            'Host': 'api.likesjet.com',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'user-agent': ua,
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://likesjet.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://likesjet.com/'
        }).json()
        
        server_message = res.get('message', 'Request Sent!')
        bot.send_message(chat_id, f"✅ **सक्सेस!**\n\n📌 {server_message}\n🔥 By Aryan King Hacker", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(chat_id, f"❌ **Error:**\n`{e}`", parse_mode="Markdown")

keep_alive()
print("Aryan King Hacker Bot चालू हो गया है...")
bot.infinity_polling()
