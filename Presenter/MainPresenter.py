
from PyQt5.QtCore import pyqtSlot

# from temp import MyThread
from PyQt5 import QtCore

class MyPresenter(object):

    def __init__(self, test_model, test_view_main, myThread, config):
        self.model = test_model
        self.view_main = test_view_main
        self.start_temp_thread = myThread


        self.config = config
        # self.tamp = MyThread()


        # Подключение к пользовательским сигналам представления
        self.view_main.signal.startSignal.connect(self.on_start)
        self.view_main.signal.stopSignal.connect(self.on_stop)

        self.start_temp_thread.signal.progress_changed.connect(self.test, QtCore.Qt.QueuedConnection)
        self.start_temp_thread.signal.tef_state_Signal.connect(self.test2, QtCore.Qt.QueuedConnection)

        # self.start_temp_thread.signal.tef_state_Signal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def test(self, progress_value, tag_name):
        self.view_main.set_table_progress(progress_value, tag_name)

        # self.view_main.set_table_progress(tag_name)

    def test2(self, tag_name):
        print("======", tag_name)
        # self.view_main.set_table_progress(tag_name)


    def run_main(self):
        print("+view_run_main")
        self.view_main.on_chahge(self.config.tag_names)

    def on_start(self):
        print("+ start_signal")
        self.run_main()
        if not self.start_temp_thread.isRunning():
            self.start_temp_thread.start()

    def on_stop(self):
        print("+StopSignal")
        self.start_temp_thread.running = False
    # def on_change(self, teg_state):
    #     self.tegs_state = teg_state





    # def on_Button_clicked(self, checked=None):
    #     if checked == None: return
    #     dialog = QDialog()
    #     dialog.ui = Ui_MyDialog()
    #     dialog.ui.setupUi(dialog)
    #     dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    #     dialog.exec_()


