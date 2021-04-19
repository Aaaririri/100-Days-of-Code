STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
"""
Links:
https://www.alphavantage.co/
https://newsapi.org/docs/endpoints/everything
you need to get keys for the apis 
and change the emails for yours 
change your_email and your_password and your_reciver for your own date 
this is a tesla stocks news tracker to send via email news about the stocks in case of hight variation
only on weekdays
"""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = " N1U285ZQOSSFDA53"
NEWS_API_KEY = "dc9052570a9d49b7973a847c91eb256d"

import requests 
import datetime
import smtplib

stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

response =requests.get(STOCK_ENDPOINT, stock)
response.raise_for_status()
stock_data = response.json()

week_day = datetime.date.weekday(datetime.date.today())

dict_key = list(stock_data["Time Series (Daily)"])

    
yesterday_stock_data = stock_data["Time Series (Daily)"][dict_key[0]]
before_yesterday_stock_data = stock_data["Time Series (Daily)"][dict_key[1]]

yesterday_close = float(yesterday_stock_data["4. close"])

bfyesterday_close = float(before_yesterday_stock_data["4. close"])

difference = abs(yesterday_close - bfyesterday_close)
up_down = None

if difference > 0:
    up_down = "UP"
else:
    up_down = "DOWN"

difference_percentage = (difference/yesterday_close)*100

news = {
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API_KEY
}

if difference_percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, news)
    news_response.raise_for_status()
    article = news_response.json()["articles"]
    send_article = article[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down} {difference_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']} \nSite: {article['url']}\n\n" for article in send_article] 

    text = ""
    for items in formatted_articles:
        text += items
        
    if week_day < 5:
        my_email = "youremail@gmail.com"
        password = "yourpassword"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() 
            connection.login(user = my_email, password = password)
            connection.sendmail(
                                from_addr = my_email, 
                                to_addrs = "yourrecever@live.com", 
                                msg = f"Subject:Tesla Stocks News\n\n{text}"
                                )
        