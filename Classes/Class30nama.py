from Data import *
from Classes.ClassUtility import *


class Class30nama:

    @staticmethod
    def get_data_from_html_file(html_location):
        if os.path.exists(html_location):
            soup = Html.get_soup_from_file(html_location)

            if soup:
                film = Class30nama.get_all_infos_from_soup(soup)
                return film
        else:
            Print.print_red("Html file not exist")
            return None

    def get_all_infos_from_url(self, url) -> [Film(), str]:
        film = Film()

        full_title = None

        info_page_soup = Html.get_soup_with_chrome_driver_undetected(url, timer=30)

        if info_page_soup:
            film = self.get_all_infos_from_soup(info_page_soup)
            full_title = Class30nama.get_full_title(info_page_soup)

        return film, full_title

    def get_all_infos_for_folder(self, url, folder_location) -> Film:
        film = Film()

        info_page_soup = Html.get_soup_with_chrome_driver_undetected(url, timer=30, folder_path=folder_location,
                                                                     soup_name=CustomNames.HTML_30nama_FILE_NAME)

        if info_page_soup:
            film = self.get_all_infos_from_soup(info_page_soup)

        return film

    @staticmethod
    def get_data_from_json_file(json_file):
        if os.path.exists(json_file):
            json_data = Film.json_file_to_class(json_file)
            if json_data:
                film = Film()
                film.per_title = json_data.per_title
                film.per_genre = json_data.per_genre
                film.per_info = json_data.per_info
                film.url_imdb = json_data.url_imdb
                film.url_30nama = json_data.url_30nama

                return film
        else:
            return None

    @staticmethod
    def get_all_infos_from_soup(soup):
        if soup:
            class30nama = Class30nama()
            film = Film()
            film.per_title = class30nama.get_per_title(soup)
            film.per_info = class30nama.get_per_info(soup)
            film.per_genre = class30nama.get_genre(soup)
            film.url_30nama = class30nama.get_page_url(soup)
            film.url_imdb = class30nama.get_imdb_url_and_score(soup)

            return film
        else:
            return None

    def get_page_url(self, soup) -> str:
        url = None

        elements1_array = [
            Element("main", "main-box basic-info"),
            Element("section", "title-frame")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            a = found_element.find("a", href=True)

            if a:
                url_temp = strip_text(a['href'])

                if url_temp:
                    if find_in_text(url_temp, "https://30nama.com"):
                        url = url_temp
                    else:
                        url = str("https://30nama.com") + url_temp

        return url

    def get_imdb_url_and_score(self, soup) -> [str, str]:
        url = None
        score = None

        elements1_array = [
            Element("section", "figcaption-content"),
            Element("ul", "ratings"),
            Element("li", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for li in found_element:
                for a in li.find_all("a", href=True):
                    if strip_text(a['href']).lower().find("www.imdb.com") != -1:
                        url = strip_text(a['href'])

                        # for div in a.find_all("div", {"class": "counts"}):
                        #     counter = 0
                        #     for p in div.find_all("p"):
                        #         if counter < 1:
                        #             score = strip_text(p.text)
                        #             counter += 1

        return url

    @staticmethod
    def get_full_title(soup) -> str:
        full_title = None

        elements_array = [
            Element("section", "figcaption-content"),
            Element("div", "title-box figcaption-child"),
            Element("h2", "h2 title")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements_array)

        if found_element:
            full_title = strip_text(found_element.text)

        return full_title

    def get_per_title(self, soup) -> str:
        per_title = None

        elements1_array = [
            Element("section", "figcaption-content"),
            Element("div", "title-box figcaption-child"),
            Element("h3", "persian-title")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            per_title = found_element.text
            per_title = per_title.strip()
            per_title = per_title.replace(": ", " : ")
            per_title = per_title.replace("\u200e", " ")
            per_title = per_title.replace("-", " ")
            Print.print_white(per_title)

        return per_title

    def get_genre(self, soup) -> []:
        genre = []

        elements1_array = [
            Element("section", "figcaption-content"),
            Element("ul", "genre-ul"),
            Element("li", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for li in found_element:
                genre.append(strip_text(li.text))

        return genre

    def get_per_info(self, soup) -> str:
        found = None

        elements1_array = [
            Element("section", "figcaption-content"),
            Element("div", "plot-watchlist"),
            Element("div", "content")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            content = strip_text(found_element.text)
            content = content.replace("\u200e", " ")
            content = str(content).replace("...", "")
            found = str(content).replace("..", "")
            found = str(found).replace("'", "")

            if found[-1] == ".":
                found = found[:-1]

            found = strip_text(found)

        return found

    @staticmethod
    def is_json_complete(json_file) -> bool:
        is_complete = True

        if os.path.exists(json_file):
            film = Film.json_file_to_class(json_file)

            fields = [
                # film.per_title,
                film.per_info,
                film.per_genre,
                film.url_imdb,
                film.url_30nama
            ]

            for i in fields:
                if not i:
                    is_complete = False

        return is_complete

    @staticmethod
    def is_film_complete(film) -> bool:
        is_complete = True

        fields = [
            # film.per_title,
            film.per_info,
            film.per_genre,
            film.url_imdb,
            film.url_30nama
        ]

        for i in fields:
            if not i:
                is_complete = False

        return is_complete

    @staticmethod
    def check_for_html_file(location):
        html_file = 0

        if os.path.exists(location):
            if os.path.exists(rename_file_paths_by_os(location) + CustomNames.HTML_30nama_FILE_NAME):
                html_file = rename_file_paths_by_os(location) + CustomNames.HTML_30nama_FILE_NAME

        return html_file
