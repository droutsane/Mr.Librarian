import database1
import database2
import database3


from telegram.ext import Updater
updater = Updater(token='5345156986:AAE3nrt2_XHks655fazgDHqjdkN98cojmzs', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register(update: Update, context: CallbackContext):
  user = update.message.from_user
  x = user['username']
  print(x)
  
  details = context.args
  print(details[0] +' '+ details[1])
  context.bot.send_message(chat_id= update.effective_chat.id, text=x + " you are registered with the bot, check available services by typing /help")
  database1.register(x,details[0],details[1])
  
def addbook(update: Update, context: CallbackContext):
  add = context.args
  database2.add_book(add[0], add[1], add[2], add[3])
  context.bot.send_message(chat_id= update.effective_chat.id, text=" book added...")


def status(update: Update, context: CallbackContext):
  user = update.message.from_user
  x = user['username']
  context.bot.send_message(chat_id=update.effective_chat.id, text=database3.status(x))

def search_code(update: Update, context: CallbackContext):
     context.bot.send_message(chat_id=update.effective_chat.id, 
     text="searching...")
     srch_bk_cd = context.args
     context.bot.send_message(chat_id=update.effective_chat.id, text=database2.search_code(srch_bk_cd) )

def search_key(update: Update, context: CallbackContext):
     context.bot.send_message(chat_id=update.effective_chat.id, 
     text="searching...")
     srch_bk_ky = context.args
     
  
     context.bot.send_message(chat_id=update.effective_chat.id, text=database2.search_name(srch_bk_ky))

def issue_lib(update: Update, context: CallbackContext):
     context.bot.send_message(chat_id=update.effective_chat.id, text="book issued, check /status for details")
     user = update.message.from_user
     x = user['username']
     details = context.args
     database3.add_record(x, details[0], details[1])

def issue_p2p(update: Update, context: CallbackContext):
     bookcode = context.args
     user = update.message.from_user
     x = user['username']
     context.bot.send_message(chat_id=update.effective_chat.id, text="have you received book? type yes/no")
     conf = update.message.text
  
     print(conf[11:])
     if conf[11:] == 'yes':
       context.bot.send_message(chat_id=update.effective_chat.id, text="have you received book? type yes/no")
      #database3.add_record(x, bookcode[0], "ytr")

  
  


from telegram.ext import CommandHandler
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


register_handler = CommandHandler('register', register)
dispatcher.add_handler(register_handler)

status_handler = CommandHandler('status', status)
dispatcher.add_handler(status_handler)

search_code_handler = CommandHandler('search_code', search_code)
dispatcher.add_handler(search_code_handler)

search_key_handler = CommandHandler('search_key', search_key)
dispatcher.add_handler(search_key_handler)

issue_lib_handler = CommandHandler('issue_lib', issue_lib)
dispatcher.add_handler(issue_lib_handler)

issue_p2p_handler = CommandHandler('issue_p2p', issue_p2p)
dispatcher.add_handler(issue_p2p_handler)

addbook_handler = CommandHandler('addbook', addbook)
dispatcher.add_handler(addbook_handler)

updater.start_polling()
