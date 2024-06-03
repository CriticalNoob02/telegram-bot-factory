from config import BOT
from utils import LOG
from telebot.types import Message


@BOT.message_handler(func=lambda message: True)
def send_default_message(message):
    LOG.debug("🛞 Run: default")
    BOT.reply_to(message, "Comando não identificado...")
    print(BOT.get_my_commands())
