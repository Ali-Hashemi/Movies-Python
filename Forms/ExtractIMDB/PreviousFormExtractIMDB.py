from Classes import *
from Forms.ExtractIMDB.ClassExtractImdb import ExtractImdb
from Base import *
from Config import *
import re

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 1
POSTER_MODE_FINAL = 1


# ------------- Absolutes --------------- #


# file = open("qwer.json", "w", encoding="utf-8")
# f = my_class("my name")
# file.write(f.toJSON())
# file.close()

# myfile = open("qwer.json")
# Data = json.load(myfile, object_hook=lambda d: SimpleNamespace(**d))
# Print.print_white(str(Data.fname))

class FilmTypeWidget(QWidget):
    def __init__(self, parent):
        super(FilmTypeWidget, self).__init__(parent)

        self.layout = QHBoxLayout(self)

        self.radio_button_film = QRadioButton("Film")
        self.radio_button_film.setChecked(True)
        self.radio_button_film.film_type = 1
        self.radio_button_film.toggled.connect(self.onClickedRadio)
        self.radio_button_film.setFont(CustomStyle.radio_btn_font_size)

        self.radio_button_tvshow = QRadioButton("TV Show")
        self.radio_button_tvshow.film_type = 2
        self.radio_button_tvshow.toggled.connect(self.onClickedRadio)
        self.radio_button_tvshow.setFont(CustomStyle.radio_btn_font_size)

        self.layout.addWidget(self.radio_button_film)
        self.layout.addWidget(self.radio_button_tvshow)

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
                    Print.print_white(str(t))
                    if FILM_TYPE_FINAL == 1:
                        ExtractImdb(t, FILM_TYPE_FINAL, h + t)
                    elif FILM_TYPE_FINAL == 2:
                        ExtractImdb(t, FILM_TYPE_FINAL, h + t)
                        pass
                elif os.path.isfile(file):
                    Print.print_white(str(t))
                    if FILM_TYPE_FINAL == 1:
                        t = os.path.splitext(t)[0]
                        ExtractImdb(t, FILM_TYPE_FINAL, h + t)
                    elif FILM_TYPE_FINAL == 2:
                        pass
                # cla = ExportToJson()
                # film = cla.json_to_class(file)

                Print.print_full_line()
