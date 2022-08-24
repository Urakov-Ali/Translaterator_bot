# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin


API_TOKEN = '5112320592:AAEoBW5MFvOO5JDtYMNN0iFWmV6oFNGcEfs'
from classs import Infos
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
x =Infos()
Admin ='1344241185'
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    #Create our table to save the users in our database 
    #(so by the command of [/alluser] we can know how many people are using our bot now)
    x.create_table()
    global userid
    #taking all the needed informations about the new user
    userid =message.from_user.id
    username =message.from_user.username
    firstname =message.from_user.first_name
    #to check if user's data exist in basa
    #1 -it doesn't let to one person subscribe twice on our bot
    #2 -so the database will sort and add only those subscribers who is new in our bot
    check_it =x.check(userid)
    
    #here is the process of sorting 
    if check_it is None:
        x.insert(userid, username, firstname)
        z =x.admin_notify(userid)
        await bot.send_message(Admin, f"New user has been registered \nUser_id: {z[0]} \nUsername: @{z[1]} \nFirstname: {z[2]}")
        await message.reply('''Салом Кирилбот га хуш келибсиз \nменга матнингизни жунатинг! : ''')
    else:
        await message.reply('''Салом Кирилбот га хуш келибсиз \nменга матнингизни жунатинг! : ''')


@dp.message_handler(commands='alluser', user_id=Admin)
async def count(message: types.Message):
	user_id =message.from_user.id
	counted =x.count(user_id)
	users =x.users_id()
	son =0
	userlist =""
	for user in users:
		son +=1
		userlist +=f"\n {son}) Id: {user[0]} \nUsername: @{user[1]}\n" 
		
	await bot.send_message(Admin, f"Foydalanuvchilar soni: {counted[0][0]} ta \
		\n{userlist}")
@dp.message_handler()
async def jav_ob(message: types.Message):
    msg = message.text
    msg = (to_cyrillic(msg)) if msg.isascii() else (to_latin(msg))
    message.reply(msg)
    await message.reply(msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
