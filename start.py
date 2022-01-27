from pickle import TRUE
from telegram import *
from telegram.ext import *
from requests import *
from messagehandler import dictionary
 






def startCommand(update: Update, context: CallbackContext):
    name = update.effective_chat.full_name
    dictionary[str(update.effective_chat.id)]="id"+str(update.effective_chat.id)
    dictionary["progress"+str(update.effective_chat.id)]="progress from yesterday 📅:"
    dictionary["plan"+str(update.effective_chat.id)]="today's plan 📝:"
    dictionary["stuck"+str(update.effective_chat.id)]="stucks 🥵:"
    dictionary["job"+str(update.effective_chat.id)]="0"
    dictionary["time"+str(update.effective_chat.id)]="time when he answered🕒:"
    dictionary["phone"+str(update.effective_chat.id)]=""
 
    buttons = [[KeyboardButton("Press Here",request_contact=True)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Hello  {update.effective_chat.full_name } 👋 welcome to my bot. I will send you notification at certain time⏲, please share your contact.",reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

 

 