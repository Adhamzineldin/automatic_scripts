import datetime as dt
import smtplib
from random import randint
import os

Now = dt.datetime.now()
day_of_week = Now.weekday()



with open("quote_mailer/quotes.txt", "r") as quotes:
    text = quotes.readlines()
    quote = text[randint(0, len(text) - 1)]
try:
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
