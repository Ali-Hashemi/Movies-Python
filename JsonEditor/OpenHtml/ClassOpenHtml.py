from Base import *
from Config import *
from Classes.Class30nama import Class30nama
from Classes.ClassIMDB import ClassIMDB
from Classes.ClassUtility import *
from Base import *


class OpenHtml:

    def __init__(self, folder, combo_box_index):

        html_30nama = rename_file_paths_by_os(folder) + CustomNames.HTML_30nama_FILE_NAME
        html_imdb = rename_file_paths_by_os(folder) + CustomNames.HTML_IMDB_FILE_NAME
        html_doostiha = rename_file_paths_by_os(folder) + CustomNames.HTML_DOOSTIHA_FILE_NAME
        html_hexdownload = rename_file_paths_by_os(folder) + CustomNames.HTML_Hex_FILE_NAME

        json_path = rename_file_paths_by_os(folder) + CustomNames.EXTRACTED_DATA

        if combo_box_index == 0:
            if os.path.exists(html_30nama):
                open_html_file_in_browser(html_30nama)
            elif os.path.exists(json_path):
                class30nama = Class30nama()
                film = class30nama.get_data_from_json_file(json_path)
                url_30nama = film.url_30nama

                if url_30nama:
                    open_in_browser(url_30nama)
                    sleep(12)

        elif combo_box_index == 1:
            if os.path.exists(html_imdb):
                # soup = Html.get_soup_from_file(html_imdb)
                # if soup:
                # self.get_parent_guide(soup, folder_name=get_last_file_or_folder_from_path(folder))
                open_html_file_in_browser(html_imdb)
            elif os.path.exists(json_path):
                class30nama = Class30nama()
                film = class30nama.get_data_from_json_file(json_path)
                url_imdb = film.url_imdb

                if url_imdb:
                    open_in_browser(url_imdb)
            elif os.path.exists(html_30nama):
                class30nama = Class30nama()
                film = class30nama.get_data_from_html_file(html_30nama)
                url_imdb = film.url_imdb
                if url_imdb:
                    open_in_browser(url_imdb)

        elif combo_box_index == 2:
            if os.path.exists(html_doostiha):
                open_html_file_in_browser(html_doostiha)

        elif combo_box_index == 3:
            if os.path.exists(html_hexdownload):
                open_html_file_in_browser(html_hexdownload)

    def get_parent_guide(self, soup, folder_name):
        Print.print_blue(folder_name)

        parent_guide = ClassIMDB.get_parent_guide(soup)

        if parent_guide:
            Print.print_yellow(parent_guide)

        Print.print_full_line(CustomColor.WHITE)
