from cgitb import text
import imp
from requests import *
from telegram import *
from telegram.ext import *
 
 
 
 


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer(query)
    global order_status

    if "Yes" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="please write to BackUP group to get help!")
    if "No" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="thanks! man")