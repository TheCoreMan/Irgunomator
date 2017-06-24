from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import handlers
from config import config


# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher


# creating handlers
start_handler = CommandHandler('start', handlers.start.start)
help_handler = CommandHandler('help', handlers.start.start)
support_handler = CommandHandler('support', handlers.support.support, pass_args=True)
list_requests = CommandHandler('list', handlers.list_requests.list_requests)
show_request = CommandHandler('show', handlers.unknown.unknown)
close_request = CommandHandler('close', handlers.unknown.unknown)
support_msg_handler = MessageHandler([Filters.text], handlers.support.support_message)
unknown_handler = MessageHandler([Filters.command], handlers.unknown.unknown)

# adding handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(support_handler)
dispatcher.add_handler(list_requests)
dispatcher.add_handler(show_request)
dispatcher.add_handler(close_request)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(unknown_handler)

# Message handler must be the last one
dispatcher.add_handler(support_msg_handler)


def main():
    updater.stop()
    updater.start_polling()


if __name__ == '__main__':
    main()
