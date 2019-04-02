# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\ReadWrite_v.1.3.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QAbstractItemView


class Communicate(QObject):
    # ---Создаем сигналы---
    save_read_write_Signal = QtCore.pyqtSignal()
    # delete_row_signal = QtCore.pyqtSignal()


class Ui_Dialog(object):
    def __init__(self):
        self.signal = Communicate()
        self.dialog = QtWidgets.QDialog()
        # self.number_lines = number_lines
        self.setupUi(self.dialog)

    def delete_row(self):

        index_list = []
        # Получаем индекс выделенных строк
        for model_index in self.tableWidget.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)

        # Удаляем выделенные строки по полученному индексу
        for index in index_list:
            self.tableWidget.removeRow(index.row())

    def add_line(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def signal_save_read_write(self):

        # записываем результаты заполнения полей
        print("+ signal_save_read_write")
        self.table_name = self.lineEdit.text()
        self.from_date = self.dateTimeEdit.text()
        self.to_date = self.dateTimeEdit_2.text()

        self.tags_key = self.tableWidget.item(0, 0)
        self.tags_val = self.tableWidget.item(0, 1)

        self.tag_dict = {}

        rowCount = self.tableWidget.rowCount()

        # Заполняем словарь тегами из таблицы
        for i in range(0, rowCount):
            item = self.tableWidget.item(i, 0)
            if item is None:
                print("Пустая строка")
            else:
                t = item.text()
                item2 = self.tableWidget.item(i, 1)
                t2 = item2.text()
                self.tag_dict[t] = t2

        # отправляем в сигнал, презентор ловит
        self.signal.save_read_write_Signal.emit()

    def set_read_write(self, table_name, from_date, to_date):
        _translate = QtCore.QCoreApplication.translate

        self.lineEdit.setText(_translate("Dialog", table_name))

        formated_from_date = QtCore.QDateTime(from_date.year, from_date.month, from_date.day, from_date.hour,
                                              from_date.minute,
                                              from_date.second)
        self.dateTimeEdit.setDateTime(formated_from_date)

        formated_to_date = QtCore.QDateTime(to_date.year, to_date.month, to_date.day, to_date.hour, to_date.minute,
                                            to_date.second)
        self.dateTimeEdit_2.setDateTime(formated_to_date)

    # Заполняем таблицу
    def add_row(self, tag_names):
        # tag_names_key, tag_names_val
        _translate = QtCore.QCoreApplication.translate

        # for index, (key, value) in enumerate(some_dict.items()):
        #    print(index, key, value)

        for i, (key, val) in enumerate(tag_names.items()):
            self.tableWidget.setRowCount(i + 1)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)

            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", key))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)

            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Dialog", val))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(489, 400)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        Dialog.setPalette(palette)

        font = QtGui.QFont()
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)

        Dialog.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 370, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_line)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 370, 31, 23))
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete_row)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 370, 71, 23))
        self.pushButton_3.clicked.connect(self.signal_save_read_write)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 461, 260))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 461, 260))
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))

        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.tableWidget.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.tableWidget.setFont(font)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)

        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)

        self.tableWidget.horizontalHeader().setMinimumSectionSize(37)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(250, 10, 221, 81))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)

        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 21, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(50, 20, 161, 22))

        font = QtGui.QFont()
        font.setItalic(False)

        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(1, 0, 1)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 1)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 21, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(50, 50, 161, 22))

        font = QtGui.QFont()
        font.setItalic(False)

        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setWrapping(False)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(1, 0, 1)))
        self.dateTimeEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 1)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 221, 80))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)

        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 41, 20))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Read and write"))
        self.pushButton.setText(_translate("Dialog", "+"))
        self.pushButton_2.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя тега"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Описание"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("Dialog", "Временной интервал:"))
        self.label_9.setText(_translate("Dialog", "До:"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy HH:mm:ss"))
        self.label_8.setText(_translate("Dialog", "От:"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy HH:mm:ss"))
        self.groupBox_2.setTitle(_translate("Dialog", "Параметры таблицы:"))
        self.label_6.setText(_translate("Dialog", "Имя :"))
        self.lineEdit.setText(_translate("Dialog", "Valie"))

    def run_rw(self):
        print("+run_rw")
        self.dialog.exec_()
