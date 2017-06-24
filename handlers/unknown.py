def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = u"Sorry, I don't know what you're asking for.\nUse /help to see what I can do!"
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)
