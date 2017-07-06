# coding=utf-8
import telegram
from tabulate import tabulate


def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    # Welcome message

    msg = u"""שלום!
אני הארגונומטור ובאתי לעזור לך. 💪
מה תרצה לעשות?

    💬 /support 
    📓 /list 
    🏆 /leaderboards
    ❓ /help 
    
    הסבר על כל אחת מן הפעולות שאני יודע לעשות:
```
"""

    msg += tabulate(
        [
            [u"/support", u"פותח בקשה חדשה לעזרה."],
            [u"/list", u"רושם את כל הבקשות הפתוחות."],
            [u"/leaderboards", u"מראה מי מוביל בפתיחת הודעות."],
            [u"/help", u"מראה את ההודעה הזו."]
        ], tablefmt="simple")
    msg += u"```"
    # Commands menu
    main_menu_keyboard = [
        [telegram.KeyboardButton('/support')],
        [telegram.KeyboardButton('/list')],
        [telegram.KeyboardButton('/leaderboards')],
        [telegram.KeyboardButton('/help')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(
        main_menu_keyboard,
        resize_keyboard=True,
        one_time_keyboard=False)

    # Send the message with menu
    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        reply_markup=reply_kb_markup,
        parse_mode="Markdown")
