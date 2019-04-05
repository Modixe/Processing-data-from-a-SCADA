import datetime
import sys
import time

from Models.Configuration import Configuration


class ProgressBa(object):

    def __init__(self):
        self.config = Configuration()
        self.progress_value = 0.0
        self.config.load()
        self.from_date_sec = time.mktime(self.config.from_date.timetuple())
        self.to_date_sec = time.mktime(self.config.to_date.timetuple())

        total = self.to_date_sec - self.from_date_sec
        self.percent_sec = total / 100

    def row_update(self):
        sys.stdout.write("\r100%")
        sys.stdout.flush()

    def increment(self, tag_value):
        current_date_sec = time.mktime(tag_value.timestamp.timetuple())
        current_sec = current_date_sec - self.from_date_sec

        current_percent = current_sec / self.percent_sec

        if (current_percent > 1 and current_percent < 5):
            test = 1

        # if value_index == 0 or (value_index % 5) == 0:
        sys.stdout.write("\r%.2f%%" % current_percent)
        self.progress_value = current_percent
        sys.stdout.flush()



