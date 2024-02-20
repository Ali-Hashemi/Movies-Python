from Forms.CreateCovers.ClassTable import *
from Base import *
from Data.Film import *

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 0
POSTER_MODE_FINAL = 1
DUBBED_MODE_FINAL = 1
SUBBED_MODE_FINAL = 1
RELEASE_INFO_FINAL = 1
SCORE_INFO_FINAL = 0
TV_SERIES_FINISHED_INFO_FINAL = 0


# ------------- Absolutes --------------- #


class ExportModeWidget(QWidget):
    def __init__(self, parent):
        super(ExportModeWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.radio_button_one = QRadioButton("1 in one")
        self.radio_button_one.setChecked(True)
        self.radio_button_one.mode = 1
        self.radio_button_one.toggled.connect(self.onClickedRadio)
        self.radio_button_one.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_two = QRadioButton("2 in one")
        self.radio_button_two.mode = 2
        self.radio_button_two.toggled.connect(self.onClickedRadio)
        self.radio_button_two.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_four = QRadioButton("4 in one")
        self.radio_button_four.mode = 4
        self.radio_button_four.toggled.connect(self.onClickedRadio)
        self.radio_button_four.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_eight = QRadioButton("8 in one")
        self.radio_button_eight.mode = 8
        self.radio_button_eight.toggled.connect(self.onClickedRadio)
        self.radio_button_eight.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_nine = QRadioButton("9 in one")
        self.radio_button_nine.mode = 9
        self.radio_button_nine.toggled.connect(self.onClickedRadio)
        self.radio_button_nine.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_twelve = QRadioButton("12 in one")
        self.radio_button_twelve.mode = 12
        self.radio_button_twelve.toggled.connect(self.onClickedRadio)
        self.radio_button_twelve.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_fifteen = QRadioButton("15 in one")
        self.radio_button_fifteen.mode = 15
        self.radio_button_fifteen.toggled.connect(self.onClickedRadio)
        self.radio_button_fifteen.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_sixteen = QRadioButton("16 in one")
        self.radio_button_sixteen.mode = 16
        self.radio_button_sixteen.toggled.connect(self.onClickedRadio)
        self.radio_button_sixteen.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_eighteen = QRadioButton("18 in one")
        self.radio_button_eighteen.mode = 18
        self.radio_button_eighteen.toggled.connect(self.onClickedRadio)
        self.radio_button_eighteen.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_twenty = QRadioButton("20 in one")
        self.radio_button_twenty.mode = 20
        self.radio_button_twenty.toggled.connect(self.onClickedRadio)
        self.radio_button_twenty.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_one)
        self.layout.addWidget(self.radio_button_two)
        self.layout.addWidget(self.radio_button_four)
        self.layout.addWidget(self.radio_button_eight)
        self.layout.addWidget(self.radio_button_nine)
        self.layout.addWidget(self.radio_button_twelve)
        self.layout.addWidget(self.radio_button_fifteen)
        self.layout.addWidget(self.radio_button_sixteen)
        self.layout.addWidget(self.radio_button_eighteen)
        self.layout.addWidget(self.radio_button_twenty)

    def onClickedRadio(self):
        global POSTER_MODE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            POSTER_MODE_FINAL = radio_button.mode


class DubbedModeWidget(QWidget):
    def __init__(self, parent):
        super(DubbedModeWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.checkbox_dubbed = QCheckBox("Dubbed")
        self.checkbox_dubbed.setChecked(True)
        self.checkbox_dubbed.toggled.connect(self.dubbed_toggled)
        self.checkbox_dubbed.setFont(CustomStyle.radio_btn_font_size)

        self.checkbox_subbed = QCheckBox("Subbed")
        self.checkbox_subbed.setChecked(True)
        self.checkbox_subbed.toggled.connect(self.subbed_toggled)
        self.checkbox_subbed.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.checkbox_dubbed)
        self.layout.addWidget(self.checkbox_subbed)

    def dubbed_toggled(self):
        global DUBBED_MODE_FINAL
        radio_button = self.sender()

        if radio_button.isChecked():
            DUBBED_MODE_FINAL = 1
        else:
            DUBBED_MODE_FINAL = 0

    def subbed_toggled(self):
        global SUBBED_MODE_FINAL
        radio_button = self.sender()

        if radio_button.isChecked():
            SUBBED_MODE_FINAL = 1
        else:
            SUBBED_MODE_FINAL = 0


