from Classes.ClassSearchWeb import *
from Base import *
from Config import *
import os
from Classes.ClassUtility import *

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 1
SEARCH_TYPE_FINAL = 1
BROWSER_TYPE_FINAL = 1


# ------------- Absolutes --------------- #


# file = open("qwer.json", "w", encoding="utf-8")
# f = my_class("my name")
# file.write(f.toJSON())
# file.close()

# myfile = open("qwer.json")
# Data = json.load(myfile, object_hook=lambda d: SimpleNamespace(**d))
# Print.print_white(Data.fname)

class SearchTypeWidget(QWidget):
    def __init__(self, parent):
        super(SearchTypeWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.radio_button_web = QRadioButton("Web")
        self.radio_button_web.setChecked(True)
        self.radio_button_web.search_type = 1
        self.radio_button_web.toggled.connect(self.onClickedRadio)
        self.radio_button_web.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_image = QRadioButton("Image")
        self.radio_button_image.search_type = 2
        self.radio_button_image.toggled.connect(self.onClickedRadio)
        self.radio_button_image.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_wikipedia = QRadioButton("Wikipedia")
        self.radio_button_wikipedia.search_type = 3
        self.radio_button_wikipedia.toggled.connect(self.onClickedRadio)
        self.radio_button_wikipedia.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_imdb = QRadioButton("IMDB")
        self.radio_button_imdb.search_type = 4
        self.radio_button_imdb.toggled.connect(self.onClickedRadio)
        self.radio_button_imdb.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_30nama = QRadioButton("30nama")
        self.radio_button_30nama.search_type = 5
        self.radio_button_30nama.toggled.connect(self.onClickedRadio)
        self.radio_button_30nama.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_kingmovie = QRadioButton("KingMovie")
        self.radio_button_kingmovie.search_type = 6
        self.radio_button_kingmovie.toggled.connect(self.onClickedRadio)
        self.radio_button_kingmovie.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_hex = QRadioButton("HexDownload")
        self.radio_button_hex.search_type = 7
        self.radio_button_hex.toggled.connect(self.onClickedRadio)
        self.radio_button_hex.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_doostiha = QRadioButton("Doostiha")
        self.radio_button_doostiha.search_type = 8
        self.radio_button_doostiha.toggled.connect(self.onClickedRadio)
        self.radio_button_doostiha.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_dibamovie = QRadioButton("Dibamovie")
        self.radio_button_dibamovie.search_type = 9
        self.radio_button_dibamovie.toggled.connect(self.onClickedRadio)
        self.radio_button_dibamovie.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_animation_download = QRadioButton("Animation Download")
        self.radio_button_animation_download.search_type = 10
        self.radio_button_animation_download.toggled.connect(self.onClickedRadio)
        self.radio_button_animation_download.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_subtitle = QRadioButton("Subscene")
        self.radio_button_subtitle.search_type = 11
        self.radio_button_subtitle.toggled.connect(self.onClickedRadio)
        self.radio_button_subtitle.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_web)
        self.layout.addWidget(self.radio_button_image)
        self.layout.addWidget(self.radio_button_wikipedia)
        self.layout.addWidget(self.radio_button_imdb)
        self.layout.addWidget(self.radio_button_30nama)
        self.layout.addWidget(self.radio_button_kingmovie)
        self.layout.addWidget(self.radio_button_hex)
        self.layout.addWidget(self.radio_button_doostiha)
        self.layout.addWidget(self.radio_button_dibamovie)
        self.layout.addWidget(self.radio_button_animation_download)
        self.layout.addWidget(self.radio_button_subtitle)

    def onClickedRadio(self):
        global SEARCH_TYPE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            SEARCH_TYPE_FINAL = radio_button.search_type


class BrowserTypeWidget(QWidget):
    def __init__(self, parent):
        super(BrowserTypeWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.radio_button_chrome = QRadioButton("Chrome")
        self.radio_button_chrome.setChecked(True)
        self.radio_button_chrome.browser_type = 1
        self.radio_button_chrome.toggled.connect(self.onClickedRadio)
        self.radio_button_chrome.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_firefox = QRadioButton("Firefox")
        self.radio_button_firefox.browser_type = 2
        self.radio_button_firefox.toggled.connect(self.onClickedRadio)
        self.radio_button_firefox.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_chrome)
        self.layout.addWidget(self.radio_button_firefox)

    def onClickedRadio(self):
        global BROWSER_TYPE_FINAL
        radio_button = self.sender()
        if radio_button.isChecked():
            BROWSER_TYPE_FINAL = radio_button.browser_type


class FilmTypeWidget(QWidget):
    def __init__(self, parent):
        super(FilmTypeWidget, self).__init__(parent)

        self.layout = QHBoxLayout(self)

        self.radio_button_film = QRadioButton("Film")
        self.radio_button_film.setChecked(True)
        self.radio_button_film.film_type = 1
        self.radio_button_film.toggled.connect(self.onClickedRadio)
        self.radio_button_film.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_film_irani = QRadioButton("فیلم ایرانی")
        self.radio_button_film_irani.film_type = 2
        self.radio_button_film_irani.toggled.connect(self.onClickedRadio)
        self.radio_button_film_irani.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_tv_irani = QRadioButton("سریال ایرانی")
        self.radio_button_tv_irani.film_type = 3
        self.radio_button_tv_irani.toggled.connect(self.onClickedRadio)
        self.radio_button_tv_irani.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_animation = QRadioButton("انیمیشن")
        self.radio_button_animation.film_type = 4
        self.radio_button_animation.toggled.connect(self.onClickedRadio)
        self.radio_button_animation.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_film)
        self.layout.addWidget(self.radio_button_tv_irani)
        self.layout.addWidget(self.radio_button_tv_irani)
        self.layout.addWidget(self.radio_button_animation)

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

        self.search_type_layout = SearchTypeWidget(self)
        self.search_type_layout.setGeometry(CustomStyle.search_type_size)

        self.browser_layout = BrowserTypeWidget(self)
        self.browser_layout.setGeometry(CustomStyle.browser_type_size)

    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):

                item = self.list[index]
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                if os.path.isdir(file):
                    Print.print_white(t)
                    ClassSearchWeb(t, FILM_TYPE_FINAL, SEARCH_TYPE_FINAL, BROWSER_TYPE_FINAL)
                    # sleep(5)
                elif os.path.isfile(file):
                    Print.print_white(t)
                    t = os.path.splitext(t)[0]
                    ClassSearchWeb(t, FILM_TYPE_FINAL, SEARCH_TYPE_FINAL)
                Print.print_full_line()
