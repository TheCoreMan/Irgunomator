import config
import requests_dal
from handlers.unknown import unknown


def support(bot, update, args):
    """
        Sends the support message. Some kind of "How can I help you?".
    """
    support_request = ' '.join(args)
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


def support_message(bot, update):
    """
        Receives a message from the user.

        If the message is a reply to the user, the bot speaks with the user
        sending the message content. If the message is a request from the user,
        the bot forwards the message to the support group.
    """
    if update.message.reply_to_message:
        req_id = update.message.reply_to_message.text.split('\n')[0]
        req = requests_dal.get_request(req_id)
        req.append_message(update.message.text)
        bot.send_message(chat_id=req._creator,
                         text=update.message.text)
        req.save()
    else:
        return unknown(bot, update)
