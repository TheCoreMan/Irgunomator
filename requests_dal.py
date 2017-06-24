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
        self._messages = [message.text]

    def __repr__(self):
        return "{0}\n{1}".format(
            self.id,
            self._messages[0])

    def save(self):
        db.set(self.id, pickle.dumps(self))
        db.lpush("open_requests", self.id)
        db.lpush("requests", self.id)


def get_request(request_id):
    return pickle.loads(db.get(request_id))


def get_all_open_requests():
    open_requests = []
    open_requests_ids = db.lrange("open_requests", 0, -1)
    if open_requests_ids:
        for open_request_id in open_requests_ids:
            open_requests.append(get_request(open_request_id))
    return open_requests
