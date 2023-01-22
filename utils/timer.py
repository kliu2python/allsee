import time


class RunningTimer:
    @classmethod
    def start_timer(cls):
        return time.time()

    @classmethod
    def stop_timer(cls):
        return time.time()

    @classmethod
    def timer(cls, start_time, stop_time):
        return f"The running time is: {stop_time - start_time}"
