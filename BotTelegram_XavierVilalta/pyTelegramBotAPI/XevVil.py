#!/usr/bin/env python
# -"- coding: utf-8 -"-
import telebot
import json

bot = telebot.TeleBot("948463735:AAEpz18IkUQBGX3wTtaqsEk9G7IxjQJhlrY")

rTop = ["Top","top"]

rJung = ["jugler","jung"]



json_lol_keyboard = json.dumps({'keyboard': [["Top", "Support"]],
						   'one_time_keyboard': False,
						   'resize_keyboard': True})

json_build_keyboard = json.dumps({'keyboard': [["all", "items","skills"]],
						   'one_time_keyboard': False,
						   'resize_keyboard': True})


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['LeagueOfLegends','lol','help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to the League of legends build helper.")

@bot.message_handler(commands=['Alistar','alistar'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Whitch position do you wanna play? (Recomendated position: Support, Top.)",reply_markup=json_lol_keyboard)
	





@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
