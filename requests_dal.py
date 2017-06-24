import redis
import pickle
from config import config

# Connecting to Redis db
db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])


class Request(object):
    def __init__(self, message, request_id):
        self.id = request_id
        self._creation_time = message.date
        self._creator = message.chat.id
        self._messages = []
        self._is_open = True

    def append_message(self, message):
        self._messages.append(message)

    def save(self):
        db.set(self.id, pickle.dumps(self))


def get_request(request_id):
    return pickle.loads(db.get(request_id))
