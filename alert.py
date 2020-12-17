from telegram import Update
from telegram.ext import CallbackContext


def alert(update: Update, context: CallbackContext) -> None:
    update.message.reply_sticker(
        "CAACAgEAAxkBAAICXV_bkqRBoWGNeZnvtKS1EGwvjp8zAAJGAAOeM5wf2h0che1-Ca8eBA")
