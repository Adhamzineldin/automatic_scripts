import datetime as dt
import json
import os
import random
import smtplib



##################### Extra Hard Starting Project ######################

with open("birthdays.json", "r") as file:
    data = json.load(file)

names = [name for name in data.keys()]


def send_mail(name, mail):
    letters = [
        "letter_templates/letter_1.txt",
        "letter_templates/letter_2.txt",
        "letter_templates/letter_3.txt"]
    letter_file = f"{random.choice(letters)}"
    with open(letter_file, "r") as letter:
        text = letter.read()
        text = text.replace("[NAME]", name.title())

    with smtplib.SMTP(os.environ["SMTP"], int(os.environ["PORT"])) as connection:
        connection.starttls()
        connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASS"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=mail,
            msg="Subject:Happy Birthday\n\n"
                f"{text}"

        )
        print(f"Email Sent Successfully to {name}")


now = dt.datetime.now()
for name in names:
    if data[name]["month"] == now.month and data[name]["day"] == now.day:
        send_mail(name, data[name]["email"])

# python -m PyInstaller --windowed --onefile  main.py
