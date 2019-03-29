import json
import os
import sys


class JsonCreature(object):


    def creature(self):
        file_name = os.path.dirname(sys.argv[0]) + "\\options.json"
        data = {
            "_from_date": "2019-01-01 18:00:00",
            "_table_name": "values",
            "_to_date": "2019-01-01 18:00:00",
            "db_parameters": {
                "dbname": "dbname",
                "host": "localhosts",
                "password": "password",
                "user": "user"
            },
            "oledb_parameters": {
                "host": "localhost",
                "user": "User"
            },
            "tag_names": {
                "bool_test": "описание",
                "test": "описание",
                "test.test2": "описание",
                "test1": "описание"
            }
        }

        # если json файл существует
        if os.path.exists(file_name) == True:
            try:
                print("Json найден")
                file = open(file_name)
            except IOError as e:
                print(u'не удалось открыть файл')

        # если json файл не существует
        if os.path.exists(file_name) == False:

            try:
                print("Json файл не существует, создаем новый")
                with open(file_name, "w") as write_file:
                    json.dump(data, write_file)

            except IOError as e:
                print(u'не удалось открыть файл')

        # если json файл пустой
        if os.stat(file_name).st_size == 0:
            try:
                print("Json файл пустой, пезаписываем")
                with open(file_name, "w") as write_file:
                    json.dump(data, write_file)

            except IOError as e:
                print(u'не удалось открыть файл')





