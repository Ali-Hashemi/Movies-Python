# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tab\JsonEditor\JsonChecker\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_check = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check.setGeometry(QtCore.QRect(230, 70, 171, 71))
        self.pushButton_check.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(260, 150, 111, 51))
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 20, 181, 41))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget_result = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_result.setGeometry(QtCore.QRect(10, 50, 200, 170))
        self.listWidget_result.setObjectName("listWidget_result")
        self.listWidget_result_irani = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_result_irani.setGeometry(QtCore.QRect(10, 300, 200, 170))
        self.listWidget_result_irani.setObjectName("listWidget_result_irani")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_check_irani = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check_irani.setGeometry(QtCore.QRect(230, 370, 201, 61))
        self.pushButton_check_irani.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_check_irani.setObjectName("pushButton_check_irani")
        self.comboBox_irani = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_irani.setGeometry(QtCore.QRect(240, 310, 181, 41))
        self.comboBox_irani.setObjectName("comboBox_irani")
        self.comboBox_irani.addItem("")
        self.comboBox_irani.addItem("")
        self.comboBox_irani.addItem("")
        self.comboBox_irani.addItem("")
        self.listWidget_hidden = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_hidden.setGeometry(QtCore.QRect(440, 40, 220, 171))
        self.listWidget_hidden.setObjectName("listWidget_hidden")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_check.setText(_translate("MainWindow", "Check"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear List"))
        self.label.setText(_translate("MainWindow", "Result"))
        self.label_2.setText(_translate("MainWindow", "Result Irani"))
        self.pushButton_check_irani.setText(_translate("MainWindow", "Check Irani"))
        self.comboBox_irani.setItemText(0, _translate("MainWindow", "Director"))
        self.comboBox_irani.setItemText(1, _translate("MainWindow", "Actors"))
        self.comboBox_irani.setItemText(2, _translate("MainWindow", "Per Genre"))
        self.comboBox_irani.setItemText(3, _translate("MainWindow", "Per Info"))