import os
from Forms.CategorizeFilms.ClassCategorize import ClassCategorize
from Base import *
from Config import *
from Classes import *


class Form(BaseMainWindow):
    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                if os.path.isdir(file):
                    ClassCategorize(t, h)
