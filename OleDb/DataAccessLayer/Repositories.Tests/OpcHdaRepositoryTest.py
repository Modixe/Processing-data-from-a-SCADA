import unittest

from datetime import datetime
from unittest import mock

from DataAccessLayer.Repositories.opc_hda.OpcHdaRepository import OpcHdaRepository


class OpcHdaRepositoryTest(unittest.TestCase):

    def test_get_query_tag_name_not_none(self):
        # arrange
        repository = OpcHdaRepository()
        # act
        excepted = repository.get_query(tag_name="test")
        # assert
        self.assertEqual(excepted, "select * from hda.History where item='test'")

    def test_get_query_all_arguments_not_none(self):
        # arrange
        repository = OpcHdaRepository()
        # act
        expected = repository.get_query(from_date=datetime(2019, 1, 10, 0, 0, 0, 000000))
        # assert
        actual = "select * " \
                   "from hda.History where localtime > timestamp '2019-01-10 00:00:00.000000'"

        self.assertEqual(expected, actual)

    @unittest.skip("Для корректной проверки необходим Infinity.OPCHDDAServer")
    def test_read__readed_values_are_correct(self):
        # arrange
        repository = OpcHdaRepository()

        # act
        values = []

        for tag_value in repository.read():
            values.append(tag_value)

        # assert
        self.assertTrue(len(values) > 0)

    def test_read__record_set_values_are_loaded(self):
        # arrange
        connection_mock = mock.Mock()
        connection_mock.configure_mock(state=0, Open=lambda: {})

        #connection_mock = type('', (object,), {"state": 0, "Open": lambda self_obj: {}})()

        fields_mock = type('', (object,), {"Item": lambda self_obj, number: get_test_value_by_number(number)})()
        record_set_mock = type('', (object,), {
            "ActiveConnection": None,
            "EOF": False,
            "Fields": fields_mock,
            "Open": lambda self_obj: {},
            "Close": lambda self_obj: {},
            "MoveNext": lambda self_obj: set_eof(self_obj)
        })()

        repository = OpcHdaRepository()
        repository.connection = connection_mock
        repository.record_set = record_set_mock

        # act
        values = []
        tag_value = None

        for tag_value in repository.read():
            values.append(tag_value)

        # assert
        self.assertTrue(len(values) > 0)

        self.assertEqual("name", tag_value.name)
        self.assertEqual(datetime(2019, 1, 1), tag_value.timestamp)
        self.assertEqual(10, tag_value.value)
        self.assertEqual(1, tag_value.quality)


def get_test_value_by_number(number):
    if number == 0:
        return type('', (object,), {"Value": "name"})()
    elif number == 2:
        return type('', (object,), {"Value": datetime(2019, 1, 1)})()
    elif number == 3:
        return type('', (object,), {"Value": 10})()
    elif number == 4:
        return type('', (object,), {"Value": 1})()


def set_eof(self_obj):
    self_obj.EOF = True
