# coding=utf-8
import config
from DAL import requests_dal


def generate_open_requests_text(number_of_requests):
    if 0 == number_of_requests:
        return u"אין לך בקשות פתוחות. לעזרה, הקש על /help :)"
    if 1 == number_of_requests:
        return u"יש בקשה פתוחה אחת."
    else:
        return u"יש {0} בקשות פתוחות.".format(number_of_requests)


def list_requests(bot, update):
    all_open_requests = requests_dal.get_all_open_requests()

    if update.message.chat_id == config.support_chat_id:
        bot.send_message(
            chat_id=config.support_chat_id,
            text=generate_open_requests_text(len(all_open_requests)))
        for open_request in all_open_requests:
            try:
                bot.send_message(
                    chat_id=config.support_chat_id,
                    text=open_request.to_unicode(),
                    parse_mode="Markdown")
            except Exception as e:
                bot.send_message(chat_id=config.support_chat_id, text=e.message)
    else:
        my_open_requests = filter(lambda x: x.chat_id == update.message.chat.id, all_open_requests)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=generate_open_requests_text(len(my_open_requests)))
        for open_request in my_open_requests:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=open_request.to_unicode(),
                parse_mode="Markdown")
