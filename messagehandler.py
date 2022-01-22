from telegram import *
from telegram.ext import *
from requests import *
import requests
from datetime import datetime
from  config  import TOKEN
 


dictionary=dict()
raw_IS= datetime.now()
curr_date=raw_IS.strftime("%d-%m-%Y")
curr_time=raw_IS.strftime("%H:%M:%S")
telegram_group_id="MAAB_Stand_Up"
 





def messageHandler(update: Update, context: CallbackContext):
    if update.message.text!="":
        dictionary[update.effective_chat.id]=str(update.message.text)+"\n"+str(curr_date)+" " +str(curr_time)+"\n"+ str(update.effective_chat.full_name)
    #      buttons = [[InlineKeyboardButton("Yes", callback_data="Yes")], 
    #    [InlineKeyboardButton("No", callback_data="No")]]
    #     context.bot.send_message(chat_id=update.effective_chat.id,
    #                              reply_markup=InlineKeyboardMarkup(buttons), text="okey thanks, do you have any stucks?")
        context.bot.send_message(chat_id=update.effective_chat.id,text="sorry man I can not understand you :(")
        print(dictionary)
        telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={dictionary[update.effective_chat.id]}"
        tel_resp=requests.get(telegram_api_url)

        if tel_resp.status_code==200:
            print("sent")
        else:
            print("error")

        print(update.message.text)


        

        

        







