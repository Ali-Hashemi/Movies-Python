import os

from Forms.IMDBSearch.ClassIMDBSearch import IMDBSearch
from Base import *
from Config import *
from Classes.ClassUtility import *

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 1


# ------------- Absolutes --------------- #


# file = open("qwer.json", "w", encoding="utf-8")
# f = my_class("my name")
# file.write(f.toJSON())
# file.close()

# myfile = open("qwer.json")
# Data = json.load(myfile, object_hook=lambda d: SimpleNamespace(**d))
# Print.print_white(Data.fname)

class FilmTypeWidget(QWidget):
    def __init__(self, parent):
        super(FilmTypeWidget, self).__init__(parent)

        self.layout = QHBoxLayout(self)

        self.radio_button_film = QRadioButton("Film")
        self.radio_button_film.setChecked(True)
        self.radio_button_film.film_type = 1
        self.radio_button_film.toggled.connect(self.onClickedRadio)
        self.radio_button_film.setFont(CustomStyle.radio_btn_font_size)

        self.film_irani = QRadioButton("TV Show")
        self.film_irani.film_type = 2
        self.film_irani.toggled.connect(self.onClickedRadio)
        self.film_irani.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_film)
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

    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                if os.path.isdir(file):
                    Print.print_white(t)
                    IMDBSearch(t, FILM_TYPE_FINAL, h + t)
                elif os.path.isfile(file):
                    Print.print_white(t)
                    t = os.path.splitext(t)[0]
                    IMDBSearch(t, FILM_TYPE_FINAL, h + t)
                Print.print_full_line()
