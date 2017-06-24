from telegram.ext import filters

import messages


class NewRequestFilter(filters.BaseFilter):
    name = 'NewRequestFilter'

    def filter(self, message):
        return (message.reply_to_message is not None) and \
               message.reply_to_message.text == messages.ASK_FOR_NEW_REQUEST
