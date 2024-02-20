from Classes.ClassUtility import *
from Base import *

class TakeScreenshot:
    def __init__(self, name, location, spin_box, combo_box_index):
        folder_path = location + name

        html_file = None
        png_file = None

        if combo_box_index == 0:
            html_file = rename_file_paths_by_os(folder_path) + CustomNames.HTML_30nama_FILE_NAME
            png_file = rename_file_paths_by_os(folder_path) + CustomNames.PNG_30nama_FILE_NAME
        elif combo_box_index == 1:
            html_file = rename_file_paths_by_os(folder_path) + CustomNames.HTML_IMDB_FILE_NAME
            png_file = rename_file_paths_by_os(folder_path) + CustomNames.PNG_IMDB_FILE_NAME

        if html_file and png_file:
            if os.path.exists(html_file):
                Print.print_green(name)
                Html.html2png(html_file, png_file, zoom=str(spin_box))
                Print.print_full_line(CustomColor.WHITE)
