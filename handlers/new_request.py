import config
from DAL import requests_dal


def new_request(bot, update):
    support_request = update.message.text
    request_id = update.update_id

    new_request = requests_dal.Request(update.message, request_id)
    new_request.append_message(support_request)
    new_request.save()

    support_chat_message_text = "{0}\n{1}".format(request_id, support_request)
    bot.send_message(
        chat_id=int(config.config['DEFAULT']['support_chat_id']),
        text=support_chat_message_text)

    user_message_text = "Received new request:\n{0}".format(support_request)
    bot.send_message(chat_id=update.message.chat_id,
                     text=user_message_text)
