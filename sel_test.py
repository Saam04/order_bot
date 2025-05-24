from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://whatsapp.com")
print("Instagram is opened")

time.sleep(15)

driver.quit()
