# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui.url'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 110, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.llllll = QtWidgets.QLabel(self.centralwidget)
        self.llllll.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.llllll.setObjectName("llllll")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 181, 16))
        self.label_4.setObjectName("label_4")
        self.title = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(193, 10, 171, 21))
        self.title.setObjectName("title")
        self.year = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(190, 60, 171, 21))
        self.year.setObjectName("year")
        self.duration = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(190, 160, 171, 21))
        self.duration.setObjectName("duration")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить элемент"))
        self.llllll.setText(_translate("MainWindow", "Сорт"))
        self.label_2.setText(_translate("MainWindow", "Цена(руб)"))
        self.label_3.setText(_translate("MainWindow", "Молотое(0)\\В зернах(1)"))
        self.label_4.setText(_translate("MainWindow", "В пачке(кг)"))
        self.pushButton.setText(_translate("MainWindow", "добавить"))