class InfoModeWidget(QWidget):
    def __init__(self, parent):
        super(InfoModeWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.checkbox_release = QCheckBox("Has Release in Cover")
        self.checkbox_release.setChecked(True)
        self.checkbox_release.toggled.connect(self.release_toggled)
        self.checkbox_release.setFont(CustomStyle.radio_btn_font_size)

        self.checkbox_score = QCheckBox("Has Score in Cover")
        self.checkbox_score.setChecked(False)
        self.checkbox_score.toggled.connect(self.score_toggled)
        self.checkbox_score.setFont(CustomStyle.radio_btn_font_size)

        self.checkbox_tv_series_finished = QCheckBox("Has TV Show Finished")
        self.checkbox_tv_series_finished.setChecked(False)
        self.checkbox_tv_series_finished.toggled.connect(self.tv_series_finished_toggled)
        self.checkbox_tv_series_finished.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.checkbox_release)
        self.layout.addWidget(self.checkbox_score)
        self.layout.addWidget(self.checkbox_tv_series_finished)

    def release_toggled(self):
        global RELEASE_INFO_FINAL
        radio_button = self.sender()

        if radio_button.isChecked():
            RELEASE_INFO_FINAL = 1
        else:
            RELEASE_INFO_FINAL = 0

    def score_toggled(self):
        global SCORE_INFO_FINAL
        radio_button = self.sender()

        if radio_button.isChecked():
            SCORE_INFO_FINAL = 1
        else:
            SCORE_INFO_FINAL = 0

    def tv_series_finished_toggled(self):
        global TV_SERIES_FINISHED_INFO_FINAL
        radio_button = self.sender()

        if radio_button.isChecked():
            TV_SERIES_FINISHED_INFO_FINAL = 1
        else:
            TV_SERIES_FINISHED_INFO_FINAL = 0


class FilmTypeWidget(QWidget):
    def __init__(self, parent):
        super(FilmTypeWidget, self).__init__(parent)

        self.layout = QHBoxLayout(self)

        self.radio_button_film = QRadioButton("Film")
        self.radio_button_film.setChecked(True)
        self.radio_button_film.film_type = 0
        self.radio_button_film.toggled.connect(self.onClickedRadio)
        self.radio_button_film.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_film_irani = QRadioButton("Irani")
        self.radio_button_film_irani.film_type = 1
        self.radio_button_film_irani.toggled.connect(self.onClickedRadio)
        self.radio_button_film_irani.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_animation = QRadioButton("Animation")
        self.radio_button_animation.film_type = 2
        self.radio_button_animation.toggled.connect(self.onClickedRadio)
        self.radio_button_animation.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_tv_series = QRadioButton("TV Series")
        self.radio_button_tv_series.film_type = 3
        self.radio_button_tv_series.toggled.connect(self.onClickedRadio)
        self.radio_button_tv_series.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_film)
        self.layout.addWidget(self.radio_button_film_irani)
        self.layout.addWidget(self.radio_button_animation)
        self.layout.addWidget(self.radio_button_tv_series)

    def onClickedRadio(self):
        global FILM_TYPE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            FILM_TYPE_FINAL = radio_button.film_type


class Form(BaseMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.film_type_layout = FilmTypeWidget(self)
        self.film_type_layout.setGeometry(CustomStyle.film_type_size)

        self.mode_layout = ExportModeWidget(self)
        self.mode_layout.setGeometry(CustomStyle.mode_type_size)

        # self.mode_dubbed_layout = DubbedModeWidget(self)
        # self.mode_dubbed_layout.setGeometry(CustomStyle.dubbed_mode_cover_size)

        self.info_layout = InfoModeWidget(self)
        self.info_layout.setGeometry(CustomStyle.info_cover_size)

    class Runnable(BaseRunnable):
        def run(self):
            films_array = []

            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_by_os(item)
                h, t = get_path_and_file(file)

                film = None
                all_details = []

                if os.path.isdir(file):
                    if os.path.exists(file + CustomNames.EXTRACTED_DATA):
                        film = Film.json_file_to_class(file + CustomNames.EXTRACTED_DATA)

                if film:
                    all_details.append(file)
                    all_details.append(film)

                    films_array.append(all_details)

            if films_array:
                # Table(films_array, POSTER_MODE_FINAL, FILM_TYPE_FINAL, DUBBED_MODE_FINAL, SUBBED_MODE_FINAL,
                #       RELEASE_INFO_FINAL, SCORE_INFO_FINAL, TV_SERIES_FINISHED_INFO_FINAL)

                Table(films_array, POSTER_MODE_FINAL, FILM_TYPE_FINAL,
                      RELEASE_INFO_FINAL, SCORE_INFO_FINAL, TV_SERIES_FINISHED_INFO_FINAL, "ex")
