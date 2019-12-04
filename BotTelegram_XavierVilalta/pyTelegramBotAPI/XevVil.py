#!/usr/bin/env python
# -"- coding: utf-8 -"-
import telebot

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
		bot.send_message(message.chat.id,"Alistar Support -> Runes, Skills , Items(essential items only)", 'rb')
		photo = open('Imatges/Alistar/AlistarSuppRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Alistar/AlistarSuppSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Alistar/AlistarSuppItem.png', )
		bot.send_photo(message.chat.id,photo)
	else:
		bot.send_message(message.chat.id,"Alistar is only support lmao, good luck playing this little shit somewhere else.", 'rb')


@bot.message_handler(commands=['Aatrox','aatrox'])
def character(message):
	if message.text.split(' ')[1] == 'top':
		bot.send_message(message.chat.id,"Aatrox Top -> Runes, Skills , Items(essential items only)", 'rb')
		photo = open('Imatges/Aatrox/AatroxTopRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopItem.png', )
		bot.send_photo(message.chat.id,photo)

	elif message.text.split(' ')[1] == 'jungle':
		bot.send_message(message.chat.id,"Aatrox Jungler -> Runes, Skills , Items(essential items only)", 'rb')
		photo = open('Imatges/Aatrox/AatroxJungleRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxJungleItem.png', )
		bot.send_photo(message.chat.id,photo)

	elif message.text.split(' ')[1] == 'mid':
		bot.send_message(message.chat.id,"Aatrox Jungler -> Runes, Skills , Items(essential items only)", 'rb')
		photo = open('Imatges/Aatrox/AatroxMidRunes.png', )
		bot.send_photo(message.chat.id,photo)

	else:
		bot.send_message(message.chat.id,"Alistar is only support lmao, good luck playing this little shit somewhere else.", 'rb')




@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'aquest personatge no estar en memòria')

bot.polling()
