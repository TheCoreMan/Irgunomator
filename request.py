class Request(object):
    def __init__(self, message):
        self._creation_time = message.date
        self._creator = message.chat.id
        self._messages = [message.text]
        self._is_open = True
