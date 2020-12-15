from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from config import colors


def get_tasks(update: Update, context: CallbackContext) -> None:
    color = update.message.text

    keyboard = [[]]

    for task in colors.get(color):
        keyboard.append(
            [KeyboardButton(task, callback_data=color + '/' + task)])

    buttons = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
        text="Tasks del team " + color, reply_markup=buttons)
