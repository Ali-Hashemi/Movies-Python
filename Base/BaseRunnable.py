from Config import *
from PyQt5.QtCore import QRunnable

class BaseRunnable(QRunnable):
    def __init__(self, array, listbox, form=None):
        super().__init__()

        self.form = form

        self.list = array

        self.listbox = listbox

    def run(self):
        pass
