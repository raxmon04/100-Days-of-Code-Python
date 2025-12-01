from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "burkgnar"
USERNAME = "campgadgetsco"
PASSWORD = "Pramon14"
URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 2)

    def login(self):
        self.driver.get(URL)
        time.sleep(2)
        cookie_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        if cookie_button:
            cookie_button.click()
        time.sleep(2)
        username_input = self.wait.until(ec.presence_of_element_located((By.NAME, 'username')))
        password_input = self.wait.until(ec.presence_of_element_located((By.NAME, 'password')))
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(15)
        # ok_button = self.driver.find_element(By.TAG_NAME, "body")
        # if ok_button:
        #     ok_button.send_keys(Keys.ESCAPE)

    def find_followers(self):
        self.driver.get(f"{URL}{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers_link = self.wait.until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
        followers_link.click()
        time.sleep(2)
        modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

input("")