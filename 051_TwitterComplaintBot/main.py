from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

# Constants
PROMISED_DOWN = 150  # in Mbps
PROMISED_UP = 10  # in Mbps
CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
TWITTER_EMAIL = "ramonpeter6@gmail.com"
TWITTER_PASSWORD = "hypjet-Hoqju6-sosxif"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 2)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.wait.until(ec.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))).click()
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "start-text"))).click()
        time.sleep(60)  # Wait for the test to complete
        self.down = float(self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "download-speed"))).text)
        self.up = float(self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "upload-speed"))).text)
        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")
    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        email_input = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        try:
            password_input = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)
            tweet_compose = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div')))
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            tweet_button = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')))
            tweet_button.click()
        except TimeoutException:
            print("There was a login issue. X thinks you are a bot.")

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()

input("")