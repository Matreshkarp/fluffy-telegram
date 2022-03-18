import random
import telebot
from telebot import types
import marker as nav

token='5135058166:AAEQN6Pv4juK4eHUh1Vn1ayXrqQFCY5uMZA'
bot = telebot.TeleBot(token)
benedikt = ['Yes', 'No', 'HOHOHO', 'BRBRBR', 'What?(Что?)', 'Repeat(повтори)', 'Возможно', 'Не знаю!']

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, "Добро пожаловать, <code>{0}</code>!".format(user_name), reply_markup = nav.markup, parse_mode = 'html')
@bot.message_handler(content_types=['text'])
def text_message(message):
 if message.text == '🔮Всевидящий Бэн':
    bot.send_message(message.chat.id, 'Скажешь "👨‍🌾Загадал", когда спросишь!', reply_markup = nav.markup2)
 if message.text == '👨‍🌾Загадал':
    bot.send_message(message.chat.id,  '<code>Бэн говорит: </code>' + str(random.choice(benedikt)), parse_mode = 'html')
 if message.text == '🔙Назад':
 	bot.send_message(message.chat.id, '<b>Вы вернулись в главное меню</b>', parse_mode = 'html', reply_markup = nav.markup)
 if message.text == '💬Информация':
 	bot.send_message(message.chat.id, '<b>Всевидящий Бэн v1.0\nБот создан за 1 час на TeleBot.</b>', parse_mode = 'html', reply_markup = nav.markup)
bot.polling(none_stop=True)