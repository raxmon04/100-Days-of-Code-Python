from bs4 import BeautifulSoup
import requests
import smtplib
# Add the os and dotenv modules
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

# Practice
# url = "https://appbrewery.github.io/instant_pot/"
# Live Site
url = "https://www.amazon.de/-/en/Philips-OneBlade-Original-Blades-Replacement/dp/B0BS747TYL/ref=zg_bs_c_drugstore_d_sccl_3/259-1767365-8564830"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36", 
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()
# print(price)

# REGEX: finde die erste Zahl mit zwei Dezimalstellen
match = re.search(r"(\d+[.,]\d{2})", price)

if not match:
    raise ValueError("Kein gültiger Preis gefunden!")

number_str = match.group(1).replace(",", ".")
price_as_float = float(number_str)

# print("Preis als Float:", price_as_float)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Use environment variables ===========================
    
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )