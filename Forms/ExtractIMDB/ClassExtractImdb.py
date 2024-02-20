from Classes.ClassIMDB import *
from Classes.Class30nama import *


class ExtractImdb:
    name_without_date = None
    release_date = None
    film_type = None
    main_page_url = None
    posters_slider_url = []
    posters_final_url = []
    location = None

    def __init__(self, name, film_type, location):
        self.name_without_date = File.trim_name_movie(str(name))
        self.release_date = File.trim_released_date(name)

        self.film_type = film_type
        self.location = location

        json_path = rename_file_paths_by_os(location) + CustomNames.EXTRACTED_DATA
        html_30nama = rename_file_paths_by_os(location) + CustomNames.HTML_30nama_FILE_NAME
        html_imdb = rename_file_paths_by_os(location) + CustomNames.HTML_IMDB_FILE_NAME

        if os.path.exists(html_imdb):
            self.get_poster_from_html(html_imdb)

        elif os.path.exists(json_path):
            film_json = Film.json_file_to_class(json_path)
            if film_json:
                if film_json.url_imdb:
                    self.get_poster(film_json.url_imdb)

        elif os.path.exists(html_30nama):
            film_30nama = Class30nama.get_data_from_html_file(html_30nama)
            if film_30nama:
                if film_30nama.url_imdb:
                    soup = self.get_poster(film_30nama.url_imdb)
                    # if soup:
                    #     film_imdb = ClassIMDB.get_all_infos_from_soup(soup)
                    #     if film_imdb:
                    #         if not Class30nama.check_film_for_empty_fields(
                    #                 film_30nama) and not ClassIMDB.check_film_for_empty_fields(film_imdb):
                    #             film_combine = ClassIMDB.combine_30nama_into_imdb_data(film_30nama, film_imdb)
                    #             Json.write_to_json_file(film_combine, json_path)

        else:
            search_url = self.get_search_url()

            if search_url:
                soup = self.get_poster(search_url)
                # if soup:
                #     film_imdb = ClassIMDB.get_all_infos_from_soup(soup)
                #     if film_imdb:
                #         if not ClassIMDB.check_film_for_empty_fields(film_imdb):
                #             Json.write_to_json_file(film_imdb, json_path)

    def get_poster_from_html(self, html_path):
        soup = Html.get_soup_from_file(html_path)

        if soup:
            elements1_array = [
                Element("div", "ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width "),
                Element("a", "ipc-lockup-overlay ipc-focusable")
            ]

            a = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

            if a:
                poster_url = str(a['href'])
                if poster_url:
                    poster_url = "https://www.imdb.com" + poster_url
                    # open_in_browser(poster_url)

                    # poster_soup = Html.get_soup(poster_url)
                    poster_soup = Html.get_soup_for_subscene(poster_url)

                    if poster_soup:
                        elements2_array = [
                            Element("div", "sc-7c0a9e7c-2 kEDMKk"),
                            Element("img", "sc-7c0a9e7c-0 fEIEer")
                        ]

                        found_element2 = Html.find_elements_in_multiple_soup_array_best(poster_soup, elements2_array)

                        if found_element2:
                            poster_url = str(found_element2['src'])
                            Print.print_white("Poster-Url : " + poster_url)
                            # open_in_browser(poster_url)

                            self.download_poster(poster_url)

    def get_poster(self, url):
        poster_url = None
        # soup = Html.get_soup(url)
        soup = Html.get_soup_for_subscene(url)

        if soup:

            elements1_array = [
                Element("div", "ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width "),
                Element("a", "ipc-lockup-overlay ipc-focusable")
            ]

            a = Html.find_elements_in_multiple_soup_array_best(soup, elements1_array)

            if a:
                poster_url = str(a['href'])
                if poster_url:
                    poster_url = "https://www.imdb.com" + poster_url
                    # open_in_browser(poster_url)

                    # poster_soup = Html.get_soup(poster_url)
                    poster_soup = Html.get_soup_for_subscene(poster_url)

                    if poster_soup:
                        elements2_array = [
                            Element("div", "sc-7c0a9e7c-2 kEDMKk"),
                            Element("img", "sc-7c0a9e7c-0 fEIEer")
                        ]

                        found_element2 = Html.find_elements_in_multiple_soup_array_best(poster_soup, elements2_array)

                        if found_element2:
                            poster_url = str(found_element2['src'])
                            Print.print_white("Poster-Url : " + poster_url)
                            # open_in_browser(poster_url)

                            self.download_poster(poster_url)

        return soup

    def get_search_url(self):
        name = filter_name_for_url(self.name_without_date)

        url = None
        found = None

        json_file_imdb_url = ClassIMDB.check_json_file_for_url(self.location)

        if json_file_imdb_url:
            found = json_file_imdb_url
        else:
            if self.film_type == 1:
                url = "https://www.imdb.com/search/title/?title=" + name + \
                      "&title_type=feature,tv_movie&num_votes=5,&release_date=" + self.release_date + \
                      "-01-01," + self.release_date + "-12-31"

            elif self.film_type == 2:
                url = "https://www.imdb.com/search/title/?title=" + name + \
                      "&title_type=tv_series,tv_miniseries&num_votes=5,&release_date=" + self.release_date + \
                      "-01-01," + self.release_date + "-12-31"

            if url:
                soup = Html.get_soup_for_subscene(url)

                if soup:
                    div = soup.find("div", attrs={'class': "lister-list"})

                    if div:
                        sub_divs = div.find_all("div", attrs={'class': 'lister-item'})

                        if sub_divs:
                            for idx, item in enumerate(sub_divs):
                                h3 = item.find("h3", attrs={'class': 'lister-item-header'})

                                a = h3.find("a", href=True)

                                span = h3.find("span", attrs={'class': 'lister-item-year'})

                                title_name = filter_name(a.text)

                                title_released_date = File.trim_released_date(span.text)

                                folder_name = filter_name(self.name_without_date)

                                if title_name.lower().find(folder_name.lower()) != -1:
                                    if str(title_released_date.lower()).find(self.release_date.lower()) != -1:
                                        found = "https://www.imdb.com" + a['href']
                                        found = found.replace("?ref_=adv_li_tt", "")
                                        break

        if found:
            Print.print_white(str(found))
        else:
            Print.print_red("Not found !!!")

        return found

    def download_poster(self, url):
        # file = urllib.request.urlopen(url)

        # file_size = file.length / 1024

        Download(url, self.location, str("Imdb-Cover"), ".jpg")
