import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

URL = "https://appbrewery.github.io/Zillow-Clone/"

# Scrape data from the webpage
response = requests.get(URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
listings_links = [listing["href"] for listing in all_links]
all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
listing_prices = [price.getText().split("+")[0].replace("/mo", "") for price in all_prices]
all_addresses = soup.find_all(name="address")
listing_addresses = [address.get_text().split(" | ")[-1].strip() for address in all_addresses]

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc4R7CKpT-U0W3t_iijTN243Lp7Av5z5fjCeytN5UqqprQ8ww/viewform?usp=dialog")

for n in range(len(listings_links)):
    time.sleep(2)
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    link_input.send_keys(listings_links[n])
    price_input.send_keys(listing_prices[n])
    address_input.send_keys(listing_addresses[n])
    submit_button.click()
    time.sleep(2)
    another_response_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response_link.click()
