

from flask import Flask, request

import telebot
import os

app = Flask(__name__)
#TOKEN = '5269219119:AAFrmHRH-rCbS9ABReFB86ZXk208zaq4Jmg'
TOKEN = os.environ.get('TOKEN')


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
#    bot.set_webhook(url='/' + TOKEN)
    bot.set_webhook(url ='https://telebot-first.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot",200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int(os.environ.get('PORT',5000)))

