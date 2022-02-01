from messagehandler  import dictionary
from telegram.ext import *
from telegram import *
from requests import *


def getContact(update: Update, context: CallbackContext):
            
                
            context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks, please wait",reply_markup=ReplyKeyboardRemove())
            print(update.message.contact.phone_number)
            dictionary["phone"+str(update.effective_chat.id)]="number☎️: "+update.message.contact.phone_number

            dictionary["job"+str(update.effective_chat.id)]="0"




