# coding=utf-8

from collections import Counter

from DAL import requests_dal

import inflect
engine = inflect.engine()


def get_leaders_string(all_users_counter):
    if len(all_users_counter.values()) == 0:
        return u"Empty!"

    msg = u""
    for i, user in enumerate(all_users_counter.most_common(3)):
        msg += u"{0} place: {1} with {2} requests\n".format(engine.ordinal(i+1), user[0], user[1])

    return msg


def show_leaderboard(bot, update):
    all_open_requests = requests_dal.get_all_open_requests()
    all_users = []
    for req in all_open_requests:
        all_users.append(req.creator_name)

    all_users_counter = Counter(all_users)

    message = u"""
מי המובילים בדיווחים?

🏆🏆🏆

{0}

סה"כ היו {1} דיווחים!
📈
    """.format(
        get_leaders_string(all_users_counter),
        sum(all_users_counter.values()))

    bot.send_message(
        chat_id=update.message.chat_id,
        text=message)
