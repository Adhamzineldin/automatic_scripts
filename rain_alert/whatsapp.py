import os
import time
import urllib.parse


from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Setup Chrome options for headless mode
chrome_options = Options()
current_directory = os.getcwd()
chrome_options.add_argument(f"user-data-dir={current_directory}/User Data")
chrome_options.add_argument("profile-directory=Profile 4")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Required for some environments
chrome_options.add_argument("--disable-dev-shm-usage")

def send_whatsapp_msg(phone, message):
    print("Sending WhatsApp message...")
    print(message)
    try:
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # URL-encode the message to handle spaces and special characters

        html_source = driver.page_source
        print(html_source)

        encoded_message = urllib.parse.quote(message)
        phone_number = phone
        whatsapp_url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"
        driver.get(whatsapp_url)

        time.sleep(30)

        # Click the 'Send' button
        send_button = driver.find_element(By.CSS_SELECTOR, '#main > footer > div.x1n2onr6.xhtitgo.x9f619.x78zum5.x1q0g3np.xuk3077.x193iq5w.x122xwht.x1bmpntp.xs9asl8.x1swvt13.x1pi30zi.xnpuxes.copyable-area > div > span > div > div._ak1r > div.x9f619.x12lumcd.x1qrby5j.xeuugli.xisnujt.x6prxxf.x1fcty0u.x1fc57z9.xe7vic5.x1716072.xgde2yp.x89wmna.xbjl0o0.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1a2a7pz.x13w7htt.x78zum5.x96k8nx.xdvlbce.x1ye3gou.xn6708d.x1ok221b.xu06os2.x1i64zmx.x1emribx > div > div > p')
        send_button.send_keys(Keys.ENTER)
        time.sleep(5)
        print("Message sent!")

        # Close the browser
        driver.quit()
    except Exception as e:
        print("An error occurred: ", str(e))

send_whatsapp_msg("201157000509", "niggerrrrrrrrrrrrrrr")