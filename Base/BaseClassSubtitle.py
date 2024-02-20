from Classes.ClassUtility import *

def get_inside_subs_titles_and_download_link(url):
    soup = Html.get_soup_for_subscene(url)

    div = soup.find("div", attrs={"class": "header"})

    li = div.find("li", attrs={"class": "release"})

    titles = []

    download_link = None

    if div:
        if li:
            for i in li.find_all("div"):
                text = str(i.text).strip()
                titles.append(text)

    div2 = soup.find("div", attrs={"class": "download"})

    a2 = div2.find("a", attrs={"id": "downloadButton"}, href=True)

    if div2:
        if a2:
            download_link = a2['href']

    return titles, download_link


class BaseClassSubtitle:
    WEB_SITE_FINAL = "https://subscene.com"
    location = None
    title = None
    url = None
    language = None

    def __init__(self, name, location, language):
        self.location = location
        self.language = language
        name = str(name)
        self.title = File.trim_name_tv_series(name)
        self.title = File.trim_name_movie(name)

        self.url = self.get_search_url()

    def get_search_url(self):
        name = str(self.title).replace(" (OK)", "")
        name = str(name).replace(" ", "+")

        url = "https://subscene.com/subtitles/searchbytitle?query=" + name

        return url
