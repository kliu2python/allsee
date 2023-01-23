import json

from utils.redis_client import RedisClient

r = RedisClient()


class Manage:
    def __init__(self):
        self.dic_status = []

    def save_status_to_db(self, key, status):
        self.dic_status.append(status)
        json_object = json.dumps(self.dic_status)
        r.client.set(key, json_object)

    @classmethod
    def show_db(cls, key):
        status = r.client.get(key)
        return json.loads(status)

    def release_db(self, key):
        self.dic_status.clear()
        r.client.delete(key)
