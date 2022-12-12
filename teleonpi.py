import telebot
import wikipedia
import requests
TOKEN = '5510691725:AAGKIIss8tswO0jQQBsrcfqoY0sm6WmpyRw'
CHAT_ID = 1942368034
bot = telebot.TeleBot(TOKEN)
print("begin  ")

def get_api(addess):
    api = f"http://api.weatherapi.com/v1/current.json?key=35d22932e5c64a33bc6174822221112&q={addess}&aqi=no"
    response = requests.get(api)
    data = response.json()
    location = data['location']
    current = data['current']
    add = location['name']
    country = location['country']
    lat = location['lat']
    lon = location['lon']
    temp_c = current['temp_c']
    temp_f = current['temp_f']
    return add, country, lat, lon,temp_c, temp_f


@bot.message_handler(commands=['start'])
def voice_processing(message):
    bot.reply_to(message, f"Hello {message.from_user.username}")
    print("rep oke")

@bot.message_handler(commands=['infor'])
def voice_processing(message):
    bot.reply_to(message, f"\nUsername: {message.from_user.username}"
                          f"\nID: {message.from_user.username}"
                          f"\nLastname: {message.from_user.last_name}"
                            f"\nFirstname: {message.from_user.first_name}"
                 )
    print("rep oke")
@bot.message_handler(commands=['help'])
def voice_processing(message):
    bot.reply_to(message, "Tôi có thể giúp gì cho bạn???")
    print("rep oke")

@bot.message_handler(commands=['hanoi'])
def voice_processing(message):
    addess = "hanoi"
    add, country, lat, lon, temp_c, temp_f = get_api(addess)
    bot.reply_to(message, f"\n Addess: {add}"
                          f"\n Country: {country}"
                          f"\n lat: {lat}"
                          f"\n lon: {lon}"
                          f"\n tempurature: {temp_c} ℃"
                          f"\n tempurature: {temp_f} °F "
                 )
    print("rep oke")
@bot.message_handler(commands=['korea'])
def voice_processing(message):
    addess = "korea"
    add, country, lat, lon, temp_c, temp_f = get_api(addess)
    bot.reply_to(message, f"\n Addess: {add}"
                          f"\n Country: {country}"
                          f"\n lat: {lat}"
                          f"\n lon: {lon}"
                          f"\n tempurature: {temp_c} ℃"
                          f"\n tempurature: {temp_f} °F "
                 )
    print("rep oke")
@bot.message_handler(commands=['london'])
def voice_processing(message):
    addess = "london"
    add, country, lat, lon, temp_c, temp_f = get_api(addess)
    bot.reply_to(message, f"\n Addess: {add}"
                          f"\n Country: {country}"
                          f"\n lat: {lat}"
                          f"\n lon: {lon}"
                          f"\n tempurature: {temp_c} ℃"
                          f"\n tempurature: {temp_f} °F "
                 )
    print("rep oke")
bot.polling()

