# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tab\JsonEditor\Rename\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(250, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_name.setText("")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 40, 361, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 9, 131, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_type_tv = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_type_tv.setGeometry(QtCore.QRect(10, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_type_tv.setFont(font)
        self.radioButton_type_tv.setObjectName("radioButton_type_tv")
        self.radioButton_type_film = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_type_film.setGeometry(QtCore.QRect(10, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_type_film.setFont(font)
        self.radioButton_type_film.setObjectName("radioButton_type_film")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(150, 10, 180, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.radioButton_film_per_sub = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_film_per_sub.setEnabled(False)
        self.radioButton_film_per_sub.setGeometry(QtCore.QRect(10, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_film_per_sub.setFont(font)
        self.radioButton_film_per_sub.setChecked(False)
        self.radioButton_film_per_sub.setObjectName("radioButton_film_per_sub")
        self.radioButton_film_base_folder = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_film_base_folder.setEnabled(False)
        self.radioButton_film_base_folder.setGeometry(QtCore.QRect(10, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_film_base_folder.setFont(font)
        self.radioButton_film_base_folder.setChecked(False)
        self.radioButton_film_base_folder.setObjectName("radioButton_film_base_folder")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(150, 110, 180, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.radioButton_tv_subbed = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_tv_subbed.setEnabled(False)
        self.radioButton_tv_subbed.setGeometry(QtCore.QRect(10, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_tv_subbed.setFont(font)
        self.radioButton_tv_subbed.setObjectName("radioButton_tv_subbed")
        self.radioButton_tv_dubbed = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_tv_dubbed.setEnabled(False)
        self.radioButton_tv_dubbed.setGeometry(QtCore.QRect(10, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_tv_dubbed.setFont(font)
        self.radioButton_tv_dubbed.setObjectName("radioButton_tv_dubbed")
        self.listWidget_hidden = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_hidden.setGeometry(QtCore.QRect(20, 20, 221, 231))
        self.listWidget_hidden.setObjectName("listWidget_hidden")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 270, 286, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_rename = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rename.sizePolicy().hasHeightForWidth())
        self.pushButton_rename.setSizePolicy(sizePolicy)
        self.pushButton_rename.setMinimumSize(QtCore.QSize(171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_rename.setFont(font)
        self.pushButton_rename.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.gridLayout.addWidget(self.pushButton_rename, 0, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(101, 51))
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
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
        self.radioButton_type_tv.setText(_translate("MainWindow", "TV Series"))
        self.radioButton_type_film.setText(_translate("MainWindow", "Film"))
        self.radioButton_film_per_sub.setText(_translate("MainWindow", "Per Sub"))
        self.radioButton_film_base_folder.setText(_translate("MainWindow", "Based on Folder"))
        self.radioButton_tv_subbed.setText(_translate("MainWindow", "Subbed"))
        self.radioButton_tv_dubbed.setText(_translate("MainWindow", "Dubbed"))
        self.pushButton_rename.setText(_translate("MainWindow", "Rename"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear List"))
