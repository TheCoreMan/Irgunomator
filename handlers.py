import requests_dal
import telegram
from config import config


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

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/support')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)
    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


def support(bot, update):
    """
        Sends the support message. Some kind of "How can I help you?".
    """
    bot.send_message(chat_id=update.message.chat_id,
                     text="Please, tell me what you need support with :)")


def support_message(bot, update):
    """
        Receives a message from the user.

        If the message is a reply to the user, the bot speaks with the user
        sending the message content. If the message is a request from the user,
        the bot forwards the message to the support group.
    """
    if update.message.reply_to_message:
        # If it is a reply to the user, the bot replies the user
        req_id = update.message.reply_to_message.text.split('\n')[0]
        req = requests_dal.get_request(req_id)
        bot.send_message(chat_id=req._creator,
                         text=update.message.text)
    else:
        # If it is a request from the user, the bot forwards the message
        # to the group
        new_request = requests_dal.Request(update.message, update.update_id)
        new_request.save()
        new_text = "{0}\n{1}".format(update.update_id, update.message.text)
        bot.send_message(
            chat_id=int(config['DEFAULT']['support_chat_id']),
            text=new_text)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Give me some time to think. Soon I will return to you with an answer.")


def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = "Sorry, I don't know what you're asking for."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def show_requests(bot, update):
    return unknown(bot, update)


def close_request(bot, update):
    return unknown(bot, update)


def show_single_request(bot, update):
    return unknown(bot, update)
