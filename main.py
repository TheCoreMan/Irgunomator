from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import config

import handlers


# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher


# creating handlers
start_handler = CommandHandler('start', handlers.start)
help_handler = CommandHandler('help', handlers.start)
support_handler = CommandHandler('support', handlers.support)
list_requests = CommandHandler('list', handlers.show_requests)
show_request = CommandHandler('show', handlers.show_single_request)
close_request = CommandHandler('close', handlers.close_request)
support_msg_handler = MessageHandler([Filters.text], handlers.support_message)
unknown_handler = MessageHandler([Filters.command], handlers.unknown)

# adding handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(support_handler)
dispatcher.add_handler(list_requests)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(unknown_handler)

# Message handler must be the last one
dispatcher.add_handler(support_msg_handler)


def main():
    updater.stop()
    updater.start_polling()


if __name__ == '__main__':
    main()
