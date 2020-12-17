from telegram import Update
from telegram.ext import CallbackContext


def xD(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='xD')
