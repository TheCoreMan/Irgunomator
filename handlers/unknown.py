# coding=utf-8
def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = u"סליחה, אבל לא הבנתי מה ביקשת.\nאולי שימוש ב /help יעזור?"
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)
