from datetime import datetime


class RunningTimer:
    @classmethod
    def start_timer(cls):
        return datetime.now()

    @classmethod
    def stop_timer(cls):
        return datetime.now()

    @classmethod
    def timer(cls, start_time, stop_time):
        return f"The running time is: {(stop_time - start_time).microseconds} ms"
