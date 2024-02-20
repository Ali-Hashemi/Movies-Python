from Config import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Classes.ClassUtility import *


class ListBoxWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None, rect: QtCore.QRect = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(rect)

        font = QtGui.QFont()
        font.setPointSize(CustomStyle.list_widget_font_size)
        self.setFont(font)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
                    # Print.print_red("Non local file")
            self.addItems(links)
        else:
            event.ignore()
