from Data import *


class ClassHex:
    @staticmethod
    def get_data_from_html_file(html_location):
        if os.path.exists(html_location):
            soup = Html.get_soup_from_file(html_location)

            if soup:
                film = ClassHex.get_all_infos_from_soup(soup)
                return film
        else:
            Print.print_red("Html file not exist")
            return None

    @staticmethod
    def get_all_infos_from_url(url):
        film = Film()

        soup = Html.get_soup(url)

        classHex = ClassHex()

        if soup:
            film.per_info = classHex.get_per_info(soup)
            film.per_genre = classHex.get_genre(soup)
            film.director = classHex.get_director(soup)
            film.actors = classHex.get_actors(soup)
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

        classHex = ClassHex()

        if soup:
            film.per_info = classHex.get_per_info(soup)
            film.per_genre = classHex.get_genre(soup)
            film.director = classHex.get_director(soup)
            film.actors = classHex.get_actors(soup)
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
            Element("div", "entry-content"),
            Element("div", "post-right"),
            Element("p", "film-genre")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        filter_names = [
            "ژانر (موضوع) :",
            "ژانر :"
        ]

        filters_separators = [
            "،",
            ",",
            "-"
        ]

        if found_element:
            content = strip_text(found_element.text)

            for filter in filter_names:
                if find_in_text(content, filter):
                    content = content.replace(filter, "")
                    content = filter_name_for_cast_and_info(content)
                    break

            for filter4 in filters_separators:
                if find_in_text(content, filter4):
                    for item in content.split(filter4):
                        genre.append(strip_text(item))
                    break
                if genre:
                    break
            if not genre:
                genre.append(strip_text(content))

        if not genre:
            elements2_array = [
                Element("div", "entry-content"),
                Element("p", "", find_all=True)
            ]

            found_element2 = Html.find_elements_in_multiple_soup_array_best(soup, elements2_array)

            if found_element2:
                for i in found_element2:
                    if i:
                        span = i.find("span")
                        if span != -1 and span:
                            span_text = strip_text(span.text)
                            content = None

                            for filter2 in filter_names:
                                if find_in_text(span_text, filter2):
                                    content = strip_text(i.text)

                            if content:
                                for j in content.split("|"):
                                    final = None

                                    for filter3 in filter_names:
                                        if find_in_text(j, filter3):
                                            final = j.replace(filter3, "")
                                            final = strip_text(final)

                                    if final:
                                        for filter4 in filters_separators:
                                            if find_in_text(final, filter4):
                                                for item in final.split(filter4):
                                                    genre.append(strip_text(item))
                                                break
                                            if genre:
                                                break
                                        if not genre:
                                            genre.append(strip_text(final))
        if genre:
            genre = remove_array_duplicates(genre)
            genre = Film.translate_per_genre(genre)
            genre = remove_array_duplicates(genre)

        return genre

    def get_director(self, soup) -> []:
        found = None

        elements1_array = [
            Element("div", "entry-content"),
            Element("div", "post-right"),
            Element("p", "film-director")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            content = strip_text(found_element.text)
            text = str("کارگردان :")
            content = content.replace(text, "")
            content = content.replace("\u200e", " ")
            found = strip_text(content)

        if not found:
            elements2_array = [
                Element("div", "entry-content"),
                Element("p", "", find_all=True)
            ]

            found_element2 = Html.find_elements_in_multiple_soup_array_best(soup, elements2_array)

            if found_element2:
                for i in found_element2:
                    span = i.find("span")
                    if span:
                        span_text = strip_text(span.text)
                        text_to_find = "کارگردان :"

                        if find_in_text(span_text, text_to_find):
                            content = strip_text(i.text)
                            for j in content.split("|"):
                                if find_in_text(j, text_to_find):
                                    j = j.replace(text_to_find, "")
                                    j = j.replace("\u200e", " ")
                                    j = j.replace("\u200c", " ")
                                    j = strip_text(j)
                                    found = j

        return found

    def get_actors(self, soup) -> []:
        cast = []

        elements1_array = [
            Element("div", "entry-content"),
            Element("div", "post-right"),
            Element("p", "film-actor")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            full_text = strip_text(found_element.text)
            texts_to_find = ["بازیگران فیلم :", "بازیگران :"]

            for each_text in texts_to_find:
                if find_in_text(full_text, each_text):
                    content = full_text.replace(each_text, "")
                    content = filter_name_for_cast_and_info(content)

                    characters = ["،", ",", " و "]

                    for c in characters:
                        if find_in_text(content, c):
                            for i in content.split(c):
                                item = filter_name_for_cast_and_info(i)
                                cast.append(item)

        if not cast:
            elements2_array = [
                Element("div", "entry-content"),
                Element("p", "", find_all=True)
            ]

            found_element2 = Html.find_elements_in_multiple_soup_array_best(soup, elements2_array)

            if found_element2:
                for i in found_element2:
                    full_text = i.text

                    if full_text:
                        texts_to_find = ["بازیگران فیلم :", "بازیگران :"]
                        content = None

                        if find_in_text(full_text, texts_to_find[0]):
                            content = full_text.replace(texts_to_find[0], "")
                            content = filter_name_for_cast_and_info(content)
                        elif find_in_text(full_text, texts_to_find[1]):
                            content = full_text.replace(texts_to_find[1], "")
                            content = filter_name_for_cast_and_info(content)

                        if content:
                            characters = ["،", ",", " و "]

                            for c in characters:
                                if not cast:
                                    if find_in_text(content, c):
                                        for i in content.split(c):
                                            item = filter_name_for_cast_and_info(i)
                                            cast.append(item)

        return cast

    def get_per_info(self, soup) -> str:
        found = None

        elements1_array = [
            Element("div", "entry-content"),
            Element("div", "post-center"),
            Element("p", "film-story")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            content = strip_text(found_element.text)
            text_to_find = str("خلاصه داستان :")

            content = content.replace(text_to_find, "")
            found = filter_name_for_cast_and_info(content)

        if not found:
            elements2_array = [
                Element("div", "entry-content"),
                Element("div", "post-right"),
                Element("p", "film-story")
            ]

            found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements2_array)

            if found_element:
                content = strip_text(found_element.text)
                text_to_find = str("خلاصه داستان :")

                content = content.replace(text_to_find, "")
                found = filter_name_for_cast_and_info(content)

            if not found:
                elements2_array = [
                    Element("div", "entry-content"),
                    Element("p", "", find_all=True)
                ]

                found_element2 = Html.find_elements_in_multiple_soup_array_best(soup, elements2_array)

                if found_element2:
                    for i in found_element2:
                        full_text = i.text

                        texts_to_find = ["خلاصه داستان :", "خلاصه ی داستان فیلم :"]

                        for each_text in texts_to_find:
                            if find_in_text(full_text, each_text):
                                content = full_text.replace(each_text, "")
                                found = filter_name_for_cast_and_info(content)

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
