import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from Models.Configuration import Configuration
import psycopg2

from Models.DataAccessLayer.Repositories.db.TagRepository import TagRepository
from Models.DataAccessLayer.Repositories.db.TagValueRepository import TagValueRepository
from Models.DataAccessLayer.Repositories.opc_hda.OpcHdaRepository import OpcHdaRepository
from Models.ProgressBar import ProgressBa

class Communica(QObject):
    tef_state_Signal = QtCore.pyqtSignal(str)
    progress_changed = QtCore.pyqtSignal(float, str)

class MyThread(QtCore.QThread):


    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.signal = Communica()

        # self.tef_state_Signal = QtCore.pyqtSignal()
        self.running = False   # Флаг выполнения потока
        self.count = 0

    def run(self):
        self.running = True

        progressBar = ProgressBa()
        config = Configuration()
        config.load()
        db = OpcHdaRepository(config.oledb_parameters["user"], config.oledb_parameters["host"])

        conn = psycopg2.connect(dbname=config.db_parameters["dbname"], user=config.db_parameters["user"],
                                password=config.db_parameters["password"], host=config.db_parameters["host"])

        opc_hda_repository = OpcHdaRepository(config.oledb_parameters["user"], config.oledb_parameters["host"])

        tag_repository = TagRepository(conn)
        tag_repository.create_table()

        tag_value_repository = TagValueRepository(conn)
        tag_value_repository.create_table()

        for tag_index, tag in enumerate(config.tags):

            if self.running:
                tag_repository.create_or_update(tag)

                if tag_index > 0:
                    progressBar.row_update()

                print("\nЗагружаются данные для тэга " + tag.name + "\nОписание: " + tag.description)
                self.signal.tef_state_Signal.emit(tag.name)

                for value_index, tag_value in enumerate(
                        opc_hda_repository.read(tag.name, config.from_date, config.to_date)):

                    if self.running:
                        tag_value.tag_id = tag.id
                        tag_value_repository.create_or_update(tag_value)
                    else:
                        break

                    # method2
                    progressBar.increment(tag_value)


                    self.signal.progress_changed.emit(progressBar.progress_value, tag.name)

            else:
                break

                # print(tag_value.timestamp)

        progressBar.row_update()

        conn.close()
        input("\nPress enter to exit: ")


# class tempStart(object):
#
#
#
#     def run(self):
#
#         progressBar = ProgressBa()
#         config = Configuration()
#         config.load()
#
#         db = OpcHdaRepository(config.oledb_parameters["user"], config.oledb_parameters["host"])
#
#         conn = psycopg2.connect(dbname=config.db_parameters["dbname"], user=config.db_parameters["user"],
#                                 password=config.db_parameters["password"], host=config.db_parameters["host"])
#
#         opc_hda_repository = OpcHdaRepository(config.oledb_parameters["user"], config.oledb_parameters["host"])
#
#         tag_repository = TagRepository(conn)
#         tag_repository.create_table()
#
#         tag_value_repository = TagValueRepository(conn)
#         tag_value_repository.create_table()
#
#
#
#         for tag_index, tag in enumerate(config.tags):
#             tag_repository.create_or_update(tag)
#
#             if tag_index > 0:
#                 progressBar.row_update()
#
#
#             print("\nЗагружаются данные для тэга " + tag.name + "\nОписание: " + tag.description)
#
#             for value_index, tag_value in enumerate(opc_hda_repository.read(tag.name, config.from_date, config.to_date)):
#                 tag_value.tag_id = tag.id
#                 tag_value_repository.create_or_update(tag_value)
#
#                 #method2
#                 progressBar.increment(tag_value)
#
#
#                 #print(tag_value.timestamp)
#
#
#         progressBar.row_update()
#
#         conn.close()
#         input("\nPress enter to exit: ")
