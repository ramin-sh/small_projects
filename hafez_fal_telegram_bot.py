from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler
from telegram.ext.filters import Filters


def fal(bot,update):
    rand = random.randrange(1,495)
    response = requests.get("https://api.codebazan.ir/ghazaliyathafez/?type=all&id=%i"%(rand))
    txt = response.json()['perception']
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,txt)
    
def main():
  updater = Updater('your token here')
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('fal',fal))
  updater.start_polling()
  updater.idle()
  
if __name__ == '__main__':
    main()
