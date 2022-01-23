from telegram import *
from telegram.ext import *
from requests import *
from messagehandler import dictionary
 






def startCommand(update: Update, context: CallbackContext):
    name = update.effective_chat.full_name
    dictionary[str(update.effective_chat.id)]="id"+str(update.effective_chat.id)
    dictionary["job"+str(update.effective_chat.id)]=0
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Hello {update.effective_chat.full_name } welcome to my bot. I will send you notification at certain time and your answer will be send to reponsible man so be careful when you write smth :)")

 

 