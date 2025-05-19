from whatsapp_driver import start_driver
from listener import get_last_group_message
from responder import send_group_message
import time

GROUP_NAME = "Family Orders"

def run_bot():
    driver = start_driver()
    orders = []

    while True:
        last_msg = get_last_group_message(driver, GROUP_NAME)

        if last_msg.startswith("#add"):
            item = last_msg.replace("#add", "").strip()
            orders.append(item)
            send_group_message(driver, GROUP_NAME, f" Added: {item}")

        elif last_msg.startswith("#delete"):
            item = last_msg.replace("#delete", "").strip()
            if item in orders:
                orders.remove(item)
                send_group_message(driver, GROUP_NAME, f" Deleted: {item}")
            else:
                send_group_message(driver, GROUP_NAME, f" Item not found: {item}")

        elif last_msg.startswith("#list"):
            if orders:
                order_list = "\n".join(f"- {o}" for o in orders)
                send_group_message(driver, GROUP_NAME, f" Current Orders:\n{order_list}")
            else:
                send_group_message(driver, GROUP_NAME, " No items in the order list.")

        time.sleep(100)  # Polling interval (adjust if needed)

if __name__ == "__main__":
    run_bot()
