from PyQt5.QtCore import pyqtSlot




class MyPresenter(object):

    def __init__(self, test_model, test_view_main):
        self.model = test_model
        self.view_main = test_view_main

        # Подключение к пользовательским сигналам представления
        self.view_main.signal.btnSignal.connect(self.Clicked_read_write)
        self.view_main.signal.rwSignal.connect(self.Connection_Setting)


    def Clicked_read_write(self):
        print("+Clicked_read_write")
        # self.view_main.show()
    def Connection_Setting(self):
        print("+++connection_Setting")
        # self.view_main.show()


    # def on_Button_clicked(self, checked=None):
    #     if checked == None: return
    #     dialog = QDialog()
    #     dialog.ui = Ui_MyDialog()
    #     dialog.ui.setupUi(dialog)
    #     dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    #     dialog.exec_()


