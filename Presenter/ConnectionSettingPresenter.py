from Models.Configuration import Configuration


class ConnectionSettingPresenter(object):

    def __init__(self, model_read_write, connection_setting_view, test_view_main, config=None):
        self.model = model_read_write
        self.connection_setting_view = connection_setting_view
        self.main_view = test_view_main
        # self.config = config

        # Ловим сигнал об открытии модального окна и открываем функцию запуска
        self.main_view.signal.rwSignal.connect(self.run_connection_Setting)

        # Ловим сигнал кнопки "Сохранить" и запускаем функцию сохрание пораметров
        self.connection_setting_view.signal.save_connection_setting_Signal.connect(self.save_connection_setting)

    def run_connection_Setting(self):
        print("+run_connection_Setting")
        config = Configuration()
        config.load()
        self.config = config
        # print("db name:", self.view_connection_setting.lineEdit.text())

        self.connection_setting_view.set_db_parameters(self.config.db_parameters["dbname"],
                                                       self.config.db_parameters["user"],
                                                       self.config.db_parameters["password"],
                                                       self.config.db_parameters["host"])
        self.connection_setting_view.set_oledb_parameters(self.config.oledb_parameters["user"],
                                                          self.config.oledb_parameters["host"])
        self.connection_setting_view.run_co()

    def save_connection_setting(self):
        # записываем результаты заполнения полей
        self.db_name = self.connection_setting_view.db_name
        self.db_user = self.connection_setting_view.db_user
        self.db_password = self.connection_setting_view.db_password
        self.db_localhost = self.connection_setting_view.db_localhost
        self.oledb_host = self.connection_setting_view.Oledb_user
        self.oledb_user = self.connection_setting_view.Oledb_localhost

        print("+save_connection_setting_Signal")
        print("+", self.db_name, self.db_user, self.db_password, self.db_localhost,
                                            self.oledb_host, self.oledb_user)

        self.config.save_connection_setting(self.db_name, self.db_user, self.db_password, self.db_localhost,
                                            self.oledb_host, self.oledb_user)
        # self.config.load()
        # self.config.save()
