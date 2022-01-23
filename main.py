
from config import TOKEN
import telegram
from telegram.ext import *
from requests import *
from start import *
from messagehandler import *
 


 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)

j=updater.job_queue
def once(context:  CallbackContext):
    message="what did you do yesterday man huh?"
    
    for users in dictionary.values():
        
        if users.startswith("id"):
            users=str(users[2:])
            dictionary["job"+users]=1
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







import datetime as dat
# -5 hour from my time zone
# heroku time zone is -10.5 hour from us
# bot and heroku and my timezone -5
j.run_daily(once, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=13, minute=00, second=00))
 

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer("thanks")
    global order_status

    if "yes" == query:
       

        dictionary["job"+str(update.effective_chat.id)]=dictionary["job"+str(update.effective_chat.id)]+1
        if dictionary["job"+str(update.effective_chat.id)]==2:
            j2.run_once(once2,0)
    if "yes2" == query:
        dictionary["job"+str(update.effective_chat.id)]=dictionary["job"+str(update.effective_chat.id)]+1
        if dictionary["job"+str(update.effective_chat.id)]==3:
            j3.run_once(once3,0)
    if "yes3" == query:
        text="[here](https://docs.google.com/spreadsheets/d/1vGBqxhKKlOjvNUVFVR0NHUerqVICYS_dwTHYjlr8qS8/edit#gid=974018585)"
        context.bot.send_message(chat_id=update.effective_chat.id, text="do not forget to write google sheet pls click here "+text,parse_mode="MarkdownV2")
        dictionary["job"+str(update.effective_chat.id)]=0
    if "no" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="what are you doing write faster!!!")


dispatcher.add_handler(CommandHandler("start", startCommand))

dispatcher.add_handler(CallbackQueryHandler(queryHandler))

dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
updater.idle()
