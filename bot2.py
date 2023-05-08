import telebot
import os
import time
import random
from telethon import TelegramClient, events, types

tok="6011914153:AAHUdtuEM6Spdh5yHB2SrKtI8Ms-YNtGj9o" 
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start']) 
def welcome(message):
    bot.send_message(message.chat.id, "WELLCOME TO BOT JOIN GRUP\n https://t.me/snifConfig\nhttps://t.me/EstebanUnlocker\nhttps://t.me/decrypt_vpn_file\nhttps://t.me/KMKZNET\n==========================")
    
@bot.message_handler(content_types=['document']) 
def post(message):
    print(message) 
    name=message.document.file_name 
    
    id=message.document.file_id
    file_info = bot.get_file(id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    jj=open(name,"wb") 
    jj.write(downloaded_file)
    jj.close()    
    os.system('python entrykey.py "'+name+'" > test.txt')
    jh=open("test.txt").read()
    bot.reply_to(message, jh)

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, message.text)
    elif message.chat.type == "private":
        if('@Dectnl_bot' in message.text):
            bot.reply_to(message, "Hello to all!")

print('BOT BERJALAN')
print("JAGAN LUPA TURU 🗿") 
bot.polling()