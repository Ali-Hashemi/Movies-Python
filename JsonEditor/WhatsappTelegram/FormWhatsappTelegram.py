from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.WhatsappTelegram.MainWindow import Ui_MainWindow
from JsonEditor.CustomListView import *
import pyperclip
from PIL import Image

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    RADIO_SOCIAL_MEDIA_TYPE = 0

    RADIO_FILM_TYPE = 1

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setAcceptDrops(True)

        self.setupUi(self)

        self.listWidget_hidden.hide()

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget_hidden.geometry().left(),
                                                                         self.listWidget_hidden.geometry().top(),
                                                                         self.listWidget_hidden.width(),
                                                                         self.listWidget_hidden.height()))

        self.shortcut = QShortcut(QKeySequence('F5'), self)
        self.shortcut.activated.connect(lambda: (self.rename_by_shortcuts(0)))

        self.shortcut = QShortcut(QKeySequence('F1'), self)
        self.shortcut.activated.connect(lambda: (self.rename_by_shortcuts(1)))

        self.shortcut = QShortcut(QKeySequence('F2'), self)
        self.shortcut.activated.connect(lambda: (self.rename_by_shortcuts(2)))

        self.shortcut = QShortcut(QKeySequence('F3'), self)
        self.shortcut.activated.connect(lambda: (self.rename_by_shortcuts(3)))

        self.shortcut = QShortcut(QKeySequence('F4'), self)
        self.shortcut.activated.connect(lambda: (self.rename_by_shortcuts(4)))

        self.radioButton_type_whatsapp.toggled.connect(lambda: (self.radio_social_media_clicked()))
        self.radioButton_type_whatsapp.social_media_type = 1

        self.radioButton_type_telegram.toggled.connect(lambda: (self.radio_social_media_clicked()))
        self.radioButton_type_telegram.social_media_type = 2

        self.radioButton_film_kharej_dub.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_film_kharej_dub.film_type = 1

        self.radioButton_film_kharej_sub.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_film_kharej_sub.film_type = 2

        self.radioButton_film_irani.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_film_irani.film_type = 3

        self.radioButton_film_indian.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_film_indian.film_type = 4

        self.radioButton_film_animation.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_film_animation.film_type = 5

        self.radioButton_series_kharej_dub.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_series_kharej_dub.film_type = 6

        self.radioButton_series_kharej_sub.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_series_kharej_sub.film_type = 7

        self.radioButton_series_irani.toggled.connect(lambda: (self.radio_film_type_clicked()))
        self.radioButton_series_irani.film_type = 8

        # self.shortcut = QShortcut(QKeySequence('F4'), self)
        # self.shortcut.activated.connect(lambda: (self.remove_selected_item()))
        #
        # self.shortcut = QShortcut(QKeySequence('F1'), self)
        # self.shortcut.activated.connect(lambda: (self.rename_to_eng_name_and_date()))
        #
        self.pushButton_create.clicked.connect(lambda: (self.create_text()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = str(event.mimeData().urls()[0].toLocalFile())
            parent_folder = rename_file_paths_by_os(file_path.replace(get_last_file_or_folder_from_path(file_path), ""))

            print(parent_folder)

            if os.path.isdir(parent_folder):
                parent_folder, file = get_path_and_file(parent_folder)

                h, parent_name = get_path_and_file(parent_folder)

                if self.RADIO_SOCIAL_MEDIA_TYPE == 0:
                    self.generate_text(file, parent_folder)

            event.accept()
        else:
            event.ignore()

    def radio_social_media_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.RADIO_SOCIAL_MEDIA_TYPE = radio_button.social_media_type
            # if radio_button.film_type == 1:
            #     self.radioButton_film_base_folder.setEnabled(1)
            #     self.radioButton_film_per_sub.setEnabled(1)
            #
            #     self.radioButton_tv_dubbed.setEnabled(0)
            #     self.radioButton_tv_subbed.setEnabled(0)
            #
            # elif radio_button.film_type == 2:
            #     self.radioButton_tv_dubbed.setEnabled(1)
            #     self.radioButton_tv_subbed.setEnabled(1)
            #
            #     self.radioButton_film_base_folder.setEnabled(0)
            #     self.radioButton_film_per_sub.setEnabled(0)

    def radio_film_type_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.RADIO_FILM_TYPE = radio_button.film_type
            print(radio_button.film_type)

    def rename_by_shortcuts(self, mode=None):
        if mode == 0:
            self.RADIO_SOCIAL_MEDIA_TYPE = 0
            self.create_text()

        elif mode == 1:
            self.RADIO_SOCIAL_MEDIA_TYPE = 1
            self.RADIO_FILM_TYPE = 1
            self.create_text()
        elif mode == 2:
            self.RADIO_SOCIAL_MEDIA_TYPE = 1
            self.RADIO_FILM_TYPE = 2
            self.create_text()
        elif mode == 3:
            self.RADIO_SOCIAL_MEDIA_TYPE = 2
            self.TV_SUB_TYPE = 1
            self.create_text()
        elif mode == 4:
            self.RADIO_SOCIAL_MEDIA_TYPE = 2
            self.TV_SUB_TYPE = 2
            self.create_text()

        self.create_text()

    def create_text(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    parent_folder, file = get_path_and_file(item)

                    h, parent_name = get_path_and_file(parent_folder)

                    if self.RADIO_SOCIAL_MEDIA_TYPE == 0:
                        self.generate_text(file, parent_folder)

                elif os.path.isfile(item):
                    parent_folder, file = get_path_and_file(item)

                    h, parent_name = get_path_and_file(parent_folder)

                    if self.RADIO_SOCIAL_MEDIA_TYPE == 0:
                        self.generate_text(file, parent_folder)

                    elif self.RADIO_SOCIAL_MEDIA_TYPE == 1:
                        if self.RADIO_FILM_TYPE == 1:
                            file_ext = File.get_file_ext(file)
                            filename = parent_name[parent_name.find(File.trim_name_tv_series(parent_name)):] + file_ext
                            move_or_rename_files(item, parent_folder, filename)
                        elif self.RADIO_FILM_TYPE == 2:
                            file_ext = File.get_file_ext(file)
                            filename = "(Per) " + parent_name[
                                                  parent_name.find(File.trim_name_tv_series(parent_name)):] + file_ext
                            move_or_rename_files(item, parent_folder, filename)

                    elif self.RADIO_SOCIAL_MEDIA_TYPE == 2:
                        if self.TV_SUB_TYPE == 1:
                            file_ext = File.get_file_ext(file)
                            folder_name = File.trim_name_tv_series(parent_name)
                            folder_name = folder_name.replace(" ", ".")
                            filename = folder_name + "." + File.trim_season_and_episode(
                                file) + ".Dubbed.720p" + file_ext
                            move_or_rename_files(item, parent_folder, filename)

                        elif self.TV_SUB_TYPE == 2:
                            file_ext = File.get_file_ext(file)
                            folder_name = File.trim_name_tv_series(parent_name)
                            folder_name = folder_name.replace(" ", ".")
                            filename = folder_name + "." + File.trim_season_and_episode(
                                file) + ".720p" + file_ext
                            move_or_rename_files(item, parent_folder, filename)

        self.clear_items()

    def generate_text(self, file, location):
        folder_path = rename_file_paths_by_os(location + file)
        json_path = folder_path + CustomNames.EXTRACTED_DATA

        film = Film.json_file_to_class(json_path)

        temp_actors = []
        temp_genre = []

        for idx, item in enumerate(film.actors):
            if idx >= 3:
                break
            item = re.sub("\s+", "_", item.strip())
            temp_actors.append("#" + item)

        for idx, item in enumerate(film.per_genre):
            if idx >= 5:
                break
            item = re.sub("\s+", "_", item.strip())
            temp_genre.append("#" + item)

        poster_code = (File.trim_poster_code(get_last_file_or_folder_from_path(folder_path)))

        film.per_title = "«" + film.per_title + "»"
        film.eng_title = film.eng_title + " #" + film.release + ""
        film.actors = temp_actors
        film.per_genre = temp_genre
        film.director = "#" + re.sub("\s+", "_", film.director.strip())
        film.country = "#" + re.sub("\s+", "_", film.country[0].strip())
        film.score = film.score + "/10"

        is_dubbed = ""

        if film.dubbed:
            is_dubbed = "#دوبله_بدون_سانسور"
        else:
            is_dubbed = "#زیرنویس_فارسی_چسبیده"

        film_khareji_array = {
            "🏅 کد": poster_code,
            "📺 #فیلم_خارجی": film.per_title,
            "💬": is_dubbed,
            "🎬": film.eng_title,
            "🏆 امتیاز": film.score,
            "👔 کارگردان": film.director,
            "💎 ستارگان": " , ".join(film.actors),
            "🎭 ژانر": " , ".join(film.per_genre),
            "کشور": film.country,
            "🗯 خلاصه داستان": film.per_info,
        }

        full_text = ""

        for i in film_khareji_array:
            full_text += i + " : " + film_khareji_array[i] + "\n"

        # print(full_text)

        pyperclip.copy(full_text)

        spam = pyperclip.paste()

    def remove_selected_item(self):
        list_count = self.listWidget.count()
        if list_count > 0:
            current_row = self.listWidget.currentRow()

            self.listWidget.takeItem(current_row)

    def clear_items(self):
        self.listWidget.clear()

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
