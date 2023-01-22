from algorithems.search.search_base import SearchBase


class SelectSearch(SearchBase):
    def __init__(self, num_list: list[int] = None, size: int = 0, is_random: bool = False):
        super().__init__(size, is_random)
        if not num_list:
            self.num_list = self.generator()
        self.num_list = num_list

    def select_search(self):
        items = self.num_list[:]
        for i in range(self.size - 1):
            min_index = i
            for j in range(i + 1, self.size):
                if self.compare(items[j], items[min_index]):
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        return items
