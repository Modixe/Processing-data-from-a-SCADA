# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Венберг\Modixe\ReadWrite.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject


class Communicate(QObject):
    # ---Создаем сигналы---
    save_read_write_Signal = QtCore.pyqtSignal()


class Ui_Dialog(object):

    def __init__(self):
        self.signal = Communicate()
        self.dialog = QtWidgets.QDialog()
        self.setupUi(self.dialog)

    def signal_save_read_write(self):

        # записываем результаты заполнения полей
        print("+ signal_save_read_write")
        self.table_name = self.lineEdit.text()
        self.from_date = self.dateTimeEdit.text()
        self.to_date = self.dateTimeEdit_2.text()
        self.tag_names = self.tegs1.text()


        # отправляем в сигнал, презентор ловит
        self.signal.save_read_write_Signal.emit()

    def set_read_write(self, table_name, from_date, to_date, tag_names):
        _translate = QtCore.QCoreApplication.translate

        # from_date = from_date.toString(self.from_date.format("dd.MM.yyyy HH:mm:ss"))

        self.lineEdit.setText(_translate("Dialog", table_name))

        formated_from_date = QtCore.QDateTime(from_date.year, from_date.month, from_date.day, from_date.hour, from_date.minute,
                                       from_date.second)
        self.dateTimeEdit.setDateTime(formated_from_date)

        #self.dateTimeEdit.setText(_translate("Dialog", from_date))

        formated_to_date = QtCore.QDateTime(to_date.year, to_date.month, to_date.day, to_date.hour, to_date.minute,
                                            to_date.second)
        self.dateTimeEdit_2.setDateTime(formated_to_date)
        self.tegs1.setText(_translate("Dialog", tag_names))


    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(256, 302)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 141, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 121, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(100, 100, 141, 22))
        self.dateTimeEdit_2.setWrapping(False)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(1, 0, 1)))
        self.dateTimeEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 1)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 70, 141, 22))
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(1, 0, 1)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 1)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 70, 21, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 100, 21, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.tegs1 = QtWidgets.QLineEdit(Dialog)
        self.tegs1.setGeometry(QtCore.QRect(100, 130, 141, 20))
        self.tegs1.setObjectName("tegs1")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 91, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 160, 31, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 31, 23))
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 270, 71, 23))
        self.pushButton_3.clicked.connect(self.signal_save_read_write)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 240, 71, 23))


        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Read and write"))
        self.label_6.setText(_translate("Dialog", "Имя таблицы:"))
        self.lineEdit.setText(_translate("Dialog", "Valie"))
        self.label_7.setText(_translate("Dialog", "Временной интервал:"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy HH:mm:ss"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy HH:mm:ss"))
        self.label_8.setText(_translate("Dialog", "От:"))
        self.label_9.setText(_translate("Dialog", "До:"))
        self.tegs1.setText(_translate("Dialog", "test"))
        self.label_10.setText(_translate("Dialog", "Название тега:"))
        self.pushButton.setText(_translate("Dialog", "+"))
        self.pushButton_2.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_4.setText(_translate("Dialog", "Загрузить"))

    def run_rw(self):
        print("+run_rw")
        self.dialog.exec_()

# #
# class main(object):
#
#     if __name__ != "__main__":
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         Dialog = QtWidgets.QMainWindow()
#         ui = Ui_Dialog()
#         ui.setupUi(Dialog)
#         Dialog.show()
#         sys.exit(app.exec_())