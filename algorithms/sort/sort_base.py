from algorithms.manage import Manage
from utils.generate_nums import GenerateNums


class SortBase:
    def __init__(self, size: int = 0, is_random: bool = False,
                 redis_name: str = None):
        self.size = size
        self.is_random = is_random
        self.db = Manage()
        self.redis_name = redis_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @classmethod
    def compare(cls, num1: int = 0, num2: int = 0) -> bool:
        return num1 < num2

    def generator(self):
        num_generator = GenerateNums(self.size, self.is_random)
        return num_generator.generator()

    def save_status(self, key: str, value: list):
        self.db.save_status_to_db(key, value)

    def show_status(self, key):
        return self.db.show_db(key)

    def release_db(self, key):
        self.db.release_db(key)

    def setup(self):
        return self
