import sys
from PyQt5.QtWidgets import *


class DialogOpenOneFile(QWidget):
    file_name = None

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

        self.openFileNameDialog()

    def getFileName(self):
        return self.file_name

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                        "All Files (*);;Python Files (*.py)", options=options)
        if self.file_name:
            print(self.file_name)


def main():
    app = QApplication(sys.argv)
    ex = DialogOpenOneFile()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
