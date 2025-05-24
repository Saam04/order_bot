from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def start_driver():
    options = Options()
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
   # options.add_argument("profile-directory=Default")  # Or your custom profile
    options.add_argument("--start-maximized")  # Or your custom profile
    options.add_argument("--disable-extensions")  # Or your custom profile
    options.add_argument("--no-sandbox")  # Or your custom profile
    options.add_argument("--disable-dev-shm-usage")  # Or your custom profile

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    #driver.get("https://web.whatsapp.com")
    print("Chrome & WhatsApp both are automated and set")
    time.sleep(10)  # Time for manual login (or skip if already logged in)

    return driver

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service,)
driver.get("https://web.whatsapp.com")
