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
    temp = round(result.get("main").get("temp")-273.15)
    humidity = result.get("main").get("humidity")
    pressure = round(result.get("main").get("pressure")/1.333)

    wind_speed = result.get("wind").get("speed")
    wind_direction = result.get("wind").get("deg")

    if wind_direction in range(348, 360) or wind_direction in range(0, 10):
        wind_direction = "С"

    elif wind_direction in range(11, 32):
        wind_direction = "ССВ"

    elif wind_direction in range(33, 55):
        wind_direction = "СВ"

    elif wind_direction in range(56, 77):
        wind_direction = "ВСВ"

    elif wind_direction in range(78, 100):
        wind_direction = "В"

    elif wind_direction in range(101, 122):
        wind_direction = "ВЮВ"

    elif wind_direction in range(123, 145):
        wind_direction = "ЮВ"

    elif wind_direction in range(146, 167):
        wind_direction = "ЮЮВ"

    elif wind_direction in range(168, 190):
        wind_direction = "Ю"

    elif wind_direction in range(191, 212):
        wind_direction = "ЮЮЗ"

    elif wind_direction in range(213, 235):
        wind_direction = "ЮЗ"

    elif wind_direction in range(236, 257):
        wind_direction = "ЗЮЗ"

    elif wind_direction in range(258, 280):
        wind_direction = "З"

    elif wind_direction in range(281, 302):
        wind_direction = "ЗСЗ"

    elif wind_direction in range(303, 325):
        wind_direction = "СЗ"

    elif wind_direction in range(326, 347):
        wind_direction = "ССЗ"

    text = ('''
Температура воздуха: {temp}° C
Влажность воздуха: {humidity} %
Давление: {pressure} мм рт. ст.
Ветер: {wind_direction} {wind_speed} м/с 
    ''').format(temp=temp, humidity=humidity, pressure=pressure, wind_speed=wind_speed, wind_direction=wind_direction)
    bot.send_message(update.message.chat_id, text)
    return "Menu"
