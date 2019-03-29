import datetime
import sys
import time

from DataAccessLayer.Repositories.opc_hda.OpcHdaRepository import OpcHdaRepository
from Models.Configuration import Configuration


class ProgressBa(object):


    def __init__(self):
        self.config = Configuration()
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
        sys.stdout.flush()




#
#     config = Configuration()
#     config.load()
#     opc_hda_repository = OpcHdaRepository(config.oledb_parameters["user"], config.oledb_parameters["host"])
#
#     def sss(self):
#
#         self.uts_from_date = int(time.mktime(self.config.from_date.timetuple()))
#         self.uts_to_date = int(time.mktime(self.config.to_date.timetuple()))
#
#         print("От", self.uts_from_date, "До", self.uts_to_date)
#
#         #percent = (self.uts_to_date - self.uts_from_date) // 100
#         #print("1 процент = ", percent)
#         #self.total = int(self.uts_to_date - self.uts_from_date)
#
#         for tag_value in self.opc_hda_repository.read():

            #time_stamp = str(tag_value.timestamp.replace(tzinfo=None))
            #self.uts_time_stamp = time.mktime(datetime.datetime.strptime(time_stamp, "%Y-%m-%d %H:%M:%S").timetuple())







#a = ProgressBa()
#a.sss()

