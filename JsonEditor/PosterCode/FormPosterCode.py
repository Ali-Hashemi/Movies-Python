from PyQt5 import QtWidgets
from JsonEditor.PosterCode.MainWindow import Ui_MainWindow
from Classes.ClassUtility import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    HIGHEST_NUMBER = 0
    ALL_FOUND_NUMBERS_ARRAY = []
    FIRST_NUMBER = None

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_find.clicked.connect(lambda: (self.get_poster_codes()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_boxes()))

    def get_poster_codes(self):
        self.HIGHEST_NUMBER = 0
        self.ALL_FOUND_NUMBERS_ARRAY = []

        self.listWidget_result.clear()

        poster_character = str(self.lineEdit.text())

        path = str(self.lineEdit_path.text())

        self.get_highest_number(path, poster_character)

        if self.HIGHEST_NUMBER > 0:
            self.label_found.setText(str(self.HIGHEST_NUMBER))

        unique_array = list(set(self.ALL_FOUND_NUMBERS_ARRAY))

        if unique_array:
            self.FIRST_NUMBER = unique_array[0]

            not_given_numbers = []

            if self.FIRST_NUMBER and unique_array:
                for x in range(self.FIRST_NUMBER, self.HIGHEST_NUMBER):
                    if x not in unique_array:
                        not_given_numbers.append(x)

            for i in not_given_numbers:
                self.listWidget_result.addItem(str(i))

    def get_highest_number(self, path, character=""):
        if not find_in_text(path,"System Volume Information"):
            if not find_in_text(path,"$RECYCLE.BIN"):
                for file in os.listdir(path):
                    d = os.path.join(path, file)
                    if os.path.isdir(d):
                        # print(d)

                        character = str(character).upper()
                        regex = ""

                        regex_only_number = "\d{4}"

                        if len(character) > 1:
                            character1 = "[" + character[0] + "]"
                            character2 = "[" + character[1] + "]"
                            regex = "^\(" + character1 + character2 + "\d{4}\)"
                        elif len(character) == 1:
                            regex = "^[(][" + character + "]\d{4}[)]"
                        else:
                            regex = "^[(][a-zA-Z]\d{4}[)]"

                        find = re.findall(regex, file)

                        if find:
                            find_only_number = re.findall(regex_only_number, find[0])

                            if find_only_number:
                                found_number = int(find_only_number[0])

                                self.ALL_FOUND_NUMBERS_ARRAY.append(found_number)

                                if found_number > self.HIGHEST_NUMBER:
                                    self.HIGHEST_NUMBER = found_number

                        self.get_highest_number(d, character)

    def clear_boxes(self):
        self.HIGHEST_NUMBER = 0
        self.ALL_FOUND_NUMBERS_ARRAY = []

        self.lineEdit.clear()
        self.lineEdit_path.clear()
        self.label_found.clear()
        self.listWidget_result.clear()


# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
