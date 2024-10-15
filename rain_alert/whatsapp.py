import os
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setup Chrome options for headless mode
chrome_options = Options()
current_directory = os.getcwd()
chrome_options.add_argument(f"user-data-dir={current_directory}/../User Data")
chrome_options.add_argument("profile-directory=Profile 4")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def send_whatsapp_msg(phone, message):
    try:
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # URL-encode the message to handle spaces and special characters
        encoded_message = urllib.parse.quote(message)

        phone_number = phone
        whatsapp_url = f"https://wa.me/{phone_number}/?text={encoded_message}&app_absent=1"

        driver.get(whatsapp_url)

        # Wait for the message page to load
        time.sleep(10)

        # Click on the button to open WhatsApp Web if needed
        openWebButton = driver.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a')
        openWebButton.click()
        time.sleep(10)

        # Click the 'Send' button
        send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]')
        send_button.click()

        # Simulate pressing the Enter key
        send_button.send_keys(Keys.ENTER)

        print("Message sent!")

        # Close the browser
        driver.quit()
    except Exception as e:
        print("An error occurred: ", str(e))

send_whatsapp_msg("201157000509", "Hello, this is a test message!")