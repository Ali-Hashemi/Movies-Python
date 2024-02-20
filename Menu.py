from Classes.ClassUtility import *
from Config import CustomStyle
import sys
import os
from Classes.ClassUtility import *
from PyQt5.QtWidgets import (
    QPushButton,
    QTabWidget,
    QVBoxLayout,
)
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Forms.CategorizeFilms import FormCategorize
from Forms.ExtractIMDB import FormExtractIMDB
from Forms.ExtractIMDBAllPics import FormExtractIMDBAllPics
from Forms.ExtractSubtitleEnglish import FormExtractSubtitleEnglish
from Forms.ExtractSubtitlePersian import FormExtractSubtitlePersian
from Forms.CreateCovers import FormCreateCover
from Forms.FixDubbed import FormFixDubbed
from Forms.FixSubtitle import FormFixSub
from Forms.GoogleSearch import FormGoogle
from Forms.IMDBSearch import FormIMDBSearch
from Forms.Rename import FormRename
from Forms.ExtractWebFromLinksFile import FormExtractFromLinkFile
from Forms.ExtractWebFromHtmlFiles import FormExtractFromHtmlFiles
from Forms.CinamaSearch import FormCinama

from ClassFormMyJsonEditors import FormMyJsonEditorsWidget


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()

        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        self.left = qt_rectangle.left()
        self.top = qt_rectangle.top()
        self.width = CustomStyle.main_form_weight
        self.height = CustomStyle.main_form_height

        # self.setGeometry(self.left, self.top, self.width, self.height)

        self.setGeometry(80, 100, self.width, self.height)

        self.title = 'App'
        self.setWindowIcon(QIcon("Cover.ico"))

        self.setWindowTitle(self.title)

        # menu = self.menuBar()
        #
        # file_menu = menu.addMenu("&File")
        # file_menu.addAction(button_action)
        #
        # file_menu.addSeparator()
        #
        # file_submenu = file_menu.addMenu("Submenu")
        #
        # file_submenu.addAction(button_action2)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        button_menu1 = QAction(QIcon("bug.png"), "&Main", self)
        button_menu1.triggered.connect(lambda: (self.setMainWindow(1)))
        file_menu.addAction(button_menu1)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Submenu")
        button_menu2 = QAction(QIcon("bug.png"), "&Json Editor", self)
        button_menu2.triggered.connect(lambda: (self.setMainWindow(2)))
        file_submenu.addAction(button_menu2)

        self.shortcut = QShortcut(QKeySequence('F11'), self)
        self.shortcut.activated.connect(lambda: (self.setMainWindow(1)))

        self.shortcut = QShortcut(QKeySequence('F12'), self)
        self.shortcut.activated.connect(lambda: (self.setMainWindow(2)))

        self.show()

        self.setMainWindow(2)

    def setMainWindow(self, status):
        if status == 1:
            self.form_widget = MyTableWidget(self)
            self.setCentralWidget(self.form_widget)

        elif status == 2:
            self.form_widget = FormMyJsonEditorsWidget(self)
            self.setCentralWidget(self.form_widget)


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(MyTableWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        # self.tabs.resize(300, 200)
        self.tabs.setFont(CustomStyle.tabs_font)
        self.tabs.setStyleSheet("QTabBar::tab { height: " + str(CustomStyle.tabs_height) + "px; }")

        self.tabs = self.add_tabs(self.tabs)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def add_tabs(self, tabs: QTabWidget) -> QTabWidget:

        tabs = tabs

        array = {
            "Create Cover": FormCreateCover,
            "Extract Farsi Subtitle": FormExtractSubtitlePersian,
            "Extract IMDB": FormExtractIMDB,
            "Categorize": FormCategorize,
            "Google Search": FormGoogle,
            "Extract Web from Html Files": FormExtractFromHtmlFiles,
            "Extract English Subtitle": FormExtractSubtitleEnglish,
            "Fix Dubbed": FormFixDubbed,
            "30nama Search": FormCinama,
            "Rename": FormRename,
            "IMDB Search": FormIMDBSearch,
            "Extract Web from Url File": FormExtractFromLinkFile,
            "Fix Subtitle": FormFixSub,
            "Extract IMDB All Pics": FormExtractIMDBAllPics,
        }

        for idx, item in enumerate(array.items()):
            tab = QWidget()
            tab.layout = QVBoxLayout(self)
            tab_name: QWidget = item[1].Form(self)
            tab.layout.addWidget(tab_name)
            tab.setLayout(tab.layout)

            tabs.addTab(tab, item[0])

        return tabs

    @pyqtSlot()
    def on_click(self):
        Print.print_white("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            Print.print_white(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(),
                              currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication([])

    demo = MyMainWindow()
    demo.show()

    sys.exit(app.exec_())
