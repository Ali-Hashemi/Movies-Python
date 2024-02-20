from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.CustomListView import *
from JsonEditor.ShowJson.MainWindow import Ui_MainWindow

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 0


# ------------- Absolutes --------------- #

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.array = []

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(250, 10, 256, 300))

        self.pushButton_check.clicked.connect(lambda: (self.check_items()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        self.set_combo_items()

    def set_combo_items(self):
        dict = Film.title_translate()
        for i in dict:
            self.comboBox.addItem(i)

    def check_items(self):
        dict = Film.title_translate()

        combo_item = self.comboBox.currentText()

        current_property = dict.get(combo_item)

        Print.print_cyan(str(current_property))
        Print.print_full_line(CustomColor.WHITE)

        del self.array[:]

        for index in range(self.listWidget.count()):
            self.array.append(self.listWidget.item(index).text())

        for i in self.array:
            if os.path.isdir(i):
                folder_path = rename_file_paths_for_files(i)
                folder_name = get_last_file_or_folder_from_path(folder_path)
                for name in os.listdir(folder_path):
                    if name.lower().endswith(".json"):
                        json_file_path = rename_file_paths_by_os(folder_path) + name

                        if os.path.exists(json_file_path):
                            data = (Film.json_file_to_class(json_file_path)).get_all()
                            to_check_data = data.get(current_property)
                            if to_check_data:
                                Print.print_green(folder_name)
                                Print.print_blue(to_check_data)
                                Print.print_full_line(color=CustomColor.WHITE)
            else:
                if i.lower().endswith(".json"):
                    path, filename = get_path_and_file(i)

                    json_file_path = rename_file_paths_by_os(path) + filename

                    parent_folder_name = get_last_file_or_folder_from_path(path)

                    if os.path.exists(json_file_path):
                        data = (Film.json_file_to_class(json_file_path)).get_all()
                        to_check_data = data.get(current_property)
                        if to_check_data:
                            Print.print_green(parent_folder_name)
                            Print.print_blue(to_check_data)
                            Print.print_full_line(color=CustomColor.WHITE)

    def clear_items(self):
        self.listWidget.clear()
        del self.array[:]

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
