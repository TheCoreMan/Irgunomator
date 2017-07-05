import messages


def new_request(message):
    return (message.reply_to_message is not None) and \
           message.reply_to_message.text == messages.ASK_FOR_NEW_REQUEST


def flush_db(message):
    return (message.reply_to_message is not None) and \
           message.reply_to_message.text == messages.FLUSH_DB_ARE_YOU_SURE
