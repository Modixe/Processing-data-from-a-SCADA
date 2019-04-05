import pythoncom
from win32com.client import Dispatch

from Models.DataAccessLayer.Repositories.TagValue import TagValue


class OpcHdaRepository(object):

    record_set = None

    def __init__(self, user, host):

        try:
            pythoncom.CoInitialize()
            self.connection = Dispatch('ADODB.Connection')
        except Exception as e:
            print(e)


        self.connection.ConnectionString = 'Provider=Infinity.OLEDBProvider;Persist Security Info=True;User ID={0};' \
                                           'Data Source="hda=hda://{1}/Infinity.OPCHDAServer";' \
                                           'Location="";Mode=Read;Extended Properties=""'.format(user, host)

    def read(self, tag_name=None, from_date=None, to_date=None):
        """Открывает соединение с сервером и читает результаты запроса"""
        query = self.get_query(tag_name, from_date, to_date)

        if self.connection.state == 0:
            self.connection.Open()

        if self.record_set is None:
            self.record_set = Dispatch('ADODB.RecordSet')
            self.record_set.ActiveConnection = self.connection
            self.record_set.Open(query)

        i = 0

        while not self.record_set.EOF:

            tag_value = TagValue()

            tag_value.name = self.record_set.Fields.Item(0).Value
            tag_value.timestamp = self.record_set.Fields.Item(2).Value
            tag_value.value = self.record_set.Fields.Item(3).Value
            tag_value.quality = self.convert_to_opcda_quality(self.record_set.Fields.Item(4).Value)

            # for i in tag_value.timestamp:
            #     print('Completed: {}%'.format(i), end='\r')

            yield tag_value

            self.record_set.MoveNext()

        self.record_set.Close()
        self.record_set = None

    def convert_to_opcda_quality(self, opchda_quality):
        """Конвертирует значение OPCHDA-качества в значение OPCDA-качества"""

        # Для битовых операций число должно быть целочисленным
        int_quality = int(opchda_quality)

        # Накладываем побитовую маску (1111 1111 1111 1111), чтобы получить младшие 16 бит
        return int_quality & 65535

    def get_query(self, tag_name=None, from_date=None, to_date=None):
        """Формирует запрос"""
        query = "select * from hda.History"

        # Вывод по тэгу
        if tag_name is not None and from_date is None and to_date is None:
            query = "select * from hda.History where item='{}'".format(tag_name)

        # Вывод по тэге и от даты
        elif tag_name is not None and from_date is not None and to_date is None:
            query = "select * from hda.History where item = '{0}' and localtime > timestamp '{1}'" \
                .format(tag_name, from_date.strftime('%d-%m-%Y %H:%M:%S.%f'))

        # Вывод по тэгу, от даты и по дате
        elif tag_name is not None and from_date is not None and to_date is not None:
            query = "select * from hda.History where item = '{0}' and localtime > timestamp '{1}' " \
                    "and localtime < timestamp '{2}'" \
                .format(tag_name, from_date.strftime('%d-%m-%Y %H:%M:%S'), to_date.strftime('%d-%m-%Y %H:%M:%S'))

        # Вывод по тэгу и до даты
        elif tag_name is not None and from_date is None and to_date is not None:
            query = "select * from hda.History where item = '{0}' and localtime < timestamp '{1}'" \
                .format(tag_name, to_date.strftime('%d-%m-%Y %H:%M:%S.%f'))

        # Вывод от даты
        elif tag_name is None and from_date is not None and to_date is None:
            query = "select * from hda.History where localtime > timestamp '{}'" \
                .format(from_date.strftime('%d-%m-%Y %H:%M:%S.%f'))

        # Вывод от даты и по дате
        elif tag_name is None and from_date is not None and to_date is not None:
            query = "select * from hda.History where localtime > timestamp '{0}'" \
                    "and localtime < timestamp '{1}'" \
                .format(from_date.strftime('%d-%m-%Y %H:%M:%S.%f'), to_date.strftime('%d-%m-%Y %H:%M:%S.%f'))

        # Вывод по дате
        elif tag_name is None and from_date is None and to_date is not None:
            query = "select * from hda.History where localtime < timestamp '{}'" \
                .format(to_date.strftime('%d-%m-%Y %H:%M:%S.%f'))

        return query

    def __del__(self):

        if self.connection.state == 1:
            self.connection.Close()
