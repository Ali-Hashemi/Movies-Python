# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tab\JsonEditor\GetImdbFromHtml\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_get_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_get_data.setGeometry(QtCore.QRect(360, 120, 241, 91))
        self.pushButton_get_data.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_get_data.setObjectName("pushButton_get_data")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(400, 240, 171, 81))
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
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
        self.pushButton_get_data.setText(_translate("MainWindow", "Get Data"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear List"))
