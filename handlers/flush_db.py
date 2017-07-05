# coding=utf-8
import telegram

import config
import messages
from DAL.db import bot_db as db


def flush_db(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=messages.FLUSH_DB_ARE_YOU_SURE,
        reply_markup=telegram.ForceReply())


def flush_db_reply(bot, update):
    if update.message.text == "Y":
        bot.send_message(chat_id=config.support_chat_id, text="FLUSHING DB...")
        db.flushdb()
        bot.send_message(chat_id=config.support_chat_id, text="DB FLUSHED.")
