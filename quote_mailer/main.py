import datetime as dt
import smtplib
from random import randint
import os
import requests
from Whatsapp import whatsapp as wp
Now = dt.datetime.now()
day_of_week = Now.weekday()

def telegram_bot_sendtext(bot_message):
    bot_token = '5903068974:AAEk4oBUPbTvn0rtZqMtap-Pj0vj6t7vxp4'
    bot_chatID = '1018507134'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

with open("quote_mailer/quotes.txt", "r") as quotes:
    text = quotes.readlines()
    quote = text[randint(0, len(text) - 1)]


try:
    wp.send_whatsapp_msg(os.environ["PHONE"], quote)
    with smtplib.SMTP(os.environ["SMTP"], int(os.environ["PORT"])) as connection:
        connection.starttls()
        connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASS"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["TARGET_EMAIL"],
            msg="Subject:Motivational Quote\n\n"
                f"{quote}"
        )
    print("Email Send Successfully")
except Exception as error:
    print(f"Failed to send error: {error}")

text = "Motivational Quote:\n"\
                f"{quote}"
telegram_bot_sendtext(text)
