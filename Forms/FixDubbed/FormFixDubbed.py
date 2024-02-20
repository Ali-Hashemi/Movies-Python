import os
from Forms.FixDubbed.ClassFixDubbed import FixDubbed
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

                if os.path.isdir(file):
                    pass
                    # is_folder(h + t + "\\")
                elif os.path.isfile(file):
                    Print.print_green(t)
                    Print.print_white("")
                    FixDubbed(t, h)
                    Print.print_full_line(CustomColor.RED)
