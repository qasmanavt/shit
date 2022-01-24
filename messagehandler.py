from telegram import *
from telegram.ext import *
from requests import *
import requests
from datetime import datetime,timedelta
from  config  import TOKEN
 


dictionary=dict() 
telegram_group_id="MAAB_Stand_Up"
 





def messageHandler(update: Update, context: CallbackContext):
    if update.message.text!="":
        if dictionary["job"+str(update.effective_chat.id)]==1:
            a="progress from yesterday : "+str(update.message.text)+"\n"+"time when he answered: "+str(datetime.now() - timedelta(hours=5))[:16]+"\n"+ "name: "+str(update.effective_chat.full_name)

            print(dictionary)
            telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={a}"
            tel_resp=requests.get(telegram_api_url)
            buttons=[[InlineKeyboardButton("yes",callback_data="yes")],[InlineKeyboardButton("no",callback_data="no")]]
            a=context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="so you did NOT forget anything from your yesterday's progress?")
            dictionary["delete"+str(update.effective_chat.id)]=a.message_id
            
            if tel_resp.status_code==200:
                print("sent")
            else:
                print("error")

            print(update.message.text)

        if dictionary["job"+str(update.effective_chat.id)]==2:
            a="today's plan : "+str(update.message.text)+"\n"+"time when he answered: "+str(datetime.now() - timedelta(hours=5))[:16]+"\n"+ "name: "+str(update.effective_chat.full_name)

            print(dictionary)
            telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={a}"
            tel_resp=requests.get(telegram_api_url)
            buttons=[[InlineKeyboardButton("yes",callback_data="yes2")],[InlineKeyboardButton("no",callback_data="no2")]]
            a=context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="are you sure?")
            dictionary["delete"+str(update.effective_chat.id)]=a.message_id
            if tel_resp.status_code==200:
                print("sent2")
            else:
                print("error2")

        if dictionary["job"+str(update.effective_chat.id)]==3:
            a="stucks : "+str(update.message.text)+"\n"+"time when he answered: "+str(datetime.now() - timedelta(hours=5))[:16]+"\n"+ "name: "+str(update.effective_chat.full_name)

            print(dictionary)
            telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={a}"
            tel_resp=requests.get(telegram_api_url)
            buttons=[[InlineKeyboardButton("yes",callback_data="yes3")],[InlineKeyboardButton("no",callback_data="no3")]]
            a=context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="soo main part is that all?")
            dictionary["delete"+str(update.effective_chat.id)]=a.message_id
            if tel_resp.status_code==200:
                print("sent2")
            else:
                print("error2")

            print(update.message.text)
        if dictionary["job"+str(update.effective_chat.id)]==0:
            context.bot.send_message(chat_id=update.effective_chat.id,text="you are already answered man why are you wasting your time go to work !!!")


        

        

        







