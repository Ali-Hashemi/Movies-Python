import urllib.request
from Classes.ClassUtility import *
from Config import *
from Classes.ClassIMDB import *
from Base import *

class ExtractImdbAllPics:
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

        search_url = self.get_search_url()

        if search_url:
            posters_urls = self.get_posters_url(search_url)

            if posters_urls:
                self.download_posters(posters_urls)

    def get_search_url(self):
        name = filter_name_for_url(self.name_without_date)

        url = None
        found = None

        json_file_imdb_url = ClassIMDB.check_json_file_for_url(self.location)

        if json_file_imdb_url:
            found = json_file_imdb_url

        if not found:
            if self.film_type == 1:
                url = "https://www.imdb.com/search/title/?title=" + name + \
                      "&title_type=feature,tv_movie&num_votes=5,&release_date=" + self.release_date + \
                      "-01-01," + self.release_date + "-12-31"

            elif self.film_type == 2:
                url = "https://www.imdb.com/search/title/?title=" + name + \
                      "&title_type=tv_series,tv_miniseries&num_votes=5,&release_date=" + self.release_date + \
                      "-01-01," + self.release_date + "-12-31"

            if url:
                soup = Html.get_soup(url)

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

        Print.print_white(str(found))

        return found

    def get_posters_url(self, url):
        posters_main_page = url + "/mediaindex?refine=poster&ref_=ttmi_ref_pos"

        posters_urls = []

        posters_final_url = []

        soup = Html.get_soup_with_chrome_driver_undetected(posters_main_page, folder_path=self.location)

        if soup:
            div = soup.find("div", id="media_index_thumbnail_grid")

            length = len(div.find_all("a"))

            for idx, item in enumerate(div.find_all("a", href=True)):

                if idx < length - 1:
                    text = str(item['href']).split("/")
                    final = str(url + "/mediaviewer/" + text[-1])
                    posters_urls.append(final)

        if posters_urls:
            for i in posters_urls:
                soup2 = Html.get_soup(i)

                div2 = soup2.find("div",
                                  attrs={"class": "sc-7c0a9e7c-2 bkptFa"})

                if div2:
                    img = div2.find("img")

                    if img:
                        posters_final_url.append(img['src'])

            posters_final_url = list(set(posters_final_url))

        return posters_final_url

    def download_posters(self, urls):
        for idx, item in enumerate(urls):
            file = urllib.request.urlopen(item)

            # file_size = file.length / 1024

            Download(item, self.location, str(idx), ".jpg")
