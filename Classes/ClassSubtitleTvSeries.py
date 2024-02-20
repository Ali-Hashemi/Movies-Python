from Base.BaseClassSubtitle import *
from Classes.ClassUtility import *


class ClassSubtitleTvSeries(BaseClassSubtitle):
    def __init__(self, name, location, language):
        super().__init__(name, location, language)

        if self.url:
            self.get_result_url(self.url)

    def get_result_url(self, url):
        season_array = ["Eleventh", "Tenth", "Ninth", "Eighth", "Seventh", "Sixth", "Fifth", "Fourth", "Third",
                        "Second", "First"]

        soup = Html.get_soup_for_subscene(url, timer=2)

        if soup:
            div = soup.find_all("div", attrs={"class": "title"})

            if div:
                for k in div:
                    text = str(k.text).strip()

                    for index, item in enumerate(season_array):
                        title = self.title + " - " + item + " Season"

                        if text.lower() == title.lower():
                            a = k.find("a", href=True)
                            if a:
                                url = self.WEB_SITE_FINAL + a['href']
                                Print.print_white(str(text) + " : " + str(url))
                                self.download_sub_urls(url)

                                extract_zip_files_tv_series(self.location)

    def download_sub_urls(self, inside_url):
        soup = Html.get_soup_for_subscene(inside_url, timer=2)

        if soup:
            tbody = soup.find("tbody")

            if tbody:
                white_list = []
                black_list = ["Official Teaser", "Official Trailer", "Trailer", "S15E", "S14E", "S13E", "S12E", "S11E",
                              "S10E", "S09E", "S08E", "S07E",
                              "S06E", "S05E", "S04E", "S03E", "S02E", "S01E", "S15.E", "S14.E", "S13.E", "S12.E",
                              "S11.E",
                              "S10.E", "S09.E", "S08.E", "S07.E",
                              "S06.E", "S05.E", "S04.E", "S03.E", "S02.E", "S01.E"]
                found_urls = []

                found_counter = 0

                for index, item in enumerate(tbody.find_all("tr")):

                    td = item.find("td", attrs={"class": "a1"})

                    if td:
                        span1 = str(td.select('span')[0].get_text(strip=True))

                        if span1.lower().find(self.language) != -1:
                            a = td.find('a', href=True)

                            span2 = td.select('span')[1].get_text(strip=True)

                            for i in black_list:
                                if span2.lower().find(i.lower()) != -1:
                                    break
                            else:
                                found_counter += 1

                                span2 = str.replace(span2, ":", "")

                                inside_url = self.WEB_SITE_FINAL + str(a['href'])

                                inner_titles, download_link = get_inside_subs_titles_and_download_link(inside_url)

                                final_download_link = self.WEB_SITE_FINAL + download_link

                                for i in inner_titles:
                                    black_list.append(i)

                                black_list = list(set(black_list))

                                Download(final_download_link, self.location, str(found_counter) + "-" + span2, ".zip")

                                # found_urls.append(final_download_link)

                if found_urls:
                    Html.download_with_browser(found_urls)
