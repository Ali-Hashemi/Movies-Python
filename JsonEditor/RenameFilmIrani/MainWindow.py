# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tab\JsonEditor\RenameFilmIrani\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_create_txt_and_json = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_txt_and_json.setGeometry(QtCore.QRect(240, 340, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_create_txt_and_json.setFont(font)
        self.pushButton_create_txt_and_json.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_create_txt_and_json.setObjectName("pushButton_create_txt_and_json")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(460, 340, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.lineEdit_film_eng_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_film_eng_name.setGeometry(QtCore.QRect(420, 110, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_film_eng_name.setFont(font)
        self.lineEdit_film_eng_name.setObjectName("lineEdit_film_eng_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(270, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_name.setText("")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.pushButton_create_per = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_per.setGeometry(QtCore.QRect(270, 410, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_create_per.setFont(font)
        self.pushButton_create_per.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_create_per.setObjectName("pushButton_create_per")
        self.lineEdit_film_per_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_film_per_name.setGeometry(QtCore.QRect(420, 50, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_film_per_name.setFont(font)
        self.lineEdit_film_per_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_film_per_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_film_per_name.setObjectName("lineEdit_film_per_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_film_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_film_date.setGeometry(QtCore.QRect(470, 170, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_film_date.setFont(font)
        self.lineEdit_film_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_film_date.setObjectName("lineEdit_film_date")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.checkBox_copy_folder_name = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_copy_folder_name.setGeometry(QtCore.QRect(60, 0, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_copy_folder_name.setFont(font)
        self.checkBox_copy_folder_name.setStyleSheet("color: rgb(85, 0, 255);")
        self.checkBox_copy_folder_name.setChecked(False)
        self.checkBox_copy_folder_name.setObjectName("checkBox_copy_folder_name")
        self.pushButton_create_doostiha_date = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_doostiha_date.setGeometry(QtCore.QRect(270, 470, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_create_doostiha_date.setFont(font)
        self.pushButton_create_doostiha_date.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_create_doostiha_date.setObjectName("pushButton_create_doostiha_date")
        self.pushButton_create_txt_from_json = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_txt_from_json.setGeometry(QtCore.QRect(270, 520, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_create_txt_from_json.setFont(font)
        self.pushButton_create_txt_from_json.setStyleSheet("background-color: rgb(255, 85, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_create_txt_from_json.setObjectName("pushButton_create_txt_from_json")
        self.listWidget_hidden = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_hidden.setGeometry(QtCore.QRect(20, 30, 241, 221))
        self.listWidget_hidden.setObjectName("listWidget_hidden")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 230, 181, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_filter_per_names = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_filter_per_names.sizePolicy().hasHeightForWidth())
        self.pushButton_filter_per_names.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_filter_per_names.setFont(font)
        self.pushButton_filter_per_names.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_filter_per_names.setObjectName("pushButton_filter_per_names")
        self.verticalLayout.addWidget(self.pushButton_filter_per_names)
        self.pushButton_filter_eng_names = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_filter_eng_names.sizePolicy().hasHeightForWidth())
        self.pushButton_filter_eng_names.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_filter_eng_names.setFont(font)
        self.pushButton_filter_eng_names.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_filter_eng_names.setObjectName("pushButton_filter_eng_names")
        self.verticalLayout.addWidget(self.pushButton_filter_eng_names)
        self.pushButton_filter_dates = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_filter_dates.sizePolicy().hasHeightForWidth())
        self.pushButton_filter_dates.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_filter_dates.setFont(font)
        self.pushButton_filter_dates.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_filter_dates.setObjectName("pushButton_filter_dates")
        self.verticalLayout.addWidget(self.pushButton_filter_dates)
        self.lineEdit_film_eng_name.raise_()
        self.pushButton_create_txt_and_json.raise_()
        self.pushButton_clear.raise_()
        self.label_name.raise_()
        self.pushButton_filter_per_names.raise_()
        self.pushButton_filter_dates.raise_()
        self.pushButton_create_per.raise_()
        self.pushButton_filter_eng_names.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_film_date.raise_()
        self.label_3.raise_()
        self.checkBox_copy_folder_name.raise_()
        self.lineEdit_film_per_name.raise_()
        self.pushButton_create_doostiha_date.raise_()
        self.pushButton_create_txt_from_json.raise_()
        self.listWidget_hidden.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_film_per_name, self.lineEdit_film_eng_name)
        MainWindow.setTabOrder(self.lineEdit_film_eng_name, self.lineEdit_film_date)
        MainWindow.setTabOrder(self.lineEdit_film_date, self.pushButton_filter_per_names)
        MainWindow.setTabOrder(self.pushButton_filter_per_names, self.pushButton_filter_dates)
        MainWindow.setTabOrder(self.pushButton_filter_dates, self.pushButton_create_per)
        MainWindow.setTabOrder(self.pushButton_create_per, self.pushButton_filter_eng_names)
        MainWindow.setTabOrder(self.pushButton_filter_eng_names, self.pushButton_create_txt_and_json)
        MainWindow.setTabOrder(self.pushButton_create_txt_and_json, self.pushButton_clear)
        MainWindow.setTabOrder(self.pushButton_clear, self.checkBox_copy_folder_name)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_create_txt_and_json.setText(_translate("MainWindow", "Create TXT && JSON"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear List"))
        self.pushButton_create_per.setText(_translate("MainWindow", "Create Per Name && Date from Folder"))
        self.label.setText(_translate("MainWindow", "Per Name :"))
        self.label_2.setText(_translate("MainWindow", "Eng Name :"))
        self.label_3.setText(_translate("MainWindow", "Date :"))
        self.checkBox_copy_folder_name.setText(_translate("MainWindow", "Copy Folder Name"))
        self.pushButton_create_doostiha_date.setText(_translate("MainWindow", "Create Doostiha Date TXT && JSON"))
        self.pushButton_create_txt_from_json.setText(_translate("MainWindow", "Create TXT From JSON"))
        self.pushButton_filter_per_names.setText(_translate("MainWindow", "Filter Empty Per Names"))
        self.pushButton_filter_eng_names.setText(_translate("MainWindow", "Filter Empty Eng Names"))
        self.pushButton_filter_dates.setText(_translate("MainWindow", "Filter Empty Dates"))
