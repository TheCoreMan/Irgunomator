import requests_dal
import telegram
import config


def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Hello!\n"
    msg += "I'm {0} and I came here to help you.\n".format(me.first_name)
    msg += "What would you like to do?\n\n"
    msg += "/support - Opens a new support ticket\n"
    msg += "/list - Lists all open requests\n"
    msg += "/help - Shows this help menu :)\n"

    # Commands menu
    main_menu_keyboard = [
        [telegram.KeyboardButton('/support')],
        [telegram.KeyboardButton('/list')],
        [telegram.KeyboardButton('/help')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(
        main_menu_keyboard,
        resize_keyboard=True,
        one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


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


def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = "Sorry, I don't know what you're asking for."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def show_requests(bot, update):
    all_open_requests = requests_dal.get_all_open_requests()
    if update.message.chat_id == config.support_chat_id:
        bot.send_message(
            chat_id=config.support_chat_id,
            text="There are {0} open requests".format(len(all_open_requests)))
        for open_request in all_open_requests:
            bot.send_message(chat_id=config.support_chat_id, text=repr(open_request))
    else:
        my_open_requests = filter(lambda x: x._creator == update.message.chat.id, all_open_requests)
        bot.send_message(
            chat_id=update.message.chat_id,
            text="There are {0} open requests".format(len(my_open_requests)))
        for open_request in my_open_requests:
            bot.send_message(chat_id=update.message.chat_id, text=repr(open_request))


def close_request(bot, update):
    return unknown(bot, update)


def show_single_request(bot, update):
    return unknown(bot, update)
