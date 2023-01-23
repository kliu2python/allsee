from algorithems.sort.sort_base import SortBase
from utils.timer import RunningTimer


class SelectSearch(SortBase):
    def __enter__(self):
        return self.setup()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.release_db("select_sort")

    def select_sort(self, num_list):
        items = num_list[:]
        for i in range(self.size - 1):
            min_index = i
            for j in range(i + 1, self.size):
                if self.compare(items[j], items[min_index]):
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
            self.save_status("select_sort", items)
        return items

    def setup(self):
        num_list = self.generator()
        start_time = RunningTimer.start_timer()
        new_list = self.select_sort(num_list)
        end_time = RunningTimer.stop_timer()
        return [num_list, new_list, RunningTimer.timer(start_time, end_time), self.show_status("select_sort")]

