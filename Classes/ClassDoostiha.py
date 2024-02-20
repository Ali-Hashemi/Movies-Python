from Data import *


class ClassDoostiha:
    @staticmethod
    def get_data_from_html_file(html_location):
        if os.path.exists(html_location):
            soup = Html.get_soup_from_file(html_location)

            if soup:
                film = ClassDoostiha.get_all_infos_from_soup(soup)
                return film
        else:
            Print.print_red("Html file not exist")
            return None

    @staticmethod
    def get_all_infos_from_url(url):
        film = Film()

        soup = Html.get_soup(url)

        classDoostiha = ClassDoostiha()

        if soup:
            film.per_info = classDoostiha.get_per_info(soup)
            film.per_genre = classDoostiha.get_genre(soup)
            film.director = classDoostiha.get_director(soup)
            film.actors = classDoostiha.get_actors(soup)
        return film

    @staticmethod
    def get_data_from_json_file(json_file):
        if os.path.exists(json_file):
            json_data = Film.json_file_to_class(json_file)
            if json_data:
                film = Film()
                film.per_info = json_data.per_info
                film.per_genre = json_data.per_genre
                film.director = json_data.director
                film.actors = json_data.actors

                film.per_title = json_data.per_title
                film.eng_title = json_data.eng_title
                film.release = json_data.release

                return film
        else:
            return None

    @staticmethod
    def get_all_infos_from_soup(soup):
        film = Film()

        classDoostiha = ClassDoostiha()

        if soup:
            film.per_info = classDoostiha.get_per_info(soup)
            film.per_genre = classDoostiha.get_genre(soup)
            film.director = classDoostiha.get_director(soup)
            film.actors = classDoostiha.get_actors(soup)
        return film

    def get_page_url(self, soup) -> str:
        url = None

        # main = soup.find("main", {"class": ["main-box", "basic-info"]})
        #         # if main:
        #         #     section = main.find("section", {"class": "title-frame"})
        #         #     if section:
        #         #         a = section.find("a", {"class": ["nuxt-link-exact-active", "nuxt-link-active"]})
        #         #         if a:
        #         #             url = strip_text(a['href'])

        return url

    def get_genre(self, soup) -> []:
        genre = []

        elements1_array = [
            Element("div", "article_txtc"),
            Element("div", "textkian0"),
            Element("p", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for i in found_element:
                filter_names = [
                    "ژانر فیلم:",
                    "موضوع فیلم:",
                    "موضوع:",
                    "مـوضوع:",
                    "ژانر:",
                ]
                seperator = str("|")

                if find_in_text(i, seperator):
                    all_line = strip_text(i.text).split("|")
                    if all_line:
                        for j in all_line:
                            for filter in filter_names:
                                if find_in_text(j, filter):
                                    content = strip_text(j)
                                    content = content.replace(filter, "")
                                    all_genre = filter_name_for_cast_and_info(content)

                                    if all_genre:
                                        array = all_genre.split("،")
                                        if len(array) > 1:
                                            for m in array:
                                                each_genre = filter_name_for_cast_and_info(strip_text(m))
                                                genre.append(each_genre)
                                        elif find_in_text(all_genre, " "):
                                            each_genre_with_space_between = ""
                                            genres_to_translate = {
                                                "اجتماعی": "درام",
                                                "طنز": "کمدی",
                                                "رومانتیک": "عاشقانه",
                                                "ملودرام": "درام"
                                            }
                                            if not (find_in_text(all_genre, "دفاع") and find_in_text(all_genre,
                                                                                                     "مقدس")):
                                                each_genre_with_space_between = all_genre.split(" ")
                                            else:
                                                genre.append("دفاع مقدس")
                                                all_genre.replace("دفاع مقدس", "")

                                            if each_genre_with_space_between:
                                                for m in each_genre_with_space_between:
                                                    if not m == "و":
                                                        m = filter_name_for_cast_and_info(m)
                                                        for value in genres_to_translate:
                                                            if find_in_text(m, value):
                                                                m.replace(value, genres_to_translate[value])
                                                        genre.append(m)

                                        else:
                                            each_genre = filter_name_for_cast_and_info(strip_text(all_genre))
                                            genre.append(each_genre)

                                        if genre:
                                            break
                            if genre:
                                break

        if genre:
            genre = remove_array_duplicates(genre)
            genre = Film.translate_per_genre(genre)
            genre = remove_array_duplicates(genre)

        return genre

    def get_director(self, soup) -> []:
        found = None

        elements1_array = [
            Element("div", "article_txtc"),
            Element("div", "textkian0"),
            Element("p", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for i in found_element:
                filter_names = [
                    "نویسنده و کارگردان:",
                    "کارگردان:"
                ]
                seperator = str("|")

                if find_in_text(i, seperator):
                    all_line = strip_text(i.text).split("|")
                    if all_line:
                        for j in all_line:
                            for filter in filter_names:
                                if find_in_text(j, filter):
                                    content = j.replace(filter, "")
                                    found = filter_name_for_cast_and_info(content)
                                    break
                            if found:
                                break

        return found

    def get_actors(self, soup) -> []:
        cast = []

        elements1_array = [
            Element("div", "article_txtc"),
            Element("div", "textkian0"),
            Element("p", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for i in found_element:
                filter_names = [
                    "بازیگران:"
                ]

                for filter in filter_names:
                    if find_in_text(i, filter):
                        content = strip_text(i.text)
                        content = content.replace(filter, "")
                        content = content.replace("\u200e", " ")
                        content = content.replace(" و ", "،")
                        content = content.replace("…", "")
                        all_cast = strip_text(content)

                        if all_cast:
                            array = all_cast.split("،")
                            if array:
                                for i in array:
                                    each_cast = filter_name_for_cast_and_info(strip_text(i))
                                    if each_cast:
                                        cast.append(each_cast)

        if cast:
            cast = remove_array_duplicates(cast)
        return cast

    def get_per_info(self, soup) -> str:
        found = None

        elements1_array = [
            Element("div", "article_txtc"),
            Element("div", "textkian0"),
            Element("p", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for i in found_element:
                filter_names = [
                    "خلاصه فیلم به نقل گروه تولید:",
                    "خلاصه داستان:",
                    "خلاصه فیلم:",
                    "خلاصه:"
                ]

                for filter in filter_names:
                    if find_in_text(i, filter):
                        content = strip_text(i.text)
                        content = content.replace(filter, "")
                        found = filter_name_for_cast_and_info(content)

        return found

    @staticmethod
    def get_release_date(soup) -> str:
        found = None

        elements1_array = [
            Element("div", "article_txtc"),
            Element("div", "textkian0"),
            Element("p", "", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            for i in found_element:
                filter_names = [
                    "تاریخ انتشار:",
                    "تاریخ انتشار"
                    "انتشار:",
                    "انتشار",
                    "سال تولید:",
                    "سال تولید",
                    "تاریخ تولید:",
                    "تاریخ تولید"
                ]
                seperator = str("|")

                if find_in_text(i, seperator):
                    all_line = strip_text(i.text).split("|")
                    if all_line:
                        for j in all_line:
                            for filter in filter_names:
                                if find_in_text(j, filter):
                                    content = j.replace(filter, "")
                                    content = filter_name_for_cast_and_info(content)
                                    found = File.trim_released_date(content)
                                    break
                            if found:
                                break

        return found

    @staticmethod
    def is_json_empty(json_file) -> bool:
        is_complete = True

        if os.path.exists(json_file):
            film = Film.json_file_to_class(json_file)

            fields = [
                film.per_genre,
                film.director,
                film.actors,
                film.per_info
            ]

            for i in fields:
                if not i:
                    is_complete = False

        return is_complete

    @staticmethod
    def is_film_complete(film) -> bool:
        is_complete = True

        fields = [
            film.per_genre,
            film.director,
            film.actors,
            film.per_info
        ]

        for i in fields:
            if not i:
                is_complete = False

        return is_complete
