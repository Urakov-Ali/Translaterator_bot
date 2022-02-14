# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '5112320592:AAF2GpYXBS0QVBSkwqpT0wo2dpt1oZp-QTg'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '''Salom kiril lotin botga hush kelibsiz.
Marhamat so'z kiriting: ''')
@bot.message_handler(func=lambda m: True)
def javob(message):
    msg = message.text
    jv = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, jv(msg))
    
bot.polling()


