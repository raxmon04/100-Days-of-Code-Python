import pandas
import datetime as dt
import random
import smtplib

# ============================ CONSTANTS ================================#
BIRTHDAYS = "/mnt/d/Git/python/032_EmailList/birthdays.csv"
NOW = dt.datetime.now()
TODAY = NOW.month, NOW.day
my_email = "ramon.peter@css.ch"
password = ""
letter_number = random.randint(1,3)

# ============================ LOAD DATA ================================#
data = pandas.read_csv(BIRTHDAYS)

# ============================ BUILD DICTIONARY ================================#
birthdays_dict = {
    (row["month"], row["day"]): row
    for _, row in data.iterrows()
}

# ============================ CHECK BIRTHDAY ================================#
if TODAY in birthdays_dict:
    name = birthdays_dict[TODAY]["name"]
    with open(f"/mnt/d/Git/python/032_EmailList/letter_templates/letter_{letter_number}.txt") as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace("[NAME]", name)

# ============================ SEND LETTER ================================#
email = birthdays_dict[TODAY]["email"]
with smtplib.SMTP("mailhost.css.ch", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{new_letter}")



