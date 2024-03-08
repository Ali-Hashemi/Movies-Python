from Data.MyButton import MyButton
from Classes.ClassUtility import *
from PyQt5.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
)
from PyQt5.QtWidgets import QWidget

from JsonEditor.JsonChecker import FormJsonChecker
from JsonEditor.JsonEditor import FormJsonEditor
from JsonEditor.ShowJson import Form2ShowJson
from JsonEditor.JsonReleaseChecker import FormJsonReleaseChecker
from JsonEditor.OpenHtml import FormOpenHtml
from JsonEditor.GetHtml import FormGetHtml
from JsonEditor.TakeScreenshot import FormTakeScreenshot
from JsonEditor.GetMovieData import FormGetMovieData
from JsonEditor.FixDubbed import FormFixDubbed
from JsonEditor.GetImdbFromHtml import FormGetImdbFromHtml
from JsonEditor.RenameFilmIrani import FormRenameIraniFilms
from JsonEditor.Rename import FormRename
from JsonEditor.CreateJsonIrani import FormCreateJsonIrani
from JsonEditor.PosterRenaming import FormPosterRenaming
from JsonEditor.PosterCode import FormPosterCode
from JsonEditor.WhatsappTelegram import FormWhatsappTelegram

class FormMyJsonEditorsWidget(QWidget):
    def __init__(self, parent):
        super(FormMyJsonEditorsWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.setWindowTitle("My App")

        # self.convert_uis_to_class()

        self.tabs2 = QTabWidget()

        self.tabs2.setTabPosition(QTabWidget.North)
        self.tabs2.setFont(CustomStyle.tabs_font)
        self.tabs2.setStyleSheet("QTabBar::tab { height: " + str(CustomStyle.tabs_height) + "px; }")
        self.tabs2.setMovable(True)
        self.tabs2 = self.get_tabs()

        self.layout.addWidget(self.tabs2)
        self.setLayout(self.layout)

    def get_tabs(self) -> QTabWidget:
        tabs = self.tabs2

        array = {
            "What Telegram": FormWhatsappTelegram,
            "Json Editor": FormJsonEditor,
            "Fix Rename": FormRename,
            "Poster Renaming": FormPosterRenaming,
            "Fix Dubbed": FormFixDubbed,
            "Create Json Irani": FormCreateJsonIrani,
            "Get Html": FormGetHtml,
            "Open Html": FormOpenHtml,
            "Json Checker": FormJsonChecker,
            "Rename Irani Films": FormRenameIraniFilms,
            "Get Imdb From Html": FormGetImdbFromHtml,
            "Take Screenshot": FormTakeScreenshot,
            "Json Shower": Form2ShowJson,
            "Poster Code": FormPosterCode,
        }

        for idx, item in enumerate(array.items()):
            tab = QWidget()
            tab.layout = QVBoxLayout(self)
            tab_name: QWidget = item[1].MainWindow(self)
            tab.layout.addWidget(tab_name)
            tab.setLayout(tab.layout)

            tabs.addTab(tab, item[0])

        return tabs

    def convert_uis_to_class(self):
        path, file = get_path_and_file(get_current_script_path())

        files_list = iterate_folder_with_subdirs(path)

        for name in files_list:
            if find_in_text(name, "mainwindow.ui"):
                convert_qt_creator_to_class(name)
