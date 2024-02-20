from Classes.ClassUtility import *
from Data.Element import Element
import sys
import time
from Data import Film
import sys
from PyQt5 import QtWidgets
from QtCreator.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
