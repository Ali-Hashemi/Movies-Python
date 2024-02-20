from JsonEditor.CreateJsonIrani.MainWindow import Ui_MainWindow
from JsonEditor.CreateJsonIrani.CustomListViewJsonEditor import *
from Classes.ClassDoostiha import *
from Classes.ClassHex import *
from Classes.ClassSearchWeb import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    SEARCH_TYPE_FINAL = 1
    WEB_TYPE_FINAL = 1

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.lineEdit_check_problem.setText(":")

        self.initialize_search()

        self.listWidget_hidden.hide()

        self.listWidget_items = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget_hidden.geometry().left(),
                                                                               self.listWidget_hidden.geometry().top(),
                                                                               self.listWidget_hidden.width(),
                                                                               self.listWidget_hidden.height()))

        self.label_name.setStyleSheet(StyleSheet.TEXT_EDITOR_NO_BORDER)

        self.listWidget_items.itemSelectionChanged.connect(
            lambda: (self.get_items()))

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
        self.pushButton_clear_all_and_save.clicked.connect(
            lambda: (self.clear_all_and_save()))
        self.pushButton_scan_per_title.clicked.connect(
            lambda: (self.scan_empty_fields(check_per_title=1)))
        self.pushButton_scan_eng_title.clicked.connect(
            lambda: (self.scan_empty_fields(check_eng_title=1)))
        self.pushButton_scan_release.clicked.connect(
            lambda: (self.scan_empty_fields(check_release=1)))
        self.pushButton_scan_director.clicked.connect(
            lambda: (self.scan_empty_fields(check_director=1)))
        self.pushButton_scan_actors.clicked.connect(
            lambda: (self.scan_empty_fields(check_actors=1)))
        self.pushButton_scan_genre.clicked.connect(
            lambda: (self.scan_empty_fields(check_per_genre=1)))
        self.pushButton_scan_info.clicked.connect(
            lambda: (self.scan_empty_fields(check_per_info=1)))

        self.pushButton_scan_not_complete.clicked.connect(
            lambda: (self.scan_empty_fields(check_not_complete=1)))
        self.pushButton_scan_complete.clicked.connect(
            lambda: (self.scan_empty_fields(check_complete=1)))

        self.pushButton_scan_not_ok.clicked.connect(
            lambda: (self.scan_empty_fields(check_not_ok=1)))
        self.pushButton_scan_ok.clicked.connect(
            lambda: (self.scan_empty_fields(check_ok=1)))

        self.pushButton_get_html_data.clicked.connect(lambda: (self.get_html_data()))

        self.pushButton_delete_all.clicked.connect(lambda: (self.delete_all()))

        self.pushButton_search_web.clicked.connect(lambda: (self.search_web()))

        self.pushButton_check_problem.clicked.connect(lambda: (self.check_problem()))

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

        self.clear_items()

    def open_in_browser(self, url):
        url = strip_text(str(url))

        if url:
            open_in_browser(url, 1)

    def save_item(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = self.listWidget_items.item(current_row).text()

            if os.path.isdir(item):
                self.save_item_2(CustomNames.EXTRACTED_DATA, item)
            elif str(item).lower().endswith(".json"):
                path, file = get_path_and_file(item)

                self.save_item_2(file, path)

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
                textbox_value = filter_name_for_cast_and_info(textbox_value)
                if textbox_value:
                    filters = [",", "،"]

                    array_values = []

                    for filter in filters:
                        if find_in_text(textbox_value, filter):
                            textbox_value = strip_text(textbox_value)

                            for item in textbox_value.split(filter):
                                item = filter_name_for_cast_and_info(item)
                                if item:
                                    array_values.append(item)

                    if array_values:
                        if current_film_property == "per_genre":
                            array_values = remove_array_duplicates(array_values)
                            array_values = Film.translate_per_genre(array_values)
                            array_values = remove_array_duplicates(array_values)
                        elif current_film_property == "actors":
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
                textbox_value = strip_text(textbox_value)
                if textbox_value:
                    setattr(film, current_film_property, textbox_value)

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
            "Director": self.lineEdit_director,
            "Actors": self.lineEdit_actors,
            "Per Genre": self.lineEdit_per_genre,
            "Per Info": self.textEdit_per_info,
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
            if parent_folder_name:
                parent_folder_without_poster_code = File.trim_name_movie(
                    parent_folder_name)
                parent_folder_without_poster_code = File.trim_name_tv_series(
                    parent_folder_without_poster_code)
                self.label_name.setText(parent_folder_without_poster_code)

            film = Film.json_file_to_class(json_path)

            if film:
                data = film.get_all()

                title_translate = self.title_translate()

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
                    else:
                        if current_data:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_GREY)
                            current_text_box.setText(
                                data.get(title_translate[i]))
                        else:
                            current_text_box.setStyleSheet(
                                StyleSheet.TEXT_EDITOR_BORDER_RED)

    def scan_empty_fields(self, check_per_title=0, check_eng_title=0, check_director=0, check_actors=0, check_release=0,
                          check_per_genre=0, check_per_info=0, check_not_complete=0, check_complete=0, check_not_ok=0,
                          check_ok=0):
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

                if check_per_title:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.per_title:
                                list_array.append(file)
                elif check_eng_title:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.eng_title:
                                list_array.append(file)
                elif check_actors:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.actors:
                                list_array.append(file)
                elif check_director:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.director:
                                list_array.append(file)
                elif check_release:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.release:
                                list_array.append(file)
                elif check_per_genre:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.per_genre:
                                list_array.append(file)
                elif check_per_info:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not film.per_info:
                                list_array.append(file)
                elif check_not_complete:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if not ClassDoostiha.is_film_complete(film):
                                list_array.append(file)
                        else:
                            list_array.append(file)
                elif check_complete:
                    if json_file:
                        if os.path.exists(json_file):
                            film = Film.json_file_to_class(json_file)
                            if ClassDoostiha.is_film_complete(film):
                                list_array.append(file)

                elif check_not_ok:
                    path, folder_name = get_path_and_file(file)

                    if not File.has_ok_at_the_end(folder_name):
                        list_array.append(file)
                elif check_ok:
                    path, folder_name = get_path_and_file(file)

                    if File.has_ok_at_the_end(folder_name):
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

    def get_html_data(self):
        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    json_file_path = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA

                    combo_box_index = self.comboBox.currentIndex()

                    Print.print_green(get_last_file_or_folder_from_path(item))

                    # html_file_path = None
                    #
                    # selected_class = None
                    #
                    # if combo_box_index == 0:
                    #     selected_class = ClassDoostiha()
                    #     html_file_path = rename_file_paths_by_os(item) + CustomNames.HTML_DOOSTIHA_FILE_NAME
                    # elif combo_box_index == 1:
                    #     selected_class = ClassHex()
                    #     html_file_path = rename_file_paths_by_os(item) + CustomNames.HTML_Hex_FILE_NAME
                    #
                    # if selected_class:
                    #     if os.path.exists(json_file_path):
                    #         film_json = selected_class.get_data_from_json_file(json_file_path)
                    #
                    #         if selected_class.is_film_complete(film_json):
                    #             self.save_to_json(film_json, 0, json_file_path)
                    #         else:
                    #             if os.path.exists(html_file_path):
                    #                 film_html = selected_class.get_data_from_html_file(html_file_path)
                    #
                    #                 film_all = self.concatenate_films(film_json, film_html)
                    #
                    #                 if film_all:
                    #                     if selected_class.is_film_complete(film_all):
                    #                         self.save_to_json(film_all, 0, json_file_path)
                    #     else:
                    #         if os.path.exists(html_file_path):
                    #             film_html = selected_class.get_data_from_html_file(html_file_path)
                    #
                    #             if film_html:
                    #                 if selected_class.is_film_complete(film_html):
                    #                     self.save_to_json(film_html, 0, json_file_path)

                    if combo_box_index == 0:
                        html_doostiha = rename_file_paths_by_os(item) + CustomNames.HTML_DOOSTIHA_FILE_NAME

                        if os.path.exists(json_file_path):
                            film_json = ClassDoostiha.get_data_from_json_file(json_file_path)

                            if ClassDoostiha.is_film_complete(film_json):
                                self.save_to_json(film_json, 0, json_file_path)
                            else:
                                if os.path.exists(html_doostiha):
                                    film_doostiha = ClassDoostiha.get_data_from_html_file(html_doostiha)

                                    film_all = self.concatenate_films(film_json, film_doostiha)

                                    if film_all:
                                        # if ClassDoostiha.is_film_complete(film_all):
                                        self.save_to_json(film_all, 0, json_file_path)
                        else:
                            if os.path.exists(html_doostiha):
                                film_doostiha = ClassDoostiha.get_data_from_html_file(html_doostiha)

                                if film_doostiha:
                                    if ClassDoostiha.is_film_complete(film_doostiha):
                                        self.save_to_json(film_doostiha, 0, json_file_path)

                    elif combo_box_index == 1:
                        html_hex = rename_file_paths_by_os(item) + CustomNames.HTML_Hex_FILE_NAME

                        if os.path.exists(json_file_path):
                            film_json = ClassHex.get_data_from_json_file(json_file_path)

                            if ClassHex.is_film_complete(film_json):
                                self.save_to_json(film_json, 0, json_file_path)
                            else:
                                if os.path.exists(html_hex):
                                    film_hex = ClassHex.get_data_from_html_file(html_hex)

                                    film_all = self.concatenate_films(film_json, film_hex)

                                    if film_all:
                                        # if ClassHex.is_film_complete(film_all):
                                        self.save_to_json(film_all, 0, json_file_path)
                        else:
                            film_hex = ClassHex.get_data_from_html_file(html_hex)

                            if film_hex:
                                if ClassHex.is_film_complete(film_hex):
                                    self.save_to_json(film_hex, 0, json_file_path)

                    Print.print_full_line(CustomColor.WHITE)

        self.clear_items()

    @staticmethod
    def concatenate_films(film_json, film_irani):
        film = Film()
        if film_json and film_irani:
            film.per_title = film_json.per_title
            film.eng_title = film_json.eng_title
            film.release = film_json.release

            film.director = film_irani.director
            film.actors = film_irani.actors
            film.per_genre = film_irani.per_genre
            film.per_info = film_irani.per_info

        return film

    @staticmethod
    def save_to_json(film: Film, check_dubbed_status, json_file_path):
        if check_dubbed_status:
            film.dubbed = 1

        Json.write_to_json_file(film, json_file_path)

    def check_problem(self):
        properties = [
            "director",
            "actors",
            "per_genre",
            "per_info"
        ]

        character_to_find = str(self.lineEdit_check_problem.text())

        list_array = []

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
                            # character_to_find = ":"
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

    @staticmethod
    def title_translate():
        dictionary = {
            "Per Title": "per_title",
            "Eng Title": "eng_title",
            "Release": "release",
            "Director": "director",
            "Actors": "actors",
            "Per Genre": "per_genre",
            "Per Info": "per_info",
        }
        return dictionary

    def clear_items(self):
        self.listWidget_items.clear()

        self.clear_text_boxes()

    def clear_text_boxes(self):
        self.label_name.clear()
        self.lineEdit_per_title.clear()
        self.lineEdit_eng_title.clear()
        self.lineEdit_release.clear()
        self.lineEdit_director.clear()
        self.lineEdit_actors.clear()
        self.lineEdit_per_genre.clear()
        self.textEdit_per_info.clear()

        self.lineEdit_per_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_eng_title.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_release.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_director.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_actors.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_per_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_per_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)

    def clear_all_and_save(self):
        # self.lineEdit_per_title.clear()
        # self.lineEdit_eng_title.clear()
        # self.lineEdit_release.clear()

        self.lineEdit_director.clear()
        self.lineEdit_actors.clear()
        self.lineEdit_per_genre.clear()
        self.textEdit_per_info.clear()

        # self.lineEdit_per_title.setStyleSheet(
        #     StyleSheet.TEXT_EDITOR_BORDER_GREY)
        # self.lineEdit_eng_title.setStyleSheet(
        #     StyleSheet.TEXT_EDITOR_BORDER_GREY)
        # self.lineEdit_release.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)

        self.lineEdit_director.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_actors.setStyleSheet(StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.lineEdit_per_genre.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)
        self.textEdit_per_info.setStyleSheet(
            StyleSheet.TEXT_EDITOR_BORDER_GREY)

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
