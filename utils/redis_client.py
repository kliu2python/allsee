import redis


class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host='127.0.0.1',
            port=6379,
            db=0
        )

    def db_health(self):
        if self.client.ping():
            print("PONG")
        else:
            print("Connection failed to db")
