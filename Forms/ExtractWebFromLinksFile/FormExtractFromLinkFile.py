import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Config import *
from Classes.ClassUtility import *
from Classes.Class30nama import Class30nama
from Data import *
from Classes.ClassIMDB import ClassIMDB


class FormWidget(QWidget):
    def __init__(self, parent=None):
        super(FormWidget, self).__init__(parent)

        layout = QVBoxLayout()

        self.btn1 = QPushButton("Choose path")
        self.btn1.clicked.connect(self.get_folder_path)

        self.label_path = QLabel("No folder selected yet")

        # self.btn2 = QPushButton("Choose file")
        # self.btn2.clicked.connect(self.getfile)
        # self.btn2.setFont(CustomStyle.radio_btn_font_size)
        # self.btn2.setStyleSheet("QPushButton"
        #                         "{"
        #                         "background-color : red;"
        #                         "color: white;"
        #                         "}"
        #                         "QPushButton::pressed"
        #                         "{"
        #                         "background-color : lightgreen;"
        #                         "color: red"
        #                         "}"
        #                         )
        # self.btn2.setGeometry(QRect(390, 170, 310, 300))

        self.btn3 = QPushButton("QFileDialog object")
        self.btn3.clicked.connect(self.getfiles)
        # self.btn3.setGeometry(QRect(290, 170, 310, 300))

        layout.addWidget(self.btn1)
        layout.addWidget(self.label_path)
        layout.addWidget(self.btn3)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")

    def getfile(self):
        # fname = QFileDialog.getOpenFileName(self, 'Open file',
        #                                     'd:\\', "Text files (*.txt)")
        # print(fname[0])

        pass

    def getfiles(self):

        folder_path = rename_file_paths_by_os(strip_text(self.label_path.text()))

        filter = "TXT (*.txt);;PDF (*.pdf)"
        # dlg = QFileDialog.getOpenFileNames(filter=filter)     # for multiple files
        dlg = QFileDialog.getOpenFileName(directory='d:\\', filter=filter)
        for i in dlg[0]:
            with open(i) as file:
                for line in file:
                    line = line.rstrip()
                    if len(line) > 0:
                        # self.contents.setText(line)
                        if line.find("30nama") != -1:
                            class30nama = Class30nama()
                            film, full_title = class30nama.get_all_infos_from_url(line)

                            if full_title:
                                each_film_folder = rename_file_paths_by_os(folder_path + "/" + full_title)

                                if not os.path.exists(each_film_folder):
                                    os.makedirs(each_film_folder)

                                    if film:
                                        if film.url_imdb:
                                            imdb = ClassIMDB()
                                            data_imdb = imdb.get_all_infos_from_url(film.url_imdb)
                                            film = imdb.combine_30nama_into_imdb_data(film, data_imdb)

                                            check_empty_values = Film().get_empty_values(film)
                                            if check_empty_values:
                                                Print.print_cyan("Empty Attributes :")
                                                for x in check_empty_values:
                                                    Print.print_red(x + " not found !!!")

                                        Json.write_to_json_file(film, each_film_folder + CustomNames.EXTRACTED_DATA)
                                        Print.print_full_line(CustomColor.CYAN)

    def get_folder_path(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.label_path.setText(strip_text(fname))


class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowTitle("Movies")
        self.setWindowIcon(QIcon("Cover.ico"))
        self.resize(QSize(550, 520))

        self.form_layout = FormWidget(self)
        self.form_layout.setGeometry(0, 0, 450, 420)


if __name__ == '__main__':
    app = QApplication([])

    demo = Form()
    demo.show()

    sys.exit(app.exec_())
