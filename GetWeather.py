from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests


def whereweateher(bot, update):
    keyboard = [['Москва']]
    choice_keyboard = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        update.message.chat_id,
        text="Где показать погоду ?",
        reply_markup=choice_keyboard)
    return "Weather"


def getweather(bot, update):
    url = "http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=990a7da878286d1ebaaeb45810e9a714"
    result = requests.get(url).json()
    bot.send_message(update.message.chat_id, result.get("main"))
    return "Menu"
