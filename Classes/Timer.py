import time
from Classes.ClassUtility import *


class Timer:
    start_time = None
    end_time = None

    def __init__(self):
        self.start_time = int(time.time())

    def end(self):
        self.end_time = int(time.time())

        if int(self.end_time - self.start_time) >= 60:
            execution_time_minutes = (self.end_time - self.start_time) / 60
            execution_time_seconds = (self.end_time - self.start_time) % 60
        else:
            execution_time_minutes = 0
            execution_time_seconds = (self.end_time - self.start_time) % 60

        Print.print_yellow("Execution : " + str(execution_time_minutes) + " Minutes & " + str(
            execution_time_seconds) + " Seconds")
