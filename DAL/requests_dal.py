# coding=utf-8
import pickle

import humanize

from DAL.db import bot_db as db


class Request(object):
    def __init__(self, message, request_id):
        self.id = request_id
        self.creation_time = message.date
        self.chat_id = message.chat_id
        self.creator_id = message.from_user.id
        self.creator_name = message.from_user.name
        self.creator_username = message.from_user.username
        self.messages = []

    def to_unicode(self):
        return u"""{0}
       הבקשה {1}
        נוצר על ידי {2}
_זמן פתיחה_ {3}
""".format(
            self.id,
            self.messages[0],
            self.creator_name,
            humanize.naturaltime(self.creation_time))

    def append_message(self, message):
        self.messages.append(message)  # .encode('utf-8')
        db.set(self.id, pickle.dumps(self))

    def save(self):
        db.set(self.id, pickle.dumps(self))
        db.sadd("open_requests", self.id)
        db.sadd("requests", self.id)


def get_request(request_id):
    return pickle.loads(db.get(request_id))


def close_request(request_id):
    db.srem("open_requests", request_id)


def get_all_open_requests():
    open_requests = []
    open_requests_ids = db.smembers("open_requests")
    if open_requests_ids:
        for open_request_id in open_requests_ids:
            open_requests.append(get_request(open_request_id))
    return open_requests
