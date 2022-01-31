

from flask import Flask, request

import telebot
import os
TOKEN = '5103995054:AAHz7di0xy233ynKyqH1kMjiGv4nXAHgi9Q'
app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= ['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello user!')

@app.route('/' + TOKEN, methods = ['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 30-01-22",200

@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url ='https://telebot-first.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot",200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int(os.environ.get('PORT',5000)))

