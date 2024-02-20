from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.PosterRenaming.MainWindow import Ui_MainWindow
from JsonEditor.CustomListView import *
from Classes.ClassDoostiha import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.listWidget_hidden.hide()

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget_hidden.geometry().left(),
                                                                         self.listWidget_hidden.geometry().top(),
                                                                         self.listWidget_hidden.width(),
                                                                         self.listWidget_hidden.height()))

        self.listWidget.itemSelectionChanged.connect(lambda: (self.get_items()))

        self.shortcut = QShortcut(QKeySequence('F1'), self)
        self.shortcut.activated.connect(lambda: (self.rename_items()))

        self.shortcut = QShortcut(QKeySequence('F2'), self)
        self.shortcut.activated.connect(lambda: (self.rename_current_item()))

        self.shortcut = QShortcut(QKeySequence('F3'), self)
        self.shortcut.activated.connect(lambda: (self.remove_code()))

        self.shortcut = QShortcut(QKeySequence('F4'), self)
        self.shortcut.activated.connect(lambda: (self.remove_selected_item()))

        self.pushButton_rename_current_item.clicked.connect(lambda: (self.rename_current_item()))
        self.pushButton_remove_code.clicked.connect(lambda: (self.remove_code()))

        self.pushButton_fix.clicked.connect(lambda: (self.rename_items()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        self.pushButton_count.clicked.connect(lambda: (self.count_items()))

    def get_items(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            self.clear_text_boxes()
            current_row = self.listWidget.currentRow()
            if self.listWidget.item(current_row):
                item = self.listWidget.item(current_row).text()

                path, folder_name = get_path_and_file(item)

                if os.path.isdir(item):

                    self.label_name.setText(folder_name)

                    current_poster_code = File.trim_poster_code(folder_name)

                    if current_poster_code:
                        only_digit = File.trim_only_digits(current_poster_code)

                        if only_digit:
                            self.spinBox_item_number.setValue(int(only_digit))

                    else:
                        self.spinBox_item_number.setValue(int(0))

    def count_items(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            self.label_counter.setText(str(list_count))

    def rename_current_item(self):
        if len(self.listWidget.selectedItems()) > 0:
            current_row = self.listWidget.currentRow()
            item = self.listWidget.item(current_row).text()

            path, folder_name = get_path_and_file(item)

            if os.path.isdir(item):
                current_poster_code = File.trim_poster_code(folder_name)

                if current_poster_code:
                    only_letters = File.trim_only_letters(current_poster_code)

                    spinner_number = strip_text(self.spinBox_item_number.value())

                    new_poster_name = only_letters + spinner_number

                    new_name = folder_name.replace(current_poster_code, new_poster_name)

                    move_or_rename_files(item, path, new_name)

            self.clear_text_boxes()
            self.remove_selected_item()

    def remove_code(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                path, folder_name = get_path_and_file(item)

                if os.path.isdir(item):
                    current_poster_code = "(" + File.trim_poster_code(folder_name) + ") - "

                    if current_poster_code:
                        new_name = folder_name.replace(current_poster_code, "")

                        move_or_rename_files(item, path, new_name)

        self.listWidget.clear()

    def rename_items(self):
        character = strip_text(self.lineEdit_character.text()).upper()
        starting_number = int(strip_text(self.spinBox_starting_number.text()))
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                path, folder_name = get_path_and_file(item)

                if os.path.isdir(item):
                    current_poster_code = File.trim_poster_code(folder_name)

                    new_number = str(starting_number + index)

                    new_poster_name = character + new_number

                    if current_poster_code:
                        new_name = folder_name.replace(current_poster_code, new_poster_name)
                    else:
                        new_name = "(" + new_poster_name + ") - " + folder_name

                    move_or_rename_files(item, path, new_name)

        self.listWidget.clear()

    def remove_selected_item(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            current_row = self.listWidget.currentRow()

            self.listWidget.takeItem(current_row)

    def clear_items(self):
        self.listWidget.clear()
        self.clear_text_boxes()

    def clear_text_boxes(self):
        self.label_counter.clear()
        self.label_name.clear()

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
