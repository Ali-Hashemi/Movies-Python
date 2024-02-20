from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from Data.MyButton import *
from JsonEditor.CustomListView import *
from JsonEditor.FixDubbed.MainWindow import Ui_MainWindow
from Classes.Class30nama import *
from JsonEditor.FixDubbed.ClassFixDubbed import *


class MainWindow(BaseForm, Ui_MainWindow):
    SELECTED_AUDIO_TITLE_AND_ID = None
    SELECTED_SUB_TITLE_AND_ID = None

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.listWidget_hidden.hide()

        self.listWidget_items = ListBoxWidget(self.centralwidget, QtCore.QRect(self.listWidget_hidden.geometry().left(),
                                                                               self.listWidget_hidden.geometry().top(),
                                                                               self.listWidget_hidden.width(),
                                                                               self.listWidget_hidden.height()))

        self.pushButton_fix.clicked.connect(lambda: (self.fix_dubbed()))
        self.pushButton_edit_name_and_lang.clicked.connect(lambda: (self.edit_name_and_language()))
        self.pushButton_scan.clicked.connect(lambda: (self.scan_tracks()))
        self.pushButton_filter_not_yet_fix.clicked.connect(lambda: (self.filter_not_yet_fix()))
        self.pushButton_filter_audio_tracks.clicked.connect(lambda: (self.filter_audio_tracks()))
        self.pushButton_filter_by_audio_id_and_title.clicked.connect(lambda: (self.filter_by_audio_id_and_title()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        # self.ali_button = MyButton(self.centralwidget, "ali", 200, 200, 200, 200, back_color=CustomColorRGB.BLACK,
        #                           front_color=CustomColorRGB.BLUE)

    class Runnable(BaseRunnable):
        def run(self):
            selected_audio = self.form.SELECTED_AUDIO_TITLE_AND_ID
            selected_sub = self.form.SELECTED_SUB_TITLE_AND_ID

            for item in self.list:
                item = rename_file_paths_for_files(str(item))
                h, t = get_path_and_file(item)
                FixDubbed(t, h, selected_audio, selected_sub)

    def edit_name_and_language(self):
        if len(self.listWidget_items.selectedItems()) > 0:
            current_row = self.listWidget_items.currentRow()
            item = rename_file_paths_for_files(self.listWidget_items.item(current_row).text())

            if len(self.listWidget_audio_tracks.selectedItems()) > 0:
                current_row_audio = self.listWidget_audio_tracks.currentRow()
                item_audio = self.listWidget_audio_tracks.item(current_row_audio).text()

                if item_audio:
                    selected_audio = str(item_audio).split(",")

                    selected_audio_id = strip_text(int(selected_audio[0]) + 1)

                    combo_box_index = self.comboBox.currentIndex()

                    if combo_box_index == 0:
                        set_property_cmd = 'mkvpropedit -v ' '"' + item + '" ' \
                                                                          '--edit track:' + selected_audio_id + ' --set name=Persian --set language=per'
                        subprocess.call(set_property_cmd, shell=True)

                    elif combo_box_index == 1:
                        set_property_cmd = 'mkvpropedit -v ' '"' + item + '" ' \
                                                                          '--edit track:' + selected_audio_id + ' --set name=English --set language=und'
                        subprocess.call(set_property_cmd, shell=True)

            if len(self.listWidget_sub_tracks.selectedItems()) > 0:
                current_row_sub = self.listWidget_sub_tracks.currentRow()
                item_sub = self.listWidget_sub_tracks.item(current_row_sub).text()

                if item_sub:
                    selected_sub = str(item_sub).split(",")
                    selected_sub_id = strip_text(int(selected_sub[0]) + 1)

                    set_property_cmd = 'mkvpropedit -v ' '"' + item + '" ' \
                                                                      '--edit track:' + selected_sub_id + ' --set name="Eng Parts" --set language=per'
                    subprocess.call(set_property_cmd, shell=True)

            self.listWidget_audio_tracks.clear()
            self.listWidget_sub_tracks.clear()

    def fix_dubbed(self):
        if len(self.listWidget_audio_tracks.selectedItems()) > 0 and len(
                self.listWidget_sub_tracks.selectedItems()) > 0:
            current_row_audio = self.listWidget_audio_tracks.currentRow()
            item_audio = self.listWidget_audio_tracks.item(current_row_audio).text()

            current_row_sub = self.listWidget_sub_tracks.currentRow()
            item_sub = self.listWidget_sub_tracks.item(current_row_sub).text()

            if item_audio:
                self.SELECTED_AUDIO_TITLE_AND_ID = item_audio

            if item_sub:
                self.SELECTED_SUB_TITLE_AND_ID = item_sub

            if self.SELECTED_AUDIO_TITLE_AND_ID and self.SELECTED_SUB_TITLE_AND_ID:
                self.get_items(self.listWidget_items)
        else:
            self.get_items(self.listWidget_items)

        self.clear_items()

    def scan_tracks(self):
        self.listWidget_audio_tracks.clear()
        self.listWidget_sub_tracks.clear()

        arr_audio_tracks = []

        arr_sub_tracks = []

        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                if str(file).lower().endswith(".mkv"):
                    media_info = MediaInfo.parse(file)

                    for index, value in enumerate(media_info.audio_tracks):
                        arr = [str(int(media_info.audio_tracks[index].track_id) - 1),
                               strip_text(media_info.audio_tracks[index].title),
                               strip_text(media_info.audio_tracks[index].language),
                               strip_text(media_info.audio_tracks[index].forced)]

                        language = strip_text(media_info.audio_tracks[index].language)

                        # if str(language).lower() != "en":
                        text = " , ".join(arr)
                        arr_audio_tracks.append(text)

                    for index, value in enumerate(media_info.text_tracks):
                        arr = [strip_text(int(media_info.text_tracks[index].track_id) - 1),
                               strip_text(media_info.text_tracks[index].title),
                               strip_text(media_info.text_tracks[index].forced)]

                        text = " , ".join(arr)

                        arr_sub_tracks.append(text)

        # arr_audio_tracks = list(set(arr_audio_tracks))
        # arr_sub_tracks = list(set(arr_sub_tracks))

        arr_audio_tracks = remove_array_duplicates(arr_audio_tracks)
        arr_sub_tracks = remove_array_duplicates(arr_sub_tracks)

        for i in arr_audio_tracks:
            item = QListWidgetItem(str(i))
            self.listWidget_audio_tracks.addItem(item)

        for i in arr_sub_tracks:
            item = QListWidgetItem(str(i))
            self.listWidget_sub_tracks.addItem(item)

    def filter_by_audio_id_and_title(self):
        list_array = []

        if len(self.listWidget_audio_tracks.selectedItems()) > 0:
            current_row_audio = self.listWidget_audio_tracks.currentRow()
            item_audio = self.listWidget_audio_tracks.item(current_row_audio).text()

            if item_audio:
                arr = str(item_audio).split(",")
                selected_audio_id = int(strip_text(arr[0]))
                selected_audio_title = strip_text(arr[1])

                for index in range(self.listWidget_items.count()):
                    current_item = self.listWidget_items.item(index)
                    if current_item:
                        file = current_item.text()

                        if str(file).lower().endswith(".mkv"):
                            media_info = MediaInfo.parse(file)

                            for index, value in enumerate(media_info.audio_tracks):
                                found_audio_id = int(strip_text(media_info.audio_tracks[index].track_id - 1))
                                found_audio_title = strip_text(media_info.audio_tracks[index].title)

                                if selected_audio_id == found_audio_id and selected_audio_title == found_audio_title:
                                    list_array.append(file)
        self.listWidget_items.clear()

        self.clear_items()

        for i in list_array:
            item = QListWidgetItem(str(i))
            self.listWidget_items.addItem(item)

    def filter_not_yet_fix(self):
        list_array = []

        for index in range(self.listWidget_items.count()):
            temp_array = {
                "Video": None,
                "Per-Audio": None,
                "Eng-Audio": None,
                "Subtitle": None
            }

            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                if str(file).lower().endswith(".mkv"):
                    media_info = MediaInfo.parse(file)

                    is_already_fixed = False

                    if FixDubbed.count_audios(media_info, 2):
                        temp_array["Video"] = media_info.video_tracks[0].track_id - 1

                        first_track = media_info.audio_tracks[0]
                        second_track = media_info.audio_tracks[1]

                        if first_track.language == "fa":
                            if first_track.title == "Persian":
                                temp_array["Per-Audio"] = first_track.track_id - 1

                        if not second_track.language:
                            if second_track.title == "English":
                                temp_array["Eng-Audio"] = second_track.track_id - 1

                        if FixDubbed.count_subs(media_info, 1):
                            sub_track = media_info.text_tracks[0]

                            if sub_track.language == "fa":
                                if sub_track.title == "Eng Parts":
                                    temp_array["Subtitle"] = sub_track.track_id - 1

                        compare_array = []
                        perfect_array = [0, 1, 2, 3]

                        for i in temp_array:
                            compare_array.append(temp_array[i])

                        if compare_array == perfect_array:
                            is_already_fixed = True

                        elif compare_array == [0, 1, 2, None]:
                            is_already_fixed = True

                        if not is_already_fixed:
                            list_array.append(file)

                    else:
                        list_array.append(file)

        self.listWidget_items.clear()

        self.clear_items()

        for i in list_array:
            item = QListWidgetItem(str(i))
            self.listWidget_items.addItem(item)

    def filter_audio_tracks(self):
        list_array = []

        number_of_audios = int(self.spinBox_audio_numbers.text())

        for index in range(self.listWidget_items.count()):
            current_item = self.listWidget_items.item(index)
            if current_item:
                file = current_item.text()

                if str(file).lower().endswith(".mkv"):
                    media_info = MediaInfo.parse(file)

                    if FixDubbed.count_audios(media_info, number_of_audios):
                        list_array.append(file)

        self.listWidget_items.clear()

        self.clear_items()

        for i in list_array:
            item = QListWidgetItem(str(i))
            self.listWidget_items.addItem(item)

    def clear_items(self, **kwargs):
        self.listWidget_items.clear()
        self.listWidget_audio_tracks.clear()
        self.listWidget_sub_tracks.clear()

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
