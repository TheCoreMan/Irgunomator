from config import config
import redis

# Connecting to Redis db
bot_db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])