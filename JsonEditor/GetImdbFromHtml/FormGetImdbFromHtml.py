from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.GetImdbFromHtml.MainWindow import Ui_MainWindow
from JsonEditor.CustomListView import *
from Classes.ClassIMDB import ClassIMDB


class MainWindow(BaseForm, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(20, 20, CustomStyle.main_list_widget_width,
                                                                         CustomStyle.main_list_widget_height))

        self.pushButton_get_data.clicked.connect(lambda: (self.get_items(self.listWidget)))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items(self.listWidget)))

    class Runnable(BaseRunnable):
        def run(self):
            for item in self.list:
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                if str(file).lower().endswith(".html"):
                    classImdb = ClassIMDB()
                    film_imdb = classImdb.get_data_from_html_file(file)
                    if ClassIMDB.is_film_complete(film_imdb):
                        new_name = filter_name(film_imdb.eng_title + " (" + film_imdb.release + ")")

                        html_new_name = new_name + ".html"

                        folder_path = rename_file_paths_by_os(h + new_name)

                        json_file_path = folder_path + CustomNames.EXTRACTED_DATA

                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)

                        if os.path.exists(folder_path):
                            Json.write_to_json_file(film_imdb, json_file_path)

                            if os.path.exists(json_file_path):
                                move_or_rename_files(file, folder_path, html_new_name)

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
