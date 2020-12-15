from telegram import Update
from telegram.ext import CallbackContext


def xD(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='xD')
