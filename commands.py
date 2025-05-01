from storage import load_orders, save_orders
import pywhatkit
from datetime import datetime

GROUP_ID = "Family Orders"

def send_to_group(message):
    try:
        print(f"Sending to group: (GROUP_ID)")
        pywhatkit.sendwhatmsg_to_group_instantly(GROUP_ID, message, wait_time=15, tab_close=True)
    except Exception as e:
        print("Failed to send message: (e)")

def handle_command(command: str):
    orders = load_orders()
    cmd = command.strip()

    if cmd.startswith("#add "):
        item = cmd[5:].strip()
        orders.append(item)
        save_orders(orders)
        send_to_group(f"✅ Added: {item}")

    elif cmd.startswith("#delete "):
        item = cmd[8:].strip()
        if item in orders:
            orders.remove(item)
            save_orders(orders)
            send_to_group(f"❌ Deleted: {item}")
        else:
            send_to_group(f"⚠️ Item not found: {item}")

    elif cmd == "#list":
        if orders:
            msg = "**📝 Order List:**\n" + "\n".join([f"{i+1}. {item}" for i, item in enumerate(orders)])
        else:
            msg = "📭 Order list is empty."
        send_to_group(msg)

    elif cmd == "#clear":
        orders.clear()
        save_orders(orders)
        send_to_group("🧹 Order list cleared.")

    elif cmd == "#undo":
        if orders:
            removed = orders.pop()
            save_orders(orders)
            send_to_group(f"↩️ Removed last item: {removed}")
        else:
            send_to_group("⚠️ Nothing to undo.")

    else:
        send_to_group("❓ Unknown command. Try #add, #list, #delete, #clear, or #undo.")
