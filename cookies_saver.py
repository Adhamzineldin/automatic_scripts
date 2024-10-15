from selenium import webdriver
import pickle
import time

# Set up Chrome options (use your default profile for login)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/mohal/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Profile 4")

# Replace with your profile path

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open WhatsApp Web manually
driver.get("https://web.whatsapp.com")

# Wait for you to scan the QR code manually and login
time.sleep(20)  # Adjust if you need more time

# Save cookies to a file after manual login
with open("whatsapp_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("Cookies saved successfully.")

# Close the browser
driver.quit()
