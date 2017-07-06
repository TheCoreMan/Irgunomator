import config
from DAL import requests_dal
import messages


def new_request(bot, update):
    support_request = update.message.text
    request_id = update.update_id

    request = requests_dal.Request(update.message, request_id)
    request.append_message(support_request)
    request.save()

    bot.send_message(
        chat_id=config.support_chat_id,
        text=request.to_unicode(),
        parse_mode="Markdown")

    user_message_text = messages.NEW_REQUEST_CREATED.format(support_request)
    bot.send_message(chat_id=update.message.chat_id,
                     text=user_message_text)
