from send2trash import send2trash
from Classes.ClassUtility import *
from Base.BaseClassSubtitle import *


class ClassSubtitleMovie(BaseClassSubtitle):
    release_date = None

    def __init__(self, name, location, language):
        super().__init__(name, location, language)

        self.release_date = File.trim_released_date(str(name))

        if self.url:
            result_url = self.get_result_url(self.url)

            if result_url:
                print("Result Url : ", result_url)
                self.download_sub_urls(result_url)

                extract_zip_files_movies(self.location, name)

            else:
                Print.print_red(name)
                Print.print_red("did not found anything")
        else:
            Print.print_red(name)
            Print.print_red("did not found anything")

    def get_search_url(self):
        name = str(self.title).replace(" (OK)", "")
        name = str(name).replace(" ", "+")

        url = "https://subscene.com/subtitles/searchbytitle?query=" + name
        print("Search Url : ", url)

        return url

    def get_result_url(self, url):
        title = str(self.title).replace("'", "")
        title = title.replace(".", "")
        title = title.strip()
        title = strip_text(title)

        found = ""

        soup = Html.get_soup_for_subscene(url, timer=2)
        # soup = Html.get_soup_for_subscene(url, timer=3, script_timer=5)
        # soup = Html.get_soup_with_chrome_driver_undetected(url, timer=3)

        if soup:
            div = soup.find_all("div", attrs={"class": "title"})

            for i in div:
                a = i.find("a", href=True)
                if a:
                    a_text = str(a.text).strip()

                    a_text = a_text.replace(":", "")
                    a_text = a_text.replace(".", "")
                    a_text = a_text.replace("'", "")

                    a_text = str(a_text).strip()

                    if a_text.lower().find(title.lower()) != -1:
                        if find_in_text(a_text, self.release_date):
                            found = self.WEB_SITE_FINAL + str(a['href'])
                            break

            if not found:
                for i in div:
                    a = i.find("a", href=True)
                    if a:
                        a_text = str(a.text).strip()

                        a_text = a_text.replace(":", "")
                        a_text = a_text.replace(".", "")
                        a_text = a_text.replace("'", "")

                        a_text = str(a_text).strip()

                        if a_text.lower().find(title.lower()) != -1:
                            if find_in_text(a_text, str(int(self.release_date) - 1)) or \
                                    find_in_text(a_text, str(int(self.release_date) + 1)):
                                found = self.WEB_SITE_FINAL + str(a['href'])
                                break

        return found

    def download_sub_urls(self, url):
        soup = Html.get_soup_for_subscene(url, timer=2)
        # soup = Html.get_soup_with_chrome_driver_undetected(url, timer=3)

        if soup:
            tbody = soup.find("tbody")

            if tbody:
                white_list = ['bdrip', 'bluray', 'web-dl', 'webrip']
                black_list = ["Official Teaser", "Official Trailer", "Trailer"]
                found_urls = []

                found_counter = 0

                for index, item in enumerate(tbody.find_all("tr")):
                    if found_counter < 6:
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
                                    for j in white_list:
                                        if str(span2).lower().find(j.lower()) != -1:
                                            found_counter += 1

                                            span2 = str.replace(span2, ":", "")

                                            inside_url = self.WEB_SITE_FINAL + str(a['href'])

                                            inner_titles, download_link = get_inside_subs_titles_and_download_link(
                                                inside_url)

                                            final_download_link = self.WEB_SITE_FINAL + download_link

                                            for i in inner_titles:
                                                black_list.append(i)

                                            black_list = list(set(black_list))

                                            Download(final_download_link, self.location,
                                                     str(found_counter) + "-" + span2,
                                                     ".zip")

                                            # found_urls.append(final_download_link)
                    else:
                        break

                for index, item in enumerate(tbody.find_all("tr")):
                    if found_counter < 6:
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

                                    inside_url = self.WEB_SITE_FINAL + str(a['href'])

                                    inner_titles, download_link = get_inside_subs_titles_and_download_link(
                                        inside_url)

                                    final_download_link = self.WEB_SITE_FINAL + download_link

                                    for i in inner_titles:
                                        black_list.append(i)

                                    black_list = list(set(black_list))

                                    Download(final_download_link, self.location, str(found_counter) + "-" + span2,
                                             ".zip")

                                    # found_urls.append(final_download_link)

                    else:
                        break

                if found_urls:
                    Html.download_with_browser(found_urls)

                if found_counter == 0:
                    Print.print_red("No " + self.language + " sub found !!!")
