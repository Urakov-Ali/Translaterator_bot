# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin

API_TOKEN = '5112320592:AAF2GpYXBS0QVBSkwqpT0wo2dpt1oZp-QTg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('''Салом Кирилбот га хуш келибсиз менга матнингизни жунатинг! : ''')


@dp.message_handler()
async def jav_ob(message: types.Message):
    msg = message.text
    msg = (to_cyrillic(msg)) if msg.isascii() else (to_latin(msg))
    message.reply(msg)
    await message.reply(msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
