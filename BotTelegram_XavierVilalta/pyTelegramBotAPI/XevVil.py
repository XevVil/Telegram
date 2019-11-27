#!/usr/bin/env python
# -"- coding: utf-8 -"-
import telebot
import json

bot = telebot.TeleBot("948463735:AAEpz18IkUQBGX3wTtaqsEk9G7IxjQJhlrY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['LeagueOfLegends','lol'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to the League of legends build helper.")

@bot.message_handler(commands=['Alistar','alistar'])
def character(message):

	if message.text.split(' ')[1] == 'supp':
		bot.send_message(message.chat.id,"Alistar Support", 'rb')
		photo = open('Imatges/AlistarSuppRunes.png')
		bot.send_photo(chat_id, photo)
		#bot.send_message(message.chat.id,"Whitch position do you wanna play? (Recomended position: Support, Top.)",reply_markup = json_lol_keyboard)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'aquest personatge no estar en memòria')

bot.polling()
