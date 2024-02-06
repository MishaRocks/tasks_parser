import telebot

import os
from dotenv import load_dotenv

load_dotenv()

tl_token = '6934334873:AAGqhNb8Dg6TvBh1BWxvdsbIYx7DEysXzaM'
bot = telebot.TeleBot(tl_token)


@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, "Тут будет текст с вариантами запросов")


bot.polling(none_stop=True)
