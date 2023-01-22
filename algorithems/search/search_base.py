from utils.generate_nums import GenerateNums


class SearchBase(GenerateNums):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @classmethod
    def compare(cls, num1: int = 0, num2: int = 0) -> bool:
        return num1 > num2
