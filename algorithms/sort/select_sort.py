from algorithms.sort.sort_base import SortBase
from utils.timer import RunningTimer


class SelectSearch(SortBase):
    def __enter__(self):
        return self.setup()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def select_sort(self, num_list):
        status_queue = []
        items = num_list[:]
        for i in range(self.size - 1):
            status_dict = {}
            min_index = i
            for j in range(i + 1, self.size):
                status_dict = {}
                if self.compare(items[j], items[min_index]):
                    min_index = j
                    status_dict["i"] = i
                    status_dict["j"] = j
                    status_dict["min_index"] = min_index
                else:
                    status_dict["i"] = i
                    status_dict["j"] = j
                    status_dict["min_index"] = min_index
                status_dict["items"] = items
                status_queue.append(status_dict)
            items[i], items[min_index] = items[min_index], items[i]
            status_dict["after_switch"] = items
            status_queue.append(status_dict)
            self.save_status(self.redis_name, status_queue)
        return items

    def setup(self):
        num_list = self.generator()
        start_time = RunningTimer.start_timer()
        new_list = self.select_sort(num_list)
        end_time = RunningTimer.stop_timer()
        return [num_list, new_list, RunningTimer.timer(start_time, end_time),
                self.show_status(self.redis_name)]

