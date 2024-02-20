from Base.BaseListBox import *
from Base.BasePrimaryButton import *
from Base.BaseSecondaryButton import *


class BaseMainWindow(QMainWindow):

    def __init__(self, parent=None, width=None, height=None):
        super(BaseMainWindow, self).__init__(parent)
        self.setWindowTitle("Movies")
        self.setWindowIcon(QIcon("Cover.ico"))
        if width and height:
            self.resize(QSize(width, height))
        else:
            self.resize(CustomStyle.form_size)

        self.array = []

        self.listbox_view = BaseListBoxWidget(self)

        self.fix_button = BasePrimaryButton('Fix list', self)

        self.clear_button = BaseSecondaryButton('Clear list', self)

    def get_items(self, listbox: QListWidget):
        listbox.setAcceptDrops(False)

        del self.array[:]

        for index in range(listbox.count()):
            self.array.append(listbox.item(index).text())

        pool = QThreadPool.globalInstance()
        runnable = self.Runnable(self.array, listbox)
        pool.start(runnable)

        listbox.setAcceptDrops(True)

        listbox.clear()
