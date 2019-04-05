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

        directory = os.path.dirname(sys.argv[0]) + "\\options.json"

        with open(directory, encoding='utf-8') as data_file:
            self.data = json.load(data_file, )

        self.__dict__ = self.data

        try:
            self.from_date = datetime.strptime(self._from_date, '%Y-%m-%d %H:%M:%S')
            self.to_date = datetime.strptime(self._to_date, '%Y-%m-%d %H:%M:%S')
        except Exception as er:
            print("Вывод :", er)

        self.table_name = self._table_name

        for tag_name, tag_description in self.tag_names.items():
            self.tags.append(Tag(tag_name, tag_description))

        # for key, val in self.tag_names.items():
        #     self.tag_names_key = key
        #     self.tag_names_val =




            # print("Ключ", self.tag_names_key, "Значение", self.tag_names_val)

    def save_connection_setting(self, db_name, db_user, db_password, db_host, oledb_localhost, oledb_user):
        directory = os.path.dirname(sys.argv[0]) + "\\options.json"

        # открываем json для чтения
        with open(directory, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            json_data["db_parameters"]["dbname"] = db_name
            json_data["db_parameters"]["user"] = db_user
            json_data["db_parameters"]["password"] = db_password
            json_data["db_parameters"]["host"] = db_host
            json_data["oledb_parameters"]["user"] = oledb_user
            json_data["oledb_parameters"]["host"] = oledb_localhost

        # открываем json для записи
        with open(directory, 'w', encoding='utf-8') as f:
            f.write(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))
            f.close()

    def dt_converter(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()

    def save_read_write(self, table_name, from_date, to_date, tag_dict):
        directory = os.path.dirname(sys.argv[0]) + "\\options.json"

        from_date_datetime = datetime.strptime(from_date, '%d.%m.%Y %H:%M:%S')
        to_date_datetime = datetime.strptime(to_date, '%d.%m.%Y %H:%M:%S')

        self.number_lines = 0
        # открываем json для чтения
        with open(directory, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            json_data["_table_name"] = table_name
            json_data["_from_date"] = from_date_datetime
            f.close()
            json_data["_to_date"] = to_date_datetime
            json_data["tag_names"] = tag_dict

            # A = dict(zip(json_data["tag_names"], list(range(4))))







        # config.table_name,
        # config.from_date,
        # config.to_date,
        # config.tags[1].name

        # открываем json для записи
        with open(directory, 'w', encoding='utf-8') as f:

            try:
                f.write(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False, default=self.dt_converter))
            except Exception as er:
                print("Вывод :", er)
            finally:
                f.close()