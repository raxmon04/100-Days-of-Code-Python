from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)

# Navigate to the (fake) newsletter registration page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Ramon")
last_name.send_keys("Peter")
email.send_keys("ramon.peter@gmail.com")

# Locate the "Sign Up" button. The click on it
sign_up = driver.find_element(By.CSS_SELECTOR, value=".btn")
sign_up.send_keys(Keys.ENTER)

#Keep the Browser opened
input("Browser offen lassen... Enter drücken zum Schliessen.")