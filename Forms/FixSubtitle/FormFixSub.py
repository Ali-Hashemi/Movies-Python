import os
import subprocess
from Classes.ClassUtility import *
from pymediainfo import MediaInfo

from Base import *
from Config import *
from Forms.FixSubtitle.ClassFixSub import FixSubbed


class Form(BaseMainWindow):
    class Runnable(BaseRunnable):
        def run(self):
            for index in range(len(self.list)):
                item = self.list[index]
                file = rename_file_paths_for_files(item)

                FixSubbed(file)

