import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from start import *
from messagehandler import *
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)




 
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(
    Filters.text, messageHandler))
updater.start_polling()