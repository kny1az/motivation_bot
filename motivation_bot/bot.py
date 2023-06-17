# В этом файле находится основная логика телеграмм бота
import aiogram
import time
import logging

from aiogram import Bot, Dispatcher, types,executor

from config import *

#Привязка бота к токену
bot = Bot(TOKEN)
dp = Dispatcher(bot)

#Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, startMes)

#Обработка команды /motivation
@dp.message_handler(commands=['motivation'])
async def motivation(message):
    await bot.send_message(message.chat.id, motivationMes)

#Обработка команды /about
@dp.message_handler(commands=['about'])
async def about(message):
    await bot.send_message(message.chat.id, aboutMes)

#Обработка команды /help
@dp.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(message.chat.id, helpMes)

#Обработка неизвестных команд
@dp.message_handler()
async def error(message):
    await bot.send_message(message.chat.id, errorMes)

#Постоянная работа бота
executor.start_polling(dp)

