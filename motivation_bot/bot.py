# В этом файле находится основная логика телеграмм бота
import telebot

bot = telebot.TeleBot('5996242526:AAGRh-F7JJzW4sCOQzdwvVeHnmAmDn-J4KU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} !')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Some instructions!')

@bot.message_handler()
def error(message):
    bot.send_message(message.chat.id, 'Error, I don\'t have such a command!')

bot.polling(none_stop=True)
