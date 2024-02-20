import sys

from Config import *

from Classes.ClassUtility import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "My Code Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        txt_username = QLineEdit(self)
        txt_username.setPlaceholderText("username")
        txt_username.move(100, 100)

        txt_password = QLineEdit(self)
        txt_password.setPlaceholderText("password")
        txt_password.move(100, 150)

        btn = QPushButton("Click me", self)
        btn.move(100, 200)

        btn.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        Print.print_white("Hello iran")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())
