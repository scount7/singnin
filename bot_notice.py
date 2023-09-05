from telegram.ext import Updater
from sys import argv

def notice():
    TOKEN = argv[1]
    CHAT_ID = argv[2]
    with open("result.txt", mode="r", encoding="utf-8") as f:
        res = f.read()
    myBot = Updater(TOKEN)
    myBot.bot.send_message(
        chat_id = int(CHAT_ID),
        text = res
    )
    print("notice sent successfully.")

if __name__ == "__main__":
    notice()