from Base import *
from Config import *
from PyQt5 import QtCore, QtWidgets
from Data.Film import *
from JsonEditor.CustomListView import *
from JsonEditor.TakeScreenshot.MainWindow import Ui_MainWindow
from Classes.Class30nama import *
from JsonEditor.TakeScreenshot.ClassTakeScreenshot import TakeScreenshot


class MainWindow(BaseForm, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.listWidget = ListBoxWidget(self.centralwidget, QtCore.QRect(20, 20, 300, 451))

        self.pushButton_get_htmls.clicked.connect(lambda: (self.get_items(self.listWidget)))
        self.pushButton_clear.clicked.connect(lambda: (self.clear_items(self.listWidget)))

    class Runnable(BaseRunnable):
        def run(self):
            for item in self.list:
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)
                spin_box_value = self.form.spinBox.text()
                combo_box_index = self.form.comboBox.currentIndex()

                TakeScreenshot(t, h, spin_box_value, combo_box_index)

# app = QtWidgets.QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()
