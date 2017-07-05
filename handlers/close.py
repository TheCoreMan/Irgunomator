# coding=utf-8
import config
from DAL import requests_dal


def close(bot, update):
    request_id = update.message.reply_to_message.text.split('\n')[0]
    request = requests_dal.get_request(request_id)
    requests_dal.close_request(request_id)

    close_message_text = u"The following Request was closed ✅:\n{0}".format(repr(request))
    bot.send_message(chat_id=request.creator, text=close_message_text)
    bot.send_message(chat_id=config.support_chat_id, text=close_message_text)
