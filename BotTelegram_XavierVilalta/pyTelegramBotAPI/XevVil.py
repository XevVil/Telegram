#!/usr/bin/env python
# -"- coding: utf-8 -"-
import telebot

bot = telebot.TeleBot("948463735:AAEpz18IkUQBGX3wTtaqsEk9G7IxjQJhlrY")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Welcome to LeagueOfIron, press /list to see the champs you can search")

@bot.message_handler(commands=['list'])
def send_welcome(message):
	bot.send_message(message.chat.id,'/alistar  /aatrox  /kaisa  /lucian  /caitlyn /thresh')

@bot.message_handler(commands=['Alistar','alistar'])
def character(message):
		bot.send_message(message.chat.id,"Alistar Support (Only)-> Runes, Skill order , Items(essential items only)", 'rb')
		photo = open('Imatges/Alistar/AlistarSuppRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Alistar/AlistarSuppSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Alistar/AlistarSuppItem.png', )
		bot.send_photo(message.chat.id,photo)
		bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')


@bot.message_handler(commands=['Aatrox','aatrox'])
def menu(message):
	bot.send_message(message.chat.id,"Here you have all the positions you can play with Aatrox")
	bot.send_message(message.chat.id,"/aatrox_top, /aatrox_jung , /aatrox_mid", 'rb')

@bot.message_handler(commands=['aatrox_top'])
def character(message):

		bot.send_message(message.chat.id,"Aatrox Top -> Runes, Skill order , Items(essential items only)", 'rb')
		photo = open('Imatges/Aatrox/AatroxTopRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopItem.png', )
		bot.send_photo(message.chat.id,photo)
		bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['aatrox_jung'])
def character(message):
	bot.send_message(message.chat.id,"Aatrox Jungler -> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Aatrox/AatroxJungleRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Aatrox/AatroxTopSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Aatrox/AatroxJungleItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['aatrox_mid'])
def character(message):
		bot.send_message(message.chat.id,"Aatrox Jungler -> Runes, Skill order , Items(essential items only)", 'rb')
		photo = open('Imatges/Aatrox/AatroxMidRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Aatrox/AatroxTopItem.png', )
		bot.send_photo(message.chat.id,photo)
		bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['kaisa'])
def character(message):
	bot.send_message(message.chat.id,"Kai'sa ADC (Only)-> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Kaisa/KaisaAdcRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Kaisa/KaisaAdcSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Kaisa/KaisaAdcItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['lucian'])
def menu(message):
	bot.send_message(message.chat.id,"Here you have all the positions you can play with Lucian")
	bot.send_message(message.chat.id,"/lucian_top, /lucian_mid, /lucian_adc", 'rb')

@bot.message_handler(commands=['lucian_adc'])
def character(message):
	bot.send_message(message.chat.id,"Lucian ADC -> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Lucian/LucianAdcRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianAdcSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianAdcItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list")


@bot.message_handler(commands=['lucian_top'])
def character(message):
	bot.send_message(message.chat.id,"Lucian Top -> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Lucian/LucianAdcRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianAdcSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianTopItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['lucian_mid'])
def character(message):
	bot.send_message(message.chat.id,"Lucian Mid -> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Lucian/LucianMidRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianAdcSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Lucian/LucianTopItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['caitlyn'])
def character(message):
	bot.send_message(message.chat.id,"Caitlyn ADC (Only)-> Runes, Skill order , Items(essential items only)", 'rb')
	photo = open('Imatges/Caitlyn/CaitlynAdcRunes.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Caitlyn/CaitlynAdcSkill.png', )
	bot.send_photo(message.chat.id,photo)
	photo = open('Imatges/Caitlyn/CaitlynAdcItem.png', )
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')

@bot.message_handler(commands=['thresh'])
def character(message):
		bot.send_message(message.chat.id,"Thresh Support (Only)-> Runes, Skill order , Items(essential items only)", 'rb')
		photo = open('Imatges/Thresh/ThreshSuppRunes.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Thresh/ThreshSuppSkill.png', )
		bot.send_photo(message.chat.id,photo)
		photo = open('Imatges/Thresh/ThreshSuppItem.png', )
		bot.send_photo(message.chat.id,photo)
		bot.send_message(message.chat.id,"if you want to see another character click /list", 'rb')



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'aquest personatge no esta en memòria')

bot.polling()
