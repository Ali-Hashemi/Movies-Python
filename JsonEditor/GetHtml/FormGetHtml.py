import time
from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.CustomListView import *
from JsonEditor.GetHtml.MainWindow import Ui_MainWindow
from Classes.Class30nama import *
from Classes.Timer import Timer

# ------------- Absolutes --------------- #
FILM_TYPE_FINAL = 0


# ------------- Absolutes --------------- #

class MainWindow(BaseForm, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(20, 20, CustomStyle.main_list_widget_width,
                                                                         CustomStyle.main_list_widget_height))

        self.pushButton_get_htmls.clicked.connect(lambda: (self.get_items(self.listWidget)))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items(self.listWidget)))

    class Runnable(BaseRunnable):
        def run(self):
            timer = Timer()

            for item in self.list:
                item = rename_file_paths_for_files(str(item))
                combo_box_index = self.form.comboBox.currentIndex()
                if os.path.isdir(item):
                    json_path = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA
                    html_30nama = rename_file_paths_by_os(item) + CustomNames.HTML_30nama_FILE_NAME

                    Print.print_green(get_last_file_or_folder_from_path(item))

                    if os.path.exists(json_path):
                        if combo_box_index == 0:
                            cinama_url = Film.json_file_to_class(json_path).url_30nama

                            if cinama_url:
                                # Html.get_soup_with_chrome_driver(cinama_url, timer=30, folder_path=i,
                                #                                  soup_name=CustomNames.HTML_30nama_FILE_NAME)

                                Html.get_soup_with_chrome_driver_undetected(cinama_url, timer=15, folder_path=item,
                                                                            soup_name=CustomNames.HTML_30nama_FILE_NAME)

                        elif combo_box_index == 1:
                            imdb_url = Film.json_file_to_class(json_path).url_imdb

                            if imdb_url:
                                # MainWindow.get_imdb_html(imdb_url, rename_file_paths_by_os(item))
                                Html.get_soup(imdb_url, folder_path=item,
                                              soup_name=CustomNames.HTML_IMDB_FILE_NAME)
                    elif os.path.exists(html_30nama):
                        film_30nama = Class30nama.get_data_from_html_file(html_30nama)

                        if film_30nama.url_imdb:
                            # MainWindow.get_imdb_html(film_30nama.url_imdb, rename_file_paths_by_os(item))
                            Html.get_soup(film_30nama.url_imdb, folder_path=item,
                                          soup_name=CustomNames.HTML_IMDB_FILE_NAME)

                            # Html.get_soup_for_subscene(film_30nama.url_imdb, timer=2, folder_path=item,
                            #               soup_name=CustomNames.HTML_IMDB_FILE_NAME)

                    Print.print_full_line(CustomColor.WHITE)
            timer.end()

    @staticmethod
    def get_imdb_html(url, folder=None):
        Html.get_soup(url, timer=1, folder_path=folder, soup_name="imdb.html")
        # Html.get_soup_for_subscene(url, timer=1, folder_path=folder, soup_name="imdb.html")
        # soup = Html.get_soup_for_subscene(url, timer=1,folder_path=folder)
        # if soup:
        #     ClassIMDB.get_tv_rating(soup)
