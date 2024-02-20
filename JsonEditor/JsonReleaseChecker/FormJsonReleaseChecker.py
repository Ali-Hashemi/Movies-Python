from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.CustomListView import *
from JsonEditor.JsonReleaseChecker.MainWindow import Ui_MainWindow
from Classes.Class30nama import *

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 0


# ------------- Absolutes --------------- #

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.array = []

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(320, 10, CustomStyle.main_list_widget_width,
                                                                         CustomStyle.main_list_widget_height))

        self.pushButton_check.clicked.connect(lambda: (self.check_items()))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items()))

        self.set_combo_items()

    def set_combo_items(self):
        self.comboBox.addItem("30nama")
        self.comboBox.addItem("Imdb")

    def check_items(self):
        combo_item = self.comboBox.currentText()

        Print.print_cyan(combo_item)
        Print.print_full_line(CustomColor.WHITE)

        del self.array[:]

        for index in range(self.listWidget.count()):
            self.array.append(self.listWidget.item(index).text())

        for i in self.array:
            if os.path.isdir(i):
                folder_path = rename_file_paths_for_files(i)
                folder_name = get_last_file_or_folder_from_path(folder_path)

                film_release_date = File.trim_released_date(folder_name)

                if find_in_text(combo_item, "30nama"):
                    for name in os.listdir(folder_path):
                        if find_in_text(name, CustomNames.HTML_30nama_FILE_NAME):
                            html_30nama = rename_file_paths_by_os(folder_path) + name

                            if os.path.exists(html_30nama):
                                soup = Html.get_soup_from_file(html_30nama)

                                class_30nama = Class30nama()

                                full_title = Class30nama.get_full_title(soup)

                                if full_title:
                                    if not find_in_text(full_title, film_release_date):
                                        Print.print_green(folder_name)
                                        Print.print_cyan("30nama : " + full_title)
                                        Print.print_yellow("Not Equal with 30nama date")
                                        Print.print_full_line(color=CustomColor.WHITE)
                                else:
                                    Print.print_green(folder_name)
                                    Print.print_red("30nama full_title not found !!!")
                                    Print.print_full_line(color=CustomColor.WHITE)

                elif find_in_text(combo_item, "imdb"):
                    for name in os.listdir(folder_path):
                        if name.lower().endswith(".json"):
                            json_file = rename_file_paths_by_os(folder_path) + name

                            if os.path.exists(json_file):
                                film = Film.json_file_to_class(json_file)

                                if film.release:
                                    imdb_date = film.release

                                    if not find_in_text(imdb_date, film_release_date):
                                        Print.print_green(folder_name)
                                        Print.print_cyan("Imdb date : " + imdb_date)
                                        Print.print_yellow("Not Equal with IMDB date")
                                        Print.print_full_line(color=CustomColor.WHITE)

                                else:
                                    Print.print_green(folder_name)
                                    Print.print_red("Imdb date not found !!!")
                                    Print.print_full_line(color=CustomColor.WHITE)

    def clear_items(self):
        self.listWidget.clear()
        del self.array[:]

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
