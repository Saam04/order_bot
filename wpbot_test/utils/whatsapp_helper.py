from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class WhatsAppBot:
    def __init__(self, driver):
        self.driver = driver

    def open_whatsapp(self):
        self.driver.get("https://web.whatsapp.com/")
        print("Scan QR Code to log in.")
        time.sleep(15)  # Time to scan QR manually (can be increased)

    def send_message(self, contact_name, message):
        try:
            # Search for the contact
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            ) 
            search_box.clear()
            search_box.send_keys(contact_name)

            #time.sleep(2)
            contact = WebDriverWait(self.driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, f'//span[@title="{contact_name}"]'))
            )
            contact.click()

            wait = WebDriverWait(self.driver, 20)

            msg_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')))
            msg_box.click()
            time.sleep(0.5)

            # Send the message
            #msg_box = WebDriverWait(self.driver, 20).until(
             #   EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            #)
            msg_box.send_keys(message + '\n')
            print(f"Message sent to {contact_name}")
        except Exception as e:
            print(f"Failed to send message to {contact_name}: {e}")


