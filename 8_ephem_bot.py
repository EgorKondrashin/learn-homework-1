"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('API_KEY'))

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def const_planet(update, context):
    try:
        today = datetime.datetime.today().date()
        planet_from_user = update.message.text.split()[1]
        if planet_from_user == 'Mars':
            planet = ephem.Mars(today)
        elif planet_from_user == 'Mercury':
            planet = ephem.Mercury(today)
        elif planet_from_user == 'Venus':
            planet = ephem.Venus(today)
        elif planet_from_user == 'Jupiter':
            planet = ephem.Jupiter(today)
        elif planet_from_user == 'Saturn':
            planet = ephem.Saturn(today)
        elif planet_from_user == 'Uranus':
            planet = ephem.Uranus(today)
        elif planet_from_user == 'Neptune':
            planet = ephem.Neptune(today)
        elif planet_from_user == 'Pluto':
            planet = ephem.Pluto(today)
        elif planet_from_user == 'Sun':
            planet = ephem.Sun(today)
        elif planet_from_user == 'Moon':
            planet = ephem.Moon(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f"Сегодня {planet_from_user} находится в "
                                  f"созвездиии: {'-'.join(const)}")
    except IndexError:
        text = 'С командой /planet должна быть написана планета!\nПример использования: /planet Mars'
        update.message.reply_text(text)


def main():
    mybot = Updater(os.getenv('API_KEY'))

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", const_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
