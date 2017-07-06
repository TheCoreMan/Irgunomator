# coding=utf-8
import telegram

import config
import messages
from DAL.db import bot_db


def flush_db(bot, update):
    if update.message.chat_id != config.support_chat_id:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=messages.FLUSH_DB_UNAUTHORISED)
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=messages.FLUSH_DB_ARE_YOU_SURE,
            reply_markup=telegram.ForceReply())


def flush_db_reply(bot, update):
    if update.message.text == "Y":
        bot.send_message(chat_id=config.support_chat_id, text="FLUSHING DB...")
        bot_db.flushdb()
        bot.send_message(chat_id=config.support_chat_id, text="DB FLUSHED. TESTING...")
        keys = bot_db.keys("*")
        bot.send_message(chat_id=config.support_chat_id, text="DB FLUSHED. NUMBER OF KEYS: {0}".format(len(keys)))
    else:
        bot.send_message(chat_id=config.support_chat_id, text="ABORTING.")
