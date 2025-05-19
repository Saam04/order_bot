from selenium.webdriver.common.by import By
import time

def send_group_message(driver, group_name, message):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(15)

    group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
    group.click()
    time.sleep(15)

    input_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    input_box.send_keys(message)
    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()
    print(f"Sent message to {group_name}: {message}")
