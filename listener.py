from selenium.webdriver.common.by import By
import time

def get_last_group_message(driver, group_name):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(2)

    group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
    group.click()
    time.sleep(2)

    messages = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
    last_msg = messages[-1].text if messages else ""
    print(f"🔍 Last message in {group_name}: {last_msg}")
    return last_msg
