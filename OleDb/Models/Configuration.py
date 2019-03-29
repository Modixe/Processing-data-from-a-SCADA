from datetime import datetime
import json
import sys
import os

from Models.Tag import Tag


class Configuration(object):

    tags = []
    tag_names = {}
    db_parameters = {}
    oledb_parameters = {}

    _to_date = None
    _from_date = None

    to_date = None
    from_date = None

    table_name = None
    _table_name = None






    def load(self):

        directory = os.path.dirname(sys.argv[0]) + "\\test.json"

        with open(directory, encoding='utf-8') as data_file:
            data = json.load(data_file, )

        self.__dict__ = data
        self.from_date = datetime.strptime(self._from_date, '%d-%m-%Y %H:%M:%S.%f')
        self.to_date = datetime.strptime(self._to_date, '%d-%m-%Y %H:%M:%S.%f')
        self.table_name = self._table_name

        for tag_name, tag_description in self.tag_names.items():
            self.tags.append(Tag(tag_name, tag_description))

    def save(self):
        pass

