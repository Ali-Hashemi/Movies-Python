from Config import *
from Classes.ClassUtility import *
from Classes.ClassIMDB import *


class IMDBSearch:
    name = None
    release_date = None
    film_type = None
    location = None

    def __init__(self, name, film_type, location):
        self.name = File.trim_name_movie(name)
        self.release_date = File.trim_released_date(name)
        self.film_type = film_type
        self.location = location

        search_url = self.get_search_url()

        if search_url:
            open_in_browser(search_url, 1)

    def get_search_url(self):
        url = None
        found = None

        json_file_imdb_url = ClassIMDB.check_json_file_for_url(self.location)

        if json_file_imdb_url:
            found = json_file_imdb_url

        else:
            name = filter_name_for_url(self.name)

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

                                folder_name = filter_name(self.name)

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
