from Config import *
from Classes import *
from Classes.ClassUtility import *
from Data import *
from selenium.webdriver.common.by import By


class ClassIMDB:
    engtitle_release_parent_first_element1 = Element("div", "sc-e226b0e3-3 jJsEuz")
    engtitle_release_parent_first_element2 = Element("div", "sc-dffc6c81-0 iwmAVw")

    @staticmethod
    def get_data_from_html_file(html_location) -> Film:
        soup = Html.get_soup_from_file(html_location)

        film = ClassIMDB.get_all_infos_from_soup(soup)

        return film

    @staticmethod
    def get_all_infos_from_url(url, folder_path=None):
        Print.print_yellow("Getting IMDB informations ......")

        # soup = Html.get_soup(url)
        # soup = Html.get_soup(url, timer=1, folder_path=folder_path,
        #                      soup_name=CustomNames.HTML_IMDB_FILE_NAME)

        # soup = Html.get_soup(url, timer=1, folder_path=folder_path,
        #                      soup_name=CustomNames.HTML_IMDB_FILE_NAME)

        soup = Html.get_soup(url, timer=1, folder_path=folder_path, soup_name="imdb.html")
        # soup = Html.get_soup_for_subscene(url, timer=4, folder_path=folder_path, soup_name="imdb.html")

        if soup:
            classImdb = ClassIMDB()

            film = Film()
            film.eng_title = classImdb.get_eng_title(soup)
            film.release = classImdb.get_release_date(soup)
            film.score = classImdb.get_score(soup)
            film.director = classImdb.get_director(soup)
            film.actors = classImdb.get_cast(soup)
            film.eng_genre = classImdb.get_eng_genre(soup)
            film.eng_info = classImdb.get_eng_info(soup)
            film.country = classImdb.get_country(soup)
            film.parent_guide = classImdb.get_parent_guide(soup)

            return film
        else:
            return None

    @staticmethod
    def get_data_from_json_file(json_file):
        if os.path.exists(json_file):
            json_data = Film.json_file_to_class(json_file)

            film = Film()
            film.eng_title = json_data.eng_title
            film.release = json_data.release
            film.score = json_data.score
            film.director = json_data.director
            film.actors = json_data.actors
            film.eng_info = json_data.eng_info
            film.eng_genre = json_data.eng_genre
            film.country = json_data.country
            film.parent_guide = json_data.parent_guide

            return film
        else:
            return None

    @staticmethod
    def get_all_infos_from_soup(soup):
        if soup:
            classImdb = ClassIMDB()

            film = Film()
            film.eng_title = classImdb.get_eng_title(soup)
            film.release = classImdb.get_release_date(soup)
            film.score = classImdb.get_score(soup)
            film.director = classImdb.get_director(soup)
            film.actors = classImdb.get_cast(soup)
            film.eng_genre = classImdb.get_eng_genre(soup)
            film.eng_info = classImdb.get_eng_info(soup)
            film.country = classImdb.get_country(soup)
            film.parent_guide = classImdb.get_parent_guide(soup)
            return film
        else:
            return None

    def get_eng_title(self, soup) -> str:
        eng_title = None

        elements1_array = [
            Element("div", "sc-b5e8e7ce-0 dZsEkQ"),
            Element("div", "sc-b5e8e7ce-1 kNhUtn"),
        ]

        elements2_array = [
            Element("div", "sc-ab3b6b3d-3 goiwap"),
            Element("div", "sc-eda143c4-0 gGwFYG"),
        ]

        elements3_array = [
            Element("div", "sc-ab3b6b3d-3 goiwap"),
            Element("div", "sc-2971dade-0 YVoIO"),
        ]

        elements4_array = [
            Element("div", "sc-385ac629-3 kRUqXl"),
            Element("div", "sc-2971dade-0 YVoIO"),
        ]

        elements5_array = [
            self.engtitle_release_parent_first_element1,
            self.engtitle_release_parent_first_element2,
        ]

        found = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array,
                                                               elements2_array, elements3_array,
                                                               elements4_array, elements5_array)

        if found:
            # find2 = found.select("h1")
            find2 = found.select("h1[data-testid='hero__pageTitle']")

            if find2:
                eng_title = find2[0].text
                eng_title = str(eng_title).replace(":", " ")
                eng_title = strip_text(eng_title)

        return eng_title

    @staticmethod
    def get_parent_guide(soup) -> str:
        parent_guide = None

        elements1_array = [
            Element("div", "sc-b5e8e7ce-0 dZsEkQ"),
            Element("div", "sc-b5e8e7ce-2 AIESV"),
            Element("ul", "sc-f26752fb-0 iQHuAC"),
            Element("li", "", find_all=True)
        ]

        elements2_array = [
            Element("div", "sc-b5e8e7ce-1 kNhUtn"),
            Element("div", "sc-b5e8e7ce-2 AIESV"),
            Element("ul", "sc-f26752fb-0 iQHuAC"),
            Element("li", "", find_all=True)
        ]

        elements3_array = [
            Element("div", "sc-ab3b6b3d-3 goiwap"),
            Element("div", "sc-2971dade-0 YVoIO"),
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
            Element("li", "", find_all=True)
        ]

        elements4_array = [
            Element("div", "sc-385ac629-3 kRUqXl"),
            Element("div", "sc-2971dade-0 YVoIO"),
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
            Element("li", "", find_all=True)
        ]

        elements5_array = [
            ClassIMDB.engtitle_release_parent_first_element1,
            ClassIMDB.engtitle_release_parent_first_element2,
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
            Element("li", "", find_all=True)
        ]

        found = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array, elements2_array, elements3_array,
                                                               elements4_array, elements5_array)

        if found:
            for li in found:
                a = li.find_all("a", {"role": "button"})
                if a:
                    for k in a:
                        content = strip_text(k.text)
                        if not is_contain_4_digit_numbers(content) and not is_contain_hour_or_minute(content):
                            parent_guide = content
                            break
                if parent_guide:
                    break

        return parent_guide

    def get_release_date(self, soup) -> str:
        release_date = None

        regex = str("20\d{2}" + "|" + "19\d{2}")

        elements1_array = [
            Element("div", "sc-b5e8e7ce-0 dZsEkQ"),
            Element("div", "sc-b5e8e7ce-2 AIESV"),
            Element("ul", "sc-f26752fb-0 iQHuAC"),
        ]

        elements2_array = [
            Element("div", "sc-b5e8e7ce-1 kNhUtn"),
            Element("div", "sc-b5e8e7ce-2 AIESV"),
            Element("ul", "sc-f26752fb-0 iQHuAC"),
        ]

        elements3_array = [
            Element("div", "sc-ab3b6b3d-3 goiwap"),
            Element("div", "sc-2971dade-0 YVoIO"),
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
        ]

        elements4_array = [
            Element("div", "sc-385ac629-3 kRUqXl"),
            Element("div", "sc-2971dade-0 YVoIO"),
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
        ]

        elements5_array = [
            self.engtitle_release_parent_first_element1,
            self.engtitle_release_parent_first_element2,
            Element("ul", "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"),
        ]

        found = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array, elements2_array, elements3_array,
                                                               elements4_array, elements5_array)

        if found:
            text = strip_text(found.text)

            j = re.findall(regex, text)

            if j:
                date = j[0]
                date = str(date).replace("(", "")
                date = str(date).replace(")", "")

                release_date = date

        return release_date

    def get_score(self, soup):
        score = None

        elements_array1 = [
            Element("div", "sc-e457ee34-0 kqTStR"),
            Element("div", "sc-e457ee34-2 liUcIh"),
            Element("span", "sc-e457ee34-1 squoh")
        ]

        elements_array2 = [
            Element("div", "sc-bde20123-0 gtEgaf"),
            Element("div", "sc-bde20123-2 gYgHoj"),
            Element("span", "sc-bde20123-1 iZlgcd")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements_array1, elements_array2)

        if found_element:
            score = strip_text(found_element.text)
            Print.print_white(score)

        return score

    def get_director(self, soup) -> str:
        director = None

        elements_array = [
            Element("ul", "ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"),
            Element("li", "ipc-metadata-list__item", find_all=True),
        ]

        li = Html.find_elements_in_multiple_soup_array_best(soup, elements_array)

        if li:
            for a in li:
                dir_elements_array = [
                    Element("span", "ipc-metadata-list-item__label ipc-metadata-list-item__label--btn"),
                    Element("a", "ipc-metadata-list-item__label ipc-metadata-list-item__label--link")
                ]

                for p in dir_elements_array:
                    span = Html.find_elements_in_soup(a, p)

                    if span:
                        if (strip_text(span.text).lower().find("creator") != -1) or (
                                strip_text(span.text).lower().find("director") != -1):
                            inner_element = Element("ul",
                                                    "ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt")
                            ul = Html.find_elements_in_soup(a, inner_element)
                            if ul:
                                inner2_li = ul.find_all("li", {"class": "ipc-inline-list__item"})
                                if inner2_li:
                                    for value in inner2_li:
                                        director = strip_text(value.text)
                                        if director:
                                            break
                    if director:
                        break

                if director:
                    break

        return director

    def get_cast(self, soup) -> []:
        cast = []

        elements1_array = [
            Element("section", "sc-bfec09a1-0 bzDutS title-cast title-cast--movie"),
            Element("div", "ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid"),
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

        if found_element:
            counter = 0
            for items in found_element.find_all("div", {"class": ["sc-bfec09a1-5", "dGCmsL"]}):
                if counter < 7:
                    elements_array1 = [
                        Element("div", "sc-bfec09a1-7 iDmJtd"),
                        Element("a", "sc-bfec09a1-1 gfeYgX"),
                    ]

                    found_element2 = Html.find_elements_in_multiple_soup_array_best(items, elements_array1)

                    if found_element2:
                        cast.append(strip_text(found_element2.text))
                        counter += 1

        return cast

    def get_eng_genre(self, soup) -> []:
        eng_genre = []

        elements1_array = [
            Element("div", "sc-663f405c-4 hQbEKe"),
            Element("div", "sc-6cc92269-8 hmNIYl sc-663f405c-11 kHBavT"),
            Element("div", "ipc-chip-list--baseAlt ipc-chip-list sc-6cc92269-4 dYnuUz"),
            Element("a", "sc-6cc92269-3 iPPPLI ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements2_array = [
            Element("div", "sc-663f405c-2 lhDUmU"),
            Element("div", "sc-6cc92269-8 hmNIYl sc-663f405c-11 kHBavT"),
            Element("div", "ipc-chip-list--baseAlt ipc-chip-list sc-6cc92269-4 dYnuUz"),
            Element("a", "sc-6cc92269-3 iPPPLI ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements3_array = [
            Element("div", "sc-ab3b6b3d-10 eIuQVa"),
            Element("div", "ipc-chip-list--baseAlt ipc-chip-list"),
            Element("div", "ipc-chip-list__scroller"),
            Element("a", "ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements4_array = [
            Element("div", "sc-2971dade-4 fCmvlv"),
            Element("div", "ipc-chip-list--baseAlt ipc-chip-list"),
            Element("div", "ipc-chip-list__scroller"),
            Element("a", "ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements5_array = [
            Element("div", "sc-6cc92269-9 iamfBw sc-93323f1b-11 kaNNRp"),
            Element("div", "ipc-chip-list--baseAlt ipc-chip-list sc-6cc92269-5 jgrASN"),
            Element("div", "ipc-chip-list__scroller"),
            Element("a", "sc-6cc92269-3 iPPPLI ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements6_array = [
            Element("div", "sc-385ac629-6 nnaaE"),
            Element("div", "sc-385ac629-10 SacCW"),
            Element("div", "ipc-chip-list__scroller"),
            Element("a", "ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        elements6_array = [
            Element("div", "sc-e226b0e3-6 hfusNC"),
            Element("div", "sc-e226b0e3-10 jcOwsU"),
            Element("div", "ipc-chip-list__scroller"),
            Element("a", "ipc-chip ipc-chip--on-baseAlt", find_all=True)
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array, elements2_array,
                                                                       elements3_array, elements4_array,
                                                                       elements5_array, elements6_array)

        if found_element:
            for i in found_element:
                eng_genre.append(i.text)

        return eng_genre

    def get_eng_info(self, soup) -> str:
        eng_info = None

        elements1_array = [
            Element("div", "sc-663f405c-4 hQbEKe"),
            Element("div", "sc-6cc92269-8 hmNIYl sc-663f405c-11 kHBavT"),
            Element("span", "sc-6cc92269-1 dzxjtm")
        ]

        elements2_array = [
            Element("div", "sc-ab3b6b3d-6 cPsHQQ"),
            Element("div", "sc-ab3b6b3d-10 eIuQVa"),
            Element("span", "sc-35061649-1 NHBDz")
        ]

        elements3_array = [
            Element("section", "sc-eda143c4-4 foQtzo"),
            Element("p", "sc-35061649-3 hEmoAR"),
            Element("span", "sc-35061649-2 gtFTOy")
        ]

        elements4_array = [
            Element("section", "sc-2971dade-4 fCmvlv"),
            Element("p", ""),
            Element("span", "sc-35061649-1 NHBDz")
        ]

        elements5_array = [
            Element("section", "sc-2971dade-4 fCmvlv"),
            Element("p", "sc-5f699a2-3 lopbTB"),
            Element("span", "sc-5f699a2-1 cfkOAP")
        ]

        elements6_array = [
            Element("div", "sc-385ac629-10 SacCW"),
            Element("section", "sc-2971dade-4 fCmvlv"),
            Element("p", "sc-35061649-3 hEmoAR"),
            Element("span", "sc-35061649-1 NHBDz")
        ]

        elements7_array = [
            Element("div", "sc-385ac629-10 SacCW"),
            Element("section", "sc-52d569c6-4 eAiKYC"),
            Element("p", "sc-5f699a2-3 lopbTB"),
            Element("span", "sc-5f699a2-0 kcphyk")
        ]

        elements8_array = [
            Element("div", "sc-e226b0e3-10 jcOwsU"),
            Element("section", "sc-acac9414-4 jNMLqW"),
            Element("p", "sc-7193fc79-3 cLAPJs"),
            Element("span", "sc-7193fc79-1 jEFtFe")
        ]

        elements9_array = [
            Element("div", "sc-e226b0e3-10 jcOwsU"),
            Element("section", "sc-acac9414-4 jNMLqW"),
            Element("p", "sc-466bb6c-3 llCpwq"),
            Element("span", "sc-466bb6c-2 eVLpWt")
        ]

        elements10_array = [
            Element("div", "sc-e226b0e3-10 jcOwsU"),
            Element("section", "sc-dffc6c81-4 dsxJBN"),
            Element("p", "sc-466bb6c-3 llCpwq"),
            Element("span", "sc-466bb6c-0 kJJttH")
        ]

        found_element = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array, elements2_array,
                                                                       elements3_array, elements4_array,
                                                                       elements5_array, elements6_array,
                                                                       elements7_array, elements8_array,
                                                                       elements9_array, elements10_array)
        if found_element:
            for span in found_element:
                eng_info = strip_text(span.text)

                if eng_info and eng_info[-1] == ".":
                    eng_info = eng_info[:-1]

                if eng_info:
                    break

        # if not eng_info:
        #     elements5_array = [
        #         Element("div", "sc-385ac629-8 kewfc"),
        #         Element("div", "ipc-slate ipc-slate--baseAlt ipc-slate--dynamic-width sc-248bafc1-0 dyDUyK undefined undefined ipc-sub-grid-item ipc-sub-grid-item--span-4"),
        #         Element("div", "ipc-media ipc-media--slate-16x9 ipc-image-media-ratio--slate-16x9 ipc-media--baseAlt ipc-media--slate-m ipc-slate__slate-image ipc-media__img"),
        #         Element("img", "ipc-image")
        #     ]
        #
        #     found_element2 = Html.find_elements_in_multiple_soup_array_best(soup, elements5_array)
        #
        #     if found_element2:
        #         text = strip_text(found_element2.attrs['alt'])
        #         if not find_in_text(text,"trailer"):
        #             eng_info = text

        return eng_info

    def get_country(self, soup) -> []:
        countries = []

        for s in soup.find_all("section", {"class": ["ipc-page-section", "ipc-page-section--base", "celwidget"]}):

            elements1_array = [
                Element("hgroup", ""),
                Element("h3", "ipc-title__text")
            ]

            h3 = Html.find_elements_in_multiple_soup_array_best(s, elements1_array)

            if h3:
                if find_in_text(h3.text, "details"):
                    elements_array = [
                        Element("div", "sc-f65f65be-0 fVkLRr"),
                        Element("ul", "ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base"),
                        Element("li", "ipc-metadata-list__item ipc-metadata-list-item--link", find_all=True)
                    ]

                    found_element = Html.find_elements_in_multiple_soup_array_best(s, elements_array)

                    if found_element:
                        for li in found_element:
                            li_text = strip_text(li.text)

                            filters = [
                                "Countries of origin",
                                "Country of origin"
                            ]

                            for filter in filters:
                                if find_in_text(li_text, filter):

                                    ul2 = li.find("ul", {
                                        "class": ["ipc-inline-list", "ipc-inline-list--show-dividers",
                                                  "ipc-inline-list--inline", "ipc-metadata-list-item__list-content",
                                                  "base"]})
                                    if ul2:
                                        for li2 in ul2.find_all("li", {"class": "ipc-inline-list__item"}):
                                            a = li2.find("a", {
                                                "class": ["ipc-metadata-list-item__list-content-item",
                                                          "ipc-metadata-list-item__list-content-item--link"]})
                                            if a:
                                                countries.append(strip_text(a.text))

                                    if countries:
                                        break

                            if countries:
                                break

        if countries:
            print(*countries, sep=", ")

        return countries

    @staticmethod
    def combine_30nama_into_imdb_data(data_30nama, data_imdb) -> Film:
        full_data = data_imdb
        full_data.per_title = data_30nama.per_title
        full_data.per_genre = data_30nama.per_genre
        full_data.per_info = data_30nama.per_info
        full_data.url_imdb = data_30nama.url_imdb
        full_data.url_30nama = data_30nama.url_30nama

        return full_data

    @staticmethod
    def is_json_complete(json_path) -> bool:
        is_complete = True

        if os.path.exists(json_path):
            film = Film.json_file_to_class(json_path)

            fields = [
                film.eng_title,
                film.release,
                film.score,
                film.director,
                film.actors,
                film.eng_genre,
                film.eng_info,
                film.country
            ]

            for i in fields:
                if not i:
                    is_complete = False

        return is_complete

    @staticmethod
    def is_film_complete(film) -> bool:
        is_complete = True

        fields = [
            film.eng_title,
            film.release,
            film.score,
            # film.director,
            film.actors,
            film.eng_genre,
            film.eng_info,
            film.country
        ]

        for i in fields:
            if not i:
                is_complete = False

        return is_complete

    @staticmethod
    def check_for_html_file(location):
        html_file = False

        if os.path.exists(location):
            if os.path.exists(rename_file_paths_by_os(location) + CustomNames.HTML_IMDB_FILE_NAME):
                html_file = rename_file_paths_by_os(location) + CustomNames.HTML_IMDB_FILE_NAME

        return html_file

    @staticmethod
    def check_json_file_for_url(location) -> str:
        url = None

        file_path = rename_file_paths_by_os(location) + CustomNames.EXTRACTED_DATA

        if os.path.exists(file_path):
            data = Json.read_from_json_file(file_path)

            imdb_url = data["_url_imdb"]

            if imdb_url:
                url = imdb_url

        return url
