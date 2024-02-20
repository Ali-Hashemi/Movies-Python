from Forms.Rename.ClassRename import Rename
from Base import *
from Config import *
from Classes.ClassUtility import *


class Form(BaseMainWindow):
    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_for_files(item)
                h, t = get_path_and_file(file)

                if os.path.isfile(file):
                    Rename(t, h)
