from utils.generate_nums import GenerateNums


class SortBase:
    def __init__(self, size: int = 0, is_random: bool = False):
        self.size = size
        self.is_random = is_random

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

    def setup(self):
        return self
