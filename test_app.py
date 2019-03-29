import sys

from Model.Configuration import Configuration
from Model.ConnectionSettingModel import ModelConnectionSetting
from Model.JsonCreature import JsonCreature
from Model.ReadWriteModel import ModelReadWrite
from Model.test_model import MyModel
from Presenter.MainPresenter import MyPresenter
from Presenter.ConnectionSettingPresenter import ConnectionSettingPresenter
from View.MainWindowView import Ui_MainWindow
from Presenter.ReadWritePresenter import ReadWritePresenter
from View.ReadWriteView import Ui_Dialog
from View.ConnectionSettingView import Ui_Connection_Setting
from PyQt5 import QtCore, QtGui, QtWidgets


class PointOfEntry(object):

    def __init__(self):

        test = JsonCreature()
        test.creature()

        # Создаем объекты конфигуратора
        # config = Configuration()
        # config.load()

        # Создаем объекты модели
        test_model = MyModel()
        model_read_write = ModelReadWrite()
        model_connection_setting = ModelConnectionSetting()

        # Создаем объекты вида
        test_view_main = Ui_MainWindow()
        view_read_write = Ui_Dialog()
        view_connection_setting = Ui_Connection_Setting()

        # Передаем модель, вид в презентер
        self.presenter_main = MyPresenter(test_model, test_view_main)
        self.presenter_read_write = ReadWritePresenter(model_read_write, view_read_write, test_view_main)
        self.presenter_connection_Setting = ConnectionSettingPresenter(model_connection_setting, view_connection_setting,
                                                                       test_view_main, config=None)

        test_view_main.setupUi()
        test_view_main.show()


def qapp():
    if QtWidgets.QApplication.instance():
        _app = QtWidgets.QApplication.instance()
    else:
        _app = QtWidgets.QApplication(sys.argv)
    return _app


if __name__ == "__main__":
    print("name = main")

    app = qapp()
    window = PointOfEntry()
    # window.show()
    app.exec_()


