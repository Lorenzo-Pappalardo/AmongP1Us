from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from config import colors


def greetings(update: Update, context: CallbackContext) -> None:
    keyboard = [[]]

    for color in colors:
        keyboard.append([KeyboardButton(color, callback_data=color)])

    buttons = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
        "Ciao! A quale team appartieni? 👇🏻", reply_markup=buttons)
