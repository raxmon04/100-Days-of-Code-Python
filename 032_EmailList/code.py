# import smtplib

# my_email = "ramon.peter@css.ch"
# password = ""

# with smtplib.SMTP("mailhost.css.ch", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="ramonpeter6@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2004, month=12, day=9, hour=17)
# print(date_of_birth)

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()
my_email = "ramon.peter@css.ch"
password = ""

def pick_quote():
    if day_of_week == 1:
        with open(file="/mnt/d/Git/python/032_EmailList/quotes.txt") as data:
            quotes = data.readlines()
            random_quote = random.choice(quotes)
            return random_quote
        
with smtplib.SMTP("mailhost.css.ch", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ramon.peter6@gmail.com", msg=f"Subject: Daily Quote\n\n{pick_quote()}")