from Config import *
from Classes.ClassUtility import *
from Data.Film import *
from Base import *


class Cinama:
    name_without_date = None
    release_date = None
    film_type = None
    search_type = None
    browser_type = None
    location = None

    def __init__(self, name, location, film_type, browser_type):
        self.name_without_date = File.trim_name_movie(name)
        self.name_without_date = File.trim_name_tv_series(self.name_without_date)

        self.location = location

        self.release_date = File.trim_released_date(name)

        self.film_type = film_type

        self.browser_type = browser_type

        folder_path = location + name

        json_path = ""

        if os.path.isdir(location + name):
            json_path = rename_file_paths_by_os(location + name) + CustomNames.EXTRACTED_DATA
        else:
            json_path = rename_file_paths_by_os(location) + CustomNames.EXTRACTED_DATA

        if os.path.exists(json_path):
            cinama_url = Film.json_file_to_class(json_path).url_30nama
            if cinama_url:
                open_in_browser(cinama_url, self.browser_type)
                sleep(8)

        else:
            search_url = self.get_search_url()

            if search_url:
                open_in_browser(search_url, self.browser_type)
                sleep(15)

    def get_search_url(self):

        url = None

        name_with_release_date = filter_name_for_url_30nama(self.name_without_date + " " + self.release_date)
        # name_with_release_date = filter_name_for_url_30nama(self.name_without_date + " ")

        if self.film_type == 1:
            url = "https://30nama.com/explore?sortBy=favorite&type=15&q=" + name_with_release_date

        elif self.film_type == 2:
            url = "https://30nama.com/explore?sortBy=favorite&type=16&q=" + name_with_release_date

        elif self.film_type == 3:
            url = "https://30nama.com/explore?sortBy=favorite&type=3357&q=" + name_with_release_date

        return url
