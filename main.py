import telegram
from telegram import Bot
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackQueryHandler

from config import token, colors
from start import greetings
from tasks import get_tasks
from easter_egg import xD

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

bot = telegram.Bot(token)

updater = Updater(token)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', greetings))
for color in colors:
    dp.add_handler(MessageHandler(Filters.regex(color), get_tasks))
dp.add_handler(MessageHandler(Filters.regex('xD'), xD))
dp.add_handler(MessageHandler(Filters.all, get_tasks))

updater.start_polling()
logging.getLogger(__name__).info("Bot started (token: " + token + ')')
updater.idle()
logging.getLogger(__name__).info("Bot stopped")
