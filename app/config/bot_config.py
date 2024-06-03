from dotenv import load_dotenv
import telebot
import os

load_dotenv('.env')


def get_token():
    return os.environ.get('BOT_TOKEN', 'Nada')


BOT = telebot.TeleBot(get_token())
