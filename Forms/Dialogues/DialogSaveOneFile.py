import sys
from PyQt5.QtWidgets import *


class DialogOpenOneFile(QWidget):

    save_file_name = None

    def __init__(self):
        super().__init__()

        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()

        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = qt_rectangle.left()
        self.top = qt_rectangle.top()
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNamesDialog()

    def getFileName(self):
        return self.file_names

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        save_file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if save_file_name:
            print(save_file_name)