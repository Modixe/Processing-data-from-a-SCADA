from Model.Configuration import Configuration


class ReadWritePresenter(object):

    def __init__(self, model_read_write, read_write_view, test_view_main):


        self.model = model_read_write
        self.read_write_view = read_write_view
        self.view_main = test_view_main

        # Подключение к пользовательским сигналам представления
        self.view_main.signal.btnSignal.connect(self.run_read_write)
        # Ловим сигнал кнопки "Сохранить" и запускаем функцию сохрание пораметров
        self.read_write_view.signal.save_read_write_Signal.connect(self.save_read_write)



    def run_read_write(self):
        print("+run_read_write")
        config = Configuration()
        config.load()
        self.config = config

        number_lines = self.config.tag_names.__len__()

        self.read_write_view.set_read_write(config.table_name,
                                            config.from_date,
                                            config.to_date)

        self.read_write_view.add_row(self.config.tag_names)
        self.read_write_view.run_rw()

    def save_read_write(self):
        print("+save_connection_setting_Signal")

        # записыва!ем результаты заполнения полей
        self.table_name = self.read_write_view.table_name
        self.from_date = self.read_write_view.from_date
        self.to_date = self.read_write_view.to_date
        self.tag_dict = self.read_write_view.tag_dict

        print("+", self.table_name, self.from_date, self.to_date)

        self.config.save_read_write(self.table_name, self.from_date, self.to_date, self.tag_dict)

