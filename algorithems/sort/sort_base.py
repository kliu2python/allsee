from algorithems.manage import Manage
from utils.generate_nums import GenerateNums


class SortBase:
    def __init__(self, size: int = 0, is_random: bool = False):
        self.size = size
        self.is_random = is_random
        self.db = Manage()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @classmethod
    def compare(cls, num1: int = 0, num2: int = 0) -> bool:
        return num1 > num2

    def generator(self):
        num_generator = GenerateNums(self.size, self.is_random)
        return num_generator.generator()

    def save_status(self, key, value):
        self.db.save_status_to_db(key, value)

    def show_status(self, key):
        return self.db.show_db(key)

    def release_db(self, key):
        self.db.release_db(key)

    def setup(self):
        return self
