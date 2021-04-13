import datetime
today = (datetime.datetime.now().month, datetime.datetime.now().day)
# you need to change the ***** for your data email, password 
import pandas 
import random
import smtplib
data = pandas.read_csv("Day 032/Birthday wish/birthdays.csv")
birthdays = {(datarow.month, datarow.day): datarow for (index , datarow) in data.iterrows()}
n = random.randint(1,3)
if today in birthdays:
    person = birthdays[today]
    with open(f"Day 032/Birthday wish/letter_templates/letter_{n}.txt") as file:
        content = file.read()
        new_content = content.replace("[NAME]",person["name"])
    my_email = "**********@gmail.com"
    password = "************"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = person["email"], 
            msg = f"Subject:Happy Birthday\n\n{new_content}"
            )
