import telegram

import messages
import requests_dal
from handlers.unknown import unknown


def support(bot, update):
    """
        Sends the support message. Some kind of "How can I help you?".
    """
    bot.send_message(chat_id=update.message.chat_id,
                     text=messages.ASK_FOR_NEW_REQUEST,
                     reply_markup=telegram.ForceReply())


def support_message(bot, update):
    """
        Receives a message from the user.

        If the message is a reply to the user, the bot speaks with the user
        sending the message content. If the message is a request from the user,
        the bot forwards the message to the support group.
    """
    if update.message.reply_to_message:
        req_id = update.message.reply_to_message.text.split(u'\n')[0]
        req = requests_dal.get_request(req_id)
        req.append_message(update.message.text)
        bot.send_message(chat_id=req.creator,
                         text=update.message.text)
        req.save()
    else:
        return unknown(bot, update)
