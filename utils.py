# utils.py
import time
import logging
from telegram import Message

logging.basicConfig(level=logging.INFO, filename='chatlog.txt', format='%(asctime)s - %(message)s')

def simulate_typing_and_reply(message: Message, reply_text: str):
    chat = message.chat
    message.bot.send_chat_action(chat_id=chat.id, action="typing")
    time.sleep(min(len(reply_text) / 15, 3))  # delay max 3 sec
    message.reply_text(reply_text)

def log_message(user_id: int, username: str, text: str):
    logging.info(f"{username} ({user_id}): {text}")
