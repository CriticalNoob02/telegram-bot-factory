from config import BOT
from utils import LOG
from telebot.types import Message


@BOT.message_handler(commands=['start'])
def get_welcome(message: Message) -> None:
    LOG.debug("🛞 Run: start")
    BOT.reply_to(message, "Bot ta ligadaço maluko, lança as brabas aee!")
