from PyQt5 import QtWidgets, QtCore
from Config import *


class MyButton(QtWidgets.QPushButton):
    def __init__(self, parent, title=None, width_postition=None, height_position=None, width=None, height=None,
                 back_color=None, front_color=None):
        super(MyButton, self).__init__(parent)

        self.setWindowTitle(title)
        self.setGeometry(QtCore.QRect(width_postition, height_position, width, height))

        # self.setStyleSheet("background-color: " + str(back_color) + ";\n"
        #                                                             "color: " + str(front_color) + ";\n"
        #                                                                                            "")

        # command = "background-color: " + CustomColorRGB.BLUE + ";"
        #
        # self.setStyleSheet(command)

        # self._height_position = height_position
        # self._width = width
        # self._height = height
