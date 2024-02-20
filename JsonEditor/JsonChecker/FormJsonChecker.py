from JsonEditor.JsonChecker.MainWindow import Ui_MainWindow
from Data import Film
from JsonEditor.CustomListView import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.array = []

        self.listWidget_hidden.hide()

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget_hidden.geometry().left(),
                                                                         self.listWidget_hidden.geometry().top(),
                                                                         self.listWidget_hidden.width(),
                                                                         self.listWidget_hidden.height()))

        self.pushButton_check.clicked.connect(lambda: (self.check_items()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        self.pushButton_check_irani.clicked.connect(lambda: (self.check_items_irani()))

        self.set_combo_items()

    def set_combo_items(self):
        dict = Film.title_translate()
        for i in dict:
            self.comboBox.addItem(i)

    def check_items(self):
        dict = Film.title_translate()

        combo_item = self.comboBox.currentText()

        current_property = dict.get(combo_item)

        self.listWidget_result.clear()

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
                            if not to_check_data:
                                self.listWidget_result.addItem(folder_name)
            else:
                if i.lower().endswith(".json"):
                    path, filename = get_path_and_file(i)

                    json_file_path = rename_file_paths_by_os(path) + filename

                    parent_folder_name = get_last_file_or_folder_from_path(path)

                    if os.path.exists(json_file_path):
                        data = (Film.json_file_to_class(json_file_path)).get_all()
                        to_check_data = data.get(current_property)
                        if not to_check_data:
                            self.listWidget_result.addItem(parent_folder_name)

    def check_items_irani(self):
        dict = Film.title_translate()

        combo_item = self.comboBox_irani.currentText()

        current_property = dict.get(combo_item)

        self.listWidget_result_irani.clear()

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
                            character_to_find = ":"
                            if find_in_text(to_check_data, character_to_find):
                                self.listWidget_result_irani.addItem(folder_name)
            else:
                if i.lower().endswith(".json"):
                    path, filename = get_path_and_file(i)

                    json_file_path = rename_file_paths_by_os(path) + filename

                    parent_folder_name = get_last_file_or_folder_from_path(path)

                    if os.path.exists(json_file_path):
                        data = (Film.json_file_to_class(json_file_path)).get_all()
                        to_check_data = data.get(current_property)
                        character_to_find = ":"
                        if find_in_text(to_check_data, character_to_find):
                            self.listWidget_result_irani.addItem(parent_folder_name)

    def clear_items(self):
        self.listWidget.clear()
        self.listWidget_result.clear()
        self.listWidget_result_irani.clear()
        del self.array[:]

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
