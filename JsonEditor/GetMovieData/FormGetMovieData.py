from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.GetMovieData.MainWindow import Ui_MainWindow
from JsonEditor.CustomListView import *
from JsonEditor.GetMovieData.ClassGetMovieData import GetMovieData


class MainWindow(BaseForm, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.comboBox.currentIndex()

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(20, 80, CustomStyle.main_list_widget_width,
                                                                         CustomStyle.main_list_widget_height))

        self.pushButton_get_htmls.clicked.connect(lambda: (self.get_items(self.listWidget)))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items(self.listWidget)))

    class Runnable(BaseRunnable):
        def run(self):
            checkbox_dubbed_status = self.form.checkBox_dubbed.isChecked()
            combo_box_index = self.form.comboBox.currentIndex()

            for item in self.list:
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                GetMovieData(t, h, checkbox_dubbed_status, combo_box_index)

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
