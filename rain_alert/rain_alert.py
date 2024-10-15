import os

import requests
from automatic_scripts import whatsapp as wp
api_key = "fc51dfd03456555e16d19dfa764b1c07"
my_lat = 30.096655
my_long = 31.662533
api_parameters = {
    "appid": api_key,
    "lat": 30.096655,
    "lon": 31.662533,
    "exclude": "current,minutely,daily"
}


def telegram_bot_sendtext(bot_message):
    bot_token = '5903068974:AAEk4oBUPbTvn0rtZqMtap-Pj0vj6t7vxp4'
    bot_chatID = '1018507134'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    wp.send_whatsapp_msg(os.environ["PHONE"], bot_message)

    return response.json()


api = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=api_parameters)
api.raise_for_status()
data = api.json()
weather_codes = [data["hourly"][code]["weather"][0]["id"] for code in range(20)]
will_rain = False

for code in weather_codes:
    if code < 700:
        print(f"{code}: RAIN!!!!")
        will_rain = True

if will_rain:
    response = telegram_bot_sendtext("IT WILL RAIN")
    print(response)
else:
    response = telegram_bot_sendtext("No Rain")
    print(response)

print(weather_codes)
