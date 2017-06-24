from telegram.ext import Filters

import messages


class NewRequestFilter(Filters.BaseFilter):
    name = 'NewRequestFilter'

    def filter(self, message):
        return (message.reply_to_message is not None) and \
               message.reply_to_message.text == messages.ASK_FOR_NEW_REQUEST
