import smtplib 
import datetime as dt
from random import choice
today = dt.datetime.now()
weekday = today.weekday()
# you need to change the ***** for your data email, password and email of the recever
if weekday == 0:
    with open("Day 032/Monday Motivational/quotes.txt") as file:
        all_quotes = file.readlines()
    todays_quote = choice(all_quotes)
    my_email = "**********@gmail.com"
    password = "********"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = "**********@hotmail.com", 
            msg = f"Subject:Monday Motivacional\n\n{todays_quote}"
            )
