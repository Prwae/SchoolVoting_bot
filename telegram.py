from telebot import TeleBot
import telebot

bot = TeleBot("5091468418:AAE0OBuw3xHxx0OT7rsAQlJiru4DfzOlv0E")

@bot.message_handler(commands=["start"])
def func(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    #test_button = telebot.types.ReplyKeyboardButton(text='Тест', callback_data='test_button')
    #keyboard.add(test_button)
    bot.send_message(message.chat.id, "Prtre", reply_markup=keyboard)


bot.polling()

'''
import telebot
from telebot import types

bot = telebot.TeleBot("5091468418:AAE0OBuw3xHxx0OT7rsAQlJiru4DfzOlv0E")
ID_CHAT = ""

def some_func(chat_id):
    bot.send_message(chat_id, "qwerty")

@bot.message_handler(commands=['start'])
def some(message):
    global ID_CHAT
    ID_CHAT = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    test_button = types.InlineKeyboardButton(text='Тест', callback_data='test_button')
    keyboard.add(test_button)
    bot.send_message(message.chat.id, 'Нажми на кнопку', reply_markup=keyboard)

# Inline keyboard


bot.polling()'''