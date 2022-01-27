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
    message="what did you do yesterday man huh 🧐 ?"
    
    for users in dictionary.values():
        
        if users.startswith("id"):
            users=str(users[2:])
            dictionary["job"+users]="1"
            print(users)
            if dictionary["phone"+users]!="":
                context.bot.send_message(chat_id=users, text=message)

 
import datetime as dat
# -5 hour from my time zone
# heroku time zone is -10.5 hour from us
# bot and heroku and my timezone -5
j.run_daily(once, days=(0, 1, 2, 3, 4, 5, 6), time=dat.time(hour=13, minute=00, second=00))
 

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer("thanks😀")
    global order_status

    if "yes" == query:
        update.effective_message.edit_reply_markup(None)
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=dictionary["delete"+str(update.effective_chat.id)])
        dictionary["job"+str(update.effective_chat.id)]="2"
        print(dictionary["progress"+str(update.effective_chat.id)])
       
     


        context.bot.send_message(chat_id=update.effective_chat.id, text="what will you do today 🤠")
    if "yes2" == query:
        update.effective_message.edit_reply_markup(None)
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=dictionary["delete"+str(update.effective_chat.id)])
        dictionary["job"+str(update.effective_chat.id)]="3"
  
        context.bot.send_message(chat_id=update.effective_chat.id, text="do you have any stucks 🤒?")
    if "yes3" == query:
        update.effective_message.edit_reply_markup(None)
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=dictionary["delete"+str(update.effective_chat.id)])
        text="[here](https://docs.google.com/spreadsheets/d/1vGBqxhKKlOjvNUVFVR0NHUerqVICYS_dwTHYjlr8qS8/edit)"
        context.bot.send_message(chat_id=update.effective_chat.id, text="do not forget to write google sheet pls click here 👉 "+text,parse_mode="MarkdownV2")
        dictionary["job"+str(update.effective_chat.id)]="0"
        time=dictionary["time"+str(update.effective_chat.id)]+" "+str(datetime.now() + timedelta(hours=5))[:16]
        a="name🤵: "+update.effective_chat.full_name+"\n"+ dictionary["progress"+str(update.effective_chat.id)] +"\n"+dictionary["plan"+str(update.effective_chat.id)] +"\n"+dictionary["stuck"+str(update.effective_chat.id)]+"\n"+time+"\n"+dictionary["phone"+str(update.effective_chat.id)]

        telegram_api_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{telegram_group_id}&text={a}"
        tel_resp=requests.get(telegram_api_url)
       
        if tel_resp.status_code==200:
            print("sent")
        else:
            print("error")
        dictionary["progress"+str(update.effective_chat.id)]="progress from yesterday 📅:"
        dictionary["plan"+str(update.effective_chat.id)]="today's plan 📝:"
        dictionary["stuck"+str(update.effective_chat.id)]="stucks 🥵:"
        dictionary["time"+str(update.effective_chat.id)]="time when he answered🕒:"
        print(dictionary)
   
    if "no" in query:
        update.effective_message.edit_reply_markup(None)
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=dictionary["delete"+str(update.effective_chat.id)])
        context.bot.send_message(chat_id=update.effective_chat.id, text="what are you doing write faster 🥱!!!")


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.contact, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
updater.idle()
