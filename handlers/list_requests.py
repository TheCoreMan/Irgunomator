import inflect

import config
from DAL import requests_dal

inflection = inflect.engine()


def list_requests(bot, update):
    all_open_requests = requests_dal.get_all_open_requests()

    if update.message.chat_id == config.support_chat_id:
        bot.send_message(
            chat_id=config.support_chat_id,
            text=u"There are {0} open {1}.".format(
                len(all_open_requests),
                inflection.plural(u"request", len(all_open_requests))))
        for open_request in all_open_requests:
            bot.send_message(chat_id=config.support_chat_id, text=repr(open_request))
    else:
        my_open_requests = filter(lambda x: x.creator == update.message.chat.id, all_open_requests)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=u"You have {0} open {1}.".format(
                len(my_open_requests),
                inflection.plural(u"request", len(my_open_requests))))
        for open_request in my_open_requests:
            bot.send_message(chat_id=update.message.chat_id, text=repr(open_request))