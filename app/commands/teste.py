from config import BOT
from utils import LOG
from telebot.types import Message

@BOT.message_handler(commands=['teste'])

def get_teste(message: Message) -> None:
    LOG.debug("🛞 Run: teste")
    BOT.reply_to(message, "Edite seu comando!")
