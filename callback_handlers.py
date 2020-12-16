from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, ConversationHandler

from config import colors_tasks

COLOR, TASKS = range(2)


def greetings(update: Update, context: CallbackContext) -> int:
    keyboard = [[]]

    for color in colors_tasks:
        keyboard.append([InlineKeyboardButton(color, callback_data=color)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Ciao! A quale team appartieni? 👇🏻", reply_markup=reply_markup)
    return COLOR


def color_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query

    keyboard = [[]]

    for task in colors_tasks.get(query.data):
        keyboard.append([InlineKeyboardButton(
            task, callback_data=query.data + '/' + task)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text="Team {}".format(
        query.data), reply_markup=reply_markup)

    return TASKS


def tasks_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query

    task_info = query.data.split('/')

    color = task_info[0]
    task = task_info[1]

    query.edit_message_text(
        text="{} - {}".format(color, task) + "\n\n" + colors_tasks.get(color).get(task))

    return ConversationHandler.END
