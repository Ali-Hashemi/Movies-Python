from Forms.CinamaSearch.ClassCinama import Cinama
from Base import *
from Config import *
import os
from Classes.ClassUtility import *

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 1
BROWSER_TYPE_FINAL = 1


# ------------- Absolutes --------------- #


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

        self.radio_button_animation = QRadioButton("Animation")
        self.radio_button_animation.film_type = 2
        self.radio_button_animation.toggled.connect(self.onClickedRadio)
        self.radio_button_animation.setFont(CustomStyle.radio_btn_font_size)

        self.film_irani = QRadioButton("TV Series")
        self.film_irani.film_type = 3
        self.film_irani.toggled.connect(self.onClickedRadio)
        self.film_irani.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_film)
        self.layout.addWidget(self.radio_button_animation)
        self.layout.addWidget(self.film_irani)

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
                    Cinama(t, h, FILM_TYPE_FINAL, BROWSER_TYPE_FINAL)
                elif os.path.isfile(file):
                    Print.print_white(t)
                    t = os.path.splitext(t)[0]
                    Cinama(t, h, FILM_TYPE_FINAL, BROWSER_TYPE_FINAL)
                Print.print_full_line()
