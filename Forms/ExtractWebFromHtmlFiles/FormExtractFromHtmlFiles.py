import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Base.BaseMainWindow import BaseMainWindow
from Base.BaseRunnable import BaseRunnable
from Classes.ClassUtility import *
from Forms.ExtractWebFromHtmlFiles.ClassExtractFromHtmlFiles import ExtractFromHtmlFiles


class Form(BaseMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                ExtractFromHtmlFiles(t, h)
