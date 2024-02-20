from Config import *
from Base import *


class ClassSearchWeb:
    name_without_date = None
    original_name_without_date = None
    release_date = None
    film_type = None
    search_type = None

    def __init__(self, name, film_type, search_type, browser_type=1):
        self.name_without_date = File.trim_name_movie(name)

        self.release_date = File.trim_released_date(name)

        self.film_type = film_type
        self.search_type = search_type

        search_url = self.get_search_url()

        if search_url:
            open_in_browser(search_url, browser_type)
            if search_type == 11:
                sleep(5)

    def get_search_url(self):
        name = filter_name_for_url(self.name_without_date)

        url = None

        if self.search_type == 1:
            if self.film_type == 2:
                text_1 = "فیلم ایرانی"
                concat = text_1 + " " + name + " wikipedia"
                url = "https://www.google.com/search?q=" + concat + "&oq=" + concat

                # text_1 = "فیلم ایرانی"
                # concat = text_1 + " " + name
                # url = "https://fa.wikipedia.org/w/index.php?&title=ویژه:جستجو&profile=advanced&fulltext=1&ns0=1&search=" + concat

            elif self.film_type == 4:
                text_1 = "انیمیشن"
                concat = text_1 + " " + name
                url = "https://www.google.com/search?q=" + concat + "&oq=" + concat

            else:
                url = "https://www.google.com/search?q=" \
                      + "فیلم" + "+" + name + "+" + self.release_date

        elif self.search_type == 2:
            if self.film_type == 1:
                # url = "https://www.google.com/search?tbm=isch&tbs=isz%3Al&client=opera&hs=BFX&hl=en&biw=1129&bih=1309&q=" \
                #       + name + "+" + self.release_date + "+poster"

                url = "https://www.google.com/search?as_st=y&tbm=isch&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=" \
                      "&safe=images&tbs=iar:t&as_q=" + name + "+" + self.release_date + "+poster"

            elif self.film_type == 2:
                n = "پوستر فیلم ایرانی "
                n = n.replace(" ", "+")
                url = "https://www.google.com/search?tbm=isch&client=opera&hs=BFX&hl=en&biw=1129&bih=1309&q=" \
                      + n + name

            elif self.film_type == 3:
                n = "پوستر سریال ایرانی "
                n = n.replace(" ", "+")
                url = "https://www.google.com/search?tbm=isch&client=opera&hs=BFX&hl=en&biw=1129&bih=1309&q=" \
                      + n + name

            elif self.film_type == 4:
                url = "https://www.themoviedb.org/search?query=" + name

        elif self.search_type == 3:
            if self.film_type == 1:
                concat = name + "+" + self.release_date + " wikipedia"
                url = "https://www.google.com/search?q=" + concat + "&oq=" + concat

            if self.film_type == 2:
                concat = name + "+" + self.release_date + "+" + "ویکی پدیا"
                url = "https://www.google.com/search?q=" + concat + "&oq=" + concat

        elif self.search_type == 4:
            url = "https://www.google.com/search?q=" \
                  + name + "+" + self.release_date + "+" + "site:imdb.com"

        elif self.search_type == 5:
            url = "https://www.google.com/search?q=" \
                  + name + "+" + self.release_date + "+" + "site:30nama.com"

            # url = "https://www.google.com/search?q=" \
            #       + name + "+" + "site:30nama.com"

        elif self.search_type == 6:
            url = "https://www.google.com/search?q=" \
                  + name + "+" + self.release_date + "+" + "site:11kingmo.xyz"

            # url = "https://www.google.com/search?q=" \
            #       + name + "+" + "site:30nama.com"

        elif self.search_type == 7:
            if self.film_type == 4:
                text_1 = "انیمیشن"
                concat = text_1 + " " + name

                url = "https://hexdownload.co/?s=" + concat
            elif self.film_type == 2:
                # text_1 = "فیلم ایرانی"
                text_1 = ""
                concat = text_1 + " " + name

                url = "https://hexdownload.co/?s=" + concat

            else:
                # name = name.replace("%20", "+")

                # url = "https://hexdownload.co/?s=" + name

                url = "https://www.google.com/search?q=" + name + "+" + "Hexdownload"

                # url = "https://www.google.com/search?q=" \
                #       + name + "+" + "site:hexdownload.co"

        elif self.search_type == 8:
            if self.film_type == 4:
                url = "https://www.doostihaa.com/?s=" + "انیمیشن" + "+" + name
            elif self.film_type == 2:
                url = "https://www.doostihaa.com/?s=" + "فیلم" + "+" + name
            else:
                text_1 = "فیلم"
                concat = text_1 + " " + name + " "

                url = "https://www.google.com/search?q=" + concat + " Doostiha"
        elif self.search_type == 9:
            url = "https://www.google.com/search?q=" \
                  + name + "+" + self.release_date + "+" + "site:dibamovie.vip"

        elif self.search_type == 10:
            text = "دانلود" + "+" + "انیمیشن" + "+" + "Uptv" + "+" + "Doostiha" + "+"
            url = "https://www.google.com/search?q=" \
                  + text + name + "+" + self.release_date

        elif self.search_type == 11:
            url = "https://subscene.com/subtitles/searchbytitle?query=" + name

        return url
