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

    if wind_direction in range(-10 , 10):
        wind_direction = "C"

    text = ('''
Температура воздуха: {temp}° C
Влажность воздуха: {humidity} %
Давление: {pressure} мм рт. ст.
Скорость ветра: {wind_speed} м/с {wind_direction}°
    ''').format(temp=temp, humidity=humidity, pressure=pressure, wind_speed=wind_speed, wind_direction=wind_direction)
    bot.send_message(update.message.chat_id, text)
    return "Menu"
