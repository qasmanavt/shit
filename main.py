
from config import TOKEN
import telegram
from telegram.ext import *
from requests import *
from start import *
from messagehandler import *
from queryhandler import *
import datetime as dt

 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)

j=updater.job_queue
def once(context:  CallbackContext):
    message="what did you do yesterday man huh?"
    for users in dictionary.values():
        
        if users.startswith("id"):
            users=str(users[2:])
            print(users)
            context.bot.send_message(chat_id=users, text=message)



 


j2=updater.job_queue
def once2(context:  CallbackContext):
    message="what will you do today man huh?"
    for users in dictionary.values():
        
        if users.startswith("id"):
            users=str(users[2:])
            print(users)
            context.bot.send_message(chat_id=users, text=message)


j3=updater.job_queue
def once3(context:  CallbackContext):
    message="do you have any stucks man huh?"
    for users in dictionary.values():
        
        if users.startswith("id"):
            users=str(users[2:])
            print(users)
            context.bot.send_message(chat_id=users, text=message)



 
dispatcher.add_handler(CommandHandler("start", startCommand))

dispatcher.add_handler(CallbackQueryHandler(queryHandler))

dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


import datetime as dat
# -5 hour from my time zone
j.run_daily(once, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=19, minute=21, second=00))
j2.run_daily(once2, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=19, minute=22, second=00))
j2.run_daily(once3, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=19, minute=23, second=00))


updater.start_polling()
updater.idle()
