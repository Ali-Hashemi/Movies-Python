from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.RenameFilmIrani.MainWindow import Ui_MainWindow
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

        self.lineEdit_film_per_name.returnPressed.connect(lambda: (self.create_items()))
        self.lineEdit_film_eng_name.returnPressed.connect(lambda: (self.create_items()))
        self.lineEdit_film_date.returnPressed.connect(lambda: (self.create_items()))

        self.shortcut = QShortcut(QKeySequence('F1'), self)
        self.shortcut.activated.connect(lambda: (self.rename_to_per_name_and_date()))

        self.shortcut = QShortcut(QKeySequence('F2'), self)
        self.shortcut.activated.connect(lambda: (self.rename_to_eng_name_and_date()))

        # self.shortcut = QShortcut(QKeySequence('F3'), self)
        # self.shortcut.activated.connect(lambda: (self.create_items()))

        self.shortcut = QShortcut(QKeySequence('F4'), self)
        self.shortcut.activated.connect(lambda: (self.remove_selected_item()))

        self.shortcut = QShortcut(QKeySequence('F9'), self)
        self.shortcut.activated.connect(lambda: (self.create_per_items_batch()))

        self.shortcut = QShortcut(QKeySequence('F10'), self)
        self.shortcut.activated.connect(lambda: (self.create_eng_items_batch()))

        self.shortcut = QShortcut(QKeySequence('F8'), self)
        self.shortcut.activated.connect(lambda: (self.get_doostiha_date()))

        self.pushButton_create_doostiha_date.clicked.connect(lambda: (self.get_doostiha_date()))

        self.pushButton_filter_per_names.clicked.connect(lambda: (self.scan_empty_fields(check_per_name=1)))
        self.pushButton_filter_eng_names.clicked.connect(lambda: (self.scan_empty_fields(check_eng_name=1)))
        self.pushButton_filter_dates.clicked.connect(lambda: (self.scan_empty_fields(check_date=1)))

        self.pushButton_create_txt_and_json.clicked.connect(lambda: (self.create_items()))
        self.pushButton_create_per.clicked.connect(lambda: (self.create_per_items_from_folder()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        self.pushButton_create_txt_from_json.clicked.connect(lambda: (self.create_eng_per_date_from_json()))

    def scan_empty_fields(self, check_per_name=0, check_eng_name=0, check_date=0):
        list_array = []

        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    if check_eng_name:
                        txt_eng_name = rename_file_paths_by_os(item) + CustomNames.TXT_ENG_NAME
                        if os.path.exists(txt_eng_name):
                            text_value = strip_text(File.load_from_file(txt_eng_name))

                            if not text_value:
                                list_array.append(item)
                        else:
                            list_array.append(item)

                    elif check_per_name:
                        txt_eng_name = rename_file_paths_by_os(item) + CustomNames.TXT_PER_NAME
                        if os.path.exists(txt_eng_name):
                            text_value = strip_text(File.load_from_file(txt_eng_name))

                            if not text_value:
                                list_array.append(item)
                        else:
                            list_array.append(item)
                    elif check_date:
                        txt_date = rename_file_paths_by_os(item) + CustomNames.TXT_DATE
                        if os.path.exists(txt_date):
                            text_value = strip_text(File.load_from_file(txt_date))

                            if not text_value:
                                list_array.append(item)
                        else:
                            list_array.append(item)

        self.clear_items()

        for i in list_array:
            item = QListWidgetItem(str(i))
            self.listWidget.addItem(item)

    def rename_to_eng_name_and_date(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    location, path = get_path_and_file(item)

                    full_path = rename_file_paths_by_os(location + path)

                    eng_name_txt_path = str(full_path + CustomNames.TXT_ENG_NAME)
                    date_txt_path = str(full_path + CustomNames.TXT_DATE)

                    if os.path.exists(eng_name_txt_path) and os.path.exists(date_txt_path):
                        eng_name_value = str(File.load_from_file(eng_name_txt_path))
                        date_value = str(File.load_from_file(date_txt_path))

                        film_poster_code = File.trim_poster_code(path)

                        if film_poster_code:
                            full_name = "(" + film_poster_code + ") - " + eng_name_value + " (" + date_value + ")"

                            move_or_rename_files(item, location, full_name)
                        else:
                            full_name = eng_name_value + " (" + date_value + ")"

                            move_or_rename_files(item, location, full_name)

                    else:
                        json_file = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA

                        if os.path.exists(json_file):
                            film_json = Film.json_file_to_class(json_file)

                            if film_json.eng_title and film_json.release:
                                film_poster_code = File.trim_poster_code(path)

                                if film_poster_code:
                                    full_name = "(" + film_poster_code + ") - " + film_json.eng_title + " (" + film_json.release + ")"

                                    move_or_rename_files(item, location, full_name)
                                else:
                                    full_name = film_json.eng_title + " (" + film_json.release + ")"

                                    move_or_rename_files(item, location, full_name)

        self.clear_items()

    def rename_to_per_name_and_date(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    location, path = get_path_and_file(item)

                    full_path = rename_file_paths_by_os(location + path)

                    per_name_txt_path = str(full_path + CustomNames.TXT_PER_NAME)
                    date_txt_path = str(full_path + CustomNames.TXT_DATE)

                    if os.path.exists(per_name_txt_path) and os.path.exists(date_txt_path):
                        per_name_value = str(File.load_from_file(per_name_txt_path))
                        date_value = str(File.load_from_file(date_txt_path))

                        film_poster_code = File.trim_poster_code(path)

                        if film_poster_code:
                            full_name = "(" + film_poster_code + ") - " + per_name_value + " (" + date_value + ")"

                            move_or_rename_files(item, location, full_name)
                        else:
                            full_name = per_name_value + " (" + date_value + ")"

                            move_or_rename_files(item, location, full_name)

                    else:
                        json_file = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA

                        if os.path.exists(json_file):
                            film_json = Film.json_file_to_class(json_file)

                            if film_json.per_title and film_json.release:
                                film_poster_code = File.trim_poster_code(path)

                                if film_poster_code:
                                    full_name = "(" + film_poster_code + ") - " + film_json.per_title + " (" + film_json.release + ")"

                                    move_or_rename_files(item, location, full_name)
                                else:
                                    full_name = film_json.per_title + " (" + film_json.release + ")"

                                    move_or_rename_files(item, location, full_name)

        self.clear_items()

    def create_per_items_from_folder(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    location, path = get_path_and_file(item)

                    full_path = rename_file_paths_by_os(location + path)
                    if os.path.exists(full_path):
                        name_without_date = File.get_file_name(File.trim_name_movie(path))
                        date = File.trim_released_date(path)

                        per_name_txt_path = str(full_path + CustomNames.TXT_PER_NAME)
                        per_date_txt_path = str(full_path + CustomNames.TXT_DATE)
                        json_file_path = str(rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA)

                        if name_without_date:
                            File.save_to_file(name_without_date, per_name_txt_path)
                        if date:
                            File.save_to_file(date, per_date_txt_path)

                        if os.path.exists(json_file_path):
                            film = Film.json_file_to_class(json_file_path)

                            if name_without_date:
                                film.per_title = name_without_date
                            if date:
                                film.release = date

                            Json.write_to_json_file(film, json_file_path)
                        else:
                            film = Film()

                            if name_without_date:
                                film.per_title = name_without_date
                            if date:
                                film.release = date

                            Json.write_to_json_file(film, json_file_path)

                        # name_content = File.load_from_file(per_name_txt_path)
                        # date_content = File.load_from_file(per_date_txt_path)

        self.clear_items()

    def create_per_items_batch(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    location, path = get_path_and_file(item)

                    full_path = rename_file_paths_by_os(location + path)

                    if os.path.exists(full_path):
                        per_name_txt_path = str(full_path + CustomNames.TXT_PER_NAME)
                        date_txt_path = str(full_path + CustomNames.TXT_DATE)
                        json_file_path = str(rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA)

                        name_from_folder = File.get_file_name(File.trim_name_movie(path))
                        date_from_folder = File.trim_released_date(path)

                        film = None

                        if os.path.exists(json_file_path):
                            film = Film.json_file_to_class(json_file_path)

                            if name_from_folder and not film.per_title:
                                film.per_title = name_from_folder

                            if date_from_folder and not film.release:
                                film.release = date_from_folder
                        else:
                            film = Film()

                            if name_from_folder and not film.per_title:
                                film.per_title = name_from_folder

                            if date_from_folder and not film.release:
                                film.release = date_from_folder

                        if os.path.exists(per_name_txt_path):
                            per_name_value = str(File.load_from_file(per_name_txt_path))
                            if per_name_value and not film.per_title:
                                film.per_title = per_name_value
                        else:
                            if name_from_folder:
                                File.save_to_file(name_from_folder, per_name_txt_path)

                        if os.path.exists(date_txt_path):
                            date_value = str(File.load_from_file(date_txt_path))
                            if date_value and not film.release:
                                film.release = date_value
                        else:
                            if date_from_folder:
                                File.save_to_file(date_from_folder, date_txt_path)

                        Json.write_to_json_file(film, json_file_path)

                        # name_content = File.load_from_file(per_name_txt_path)
                        # date_content = File.load_from_file(per_date_txt_path)

        self.clear_items()

    def create_eng_items_batch(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    location, path = get_path_and_file(item)

                    full_path = rename_file_paths_by_os(location + path)

                    eng_name_txt_path = str(full_path + CustomNames.TXT_ENG_NAME)
                    date_txt_path = str(full_path + CustomNames.TXT_DATE)
                    json_file_path = str(rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA)

                    film = None

                    if os.path.exists(json_file_path):
                        film = Film.json_file_to_class(json_file_path)
                    else:
                        film = Film()

                    if os.path.exists(eng_name_txt_path):
                        eng_name_value = str(File.load_from_file(eng_name_txt_path))

                        if eng_name_value and not film.eng_title:
                            film.eng_title = eng_name_value

                    if os.path.exists(date_txt_path):
                        date_value = str(File.load_from_file(date_txt_path))

                        if date_value and not film.release:
                            film.release = date_value
                    else:
                        date_from_folder = File.trim_released_date(path)
                        if date_from_folder:
                            File.save_to_file(date_from_folder, date_txt_path)

                            if not film.release:
                                film.release = date_from_folder

                    Json.write_to_json_file(film, json_file_path)

                    # film_poster_code = File.trim_poster_code(path)
                    #
                    # if film_poster_code:
                    #     full_name = "(" + film_poster_code + ") - " + per_name_value + " (" + per_date_value + ")"
                    #
                    #     move_or_rename_files(item, location, full_name)
                    # else:
                    #     full_name = per_name_value + " (" + per_date_value + ")"
                    #
                    #     move_or_rename_files(item, location, full_name)

        self.clear_items()

    def create_items(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            current_row = self.listWidget.currentRow()
            if self.listWidget.item(current_row):
                item = self.listWidget.item(current_row).text()

                if os.path.isdir(item):
                    per_name = strip_text(self.lineEdit_film_per_name.text())
                    eng_name = strip_text(self.lineEdit_film_eng_name.text())
                    date = strip_text(self.lineEdit_film_date.text())

                    per_name_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_PER_NAME)
                    eng_name_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_ENG_NAME)
                    date_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_DATE)
                    json_file_path = str(rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA)

                    if per_name:
                        File.save_to_file(per_name, per_name_txt_path)

                    if eng_name:
                        File.save_to_file(eng_name, eng_name_txt_path)

                    if date:
                        File.save_to_file(date, date_txt_path)

                    if os.path.exists(json_file_path):
                        film = Film.json_file_to_class(json_file_path)

                        if per_name:
                            film.per_title = per_name
                        if eng_name:
                            film.eng_title = eng_name
                        if date:
                            film.release = date

                        Json.write_to_json_file(film, json_file_path)
                    else:
                        film = Film()

                        if per_name:
                            film.per_title = per_name
                        if eng_name:
                            film.eng_title = eng_name
                        if date:
                            film.release = date

                        Json.write_to_json_file(film, json_file_path)

                    self.clear_text_boxes()
                    self.remove_selected_item()

    def get_items(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            self.clear_text_boxes()
            current_row = self.listWidget.currentRow()
            if self.listWidget.item(current_row):
                item = self.listWidget.item(current_row).text()

                if os.path.isdir(item):
                    folder_name = get_last_file_or_folder_from_path(str(item))
                    self.label_name.setText(folder_name)

                    per_name_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_PER_NAME)
                    eng_name_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_ENG_NAME)
                    date_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_DATE)

                    if os.path.exists(per_name_txt_path):
                        per_name_txt_value = strip_text(File.load_from_file(per_name_txt_path))
                        self.lineEdit_film_per_name.setText(per_name_txt_value)

                    if not strip_text(self.lineEdit_film_per_name.text()):
                        if self.checkBox_copy_folder_name.isChecked():
                            film_name = File.trim_name_tv_series(folder_name)
                            self.lineEdit_film_per_name.setText(film_name)

                    if os.path.exists(eng_name_txt_path):
                        eng_name_txt_value = strip_text(File.load_from_file(eng_name_txt_path))
                        self.lineEdit_film_eng_name.setText(eng_name_txt_value)

                    if os.path.exists(date_txt_path):
                        date_txt_value = strip_text(File.load_from_file(date_txt_path))
                        self.lineEdit_film_date.setText(date_txt_value)

    def get_doostiha_date(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    date_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_DATE)

                    Print.print_green(get_last_file_or_folder_from_path(item))

                    if not os.path.exists(date_txt_path):

                        doostiha_html = str(rename_file_paths_by_os(item) + CustomNames.HTML_DOOSTIHA_FILE_NAME)
                        json_file_path = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA

                        if os.path.exists(json_file_path):
                            film = Film.json_file_to_class(json_file_path)
                        else:
                            film = Film()

                        if os.path.exists(doostiha_html):
                            doostiha_soup = Html.get_soup_from_file(doostiha_html)
                            doostiha_date = ClassDoostiha.get_release_date(doostiha_soup)
                            if doostiha_date:
                                File.save_to_file(doostiha_date, date_txt_path)
                                film.release = doostiha_date

                        if film.release:
                            Json.write_to_json_file(film, json_file_path)

                    Print.print_full_line(CustomColor.CYAN)

        self.clear_items()

    def create_eng_per_date_from_json(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    per_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_PER_NAME)
                    eng_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_ENG_NAME)
                    date_txt_path = str(rename_file_paths_by_os(item) + CustomNames.TXT_DATE)

                    json_path = str(rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA)

                    if os.path.exists(json_path):
                        Print.print_green(get_last_file_or_folder_from_path(item))

                        film_json = Film.json_file_to_class(json_path)

                        if film_json.per_title:
                            File.save_to_file(film_json.per_title, per_txt_path)
                        if film_json.eng_title:
                            File.save_to_file(film_json.eng_title, eng_txt_path)
                        if film_json.release:
                            File.save_to_file(film_json.release, date_txt_path)

                        Print.print_full_line(CustomColor.WHITE)

        self.clear_items()

    def remove_selected_item(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            current_row = self.listWidget.currentRow()

            self.listWidget.takeItem(current_row)

    def clear_items(self):
        self.listWidget.clear()
        self.clear_text_boxes()

    def clear_text_boxes(self):
        self.label_name.clear()
        self.lineEdit_film_per_name.clear()
        self.lineEdit_film_eng_name.clear()
        self.lineEdit_film_date.clear()

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
