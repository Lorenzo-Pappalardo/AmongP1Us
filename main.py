import telegram
from telegram import Bot
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler

from config import token
from callback_handlers import greetings, color_handler, tasks_handler
from alert import alert
from easter_egg import xD
from error import print_error

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

bot = telegram.Bot(token)

updater = Updater(token)
dp = updater.dispatcher

COLOR, TASKS = range(2)

conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('start', greetings)],
    states={
        COLOR: [CallbackQueryHandler(color_handler)],
        TASKS: [CallbackQueryHandler(tasks_handler)]
    },
    fallbacks=[MessageHandler(Filters.all, print_error)]
)

dp.add_handler(conversation_handler)
dp.add_handler(CommandHandler('alert', alert))
dp.add_handler(MessageHandler(Filters.regex('xD'), xD))
dp.add_handler(MessageHandler(Filters.all, print_error))

updater.start_polling()
logging.getLogger(__name__).info("Bot started (token: " + token + ')')
updater.idle()
logging.getLogger(__name__).info("Bot stopped")
