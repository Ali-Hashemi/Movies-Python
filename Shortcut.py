from Config import *
from Classes.ClassIMDB import *
from Data.Element import *
from Classes.Class30nama import *
import pathlib
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # basic shortcut
        self.shortcut = QShortcut(QKeySequence('ctrl+o'), self)
        self.shortcut.activated.connect(lambda shortcut_key=self.shortcut.key().toString(): self.display_shortcut(shortcut_key))

        # standard shortcut
        self.shortcut = QShortcut(QKeySequence.Forward, self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.display_shortcut(shortcut_key))

        # standard shortcut
        self.shortcut = QShortcut(QKeySequence('ctrl+shift+T'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.display_shortcut(shortcut_key))

    def display_shortcut(self, mapping):
        print(mapping)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
