from JsonEditor.JsonEditor.MainWindow import Ui_MainWindow
from JsonEditor.JsonEditor.CustomListViewJsonEditor import *
from Classes.ClassIMDB import *
from Classes.Class30nama import *
from Classes.ClassHex import *
from Classes.ClassSearchWeb import *
from Classes.ClassExtract import ClassExtract


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    SEARCH_TYPE_FINAL = 1
    WEB_TYPE_FINAL = 1

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.lineEdit_check_problem.setText(":")

        self.initialize_search()

        self.listWidget.hide()

        self.listWidget_items = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget.geometry().left(),
                                                                               self.listWidget.geometry().top(),
                                                                               self.listWidget.width(),
                                                                               self.listWidget.height()))

        self.label_name.setStyleSheet(StyleSheet.TEXT_EDITOR_NO_BORDER)

        self.listWidget_items.itemSelectionChanged.connect(
            lambda: (self.get_items()))

        self.pushButton_go_to_imdb.clicked.connect(
            lambda: (self.open_in_browser(self.lineEdit_imdb_link.text())))
        self.pushButton_go_to_30nama.clicked.connect(
            lambda: (self.open_in_browser(self.lineEdit_30nama_link.text())))

        self.pushButton_save.clicked.connect(lambda: (self.save_item()))

        self.shortcut = QShortcut(QKeySequence('ctrl+s'), self)
        self.shortcut.activated.connect(lambda: (self.save_item()))

        self.shortcut = QShortcut(QKeySequence('ctrl+d'), self)
        self.shortcut.activated.connect(lambda: (self.remove_selected_item()))

        self.shortcut = QShortcut(QKeySequence('F4'), self)
        self.shortcut.activated.connect(lambda: (self.remove_selected_item()))

        self.shortcut = QShortcut(QKeySequence('ctrl+w'), self)
        self.shortcut.activated.connect(lambda: (self.clear_items()))

        self.shortcut = QShortcut(QKeySequence('F1'), self)
        self.shortcut.activated.connect(lambda: (self.copy_folder_name()))

        self.shortcut = QShortcut(QKeySequence('F2'), self)
        self.shortcut.activated.connect(lambda: (self.change_folder_name()))

        self.pushButton_rename_to_ok.clicked.connect(lambda: (self.rename_to_fixed(check=1)))
        self.pushButton_rename_to_not_ok.clicked.connect(lambda: (self.rename_to_fixed(check=0)))

        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))
        self.pushButton_delete.clicked.connect(lambda: (self.delete_item()))
        self.pushButton_clear_but_30nama.clicked.connect(
            lambda: (self.clear_all_but_30nama_link()))
        self.pushButton_scan_30nama.clicked.connect(
            lambda: (self.scan_empty_fields(check_30nama=1)))
        self.pushButton_scan_imdb.clicked.connect(
            lambda: (self.scan_empty_fields(check_imdb=1)))
        self.pushButton_scan_per_title.clicked.connect(
            lambda: (self.scan_empty_fields(check_per_title=1)))
        self.pushButton_scan_have_per_title.clicked.connect(
            lambda: (self.scan_empty_fields(have_per_title=1)))
        self.pushButton_scan_director.clicked.connect(
            lambda: (self.scan_empty_fields(check_director=1)))
        self.pushButton_scan_not_equal_names.clicked.connect(
            lambda: (self.scan_empty_fields(check_names=1)))
        self.pushButton_scan_parent_guide.clicked.connect(
            lambda: (self.scan_empty_fields(check_parent=1)))

        self.pushButton_copy_name.clicked.connect(
            lambda: (self.copy_folder_name()))
        self.pushButton_change_folder_name.clicked.connect(
            lambda: (self.change_folder_name()))

        self.pushButton_scan_not_complete.clicked.connect(
            lambda: (self.scan_empty_fields(check_not_complete=1)))
        self.pushButton_scan_complete.clicked.connect(
            lambda: (self.scan_empty_fields(check_complete=1)))

        self.pushButton_scan_not_ok.clicked.connect(
            lambda: (self.scan_empty_fields(check_not_ok=1)))
        self.pushButton_scan_ok.clicked.connect(
            lambda: (self.scan_empty_fields(check_ok=1)))

        self.pushButton_search_web.clicked.connect(
            lambda: (self.search_web()))

        self.pushButton_get_htmls.clicked.connect(lambda: (self.get_html_data()))

        self.pushButton_delete_all.clicked.connect(lambda: (self.delete_all()))

        self.pushButton_check_problem.clicked.connect(lambda: (self.check_problem()))

        self.pushButton_scan_different_date.clicked.connect(lambda: (self.check_different_dates()))

    def initialize_search(self):
        self.radioButton_film_type_film.toggled.connect(self.onClickedRadioFilmType)
        self.radioButton_film_type_irani_film.toggled.connect(self.onClickedRadioFilmType)
        self.radioButton_film_type_irani_tv.toggled.connect(self.onClickedRadioFilmType)
        self.radioButton_film_type_animation.toggled.connect(self.onClickedRadioFilmType)

        self.radioButton_film_type_film.search_type = 1
        self.radioButton_film_type_irani_film.search_type = 2
        self.radioButton_film_type_irani_tv.search_type = 3
        self.radioButton_film_type_animation.search_type = 4

        self.radioButton_web_type_web.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_image.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_wikipedia.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_imdb.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_30nama.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_kingmovie.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_hexdownload.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_doostiha.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_dibamovie.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_animation_download.toggled.connect(self.onClickRadioWebType)
        self.radioButton_web_type_subscene.toggled.connect(self.onClickRadioWebType)

        self.radioButton_web_type_web.web_type = 1
        self.radioButton_web_type_image.web_type = 2
        self.radioButton_web_type_wikipedia.web_type = 3
        self.radioButton_web_type_imdb.web_type = 4
        self.radioButton_web_type_30nama.web_type = 5
        self.radioButton_web_type_kingmovie.web_type = 6
        self.radioButton_web_type_hexdownload.web_type = 7
        self.radioButton_web_type_doostiha.web_type = 8
        self.radioButton_web_type_dibamovie.web_type = 9
        self.radioButton_web_type_animation_download.web_type = 10
        self.radioButton_web_type_subscene.web_type = 11

    def onClickedRadioFilmType(self):
        global SEARCH_TYPE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            self.SEARCH_TYPE_FINAL = radio_button.search_type

    def onClickRadioWebType(self):
        global SEARCH_TYPE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            self.WEB_TYPE_FINAL = radio_button.web_type

    def search_web(self):
        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    folder_name = get_last_file_or_folder_from_path(item)
                    ClassSearchWeb(folder_name, self.SEARCH_TYPE_FINAL, self.WEB_TYPE_FINAL)

        # self.clear_items()

    def open_in_browser(self, url):
        url = strip_text(str(url))

        if url:
            open_in_browser(url, 1)

    def check_problem(self):
        properties = [
            "per_title",
            "eng_title",
            "per_info",
            "eng_info",
            # "director",
            # "actors",
            # "per_genre",
            # "eng_genre"
        ]

        character_to_find = str(self.lineEdit_check_problem.text())

        list_array = []

        if character_to_find:
            for index in range(self.listWidget_items.count()):
                current_item = self.listWidget_items.item(index)
                if current_item:
                    file = current_item.text()

                    if os.path.isdir(file):
                        json_file_path = rename_file_paths_by_os(file) + CustomNames.EXTRACTED_DATA

                        if os.path.exists(json_file_path):
                            for current_property in properties:
                                data = (Film.json_file_to_class(json_file_path)).get_all()
                                to_check_data = data.get(current_property)
                                # character_to_find = "طنز"
                                # character_to_find = "اجتماعی"
                                # character_to_find = " و با حضور "
                                if find_in_text(to_check_data, character_to_find):
                                    list_array.append(file)
                                    break

            self.listWidget_items.clear()

            for i in list_array:
                item = QListWidgetItem(str(i))
                self.listWidget_items.addItem(item)

            self.clear_text_boxes()

    def check_different_dates(self):
        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                if os.path.isdir(file):
                    folder_path = rename_file_paths_for_files(file)
                    folder_name = get_last_file_or_folder_from_path(folder_path)

                    film_release_date = File.trim_released_date(folder_name)

                    for name in os.listdir(folder_path):
                        if name.lower().endswith(".json"):
                            json_file = rename_file_paths_by_os(folder_path) + name

                            if os.path.exists(json_file):
                                film = Film.json_file_to_class(json_file)

                                if film.release:
                                    imdb_date = film.release

                                    if not find_in_text(imdb_date, film_release_date):
                                        Print.print_green(folder_name)
                                        Print.print_cyan("Imdb date : " + imdb_date)
                                        Print.print_yellow("Not Equal with IMDB date")
                                        Print.print_full_line(color=CustomColor.WHITE)

                                else:
                                    Print.print_green(folder_name)
                                    Print.print_red("Imdb date not found !!!")
                                    Print.print_full_line(color=CustomColor.WHITE)

        Print.print_cyan("Check Completed !!!")
        Print.print_full_line(CustomColor.WHITE)

    def save_item(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            if os.path.isdir(item):
                for name in os.listdir(item):
                    if name.lower().endswith(".json"):
                        json_file_name = get_last_file_or_folder_from_path(
                            name)

                        self.save_item_2(json_file_name, item)

            else:
                if item.lower().endswith(".json"):
                    parent_folder_name, t = get_path_and_file(item)

                    self.save_item_2(t, parent_folder_name)

    def save_item_2(self, json_file_name, parent_folder, show_message=0):
        json_file_path = rename_file_paths_by_os(
            parent_folder) + json_file_name

        form_dict = self.get_textboxes_dict()

        titles_translate = Film.title_translate()

        film = Film()

        for i in form_dict:
            current_film_property = titles_translate.get(i)
            if i == "Actors" or i == "Per Genre" or i == "Eng Genre" or i == "Country":
                textbox_value = form_dict[i].text()
                if textbox_value:
                    filters = [",", "،"]

                    array_values = []

                    for filter in filters:
                        if find_in_text(textbox_value, filter):
                            textbox_value = strip_text(form_dict[i].text())
                            for item in textbox_value.split(filter):
                                item = filter_name_for_cast_and_info(item)
                                if item:
                                    array_values.append(item)

                    if array_values:
                        if current_film_property == "per_genre":
                            array_values = remove_array_duplicates(array_values)
                            array_values = Film.translate_per_genre(array_values)
                            array_values = remove_array_duplicates(array_values)

                        setattr(film, current_film_property, array_values)

                    if not getattr(film, current_film_property):
                        textbox_value = filter_name_for_cast_and_info(form_dict[i].text())
                        if textbox_value:
                            array_values.append(textbox_value)
                            if array_values:
                                array_values = remove_array_duplicates(array_values)
                                array_values = Film.translate_per_genre(array_values)
                                array_values = remove_array_duplicates(array_values)

                                setattr(film, current_film_property, array_values)

            elif i == "Per Info" or i == "Eng Info":
                plain_text = filter_name_for_cast_and_info(form_dict[i].toPlainText())

                if plain_text:
                    setattr(film, current_film_property, plain_text)
            else:
                textbox_value = form_dict[i].text()

                if i == "Eng Title":
                    textbox_value = str(textbox_value).replace(":", " ")

                if i == "Per Title":
                    textbox_value = str(textbox_value).replace(":", " ")
                    textbox_value = str(textbox_value).replace("/", " ")
                    textbox_value = str(textbox_value).replace("(فیلم)", " ")
                    textbox_value = str(textbox_value).replace("هٔ", "ه")

                textbox_value = strip_text(textbox_value)
                if textbox_value:
                    setattr(film, current_film_property, textbox_value)

        if self.checkBox_dubbed.isChecked():
            film.dubbed = 1

        Json.write_to_json_file(film, json_file_path)

        if show_message:
            if Message.showOk("Save", "File saved successfully !!!"):
                self.listWidget_items.clearSelection()
                self.clear_text_boxes()
                # print("OK!")

        self.remove_selected_item()

    def get_textboxes_dict(self):
        form_dict = {
            "Per Title": self.lineEdit_per_title,
            "Eng Title": self.lineEdit_eng_title,
            "Release": self.lineEdit_release,
            "Score": self.lineEdit_score,
            "Director": self.lineEdit_director,
            "Actors": self.lineEdit_actors,
            "Per Genre": self.lineEdit_per_genre,
            "Eng Genre": self.lineEdit_eng_genre,
            "Per Info": self.textEdit_per_info,
            "Eng Info": self.textEdit_eng_info,
            "Country": self.lineEdit_country,
            "Link Imdb": self.lineEdit_imdb_link,
            "Link 30nama": self.lineEdit_30nama_link,
            "Parent Guide": self.lineEdit_parent_guide
        }

        return form_dict

    def delete_item(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            self.remove_selected_item()

            # listItems = self.listWidget_items.selectedItems()
            # if not listItems: return
            # for item in listItems:
            #     self.listWidget_items.takeItem(self.listWidget_items.row(item))

            if os.path.isdir(item):
                for name in os.listdir(item):
                    if name.lower().endswith(".json"):
                        json_file_path = rename_file_paths_by_os(item) + name

                        if os.path.exists(json_file_path):
                            send2trash(json_file_path)
            else:
                if item.lower().endswith(".json"):
                    parent_folder_name, file = get_path_and_file(item)

                    json_path = rename_file_paths_by_os(
                        parent_folder_name) + file

                    send2trash(json_path)

    def delete_all(self):
        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                json_file = None

                if os.path.isdir(file):
                    json_file = rename_file_paths_by_os(
                        file) + CustomNames.EXTRACTED_DATA
                elif str(file).lower().endswith(".json"):
                    json_file = rename_file_paths_for_files(file)

                if json_file:
                    if os.path.exists(json_file):
                        send2trash(json_file)
        if Message.showOk("Delete", "All data cleared !!!"):
            self.clear_items()

    def get_items(self):
        list_count = self.listWidget_items.count()
        if list_count > 0:
            self.clear_text_boxes()
            current_row = self.listWidget_items.currentRow()
            if self.listWidget_items.item(current_row):
                item = self.listWidget_items.item(current_row).text()

                parent_folder_name = get_last_file_or_folder_from_path(item)

                if parent_folder_name:
                    parent_folder_without_poster_code = File.trim_name_movie(
                        parent_folder_name)
                    parent_folder_without_poster_code = File.trim_name_tv_series(
                        parent_folder_without_poster_code)

                    self.label_name.setText(parent_folder_without_poster_code)

                if os.path.isdir(item):
                    for name in os.listdir(item):
                        if name.lower().endswith(".json"):
                            json_file_name = get_last_file_or_folder_from_path(
                                name)
                            json_file_full_path = rename_file_paths_by_os(
                                item) + json_file_name
                            parent_folder_name = get_last_file_or_folder_from_path(
                                item)

                            self.get_data_from_json(
                                json_file_full_path, parent_folder_name)
                else:
                    if item.lower().endswith(".json"):
                        json_file_full_path = rename_file_paths_for_files(item)
                        parent_folder_name, t = get_path_and_file(
                            json_file_full_path)

                        parent_folder_name = get_last_file_or_folder_from_path(
                            parent_folder_name)

                        self.get_data_from_json(
                            json_file_full_path, parent_folder_name)

    def get_data_from_json(self, json_path, parent_folder_name):
        if os.path.exists(json_path):
            film = Film.json_file_to_class(json_path)

            if film:
                data = film.get_all()

                title_translate = Film.title_translate()

                form_dict = self.get_textboxes_dict()

                for i in title_translate:
                    current_text_box = form_dict.get(i)

                    current_data = data.get(title_translate[i])

                    if i == "Actors" or i == "Per Genre" or i == "Eng Genre" or i == "Country":
                        if current_data:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_GREY)
                            current_text_box.setText(" , ".join(current_data))
                        else:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_RED)
                    elif i == "Dubbed":
                        self.checkBox_dubbed.setChecked(
                            data.get(title_translate[i]))
                    else:
                        if current_data:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_GREY)
                            current_text_box.setText(
                                data.get(title_translate[i]))
                        else:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_RED)

    def get_html_data(self):
        if self.listWidget_items.__len__() >= 1:
            for index in range(self.listWidget_items.count()):
                current_item = self.listWidget_items.item(index)
                if current_item:
                    item = current_item.text()

                    combo_box_index = self.comboBox.currentIndex()

                    if os.path.isdir(item):
                        ClassExtract.extract(item, combo_box_index)

            # self.get_html_data()

    def change_folder_name(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            if os.path.isdir(item):
                json_file = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA
                if os.path.exists(json_file):
                    film_json = Film.json_file_to_class(json_file)

                    if Class30nama.is_film_complete(
                            film_json) and ClassIMDB.is_film_complete(film_json):
                        text = strip_text(self.lineEdit_eng_title.text())
                        if text:
                            folder_name = get_last_file_or_folder_from_path(item)
                            poster_code = folder_name[:folder_name.find(File.trim_name_tv_series(folder_name))]
                            new_name = filter_name_for_equal_checking(text) + " ("
                            date = folder_name[folder_name.find(File.trim_released_date(folder_name)):]

                            new_folder_name = poster_code + new_name + date

                            parent_path, t = get_path_and_file(item)

                            self.save_item()

                            move_or_rename_files(item, parent_path, new_folder_name)

            elif str(item).lower().endswith(".json"):
                json_file = item
                if os.path.exists(json_file):
                    film_json = Film.json_file_to_class(json_file)

                    if Class30nama.is_film_complete(
                            film_json) and ClassIMDB.is_film_complete(film_json):
                        text = strip_text(self.lineEdit_eng_title.text())
                        if text:
                            folder_path, t = get_path_and_file(item)

                            folder_name = get_last_file_or_folder_from_path(folder_path)

                            poster_code = folder_name[:folder_name.find(File.trim_name_tv_series(folder_name))]
                            new_name = filter_name_for_equal_checking(text) + " ("
                            date = folder_name[folder_name.find(File.trim_released_date(folder_name)):]

                            new_folder_name = poster_code + new_name + date

                            parent_path, t = get_path_and_file(folder_path)

                            self.save_item()

                            move_or_rename_files(folder_path, parent_path, new_folder_name)

    def copy_folder_name(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            if os.path.isdir(item):
                folder_name = filter_name_for_equal_checking(
                    File.trim_name_movie(get_last_file_or_folder_from_path(item)))

                self.lineEdit_eng_title.setText(folder_name)

                self.save_item()

            elif str(item).lower().endswith(".json"):
                h, t = get_path_and_file(item)
                folder_name = filter_name_for_equal_checking(
                    File.trim_name_movie(get_last_file_or_folder_from_path(h)))

                self.lineEdit_eng_title.setText(folder_name)

                self.save_item()

    def scan_empty_fields(self, check_30nama=0, check_imdb=0, check_per_title=0, check_director=0, check_names=0,
                          have_per_title=0, check_parent=0
                          , check_not_ok=0, check_ok=0, check_not_complete=0, check_complete=0):
        list_array = []

        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()
                json_file = None

                if os.path.isdir(file):
                    json_file = rename_file_paths_by_os(
                        file) + CustomNames.EXTRACTED_DATA
                elif str(file).lower().endswith(".json"):
                    json_file = file

                if check_30nama:
                    class30nama = Class30nama()

                    if json_file:
                        if os.path.exists(json_file):
                            if not class30nama.is_json_complete(json_file):
                                list_array.append(file)
                        else:
                            list_array.append(file)
                elif check_imdb:
                    classImdb = ClassIMDB()

                    if json_file:
                        if os.path.exists(json_file):
                            if not classImdb.is_json_complete(json_file):
                                list_array.append(file)
                        else:
                            list_array.append(file)

                elif have_per_title:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if film:
                                if film.per_title:
                                    list_array.append(file)
                elif check_per_title:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if film:
                                if not film.per_title:
                                    list_array.append(file)

                elif check_director:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if film:
                                if not film.director:
                                    list_array.append(file)

                elif check_parent:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if film:
                                if not film.parent_guide:
                                    list_array.append(file)

                elif check_names:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if film:
                                if film.eng_title:
                                    if os.path.isdir(file):
                                        parent_folder_name = filter_name_for_equal_checking(
                                            File.trim_name_movie(get_last_file_or_folder_from_path(file)))
                                        eng_title = filter_name_for_equal_checking(
                                            strip_text(film.eng_title))

                                        if parent_folder_name != eng_title:
                                            list_array.append(file)

                                    elif str(file).lower().endswith(".json"):
                                        h, t = get_path_and_file(file)
                                        parent_folder_name = filter_name_for_equal_checking(
                                            File.trim_name_movie(get_last_file_or_folder_from_path(h)))
                                        eng_title = filter_name_for_equal_checking(
                                            strip_text(film.eng_title))

                                        if parent_folder_name != eng_title:
                                            list_array.append(file)

                elif check_not_ok:
                    path, folder_name = get_path_and_file(file)

                    if not File.has_ok_at_the_end(folder_name):
                        list_array.append(file)

                elif check_ok:
                    path, folder_name = get_path_and_file(file)

                    if File.has_ok_at_the_end(folder_name):
                        list_array.append(file)

                elif check_not_complete:
                    if os.path.exists(json_file):
                        if (not Class30nama.is_json_complete(json_file)) or (not ClassIMDB.is_json_complete(json_file)):
                            list_array.append(file)
                    else:
                        list_array.append(file)

                elif check_complete:
                    if os.path.exists(json_file):
                        if Class30nama.is_json_complete(json_file) and ClassIMDB.is_json_complete(json_file):
                            list_array.append(file)

        self.listWidget_items.clear()

        for i in list_array:
            item = QListWidgetItem(str(i))
            self.listWidget_items.addItem(item)

        self.clear_text_boxes()

    def rename_to_fixed(self, check=1):
        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                path, folder_name = get_path_and_file(file)

                if check:
                    if File.has_ok_at_the_end(folder_name):
                        new_name = folder_name
                    else:
                        new_name = folder_name + " (OK)"

                    move_or_rename_files(file, path, new_name)
                else:
                    if File.has_ok_at_the_end(folder_name):
                        new_name = folder_name[:-5]
                    else:
                        new_name = folder_name

                    move_or_rename_files(file, path, new_name)

        self.listWidget_items.clear()

    def clear_items(self):
        self.listWidget_items.clear()

        self.clear_text_boxes()

    def clear_text_boxes(self):
        self.lineEdit_json_file_name.clear()

        self.label_name.clear()
        self.lineEdit_per_title.clear()
        self.lineEdit_eng_title.clear()
        self.lineEdit_release.clear()
        self.lineEdit_score.clear()
        self.lineEdit_director.clear()
        self.lineEdit_actors.clear()
        self.lineEdit_per_genre.clear()
        self.lineEdit_eng_genre.clear()
        self.lineEdit_country.clear()
        self.lineEdit_imdb_link.clear()
        self.lineEdit_30nama_link.clear()
        self.textEdit_per_info.clear()
        self.textEdit_eng_info.clear()
        self.lineEdit_parent_guide.clear()

        self.lineEdit_per_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_eng_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_release.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_score.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_director.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_actors.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_per_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_eng_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_country.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_imdb_link.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_30nama_link.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_per_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_eng_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_parent_guide.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)

        self.checkBox_dubbed.setChecked(0)

    def clear_all_but_30nama_link(self):
        self.lineEdit_per_title.clear()
        self.lineEdit_eng_title.clear()
        self.lineEdit_release.clear()
        self.lineEdit_score.clear()
        self.lineEdit_director.clear()
        self.lineEdit_actors.clear()
        self.lineEdit_per_genre.clear()
        self.lineEdit_eng_genre.clear()
        self.lineEdit_country.clear()
        self.lineEdit_imdb_link.clear()
        self.textEdit_per_info.clear()
        self.textEdit_eng_info.clear()
        self.lineEdit_parent_guide.clear()

        self.lineEdit_per_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_eng_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_release.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_score.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_director.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_actors.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_per_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_eng_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_country.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_imdb_link.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_30nama_link.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_per_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_eng_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_parent_guide.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)

        self.checkBox_dubbed.setChecked(0)

        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            if os.path.isdir(item):
                for name in os.listdir(item):
                    if name.lower().endswith(".json"):
                        json_file_name = get_last_file_or_folder_from_path(
                            name)

                        self.save_item_2(json_file_name, item)

            else:
                if item.lower().endswith(".json"):
                    parent_folder_name, t = get_path_and_file(item)

                    self.save_item_2(t, parent_folder_name)

    def remove_selected_item(self):
        list_count = self.listWidget_items.count()
        if list_count > 0:
            current_row = self.listWidget_items.currentRow()

            self.listWidget_items.takeItem(current_row)

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
