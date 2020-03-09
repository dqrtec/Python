import telegram
import dolar as ut
from telegram.ext import Updater , CommandHandler, MessageHandler, Filters

my_token = ""

bot = telegram.Bot(token=my_token)

def start(bot,update):
	update.message.reply_text("allons-y!")

updater = Updater(my_token)

dp = updater.dispatcher
#
def pay(bot,update):
	update.message.reply_text("pagamento efetuado!")
#
def error(bot,update,error):
	print(error)

#
def dolar(bot,update):
	dolar = ut.getDolar()
	update.message.reply_text("Cotação de hoje:{}".format(dolar))
	
#
dp.add_handler(CommandHandler("dolar",dolar))

dp.add_handler(CommandHandler("start",start))

dp.add_error_handler(error)

updater.start_polling()

updater.idle()