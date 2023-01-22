import random


class GenerateNums:
    def __init__(self, size: int = 0, is_random: bool = False):
        self.size = size
        self.is_random = is_random

    def generator(self) -> list[int]:
        num_list = []
        dupe = set()
        if self.is_random:
            for _ in range(self.size):
                tmp = random.randint(0, self.size + 5)
                if tmp not in dupe:
                    num_list.append(tmp)
                    dupe.add(tmp)
        return num_list
