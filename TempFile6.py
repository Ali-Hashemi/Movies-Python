import re
from Classes.ClassDoostiha import *
from Classes.ClassHex import *
from Classes.ClassIMDB import *
from Classes.Timer import Timer

class Main():
    path = rename_file_paths_by_os("E:/00-Covers/My Book 6TB")

    parent_guides_array = []

    def __init__(self):
        timer = Timer()
        for root, subdirs, files in os.walk(self.path):
            regex = str("20\d{2}" + "|" + "19\d{2}" + "|" + "13\d{2}" + "|" + "14\d{2}")
            if re.search(regex, str(root)):
                # self.get_imdb_html(root)
                self.get_parent_guide(root)
        timer.end()

    def get_parent_guide(self, item):
        folder = rename_file_paths_by_os(item)
        html_imdb = folder + CustomNames.HTML_IMDB_FILE_NAME
        json_path = folder + CustomNames.EXTRACTED_DATA

        if os.path.exists(json_path) and os.path.exists(html_imdb):
            title = get_last_file_or_folder_from_path(folder)
            print(title)

            film = Film.json_file_to_class(json_path)

            if film.parent_guide:
                self.parent_guides_array.append(film.parent_guide)

            imdb_soup = Html.get_soup_from_file(html_imdb)

            if imdb_soup and not film.parent_guide:
                film.parent_guide = ClassIMDB.get_parent_guide(imdb_soup)

            self.save_to_json(film, json_path)

    def get_imdb_html(self, item):
        folder = rename_file_paths_by_os(item)
        html_imdb = folder + CustomNames.HTML_IMDB_FILE_NAME
        json_path = folder + CustomNames.EXTRACTED_DATA
        if not os.path.exists(html_imdb):
            print(get_last_file_or_folder_from_path(item))

            if os.path.exists(json_path):
                imdb_url = Film.json_file_to_class(json_path).url_imdb

                if imdb_url:
                    Html.get_soup(imdb_url, folder_path=item, soup_name=CustomNames.HTML_IMDB_FILE_NAME)

    def save_to_json(self, film: Film, json_file_path, check_dubbed_status=0):
        film.dubbed = check_dubbed_status

        Json.write_to_json_file(film, json_file_path)


Main()