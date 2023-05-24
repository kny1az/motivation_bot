# В этом файле находится основная логика телеграмм бота
import telebot

bot = telebot.TeleBot('6031181986:AAHSbk9u58ZSbWywWe_z1KgF4_FZ2RMBbP8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ! Я мотивационный бот! И тд текст')

@bot.message_handler(commands=['motivation'])
def help(message):
    bot.send_message(message.chat.id, 'Начать работу!')

@bot.message_handler(commands=['about'])
def help(message):
    bot.send_message(message.chat.id, 'Инфа о нас!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Инструкция тебе за щеку!')

@bot.message_handler()
def error(message):
    bot.send_message(message.chat.id, 'Ошибка, отсутсвует данная команда!')

bot.polling(none_stop=True)
