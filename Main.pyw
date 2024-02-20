from Classes.ClassUtility import *
from Config import CustomStyle
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


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()

        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        # Print.print_white(qtRectangle, centerPoint, sep="\n")

        self.title = 'App'
        self.setWindowIcon(QIcon("Cover.ico"))

        self.setWindowTitle(self.title)

        self.left = qt_rectangle.left()
        self.top = qt_rectangle.top()
        self.width = CustomStyle.main_form_weight
        self.height = CustomStyle.main_form_height

        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(qtRectangle)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
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
            "Extract Farsi Subtitle": FormExtractSubtitlePersian,
            "Extract English Subtitle": FormExtractSubtitleEnglish,
            "Fix Dubbed": FormFixDubbed,
            "30nama Search": FormCinama,
            "Rename": FormRename,
            "Google Search": FormGoogle,
            "Extract Web from Html Files": FormExtractFromHtmlFiles,
            "Extract IMDB": FormExtractIMDB,
            "IMDB Search": FormIMDBSearch,
            "Extract Web from Url File": FormExtractFromLinkFile,
            "Create Cover": FormCreateCover,
            "Fix Subtitle": FormFixSub,
            "Extract IMDB All Pics": FormExtractIMDBAllPics,
            "Categorize": FormCategorize
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

    demo = App()
    demo.show()

    sys.exit(app.exec_())
