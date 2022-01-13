from telegram import *
from telegram.ext import *
from requests import *
import requests
from datetime import datetime
 
dictionary=dict()

raw_IS= datetime.now()
curr_date=raw_IS.strftime("%d-%m-%Y")
curr_time=raw_IS.strftime("%H:%M:%S")

from  config  import TOKEN
telegram_group_id="MAAB_Stand_Up"





def messageHandler(update: Update, context: CallbackContext):
    if update.message.text!="":
        dictionary[update.effective_chat.id]=str(update.message.text)+"\n"+str(curr_date)+" " +str(curr_time)+"\n"+ str(update.effective_chat.full_name)
        buttons = [[KeyboardButton("Suggestions")], [KeyboardButton("Delete old Queue")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="okey thanks, do you have any stucks?",
                                 reply_markup=ReplyKeyboardMarkup(buttons))
        print(dictionary)
        telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={dictionary[update.effective_chat.id]}"
        tel_resp=requests.get(telegram_api_url)

        if tel_resp.status_code==200:
            print("sent")
        else:
            print("error")

        

        

        







