# coding=utf-8
import telegram


def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = u"""שלום!
    אני הארגונומטור ובאתי לעזור לך. 
    מה תרצה לעשות?
    
    """

    msg += u"/support - פותח בקשה חדשה לעזרה.\n"
    msg += u"/list - רושם את כל הבקשות הפתוחות.\n"
    msg += u"/help - מראה את התפריט הזה :)\n"

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
