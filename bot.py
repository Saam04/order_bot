from commands import handle_command
import time

if __name__ == "__main__":
    print("🤖 Order Bot is live! Type a command:")
    while True:
        user_input = input(">>> ")
        handle_command(user_input)
        time.sleep(2)
