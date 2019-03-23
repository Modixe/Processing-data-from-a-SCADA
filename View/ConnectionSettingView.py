# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Венберг\Modixe\ConnectionSetting.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog
class Communicate(QObject):
    # ---Создаем сигналы---
    save_connection_setting_Signal = QtCore.pyqtSignal()

class Ui_Connection_Setting(object):

    def __init__(self):
        self.signal = Communicate()
        self.dialog = QtWidgets.QDialog()
        self.setupUi(self.dialog)

    def signal_save_connection_setting(self):

        # записываем результаты заполнения полей
        self.db_name = self.lineEdit.text()
        self.db_user = self.lineEdit_2.text()
        self.db_password = self.lineEdit_3.text()
        self.Oledb_localhost = self.lineEdit_4.text()
        self.Oledb_user = self.lineEdit_5.text()
        self.db_localhost = self.lineEdit_6.text()

        # отправляем в сигнал, презентор ловит
        self.signal.save_connection_setting_Signal.emit()

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 165)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 141))
        self.groupBox.setObjectName("groupBox")

        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 41, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 41, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 51, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 110, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 51, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 10, 181, 80))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 31, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 50, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 31, 16))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)

        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        # self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        # self.pushButton_4.setGeometry(QtCore.QRect(210, 130, 71, 23))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        # self.pushButton_4.setFont(font)
        # self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 130, 71, 23))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection settings"))
        self.groupBox.setTitle(_translate("Dialog", "БД параметры:"))
        self.label_13.setText(_translate("Dialog", "Host:"))
        self.label_8.setText(_translate("Dialog", "Логин:"))
        self.label_9.setText(_translate("Dialog", "Пароль:"))
        self.label_7.setText(_translate("Dialog", "Бд имя:"))
        self.groupBox_2.setTitle(_translate("Dialog", "OLEdb параметры"))
        self.label_10.setText(_translate("Dialog", "Host:"))
        self.label_12.setText(_translate("Dialog", "User:"))

        # self.pushButton_4.setText(_translate("Dialog", "Обновить"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_3.clicked.connect(self.signal_save_connection_setting)

    def set_db_parameters(self, db_name, db_user, db_password, db_localhost):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("Dialog", db_name))
        self.lineEdit_2.setText(_translate("Dialog", db_user))
        self.lineEdit_6.setText(_translate("Dialog", db_localhost))
        self.lineEdit_3.setText(_translate("Dialog", db_password))


    def set_oledb_parameters(self, Oledb_host, Oledb_user):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_4.setText(_translate("Dialog", Oledb_host))
        self.lineEdit_5.setText(_translate("Dialog", Oledb_user))


    def run_co(self):
        print("+run_co")
        self.dialog.exec_()



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QMainWindow()
#     ui = Ui_Connection_Setting()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())