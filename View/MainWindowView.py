import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtCore import QObject, pyqtSignal

# from View.ConnectionSetting import Ui_Dialog
from View.ReadWriteView import Ui_Dialog

class Communicate(QObject):
    # ---Создаем сигналы---
    displaySignal = QtCore.pyqtSignal()
    btnSignal = QtCore.pyqtSignal()
    rwSignal = QtCore.pyqtSignal()




class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.signal = Communicate()
        self.raw = self.Raw(self)
        self.css = self.Connection_settings(self)

    def Clicked_read_write(self):
        print("YRAAA")

    def Raw_click(self):
        try:
            self.signal.btnSignal.emit()

        except Exception as er:
            print("Вывод :", er)
            #sys.exc_info()[0]

    def Connection_settings_signal(self):
        print("+Connection_settings_signal")
        self.signal.rwSignal.emit()


#-------Создаем пункт в меню чтение и запись
    def Raw(self, MainWindow):
        self.actionRead_and_write = QtWidgets.QAction(MainWindow)
        self.actionRead_and_write.setObjectName("actionRead_and_write")
        self.actionRead_and_write.setShortcut('Shift+1')
        self.actionRead_and_write.triggered.connect(self.Raw_click)

    # -------Создаем пункт в меню параметры подключние
    def Connection_settings(self, MainWindow):
        self.actionConnection_settings = QtWidgets.QAction(MainWindow)
        self.actionConnection_settings.setObjectName("actionConnection_settings")
        self.actionConnection_settings.setShortcut('Shift+2')
        self.actionConnection_settings.triggered.connect(self.Connection_settings_signal)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(672, 350)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 631, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 75, 23))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 75, 23))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuRead_and_write = QtWidgets.QMenu(self.menuBar)
        self.menuRead_and_write.setObjectName("menuRead_and_write")

        # ------Чтение и запись---
        self.setMenuBar(self.menuBar)

        self.actionStatistical_data = QtWidgets.QAction(self)
        self.actionStatistical_data.setObjectName("actionStatistical_data")


        self.actionCharts = QtWidgets.QAction(self)
        self.actionCharts.setObjectName("actionCharts")

        self.actionFilter = QtWidgets.QAction(self)
        self.actionFilter.setObjectName("actionFilter")

        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+O')

        self.menuRead_and_write.addAction(self.actionRead_and_write)
        self.menuRead_and_write.addSeparator()
        self.menuRead_and_write.addAction(self.actionStatistical_data)
        self.menuRead_and_write.addSeparator()
        self.menuRead_and_write.addAction(self.actionConnection_settings)
        self.menuRead_and_write.addSeparator()
        self.menuRead_and_write.addAction(self.actionCharts)
        self.menuRead_and_write.addSeparator()
        self.menuRead_and_write.addAction(self.actionFilter)
        self.menuRead_and_write.addSeparator()
        self.menuRead_and_write.addAction(self.actionExit)
        self.menuBar.addAction(self.menuRead_and_write.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))

        self.pushButton.setText(_translate("MainWindow", "Пуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.menuRead_and_write.setTitle(_translate("MainWindow", "Меню"))
        self.actionRead_and_write.setText(_translate("MainWindow", "Чтение и запись"))
        self.actionStatistical_data.setText(_translate("MainWindow", "Статистика данных"))
        self.actionConnection_settings.setText(_translate("MainWindow", "Параметры соединения"))
        self.actionCharts.setText(_translate("MainWindow", "Графики"))
        self.actionFilter.setText(_translate("MainWindow", "Фильтры"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))


