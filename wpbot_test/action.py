from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os

# Auto-match ChromeDriver version
chromedriver_autoinstaller.install()

options = Options()

user_profile=r"C:\Users\sumit\AppData\Local\Google\Chrome\User Data\Profile 7"
options.add_argument(f"--user-data-dir={user_profile}")
options.add_argument("--profile-directory=Default") 

options.add_argument('--remote-debugging-port=9222')
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#user_data_path = os.path.abspath("User_Data")
#options.add_argument(f"--user-data-dir={user_data_path}")
# Comment below during debugging if needed
# options.add_argument('--user-data-dir=./User_Data')

service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Your bot logic here
from utils.whatsapp_helper import WhatsAppBot
bot = WhatsAppBot(driver)
bot.open_whatsapp()

contacts = ["Personal"]
message = "Hello from your friendly automation bot!"
for name in contacts:
    bot.send_message(name, message)
