import requests
from config import TOKEN
import telegram
from telegram.ext import *


 
 


 
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)
telegram_group_id="gufghiufgb"
j=updater.job_queue
def once(context:  CallbackContext):
 
    telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text=sheeeeeeeeeeeeeeeeeeeeeeeet"
    tel_resp=requests.get(telegram_api_url)
       
    if tel_resp.status_code==200:
        print("sent")
    else:
        print("error")

def once2(context:  CallbackContext):
 
    telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text=agaaain sheet"
    tel_resp=requests.get(telegram_api_url)
       
    if tel_resp.status_code==200:
        print("sent")
    else:
        print("error")

def once3(context:  CallbackContext):
 
    telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text=oyliq manga kkmi ya sangami?"
    tel_resp=requests.get(telegram_api_url)
       
    if tel_resp.status_code==200:
        print("sent")
    else:
        print("error")
 
import datetime as dat
# -5 hour from my time zone
# heroku time zone is -10.5 hour from us
# bot and heroku and my timezone -5

j.run_daily(once, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=14, minute=00, second=00))
j.run_daily(once2, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=15, minute=00, second=00))
j.run_daily(once3, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=22, minute=00, second=00))

updater.start_polling()
updater.idle()
