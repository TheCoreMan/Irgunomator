import configparser

# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

support_chat_id = int(config['DEFAULT']['support_chat_id'])
