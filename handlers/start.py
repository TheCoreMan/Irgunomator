import telegram


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
