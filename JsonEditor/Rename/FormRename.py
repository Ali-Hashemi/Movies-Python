from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.Rename.MainWindow import Ui_MainWindow
from JsonEditor.CustomListView import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    MAIN_RADIO_TYPE = 0

    FILM_SUB_TYPE = 1

    TV_SUB_TYPE = 1

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

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

        self.radioButton_type_film.toggled.connect(lambda: (self.radio_main_clicked()))
        self.radioButton_type_film.film_type = 1

        self.radioButton_type_tv.toggled.connect(lambda: (self.radio_main_clicked()))
        self.radioButton_type_tv.film_type = 2

        self.radioButton_film_base_folder.toggled.connect(lambda: (self.radio_film_sub_clicked()))
        self.radioButton_film_base_folder.film_type = 1
        self.radioButton_film_per_sub.toggled.connect(lambda: (self.radio_film_sub_clicked()))
        self.radioButton_film_per_sub.film_type = 2

        self.radioButton_tv_dubbed.toggled.connect(lambda: (self.radio_tv_sub_clicked()))
        self.radioButton_tv_dubbed.film_type = 1
        self.radioButton_tv_subbed.toggled.connect(lambda: (self.radio_tv_sub_clicked()))
        self.radioButton_tv_subbed.film_type = 2

        # self.shortcut = QShortcut(QKeySequence('F4'), self)
        # self.shortcut.activated.connect(lambda: (self.remove_selected_item()))
        #
        # self.shortcut = QShortcut(QKeySequence('F1'), self)
        # self.shortcut.activated.connect(lambda: (self.rename_to_eng_name_and_date()))
        #
        self.pushButton_rename.clicked.connect(lambda: (self.rename_items()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

    def radio_main_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.MAIN_RADIO_TYPE = radio_button.film_type
            if radio_button.film_type == 1:
                self.radioButton_film_base_folder.setEnabled(1)
                self.radioButton_film_per_sub.setEnabled(1)

                self.radioButton_tv_dubbed.setEnabled(0)
                self.radioButton_tv_subbed.setEnabled(0)

            elif radio_button.film_type == 2:
                self.radioButton_tv_dubbed.setEnabled(1)
                self.radioButton_tv_subbed.setEnabled(1)

                self.radioButton_film_base_folder.setEnabled(0)
                self.radioButton_film_per_sub.setEnabled(0)

    def radio_film_sub_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.FILM_SUB_TYPE = radio_button.film_type
            print(radio_button.film_type)

    def radio_tv_sub_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.TV_SUB_TYPE = radio_button.film_type
            print(radio_button.film_type)

    def rename_by_shortcuts(self, mode=None):
        if mode == 0:
            self.MAIN_RADIO_TYPE = 0
            self.rename_items()

        elif mode == 1:
            self.MAIN_RADIO_TYPE = 1
            self.FILM_SUB_TYPE = 1
            self.rename_items()
        elif mode == 2:
            self.MAIN_RADIO_TYPE = 1
            self.FILM_SUB_TYPE = 2
            self.rename_items()
        elif mode == 3:
            self.MAIN_RADIO_TYPE = 2
            self.TV_SUB_TYPE = 1
            self.rename_items()
        elif mode == 4:
            self.MAIN_RADIO_TYPE = 2
            self.TV_SUB_TYPE = 2
            self.rename_items()

        self.rename_items()

    def rename_items(self):
        for index in range(self.listWidget.count()):
            current_item = self.listWidget.item(index)
            if current_item:
                item = current_item.text()

                if os.path.isdir(item):
                    parent_folder, file = get_path_and_file(item)

                    h, parent_name = get_path_and_file(parent_folder)

                    if self.MAIN_RADIO_TYPE == 0:
                        self.rename_newly_downloaded_films(file, parent_folder)

                elif os.path.isfile(item):
                    parent_folder, file = get_path_and_file(item)

                    h, parent_name = get_path_and_file(parent_folder)

                    if self.MAIN_RADIO_TYPE == 0:
                        self.rename_newly_downloaded_films(file, parent_folder)

                    elif self.MAIN_RADIO_TYPE == 1:
                        if self.FILM_SUB_TYPE == 1:
                            file_ext = File.get_file_ext(file)
                            filename = parent_name[parent_name.find(File.trim_name_tv_series(parent_name)):] + file_ext
                            move_or_rename_files(item, parent_folder, filename)
                        elif self.FILM_SUB_TYPE == 2:
                            file_ext = File.get_file_ext(file)
                            filename = "(Per) " + parent_name[
                                                  parent_name.find(File.trim_name_tv_series(parent_name)):] + file_ext
                            move_or_rename_files(item, parent_folder, filename)

                    elif self.MAIN_RADIO_TYPE == 2:
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

    def rename_newly_downloaded_films(self, file, location):
        filename = os.path.splitext(file)[0]

        file_ext = os.path.splitext(file)[1]

        words = [
            '.720p.HDTV.Farsi.Dubbed(Film2serial.ir)',
            '.720p.Farsi.Dubbed.(Film2serial.ir)',
            '_720p_Farsi_Dubbed_(Film2serial.ir)',
            '.720p.WEB-DL.Farsi.Dubbed(Film2serial.ir)',
            '_720p_WEB-DL_Farsi_Dubbed(Film2serial.ir)',
            '.720p.BluRay.HardSub.DigiMoviez',
            '.720p.ShAaNiG.(Film2serial.ir)',
            '_720p_ShAaNiG_(Film2serial.ir)',
            '.720p.WEB-DL.KIMO.DUBLE_2',
            '.720p.WEB-DL.KIMO.DUBLE',
            '.720p.BluRay.KIMO.DUBLE',
            '.720p.BRRip.KIMO.DUBLE',
            '.720p.WEB-DL.Farsi.Dubbed',
            '[www.film2serial.ir]',
            '.720p.Farsi.Dubbed',
            '_720p_Farsi_Dubbed',
            ' 720p Farsi Dubbed',
            ' 720p BluRay Fa Dubbed',
            '.DVDRip.Farsi.Dubbed',
            '_DVDRip_Farsi_Dubbed',
            '.720p.KingMovi.DUBLE',
            '_720p_KingMovi_DUBLE',
            '.720p.KIMO.DUBLE',
            '_720p_KIMO_DUBLE',
            '.720p.Farsi.Dub',
            '_720p_Farsi_Dub',
            '_Subtitles01.PER',
            '_Subtitles01.ENG',
            '_Subtitles01',
            '(Per) ',
            '.720p',
            '_720p',
            '.Fixed',
            '.Dubbed',
            '_Dubbed']

        spaces = [
            '.',
            '_'
        ]

        new_name = filename

        x = re.findall("2\d{3}|19\d{2}", new_name)

        if x:
            new_name = slicer(new_name, x[0])
            new_name = new_name.replace("(", "")

            for word in words:
                if find_in_text(new_name, word):
                    new_name = new_name.replace(word, '')

            for i in spaces:
                if find_in_text(new_name, i):
                    new_name = new_name.replace(i, ' ')

            new_name = str(new_name).strip() + " (" + x[0] + ")"

        if os.path.isfile(location + file):
            new_file_name_with_extension = new_name + file_ext
        else:
            new_file_name_with_extension = new_name

        # if not os.path.exists(location + new_name):
        #     os.makedirs(location + new_name)

        if new_name:
            # os.rename(str(location + original_file), str(location + new_name + "\\" + new_name + file_ext))
            if os.path.isdir(location + file):
                move_or_rename_files(location + file, location, new_file_name_with_extension)
            else:
                move_or_rename_files(location + file, location + new_name, new_file_name_with_extension)
                srt_file = filename + ".srt"
                if os.path.exists(location + srt_file):
                    move_or_rename_files(location + srt_file, location + new_name, new_name + ".srt")
                    # os.rename(str(location + srt_file), str(location + new_name + "\\" + new_name + ".srt"))

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
