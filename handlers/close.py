# coding=utf-8
import humanize

import config
from DAL import requests_dal


def close(bot, update):
    request_id = update.message.reply_to_message.text.split('\n')[0]
    request = requests_dal.get_request(request_id)
    requests_dal.close_request(request_id)

    close_message_text = u"""הבקשה הבאה נסגרה ✅:
{0}

_הבקשה טופלה תוך {1}_
""".format(
        request.to_unicode(),
        humanize.naturaldelta(update.message.date - request.creation_time))
    bot.send_message(chat_id=request.chat_id, text=close_message_text, parse_mode="Markdown")
    bot.send_message(chat_id=config.support_chat_id, text=close_message_text, parse_mode="Markdown")
