from Config import *
from PyQt5 import QtWidgets


class BaseForm(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

        self.array = []

    def get_items(self, listbox):
        listbox.setAcceptDrops(False)

        del self.array[:]

        for index in range(listbox.count()):
            self.array.append(listbox.item(index).text())

        pool = QThreadPool.globalInstance()
        runnable = self.Runnable(self.array, listbox, form=self)
        pool.start(runnable)

        listbox.setAcceptDrops(True)

        listbox.clear()

    def clear_items(self, listbox):
        listbox.clear()
        del self.array[:]
