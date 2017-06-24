import messages

def new_request(message):
    return (message.reply_to_message is not None) and \
           message.reply_to_message.text == messages.ASK_FOR_NEW_REQUEST
