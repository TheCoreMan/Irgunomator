class Request(object):
    def __init__(self, message, request_id):
        self.id = request_id
        self._creation_time = message.date
        self._creator = message.chat.id
        self._messages = [message.text]
        self._is_open = True
