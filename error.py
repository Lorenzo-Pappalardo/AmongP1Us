from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler


def print_error(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        text=update.message.text + " non è un comando valido!")
    return ConversationHandler.END
