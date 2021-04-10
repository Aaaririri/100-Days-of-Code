"""
import smtplib

my_email = "youremail@gmail.com"
password = "yourpassword"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #secures the conection and encrypt the mesage
    connection.login(user = my_email, password = password)
    connection.sendmail(from_addr = my_email, to_addrs = "yourfriendsemail@live.com", msg = "Subject:Subject of your email\n\ncontent of your email")

"""
"""
import datetime as dt

now = dt.datetime.now()
print(now)
"""