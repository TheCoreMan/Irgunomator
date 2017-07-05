# coding=utf-8
import inflect

import config
from DAL import requests_dal

inflection = inflect.engine()


def list_requests(bot, update):
    all_open_requests = requests_dal.get_all_open_requests()

    if update.message.chat_id == config.support_chat_id:
        bot.send_message(
            chat_id=config.support_chat_id,
            text=u"יש {0} בקשות פתוחות.".format(len(all_open_requests)))
        for open_request in all_open_requests:
            try:
                message_text = open_request.to_unicode()
                bot.send_message(chat_id=config.support_chat_id, text=message_text)
            except Exception as e:
                bot.send_message(chat_id=config.support_chat_id, text=e.message)
    else:
        my_open_requests = filter(lambda x: x.creator == update.message.chat.id, all_open_requests)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=u"You have {0} open {1}.".format(
                len(my_open_requests),
                inflection.plural(u"request", len(my_open_requests))))
        for open_request in my_open_requests:
            bot.send_message(chat_id=update.message.chat_id, text=open_request.to_unicode())
