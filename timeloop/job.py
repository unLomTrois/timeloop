from threading import Thread, Event
from datetime import timedelta
import random

class Job(Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        Thread.__init__(self)
        self.stopped = Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        self.rand_span = args[0]

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        span = random.uniform(-self.rand_span, self.rand_span)

        while not self.stopped.wait(self.interval.total_seconds() + span):
            self.execute(*self.args, **self.kwargs)
            span = random.uniform(-self.rand_span, self.rand_span)
            print(span)